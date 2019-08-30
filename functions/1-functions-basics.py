def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(5, 5))


def cylinder_volume2(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


cylinder_volume2(10, 7)  # pass in arguments by position
cylinder_volume2(height=10, radius=7)  # pass in arguments by name
