class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # writes string
    def __str__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    # addition of vectors
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # subtraction of vectors
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # dot product of vectors
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    # scaling of vector
    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # finds the length of a vector
    def length(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # normalizes the vector
    def normalize(self):
        if(self.x == 0 and self.y == 0):
            return self
        return self.scale(1 / self.length())


