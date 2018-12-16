import pygame as pg

from body import Body

class Snake():
    # direcao do momentum 
    _DIR_UP = [0, -1] # quando ta indo pra cima, o valor do x nao muda e o y diminiu
    _DIR_DOWN = [0, 1]
    _DIR_LEFT = [-1, 0]
    _DIR_RIGHT = [1, 0]

    def __init__(self):
        self.body = [Body(), Body(), Body()]
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
            # head
            if(i == 0):
                body.image = Body._IMG_HEAD
                # body.image.fill([255, 0, 0])
            else:
                body.image.fill([0, 255, 0])
        self.body_sprites.draw(screen)

        
        