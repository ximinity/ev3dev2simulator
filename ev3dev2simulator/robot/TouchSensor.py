from ev3dev2simulator.config.config import get_config
from ev3dev2simulator.robot.BodyPart import BodyPart


class TouchSensor(BodyPart):
    """
    Class representing a TouchSensor of the simulated robot.
    """

    def __init__(self,
                 brick: int,
                 address: str,
                 robot,
                 delta_x: int,
                 delta_y: int,
                 side: str,
                 name: str):
        self.side = side
        if self.side in ['left', 'right']:
            dims = get_config().get_visualisation_config()['body_part_sizes']['touch_sensor_bar']
        else:
            dims = get_config().get_visualisation_config()['body_part_sizes']['touch_sensor_bar_rear']

        super(TouchSensor, self).__init__(brick, address, robot, delta_x, delta_y, dims['width'], dims['height'],
                                          'touch_sensor')
        self.name = name

    def setup_visuals(self, scale):
        if self.side == 'left':
            img = 'touch_sensor_left'
        elif self.side == 'right':
            img = 'touch_sensor_right'
        else:
            img = 'touch_sensor_rear'
        vis_conf = get_config().get_visualisation_config()
        self.init_texture(vis_conf['image_paths'][img], scale)

    def get_latest_value(self):
        return self.is_touching()

    def is_touching(self) -> bool:
        """
        Check if this TouchSensor is touching a TouchObstacle.
        :return: boolean value representing the outcome.
        """
        for o in self.sensible_obstacles:
            if o.collided_with(self):
                return True

        return self.get_default_value()

    def get_default_value(self):
        return False
