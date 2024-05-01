import pygame
import random 

class Ball: 
    def __init__(self,display):

        self.game_display = display # Game display
        self.size = 50 # the radius of the ball
        self.position = [151,250] # position coordonates
        self.color = [0,255,0] # color RGB
        self.horizontally = 1 # vertical movement
        self.vertically = 1 # horizontal movement

        self.color_changing_index = 0
        self.color_value = 1

    def increase_size(self):
        pass #TODO increase the size (radius)

    def change_color(self):
        
        if self.color[self.color_changing_index] == 255:
            self.color_value = -1
        elif self.color[self.color_changing_index] == 0:
            self.color_value = 1
        self.color[self.color_changing_index] += self.color_value

    def change_direction(self) -> None:
        
        # Change the horizontal size
        old_direction = (self.horizontally,self.vertically)

        while old_direction == (self.horizontally,self.vertically) or (self.horizontally,self.vertically) == (0,0):
            old_direction = (self.horizontally,self.vertically)
            self.horizontally = random.randint(-1,1)
            self.vertically = random.randint(-1,1)
            print(old_direction,(self.horizontally,self.vertically), "<<<")
            

    def follow_direction(self) -> None:
        self.position[0] += self.horizontally
        self.position[1] += self.vertically


    def collision(self) -> None:
        pass # TODO detect collision

    def draw_ball(self):
        # Change the direction before draw the ball
        self.follow_direction()
        self.change_color()
        # Draw the ball 
        pygame.draw.circle(self.game_display, tuple(self.color), self.position, self.size, width = 10)