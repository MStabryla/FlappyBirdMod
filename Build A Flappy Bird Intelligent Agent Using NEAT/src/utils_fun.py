from .settings import *



#define a function to check collision
def collide(bird, pipe, floor, screen):
    
    #Creates a Mask object from the given surface by setting all the opaque pixels and not setting the transparent pixels
    bird_mask = pygame.mask.from_surface(bird.bird_img) #get the mask of the bird
    top_pipe_mask = pygame.mask.from_surface(pipe.top_pipe_img) #get the mask of the pipe on the top
    bottom_pipe_mask = pygame.mask.from_surface(pipe.bottom_pipe_img) #get the mask of the pipe on the bottom
    
    sky_height = 0 #the sky height is the upper limit
    floor_height = floor.y #the floor height is the lower limit
    bird_lower_end = bird.y + bird.bird_img.get_height() #the y position of the lower end of the bird image
    
    #in order to check whether the bird hit the pipe, we need to find the point of intersection of the bird and the pipes
    #if overlap, then mask.overlap(othermask, offset) return (x, y)
    #if not overlap, then mask.overlap(othermask, offset) return None
    #more information regarding offset, https://www.pygame.org/docs/ref/mask.html#mask-offset-label
    top_pipe_offset = (round(pipe.x - bird.x), round(pipe.top_pipe_topleft - bird.y))
    bottom_pipe_offset = (round(pipe.x - bird.x), round(pipe.bottom_pipe_topleft - bird.y))
    
    #Returns the first point of intersection encountered between bird's mask and pipe's masks
    top_pipe_intersection_point = bird_mask.overlap(top_pipe_mask, top_pipe_offset)
    bottom_pipe_intersection_point = bird_mask.overlap(bottom_pipe_mask, bottom_pipe_offset)

    if top_pipe_intersection_point is not None or bottom_pipe_intersection_point is not None or bird_lower_end > floor_height or bird.y < sky_height:
        return True
    else:
        return False


#define a function to draw the screen to display the game
def draw_game(screen, birds, pipes, floor, score, generation, game_time, warning):
    
    #draw the background
    screen.blit(BG_IMG, (0, 0))
    
    #draw the moving floor
    screen.blit(floor.IMGS[0], (floor.x1, floor.y)) #draw the first floor image
    screen.blit(floor.IMGS[1], (floor.x2, floor.y)) #draw the second floor image
    screen.blit(floor.IMGS[2], (floor.x3, floor.y)) #draw the third floor image
    
    #draw the moving pipes
    for pipe in pipes:
        screen.blit(pipe.top_pipe_img, (pipe.x, pipe.top_pipe_topleft)) #draw the pipe on the top
        screen.blit(pipe.bottom_pipe_img, (pipe.x, pipe.bottom_pipe_topleft)) #draw the pipe on the bottom
    
    #draw the animated birds
    for bird in birds:
        rotated_image, rotated_rect = bird.animation()
        screen.blit(rotated_image, rotated_rect)
        # czy pokazać strzałkę
        if bird.should_jump:
            screen.blit(warning, (rotated_rect.x, rotated_rect.y - 40))
    
    #add additional information
    score_text = FONT.render('Score: ' + str(score), 1, FONT_COLOR) #set up the text to show the scores
    screen.blit(score_text, (SCREEN_WIDTH - 15 - score_text.get_width(), 15)) #draw the scores
    
    game_time_text = FONT.render('Timer: ' + str(game_time) + ' s', 1, FONT_COLOR) #set up the text to show the progress
    screen.blit(game_time_text, (SCREEN_WIDTH - 15 - game_time_text.get_width(), 15 + score_text.get_height())) #draw the progress
    
    generation_text = FONT.render('Generation: ' + str(generation - 1), 1, FONT_COLOR) #set up the text to show the number of generation
    screen.blit(generation_text, (15, 15)) #draw the generation
    
    bird_text = FONT.render('Birds Alive: ' + str(len(birds)), 1, FONT_COLOR) #set up the text to show the number of birds alive
    screen.blit(bird_text, (15, 15 + generation_text.get_height())) #draw the number of birds alive
    
    progress_text = FONT.render('Pipes Remained: ' + str(len(pipes) - score), 1, FONT_COLOR) #set up the text to show the progress
    screen.blit(progress_text, (15, 15 + generation_text.get_height() + bird_text.get_height())) #draw the progress
    
    pygame.display.update() #show the surface


#define a function to get the input index of the pipes
def get_index(pipes, birds):
    #get the birds' x position
    bird_x = birds[0].x
    #calculate the x distance between birds and each pipes
    list_distance = [pipe.x + pipe.IMG_WIDTH - bird_x for pipe in pipes]
    #get the index of the pipe that has the minimum non negative distance(the closest pipe in front of the bird)
    index = list_distance.index(min(i for i in list_distance if i >= 0)) 
    return index



