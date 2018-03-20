import itertools
import random

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
    def __init__(self, player):
        self.player = player
        CHARS.remove(self.player)
        self.machine = CHARS[0]
        self.state = {i: None for i in range(1, 10)}
        self.current_player = self.player if self.player == 'x' else self.machine

    def set_step(self, index):
        self.state[index] = self.current_player

    def check_winner(self):
        cells = [k for k in self.state.keys() if k == self.current_player]
        for case in list(itertools.combinations(cells, 3)):
            if case in WIN_COMBINATIONS:
                print("{} is WIN!".format(self.current_player))

    def rest_cells(self):
        return [k for k in self.state.keys() if k is None]

    def set_random(self):
        self.set_step(random.choices(self.rest_cells())[0])
