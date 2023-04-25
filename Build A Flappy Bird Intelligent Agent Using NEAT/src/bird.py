import pygame
from .settings import *

#initialize pygame
pygame.init()



#build the class Bird
class Bird:
    #Bird's attributes
    IMGS = BIRD_IMGS
    MAX_UPWARD_ANGLE = bird_max_upward_angle
    MAX_DOWNWARD_ANGLE = bird_max_downward_angle
    ANIMATION_TIME = bird_animation_time
    
    #initialize the Object
    def __init__(self, x_position, y_position):
        self.bird_img = self.IMGS[0] #use the first image as the initial image
        self.x = x_position #starting x position
        self.y = y_position #starting y position
        self.fly_angle = 0 #starting flying angle, initialized to be 0
        self.time = 0 #starting time set to calculate displacement, initialized to be 0
        self.velocity = 0 #starting vertical velocity, initialized to be 0
        self.animation_time_count = 0 #used to change bird images, initialized to be 0
        
    #defien a function to move the bird
    def move(self):
        self.time += 1 #count the time
        
        #for a body with a nonzero speed v and a constant acceleration a
        #the displacement d of this body after time t is d = vt + 1/2at^2
        displacement = self.velocity * self.time + (1/2) * bird_acceleration * self.time ** 2 #calculate the displacement when going downward
        
        #we don't want the bird going donw too fast
        #so we need to set a displacement limit per frame
        if displacement > bird_max_displacement:
            displacement = bird_max_displacement
        
        self.y = self.y + displacement #update the bird y position after the displacement
        
        if displacement < 0: #when the bird is going up
            if self.fly_angle < self.MAX_UPWARD_ANGLE: #if the flying angle is less than the maximum upward angle
                self.fly_angle += max(bird_angular_acceleration*(self.MAX_UPWARD_ANGLE - self.fly_angle), bird_min_incremental_angle) #accelerate the angle up
            else:
                self.fly_angle = self.MAX_UPWARD_ANGLE
                
        else: #when the bird is going down
            if self.fly_angle > self.MAX_DOWNWARD_ANGLE: #if the flying angle is less than the maximum downward angle
                self.fly_angle -= abs(min(bird_angular_acceleration*(self.MAX_DOWNWARD_ANGLE - self.fly_angle), -bird_min_incremental_angle)) #accelerate the angle down
            else:
                self.fly_angle = self.MAX_DOWNWARD_ANGLE

    #defien a function to jump the bird
    def jump(self):
        self.velocity = bird_jump_velocity #jump up by bird_jump_velocity
        self.time = 0 #when we jump, we reset the time to 0
    
    #define a function to get the rotated image and rotated rectangle for draw function
    def animation(self):
        self.animation_time_count += 1
        #if the bird is diving, then it shouldn't flap its wings        
        if self.fly_angle < -45:
            self.bird_img = self.IMGS[0]
            self.animation_time_count = 0 #reset the animation_time_count
        
        #if the bird is not diving, then it should flap its wings
        #keep looping the 3 bird images to mimic flapping its wings
        elif self.animation_time_count < self.ANIMATION_TIME:
            self.bird_img = self.IMGS[0]
        elif self.animation_time_count < self.ANIMATION_TIME * 2:
            self.bird_img = self.IMGS[1]
        elif self.animation_time_count < self.ANIMATION_TIME * 3:
            self.bird_img = self.IMGS[2]
        elif self.animation_time_count < self.ANIMATION_TIME * 4:
            self.bird_img = self.IMGS[1]
        else:
            self.bird_img = self.IMGS[0]
            self.animation_time_count = 0 #reset the animation_time_count
        
        #https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        #rotate the bird image for degree at self.tilt
        rotated_image = pygame.transform.rotate(self.bird_img, self.fly_angle)
        #store the center of the source image rectangle
        origin_img_center = self.bird_img.get_rect(topleft = (self.x, self.y)).center
        #update the center of the rotated image rectangle
        rotated_rect = rotated_image.get_rect(center = origin_img_center)
        #get the rotated bird image and the rotated rectangle
        return rotated_image, rotated_rect