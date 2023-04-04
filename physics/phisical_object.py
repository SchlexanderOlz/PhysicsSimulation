from physics import ForceObject
from collections import namedtuple
import math


Coordinate = namedtuple('Coordinate', ['x', 'y', 'z'])

class PhisicalObject:

    def __init__(self, m, v, postion: Coordinate) -> None:
        self.mass = m
        self.velocity = v
        self.position = postion
        self.force = ForceObject(0, 0, m * v)

    def set_target_position(self, subject_pos: Coordinate):
        y = subject_pos.y - self.position.y
        x = subject_pos.x - self.position.x
        z = subject_pos.z - self.position.z

        self.force.x = math.degrees(math.atan2(y, x))
        self.force.z = math.degrees(math.atan2(z, x))