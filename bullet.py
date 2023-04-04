from physics import *

class Bullet(PhisicalObject):

    def __init__(self, m, v, position) -> None:
        super().__init__(m, v, position)
    
    def hit(self, subject: PhisicalObject):
        subject.force += self.force