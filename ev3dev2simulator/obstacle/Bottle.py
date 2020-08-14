import arcade
import pymunk
from arcade import Sprite


class Bottle:
    """
    This class represents a 'bottle'. Bottles are circles.
    """

    def __init__(self,
                 x: int,
                 y: int,
                 radius: float,
                 color: arcade.Color):

        self.x = x
        self.y = y
        self.radius = radius

        # visualisation
        self.color = color
        self.sprite = None
        self.scale = None

        # physics
        self.body = None
        self.shape = None


    @classmethod
    def from_config(cls, config):
        x = int(config['x'])
        y = int(config['y'])
        radius = int(config['radius'])
        color = eval(config['color'])

        return cls(x, y, radius, color)

    def get_sprite(self):
        return self.sprite

    def get_pos(self):
        if hasattr(self, 'new_pos'):
            return self.new_pos.x * (1/self.scale), self.new_pos.y * (1/self.scale)
        return self.x, self.y

    def create_shape(self, scale):
        radius = scale * self.radius
        mass = 5
        friction = 0.2
        moment = pymunk.moment_for_circle(mass, 0, radius, (0, 0))

        self.body = pymunk.Body(mass, moment)
        pos_x, pos_y = self.get_pos()
        self.body.position = pymunk.Vec2d(pos_x * scale, pos_y * scale)

        self.shape = pymunk.Circle(self.body, radius, (0, 0))
        self.shape.friction = friction
        self.scale = scale

    def create_sprite(self, scale):
        pos_x, pos_y = self.get_pos()
        self.sprite = Sprite('assets/images/bottle.png', scale=scale * 2 * (self.radius / 948),
                             center_x=pos_x * scale, center_y=pos_y * scale)

    def reset(self):
        self.body.velocity = (0, 0)
        self.body.angular_velocity = 0
        self.body.position = pymunk.Vec2d(self.x * self.scale, self.y * self.scale)
