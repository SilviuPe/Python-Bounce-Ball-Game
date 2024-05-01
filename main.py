import pygame
import sys
import colorama
import threading
import random 
from ball import Ball
from space import ground
from time import sleep


pygame.init()
colorama.init()
pygame.mixer.init()

import os

def main():

    game_display = pygame.display.set_mode((900,900))
    sound = pygame.mixer.Sound('sound.wav')
    running = True 
    clock = pygame.time.Clock()

    game_ground = ground(game_display, 420)
    ball = Ball(game_display)
    print(colorama.Fore.GREEN + "Game is running ...." + colorama.Fore.WHITE)
    while running:
        game_display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(colorama.Fore.RED + "Game is closing ...")
                running = False
                pygame.quit()
                sys.exit()
        
        if game_ground.collision_ball(ball.position,ball.size):
            ball.horizontally *= -1;
            ball.vertically *= -1;
            ball.size += 1

            ball.position[0] += ball.horizontally * 2
            ball.position[1] += ball.vertically * 2
            ball.color_changing_index = random.randint(0,2)
            pygame.mixer.Sound.play(sound)

        game_ground.display()
        ball.draw_ball()
        pygame.display.update()

        clock.tick(180)


main()