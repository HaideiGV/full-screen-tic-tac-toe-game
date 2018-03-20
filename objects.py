
class GameObjects:

    def __init__(self, size):
        self.size = size
        self.background = '%'

    def x_cell(self):
        object_array = []

        for i in range(0, int(self.size/2)):
            pad = i
            pad_str = pad * " "
            middle = (self.size - 2 - 2 * pad) * " "
            object_array.append(
                "{}{}{}{}{}"
                .format(pad_str, self.background, middle, self.background, pad_str)
            )

        bottom_array = object_array.copy()
        bottom_array.reverse()
        for item in bottom_array:
            object_array.append(item)

        return object_array

    def none_cell(self, number):
        object_array = ["{}{}".format(number, (self.size-1) * ' ')]
        line = "{}".format(self.size * ' ')

        for i in range(0, self.size - 1):
            object_array.append(line)

        return object_array

    def zero_cell(self):
        object_array = []
        none_head = self.background * self.size
        object_array.append(none_head)

        for i in range(0, self.size - 2):
            object_array.append(
                '{}{}{}'.format(self.background, ' ' * (self.size - 2), self.background)
            )

        object_array.append(none_head)

        return object_array
