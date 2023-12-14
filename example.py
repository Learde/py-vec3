from main import Vec3

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