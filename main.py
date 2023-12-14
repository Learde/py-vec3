import math

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)
        else:
            raise ValueError("Division by zero is undefined.")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        length = self.length()
        if length != 0:
            return self / length
        else:
            raise ValueError("Cannot normalize the zero vector.")


# Пример использования:
v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 / 2 = {v1 / 2}")
print(f"Dot product of v1 and v2: {v1.dot(v2)}")
print(f"Cross product of v1 and v2: {v1.cross(v2)}")
print(f"Length of v1: {v1.length()}")
print(f"Normalized v1: {v1.normalize()}")
