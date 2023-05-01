import arcade

class Obstacle(arcade.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__("Images/obstacle.png", center_x=0, center_y=0)

        self.screen_width = screen_width
        self.screen_height = screen_height

        # Set hit_box to the size of the obstacle
        self.hit_box = arcade.create_rectangle(self.center_x - self.width / 2, self.center_y - self.height / 2,
                                               self.width, self.height, arcade.color.WHITE)

    def update(self):
        # Check for collisions with other sprites
        for sprite in arcade.get_sprites_at_point((self.center_x, self.center_y), self.sprite_list):
            if sprite is not self and arcade.check_for_collision(sprite, self):
                # Reset sprite position to prevent it from passing through the obstacle
                sprite.change_x *= -1
                sprite.change_y *= -1
                sprite.center_x += sprite.change_x
                sprite.center_y += sprite.change_y
