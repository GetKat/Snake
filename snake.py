import pygame as pg

from body import Body

class Snake():
    def __init__(self):
        self.body = [Body()]
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

    # metodos pra mudar de direcao
    def go_up(self):
        self.momentum = [0, -1]
    def go_down(self):
        self.momentum = [0, 1]
    def go_left(self):
        self.momentum = [-1, 0]
    def go_right(self):
        self.momentum = [1, 0]
    
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
        for i, b in enumerate(self.body):
            if(i == 0):
                b.image.fill([255, 0, 0])
            elif(i%2):
                b.image.fill([0, 0, 255])
            else:
                b.image.fill([0, 255, 0])
        self.body_sprites.draw(screen)

        
        