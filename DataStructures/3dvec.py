class Vector3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Vector3D(self.x-other.x, self.y-other.y, self.z-other.z)

    def __add__(self, other):
        return Vector3D(self.x+other.x, self.y+other.y, self.z+other.z)

    def dot(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self, other):
        return Vector3D(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
