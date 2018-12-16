import pygame as pg
import sys

from snake import Snake

# cores
black = [0, 0, 0]
white = [255, 255, 255]
gray = [128, 128, 128]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

# configuracao da tela
HEIGHT = 300
WIDTH = 300

def main():
    # inits
    pg.init()

    # configuracao da tela
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    pg.display.set_caption("Cobrinha 2")

    # clock
    clock = pg.time.Clock()

    # cria a cobrinha
    snake = Snake()

    # game loop
    while True:
        for event in pg.event.get():
            # sair do jogo
            if(event.type == pg.QUIT):
                pg.quit()
                sys.exit()
            
            # movimento da cobrinha
            if(event.type == pg.KEYDOWN):
                key = event.key
                if(key == pg.K_UP):
                    snake.go_up()
                if(key == pg.K_DOWN):
                    snake.go_down()
                if(key == pg.K_LEFT):
                    snake.go_left()
                if(key == pg.K_RIGHT):
                    snake.go_right()
                if(key == pg.K_SPACE):
                    snake.grow()
        
        # atualiza a cobrinha (movimento)
        snake.update()
        # tenha certeza q nao saia da tela
        snake.assert_screen(WIDTH, HEIGHT)

        # desenhando cada frame
        screen.fill(black)
        snake.draw(screen)

        # atualizando a tela
        pg.display.flip()

        # ajuste do FPS
        clock.tick(10)

if(__name__ == "__main__"):
    main()