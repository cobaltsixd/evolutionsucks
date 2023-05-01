import arcade
import math

from gold_polygon import GoldPolygon

BLUE_CIRCLE_SPEED = 5


class BlueCircle(arcade.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__("Images/blue-circle.png", center_x=screen_width, center_y=screen_height)
        self.speed = BLUE_CIRCLE_SPEED
        self.change_x = self.speed
        self.change_y = self.speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.polygons_eaten = 0
        self.life_timer = 5.0  # set the timer to 20 seconds
        self.closest_gold_polygon = None

    def update(self, delta_time, gold_polygon_list):
        super().update()

        # Decrement the life timer by delta_time
        self.life_timer -= delta_time
        if self.life_timer <= 0:
            self.kill()  # Kill the sprite if the life timer is less than or equal to zero
            return

        # Calculate the distance between the blue circle and each gold polygon
        distances = []
        for gold_polygon in gold_polygon_list:
            distance = math.sqrt((self.center_x - gold_polygon.center_x) ** 2 +
                                 (self.center_y - gold_polygon.center_y) ** 2)
            distances.append(distance)

        # Find the gold polygon that is closest to the blue circle
        if gold_polygon_list:
            min_distance = min(distances)
            index = distances.index(min_distance)
            self.closest_gold_polygon = gold_polygon_list[index]

        # Move the blue circle towards the closest gold polygon
        if self.closest_gold_polygon:
            if self.closest_gold_polygon.center_x < self.center_x:
                self.change_x = -BLUE_CIRCLE_SPEED
            elif self.closest_gold_polygon.center_x > self.center_x:
                self.change_x = BLUE_CIRCLE_SPEED
            else:
                self.change_x = 0

            if self.closest_gold_polygon.center_y < self.center_y:
                self.change_y = -BLUE_CIRCLE_SPEED
            elif self.closest_gold_polygon.center_y > self.center_y:
                self.change_y = BLUE_CIRCLE_SPEED
            else:
                self.change_y = 0

        # Update the position of the blue circle
        super().update()

        # Check if the blue circle has collided with any gold polygon
        for gold_polygon in gold_polygon_list:
            if arcade.check_for_collision(self, gold_polygon):
                gold_polygon.kill()
                new_gold_polygon = GoldPolygon(self.screen_width, self.screen_height)
                gold_polygon_list.append(new_gold_polygon)
                self.polygons_eaten += 1
                if self.polygons_eaten >= 51:
                    self.texture = arcade.load_texture("Images/green-circle.png")
                elif self.polygons_eaten >= 26:
                    self.texture = arcade.load_texture("Images/yellow-circle.png")
                elif self.polygons_eaten >= 11:
                    self.texture = arcade.load_texture("Images/orange-circle.png")
                else:
                    self.texture = arcade.load_texture("Images/red-circle.png")
                self.life_timer = 5.0  # Reset the timer to 20 seconds
                break
#