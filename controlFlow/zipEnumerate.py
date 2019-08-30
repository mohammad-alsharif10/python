letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

letters_num = zip(letters, nums)
print(letters_num)

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append(point)

for point in points:
    print(point)

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = list(zip(*data))
print(data_transpose[1])

squares = [x ** 2 if x % 2 == 0 else x + 3 for x in range(9)]
# squares = [x ** 2 for x in range(9) if x % 2 == 0 else x + 3]
squares = [x ** 2 for x in range(9) if x % 2 == 0]
