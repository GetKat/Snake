import pygame as pg
import sys

from snake import Snake
from food import Food

# cores basicas
black = [0, 0, 0]
white = [255, 255, 255]
gray = [128, 128, 128]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

# cores especiais
light_green = [126, 200, 126]
light_gray = [136, 140, 141]

# cores na tela
BACKGROUND_COLOR = light_gray

# configuracao da tela
HEIGHT = 300
WIDTH = 300
GAME_FPS = 12

def main():
    # inits
    pg.init()

    # configuracao da tela
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    pg.display.set_caption("Cobrinha 2")

    # clock pra controlar o FPS
    clock = pg.time.Clock()

    # cria a cobrinha
    snake = Snake()

    # cria primeira comida
    food = Food(WIDTH, HEIGHT)

    # sprite pras comidas
    food_sprites = pg.sprite.Group()
    food_sprites.add(food)

    alive = True
    # game loop
    while alive:
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
                elif(key == pg.K_DOWN):
                    snake.go_down()
                elif(key == pg.K_LEFT):
                    snake.go_left()
                elif(key == pg.K_RIGHT):
                    snake.go_right()
                elif(key == pg.K_SPACE):
                    snake.grow()

                # um movimento por frame
                break
            
        # verifica se a comida foi comida
        if(food.rect.center == snake.body[0].rect.center):
            snake.grow()
            food_sprites.remove(food)
            food = Food(WIDTH, HEIGHT)
            food_sprites.add(food)

        # atualiza a comida
        food_sprites.update()
        # atualiza a cobrinha (movimento)
        snake.update()

        # (!!DEPRECATED!!) snake.assert_screen(WIDTH, HEIGHT) SE FOR USAR ESSE METODO TEMQ ESTAR ANTES DOS UPDATES
        alive = snake.out_of_screen(WIDTH, HEIGHT) and snake.check_collision()
        # sem esse if-statement a cabeca sai da tela antes de morrer... como posso remove-lo??
        if(not alive): break

        # desenhando cada frame
        screen.fill(BACKGROUND_COLOR)
        food_sprites.draw(screen)
        snake.draw(screen)

        # atualizando a tela
        pg.display.flip()

        # ajuste do FPS
        clock.tick(GAME_FPS)

if(__name__ == "__main__"):
    main()