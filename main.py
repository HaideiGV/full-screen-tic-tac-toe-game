import os
import itertools
import random


def x_cell(size):
    top_array = []
    for i in range(0, int(size/2)):
        pad = i
        pad_str = pad * " "
        char = '#'
        middle = (size - 2 - 2 * pad) * " "
        top_array.append("{}{}{}{}{}".format(pad_str, char, middle, char, pad_str))

    bottom_array = top_array.copy()
    bottom_array.reverse()
    for item in bottom_array:
        top_array.append(item)

    return "\n".join(top_array)


def zero_cell(size):
    zero_head = " {} ".format((size - 2) * '#')
    zero_body_line = "#{}#".format((size - 2) * ' ')
    zero_array = []
    zero_array.append(zero_head)
    for i in range(0, size - 2):
        zero_array.append(zero_body_line)
    zero_array.append(zero_head)

    return "\n".join(zero_array)


WIN_COMBINATIONS = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]

CHARS = ['x', '0']


class Game:
    def __init__(self, char):
        self.char_player = char
        self.char_machine = CHARS[self.char_player][0]
        self.state = {i: None for i in range(1, 10)}
        self.current_player = self.char_player if self.char_player == 'x' else self.char_machine

    def set(self, cell_index, char):
        self.state[cell_index] = char

    def check_winner(self):
        play_cells = [k for k in self.state.keys() if k == self.current_player]
        for case in list(itertools.combinations(play_cells, 3)):
            if case in WIN_COMBINATIONS:
                print("{} is WIN!".format(self.current_player))

    def rest_cells(self):
        return [k for k in self.state.keys() if k is None]

    def set_random(self):
        self.set(random.choices(self.rest_cells())[0], self.char_machine)


while True:
    start_heigth, start_width = os.popen('stty size', 'r').read().split()
    height = int(start_heigth)
    width = int(start_width)

    for k in range(5, 7):
        i = int(width/4)
        print()
        print()
        set_1 = x_cell(i).split('\n')
        set_2 = x_cell(i).split('\n')
        set_3 = x_cell(i).split('\n')
        cell_size = len(set_1)
        for j in range(0, cell_size):
            print("{} {} {}".format(set_1.pop(0), set_2.pop(0), set_3.pop(0)))
        print()
        print()
        s_1 = zero_cell(i).split('\n')
        s_2 = zero_cell(i).split('\n')
        s_3 = zero_cell(i).split('\n')
        cell_size = len(s_1)
        for j in range(0, cell_size):
            print("{} {} {}".format(s_1.pop(0), s_2.pop(0), s_3.pop(0)))
        print()
        print()
