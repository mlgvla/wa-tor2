from fish import Fish
from shark import Shark
import random

class World():
    def __init__(self, dimensions, fish_color, shark_color, ocean_color, zoom_factor):
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.zoom_factor = zoom_factor
        
        self.fish_color = fish_color
        self.shark_color = shark_color
        self.ocean_color = ocean_color
        
        # start with a random number of fish and sharks
        num_fish = random.randint(1, self.width * self.height / 2)
        nums_harks = random.randint(1, self.width * self.height / 2)

       
    """
    # Using list comprehension, initialize the planet to just ocean
        rows = 50
        cols = 100
        array_2d = [[0 for _ in range(cols)] for _ in range(rows)]
    """