from phisical_object import *

class Person(PhisicalObject):

    def __init__(self, m, v, position: Coordinate, name) -> None:
        super().__init__(m, v, position)
        self.name = name