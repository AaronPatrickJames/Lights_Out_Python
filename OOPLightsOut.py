import pygame
import random

#gen game stuff
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700
BACKGROUND_COLOR = (255,255,255)
BUTTON_OFF = (51,39,0)
BUTTON_ON = (255,204,0)

WINDOW_SPAWN_LOCATION = [-110, 10]#I made it incriment weird. so start back further
WINDOW_SPAWN_SIZE = [100,100]


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Lights Out")
clock = pygame.time.Clock()

class window:

    def __init__(self, pos, size = [100,100], light = False):
        self.size = size
        self.pos = pos
        self.light = light
        
        draw_windows(self.pos, self.size, self.light)

        
#SPAWNS WINDOWS
def window_pos():
    if WINDOW_SPAWN_LOCATION[0] <= DISPLAY_WIDTH - 120:#last spawn in row
        WINDOW_SPAWN_LOCATION[0] = WINDOW_SPAWN_LOCATION[0] + 120
    else:
        WINDOW_SPAWN_LOCATION[0] = 10
        WINDOW_SPAWN_LOCATION[1] = WINDOW_SPAWN_LOCATION[1] + 120
    return WINDOW_SPAWN_LOCATION
    
#draw boxes on screen
def draw_windows(pos, size, on_off):
    top = pos[0]
    left = pos[1]
    x = size[0]
    y = size[1]
    if on_off == True:
        on_off = BUTTON_ON
    else:
        on_off = BUTTON_OFF
        
    pygame.draw.rect(gameDisplay, on_off,(top, left, x, y))
    
#I just flip a switch
def toggle_light(this_light):
    if this_light == True:
        this_light = False
    else:
        this_light = True
    return this_light

#really its an onclick listener for these home made buttons
def click_checker(key, value):
    mouse_pos = pygame.mouse.get_pos()
    pos = value.pos
    size = value.size
    on_off = value.light
    print(key, pos)
    #if mouse is in bounds of self.button/self.window
    #if int(pos[0] + size[0]) > mouse_pos[0] > int(pos[0]) and int(pos[1] + size[1]) > mouse_pos[1] > int(pos[1]):



        
def main():
    count = 0
    board = {}
    starting_x_windows = 5
    starting_y_windows = 5
    gameDisplay.fill(BACKGROUND_COLOR)
    draw_windows([0,600],[DISPLAY_WIDTH,10], False)#Square box (600X600)
    for j in range(starting_x_windows):
        for i in range(starting_y_windows):
            count = count + 1
            building = window(window_pos(), WINDOW_SPAWN_SIZE)
            board.update({count : [building.pos, building.size, building.light]})
    for key, value in board.items():
        print(key, value)
            
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #mouse clicked(click_checker)
        am_i_pressed = pygame.mouse.get_pressed()
        if am_i_pressed[0] == 1:
            for key, value in building.items():#note building need to be defined
                click_checker(key, value)
                
        #for key in dict (pass in values, pos, size)
            #run click_checker(dict key:(pos,size,on_off)) 
        pygame.display.update()
        clock.tick(15)
        
if __name__ == "__main__":
    main()
