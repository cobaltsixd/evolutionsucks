import arcade
from blue_circle import BlueCircle
from gold_polygon import GoldPolygon
from red_square import RedSquare
from obstacle import Obstacle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "evolveSim : eat something, get better >:-)"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Create the blue circle and set its initial position and scale
        self.blue_circle = BlueCircle(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.blue_circle.center_x = 10
        self.blue_circle.center_y = 10
        self.blue_circle.scale = 0.05

        # Create the red square and set its initial position
        self.red_square = RedSquare(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.red_square.center_x = 400
        self.red_square.center_y = 400
        self.red_square.scale = .05

        # Create the gold polygons and add them to a sprite list
        self.gold_polygon_list = arcade.SpriteList()
        for i in range(4):
            gold_polygon = GoldPolygon(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            self.gold_polygon_list.append(gold_polygon)

        # Create the obstacles and add them to a sprite list
        self.obstacle_list = arcade.SpriteList()
        for i in range(5):
            obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.obstacle_list.append(obstacle)
    def on_draw(self):
        arcade.start_render()

        # Draw the blue circle, red square, and gold polygons
        self.blue_circle.draw()
        self.red_square.draw()
        self.gold_polygon_list.draw()
        self.obstacle_list.draw()

    def on_update(self, delta_time):
        # Update the blue circle and gold polygons
        self.blue_circle.update(delta_time, self.gold_polygon_list)

        # Check if any gold polygons have been eaten by the blue circle and replace them with new ones
        for gold_polygon in self.gold_polygon_list:
            if gold_polygon.is_eaten(self.blue_circle):
                gold_polygon.kill()
                new_gold_polygon = GoldPolygon(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.gold_polygon_list.append(new_gold_polygon)

        # Update the red square, passing the blue circle object to its update method
        self.red_square.update(self.gold_polygon_list, self.blue_circle)

        # Check if the red square has collided with any gold polygon
        for gold_polygon in self.gold_polygon_list:
            if arcade.check_for_collision(self.red_square, gold_polygon):
                gold_polygon.kill()
                new_gold_polygon = GoldPolygon(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.gold_polygon_list.append(new_gold_polygon)
                self.red_square.polygons_eaten += 1

        # Change the color of the square based on the number of polygons eaten
        if self.red_square.polygons_eaten < 11:
            self.red_square.texture = arcade.load_texture("Images/red-square.png")
        elif self.red_square.polygons_eaten < 26:
            self.red_square.texture = arcade.load_texture("Images/orange-square.png")
        elif self.red_square.polygons_eaten < 51:
            self.red_square.texture = arcade.load_texture("Images/yellow-square.png")
        else:
            self.red_square.texture = arcade.load_texture("Images/green-square.png")

    def on_key_press(self, key, modifiers):
        self.blue_circle.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.blue_circle.on_key_release(key, modifiers)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
