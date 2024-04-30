import pygame
import sys
import colorama
import threading 
from ball import Ball


pygame.init()
colorama.init()




def main():

    game_display = pygame.display.set_mode((500,500))

    running = True 
    
    main_ball = Ball(game_display)
    print(colorama.Fore.GREEN + "Game is running ...." + colorama.Fore.WHITE)
    while running:
        game_display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(colorama.Fore.RED + "Game is closing ...")
                running = False
                pygame.quit()
                sys.exit()

        main_ball.draw_ball()
        main_ball.change_color()
        pygame.display.update()


main()



    
        