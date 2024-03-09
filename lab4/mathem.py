import math

# 1 Write a Python program to convert degree to radian.
def degree_to_radian(degree: int):
    return degree * (math.pi / 180)
# print(degree_to_radian(15))

# 2 Write a Python program to calculate the area of a trapezoid.
def area_trapezoid(height, base1, base2):
    return ((base1 + base2) / 2) * height
# print(area_trapezoid(5, 5, 6))

# 3 Write a Python program to calculate the area of regular polygon.
def area_regular_polygon(sides, length):
    return sides * (length ** 2) / (4 * math.tan(math.pi / sides))
# print(area_regular_polygon(4, 25))

# 4 Write a Python program to calculate the area of a parallelogram.
def area_parallelogram(base, height):
    return base * height
# print(area_parallelogram(5, 6))
