import pygame
import random 

class Ball: 
    def __init__(self,display):
        self.game_display = display
        self.size = 100
        self.position = (300,300)
        self.color = [0,255,0]

        self.colors_path = {
            0 : 
        }
    def increase_size(self):
        pass #TODO increase the size (radius)

    def change_color(self):
        rgb = random.randint(0,2)
        if self.color[rgb] == 255:
            self.color[rgb] -= 1
        else:
            self.color[rgb] += 1
    def change_direction(self):
        pass # TODO adjust the direction for the ball 


    def collision(self):
        pass # TODO detect collision

    def draw_ball(self):
        pygame.draw.circle(self.game_display, tuple(self.color), self.position, self.size)


