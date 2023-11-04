from fish import Fish
from shark import Shark
from world import World

import pygame
from pygame.locals import *
import argparse
import random


"""
Parameters for Wa-Tor
Width of Wa-Tor
Height of Wa-tor
Fish Color
Shark Color
Fish Breeding Time
Shark Breeing Time
Shark Starting Energy
Shark Energy Boost from eating
Cell Size of Creature
Number of Chronons
Framerate
"""

# Initialize pygame and random
random.seed()
pygame.init()

def get_args():
    parser = argparse.ArgumentParser(description="Wa-Tor Parameters")
    
    parser.add_argument('-w', '--width', help='Wator Width', default=16, type=int)
    parser.add_argument('-v', '--height', help='Wator Height', default=9, type=int)
    parser.add_argument('-f', '--fish_color', help='Fish Color', default='blue', type=str)
    parser.add_argument('-s', '--shark_color', help='Shark Color', default='green', type=str)
    parser.add_argument('-o', '--ocean_color', help='Ocean Color', default='lightblue', type=str)
    parser.add_argument('-z', '--zoom_factor', help='Zoom Factor', default=75, type=int)
    
    args = parser.parse_args()
    return args
    
def game_loop(args):
    """
    Error checking goes here
    """
    
    # Setup the window and clock
    window_size = (args.width * args.zoom_factor, args.height * args.zoom_factor)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Wa-Tor Simulation")
    clock = pygame.time.Clock()
    
    
    # Main Loop
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # fill the screen with ocean color
        screen.fill(args.ocean_color)
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()
    
    
    

if __name__ == '__main__':
    game_loop(get_args())
