from phisical_object import *
from person import *
from bullet import *


if __name__ == "__main__":
    '''person = Person(80, 0, Coordinate(12, 8, 5), 'Peter')
    print(person.force)
    bullet = Bullet(0.06, 1000, Coordinate(4, 2, 6))
    print(bullet.force)
    bullet.set_target_position(Coordinate(12, 8, 5))
    print(bullet.force)
    bullet.hit(person)
    print(person.force)'''

    vec1 = ForceObject(90, 0, 100)
    vec2 = ForceObject(0, 0, 100)

    print(vec1 + vec2)