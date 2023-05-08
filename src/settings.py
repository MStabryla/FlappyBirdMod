import pygame

#initialize pygame
pygame.init()



#set up the screen to display the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 550
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set up the font
FONT = pygame.font.SysFont('comicsansms', 20)
FONT_COLOR = (255, 255, 255) #white font

#load the required images
BIRD_IMGS = [pygame.image.load('img/Flappy Bird.png'),
             pygame.image.load('img/Flappy Bird Wings Up.png'),
             pygame.image.load('img/Flappy Bird Wings Down.png')]
BOTTOM_PIPE_IMG = pygame.image.load('img/Super Mario pipe.png')
TOP_PIPE_IMG = pygame.transform.flip(BOTTOM_PIPE_IMG, False, True) #flip the image of the bottom pipe to get the image for the pipe on the top
FLOOR_IMG = pygame.image.load('img/Stone Floor.png')
BG_IMG = pygame.transform.scale(pygame.image.load('img/City Skyline.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

#set the game options
FPS = 30 #run the game at rate FPS, the speed at which images are shown
max_score = 100 #the maximum score of the game before we break the loop

# -------------------------------- #

#floor options
floor_velocity = 5 #the horizontal moving velocity of the floor, this should equal to pipe_velocity
floor_starting_y_position = 500 #the starting y position of the floor

#pipe options
pipe_max_num = 100 #the maximum number of pipes in this game
pipe_vertical_gap = 150 #the gap between the top pipe and the bottom pipe, the smaller the number, the harder the game
pipe_horizontal_gap = 200 #the gap between two sets of pipes
pipe_velocity = 5 #the horizontal moving velocity of the pipes, this should equal to floor_velocity
top_pipe_min_height = 100 #the minimum height of the top pipe (carefully set this number)
top_pipe_max_height = 300 #the maximum height of the top pipe (carefully set this number)
pipe_starting_x_position = 500 #the starting x position of the first pipe

#bird options
bird_max_upward_angle = 35 #the maximum upward angle when flying up
bird_max_downward_angle = -90 #the maximum downward angle when flying down
bird_min_incremental_angle = 5 #the minimum incremental angle when tilting up or down
bird_angular_acceleration = 0.3 #the acceleration of bird's flying angle
bird_animation_time = 1 #the animation time of showing one image
bird_jump_velocity = -8 #the vertical jump up velocity
bird_acceleration = 3 #the gravity for the bird in the game
bird_max_displacement = 12 #the maximum displacement per frame
bird_starting_x_position = 150 #the starting x position of the bird
bird_starting_y_position = 250 #the starting y position of the bird

# -------------------------------- #

#NEAT options
generation = 0 #note that the first generation of the birds is 0 because index starts from zero. XD
max_gen = 50 #the maximum number of generation to run
prob_threshold_to_jump = 0.8 #the probability threshold to activate the bird to jump
failed_punishment = 10 #the amount of fitness decrease after collision
