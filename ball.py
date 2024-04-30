import pygame

class Ball: 
    def __init__(self,display):
        self.game_display = display
        self.size = 10

    def increase_size(self):
        pass #TODO increase the size (radius)


    def change_direction(self):
        pass # TODO adjust the direction for the ball 


    def collision(self):
        pass # TODO detect collision

    def draw_ball(self):
        pygame.draw.circle(self.game_display, (255,0,0), (200,200), 200)


