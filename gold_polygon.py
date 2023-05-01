import arcade
import random

GOLD_POLYGON_IMAGE = "images/banana.png"
GOLD_POLYGON_SCALING = 0.02


class GoldPolygon(arcade.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__(GOLD_POLYGON_IMAGE, GOLD_POLYGON_SCALING)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.randomize_position()

    def randomize_position(self):
        self.center_x = random.randint(0, self.screen_width)
        self.center_y = random.randint(0, self.screen_height)

    def is_eaten(self, blue_circle):
        if arcade.check_for_collision(self, blue_circle):
            return True
        else:
            return False
