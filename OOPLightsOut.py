import pygame
import random

#gen game stuff
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700
BACKGROUND_COLOR = (255,255,255)
BUTTON_OFF = (51,39,0)
BUTTON_ON = (255,204,0)


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Lights Out")
clock = pygame.time.Clock()

class window:

    def __init__(self, pos, size = [100,100], light = False):
        self.size = size
        self.pos = pos
        self.light = light


        draw_windows(self.pos, self.size, self.light)


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
    
def toggle_light(this_light):
    if this_light == True:
        this_light = False:
    else:
        this_light = True
    return this_light

def click_checker(pos_size_on):
    mouse_pos = pygame.mouse.get_pos()
    pos = pos_size_on[0]
    size = pos_size_on[1]
    on_off = pos_size_on[2]
    #left off here
    #CHECK IF CLICK IS INSIDE BUTTON, Then run button state changer(Toggle_light) return light -> make state change to object
def main():
    
    gameDisplay.fill(BACKGROUND_COLOR)
    draw_windows([0,600],[DISPLAY_WIDTH,10])#Square box (600X600)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #mouse clicked
        #for key in dict (pass in values, pos, size)
            #run click_checker(dict key:(pos,size,on_off)) 
        pygame.display.update()
        clock.tick(15)

if __name__ == "__main__":
    main()
