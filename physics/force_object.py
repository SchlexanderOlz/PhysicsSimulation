import math


class ForceObject:

    def __init__(self, x, z, n) -> None:
        self.x = x
        self.z = z
        self.force = n
    
    def __add__(self, other):
        # Find third angle 
        rad_z = math.radians(self.z)
        rad_x = math.radians(self.x)

        other_rad_z = math.radians(other.z)
        other_rad_x = math.radians(other.x)

        real = (self.force * math.cos(rad_x) * math.cos(rad_z)) + (other.force * math.cos(other_rad_x) * math.cos(other_rad_z))
        bottom = (self.force * math.cos(rad_z)) * math.sin(rad_x) + (other.force * math.cos(other_rad_z)) * math.sin(other_rad_x)
        imaginary = (self.force * math.cos(rad_x)) * math.sin(rad_z) + (other.force * math.cos(other_rad_x)) * math.sin(other_rad_z)

        x_force = math.sqrt(math.pow(real, 2) + math.pow(bottom, 2))
        new_force = math.sqrt(math.pow(x_force, 2) + math.pow(imaginary, 2))

        new_x_angle = math.atan2(bottom, real) # Could be wrong
        new_y_angle = math.atan2(imaginary, real)

        return ForceObject(math.degrees(new_x_angle),
                           math.degrees(new_y_angle),
                           new_force)

    def __str__(self) -> str:
        return "X-Axes: {}° | Z-Axes: {}° | Force: {}N".format(self.x, self.z, self.force)