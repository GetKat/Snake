import pygame as pg
import os

from body import Body

path = os.path.dirname(os.path.abspath(__file__))

class Snake():
    # direcao do momentum 
    _DIR_UP = [0, -1] # quando ta indo pra cima, o valor do x nao muda e o y diminiu
    _DIR_DOWN = [0, 1]
    _DIR_LEFT = [-1, 0]
    _DIR_RIGHT = [1, 0]

    def __init__(self):
        self.body = [Body(0, 0), Body(-1, 0), Body(-2, 0)]
        self.body_sprites = pg.sprite.Group()
        self.body_sprites.add(self.body)

        # momentum inicial eh pra esquerda
        self.momentum = [1, 0]

    # atualiza a posicao da cobrinha (mover cada parte do corpo)
    def update(self):
        """
        como fazer a cobrinha se mover? pega a ultima parte do corpo e coloca na primeira posicao (nao na mesma coordenada da cabeca, mas sim onde ela estaria baseada em momentum)
        """

        # pega o ultimo parte do corpo da lista
        last = self.body[-1]
        # pega a posicao da cabeca
        head_pos = self.body[0].rect
        # tirou esse ultimo elemento da lista
        self.body.pop()

        # calcula quanto precisa se mover nos eixos
        change_x, change_y = self.momentum
        change_x *= 20
        change_y *= 20

        # atualizar a posicao desse elemento retirado baseado na posicao da cabeca
        last.rect.x = head_pos.x + change_x 
        last.rect.y = head_pos.y + change_y

        # dps de ter atualizado a posicao, bota no inicio da lista
        self.body.insert(0, last)
    
    # ter certeza da cobrinha nao sair da tela 
    """
    esse metodo foi deprecated pq esse esquema da cobrinha passar pela tela deu ruim com a direcao da calda
        o sentido da calda (up, down, left, right) eh baseado na posicao do prox elemento. Ao sair da tela, a posicao
        do quadrado muda a logica e faz a calda ficar no sentido oposto, tirando a funcionalidade de poder 'sair' da tela resolve o problema.
    """
    def assert_screen(self, game_width, game_height):
        """caso a cobrinha saia da tela:"""
        head_rect = self.body[0].rect
        # eixo x
        if(head_rect.left < 0):           # saiu pela esquerda
            head_rect.right = game_width
        if(head_rect.right > game_width):      # saiu pela direita
            head_rect.left = 0
        # eixo y
        if(head_rect.top < 0):            # saiu por cima
            head_rect.bottom = game_height
        if(head_rect.bottom > game_height):    # saiu por baixo
            head_rect.top = 0

    def out_of_screen(self, game_width, game_height):
        head_rect = self.body[0].rect
        # sair por cima
        if(head_rect.top < 0):
            return False

        # sair por baixo
        if(head_rect.bottom > game_height):
            return False
        
        # sair pela esquerda
        if(head_rect.left < 0):
            return False
        
        # sair pela direita
        if(head_rect.right > game_width):
            return False

        # nao saiu
        return True
    
    # verifica se esta vivo ou nao (por colisao entre si)
    def check_collision(self):
        for body in self.body:
            for other_body in self.body:
                if(body != other_body and body.rect == other_body.rect):
                    return False
        return True

    """ metodos pra mudar de direcao """
    # nao pode mudar a direcao de maneira que a nova direcao va ocasionar na morte (e.g. esta indo pra cima e muda pra baixo), mas isso pode ocorrer caso exista so a cabeca
    def go_up(self):
        if(self.momentum != Snake._DIR_DOWN or len(self.body) == 1):
            self.momentum = Snake._DIR_UP
    def go_down(self):
        if(self.momentum != Snake._DIR_UP or len(self.body) == 1):
            self.momentum = Snake._DIR_DOWN
    def go_left(self):
        if(self.momentum != Snake._DIR_RIGHT or len(self.body) == 1):
            self.momentum = Snake._DIR_LEFT
    def go_right(self):
        if(self.momentum != Snake._DIR_LEFT or len(self.body) == 1):
            self.momentum = Snake._DIR_RIGHT
    
    # crescer
    def grow(self):
        """
        n precisa se preocupar com a posicao dessa nova parte do corpo, pois o metodo de movimento pega a ultima parte do corpo e coloca na frente
        """
        # cria a nova parte do corpo
        new_body = Body()
        # adicina na lista de partes do corpo
        self.body.append(new_body)
        # adicina a lista de sprites
        self.body_sprites.add(new_body)


    # desenha na tela
    def draw(self, screen):
        for i, body in enumerate(self.body):
            # desenhar head (precisa saber qual a direcao dela)
            if(i == 0):
                if(self.momentum == Snake._DIR_DOWN):
                    body.image = Body._IMG_HEAD_DOWN
                elif(self.momentum == Snake._DIR_UP):
                    body.image = Body._IMG_HEAD_UP
                elif(self.momentum == Snake._DIR_RIGHT):
                    body.image = Body._IMG_HEAD_RIGHT
                elif(self.momentum == Snake._DIR_LEFT):
                    body.image = Body._IMG_HEAD_LEFT
            # desenhar a calda
            elif(body == self.body[-1]):
                tail = body
                next_one = self.body[-2]
                if(tail.rect.x == next_one.rect.x):
                    if(tail.rect.y > next_one.rect.y):
                        tail.image = Body._IMG_TAIL_UP
                    else:
                        tail.image = Body._IMG_TAIL_DOWN
                else:
                    if(tail.rect.x > next_one.rect.x):
                        tail.image = Body._IMG_TAIL_LEFT
                    else:
                        tail.image = Body._IMG_TAIL_RIGHT
            # desenhar o corpo
            else:
                prev = self.body[i - 1].rect
                next = self.body[i + 1].rect
                # caso 1 (vertical ou orizontal) -> prev, body e next estao no mesmo eixo
                if(prev.x == body.rect.x and body.rect.x == next.x):
                    body.image = Body._IMG_BODY_VERTICAL
                elif(prev.y == body.rect.y and body.rect.y == next.y):
                    body.image = Body._IMG_BODY_HORIZONTAL
                # casos onde vai fazer curva
                else:
                    px, py = prev.x, prev.y
                    nx, ny = next.x, next.y
                    bx, by = body.rect.x, body.rect.y
                    if((py < by and nx < bx) or (ny < by and px < bx)):
                        body.image = Body._IMG_BODY_TOP_LEFT
                    elif((py < by and nx > bx) or (px > bx and ny < by)):
                        body.image = Body._IMG_BODY_TOP_RIGHT
                    elif((px > bx and ny > by) or (py > by and nx > bx)):
                        body.image = Body._IMG_BODY_RIGHT_BOTTOM
                    elif((px < bx and ny > by) or (py > by and nx < bx)):
                        body.image = Body._IMG_BODY_LEFT_BOTTOM
                    else:
                        print("deu merda")
                        

        self.body_sprites.draw(screen)

        
        