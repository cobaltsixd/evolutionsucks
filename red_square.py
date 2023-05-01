import arcade
import math
from gold_polygon import GoldPolygon

RED_SQUARE_SPEED = 5


class RedSquare(arcade.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__("Images/red-square.png")

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = 200
        self.center_y = 200
        self.polygons_eaten = 0

    def update(self, gold_polygon_list, blue_circle):
        # Calculate the distance between the red square and each gold polygon
        distances = []
        for gold_polygon in gold_polygon_list:
            distance = math.sqrt((self.center_x - gold_polygon.center_x) ** 2 +
                                 (self.center_y - gold_polygon.center_y) ** 2)
            distances.append(distance)

        # Find the gold polygon that is closest to the red square
        min_distance = min(distances)
        index = distances.index(min_distance)
        closest_gold_polygon = gold_polygon_list[index]

        # Move the red square towards the closest gold polygon
        if closest_gold_polygon.center_x < self.center_x:
            self.change_x = -RED_SQUARE_SPEED
        elif closest_gold_polygon.center_x > self.center_x:
            self.change_x = RED_SQUARE_SPEED
        else:
            self.change_x = 0

        if closest_gold_polygon.center_y < self.center_y:
            self.change_y = -RED_SQUARE_SPEED
        elif closest_gold_polygon.center_y > self.center_y:
            self.change_y = RED_SQUARE_SPEED
        else:
            self.change_y = 0

        # Update the position of the red square
        super().update()

        # Check if the red square has collided with any gold polygon
        for gold_polygon in gold_polygon_list:
            if arcade.check_for_collision(self, gold_polygon):
                gold_polygon.kill()
                new_gold_polygon = GoldPolygon(self.screen_width, self.screen_height)
                gold_polygon_list.append(new_gold_polygon)
                self.polygons_eaten += 1
                break

        # Check if the red square has collided with the blue circle
        if arcade.check_for_collision(self, blue_circle):
            # Move the red square away from the blue circle
            if self.center_x < blue_circle.center_x:
                self.center_x -= 2 * RED_SQUARE_SPEED
            else:
                self.center_x += 2 * RED_SQUARE_SPEED

            if self.center_y < blue_circle.center_y:
                self.center_y -= 2 * RED_SQUARE_SPEED
            else:
                self.center_y += 2 * RED_SQUARE_SPEED

        # Change the color of the square based on the number of polygons eaten
        if self.polygons_eaten < 11:
            self.texture = arcade.load_texture("Images/red-square.png")
        elif self.polygons_eaten < 26:
            self.texture = arcade.load_texture("Images/orange-square.png")
        elif self.polygons_eaten < 51:
            self.texture = arcade.load_texture("Images/yellow-square.png")
        else:
            self.texture = arcade.load_texture("Images/green-square.png")

