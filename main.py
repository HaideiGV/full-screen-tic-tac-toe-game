import os
from objects import GameObjects


# while True:
start_heigth, start_width = os.popen('stty size', 'r').read().split()
height = int(start_heigth)
width = int(start_width)

size = 6
obj = GameObjects(size)

x_array = obj.x_cell()
zero_array = obj.zero_cell()
none_array = obj.none_cell(7)

for raw in range(0, size):
    print("||{}||{}||{}||".format(x_array.pop(0), zero_array.pop(0), none_array.pop(0)))

