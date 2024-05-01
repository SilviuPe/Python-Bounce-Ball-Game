import pygame
from math import sqrt # import sqrt from the math to use in Pitagora theory 


class ground:
    def __init__(self, window : object, free_space : int) -> None:
        
        # basically the radius of the circle that covers the ground
        self.free_space = free_space
        
        # define the window and the center of it
        self.window = window
        self.center_point = (self.window.get_size()[0]//2,self.window.get_size()[1]//2)
    
        self.circle_color = [255,255,255]
    
    # DISPLAY THE GROUND
    def display(self) -> None:
        pygame.draw.circle(self.window, self.circle_color, self.center_point, self.free_space, width = 5)


    def collision_ball(self, ball_position : tuple, radius : int) -> bool:
        
        # use the Pitagora theory 
        # find x difference 
        x = self.center_point[0] - ball_position[0]

        # find y difference 
        y = self.center_point[1] - ball_position[1]

        # use Pitagora to find the distance between center of the center and the ball
        distance = sqrt(x**2 + y**2)

        # IF the distance if bigger then the (radius of the circle ground + radius of the ball * 2)
        # that means the ball is out the the circle of the ground
        if distance >= self.free_space - radius:
            return True
        
        # otherwise, the balll is inside the circle of the ground
        else:
            return False 
