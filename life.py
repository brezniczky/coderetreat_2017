from time import sleep
from random import random, seed

class GameOfLife():

    def __init__(self):
        self.resize((0, 0))

    def get_size(self):
        h = len(self._board)
        return h, 0 if h == 0 else len(self._board[0])

    def _create_board(self, size):
        return [[False] * size[1] for y in range(size[0])]

    def resize(self, size):
        self._board = self._create_board(size)

    def get_board(self):
        return self._board

    def set_is_alive(self, x, y, is_alive):
        self._board[x][y] = is_alive

    def get_board_as_display_at(self, x, y):
        if not self._board[x][y]:
            return " "
        else:
            return "*"

    def board_to_display_str(self):
        display = ""
        for number in range(self.get_size()[0]):
            col = self._board[number]
            display = display + "".join([self.get_board_as_display_at(number, y) for y in range(len(col))]) + "\n"
        return display

    def will_it_live(self, x, y):
        counter = 0

        # x_range = range(max(x - 1, 0), min(x + 1, len(self._board) - 1) + 1)

        # y_range = range(max(y - 1, 0), min(y + 1, (self.get_size()[1] - 1) + 1))
        # # y_range = range(y - 1, y + 2)

        for i in range(x - 1, x + 2):
            for k in range(y - 1, y + 2):
                if i < 0 or i >= self.get_size()[0]:
                    continue
                if k < 0 or k >= self.get_size()[0]:
                    continue

                if i == x and k == y:
                    pass
                elif self._board[i][k]:
                    counter = counter + 1
        if counter < 2:
            return False  # the cell is dead
        if counter > 3:
            return False  # the cell is dead
        if counter == 3:
            """ the cell is either alive, and stays like
                that, or comes back to life """
            return True
        return self._board[x][y]

    def iterate(self):
        # TODO: add test
        size = self.get_size()
        new_board = self._create_board(size)
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                new_board[x][y] = self.will_it_live(x, y)
        self._board = new_board

    def anim_print(self, iterations):
        for i in range(iterations):
            print self.board_to_display_str()
            self.iterate()
            sleep(1)

    def randomize_board(self):
        size = self.get_size()
        for i in range(size[0]):
            for j in range(size[1]):
                self.set_is_alive(i, j, random() > 0.5)

if __name__ == "__main__":
    life = GameOfLife()
    # print dir(life)
    life.resize((40, 40))
    life.randomize_board()
    life.set_is_alive(3, 3, True)
    life.set_is_alive(3, 2, True)
    life.set_is_alive(3, 4, True)
    # print life.board_to_display_str()
    # life.iterate()
    # print life.board_to_display_str()

    # # print life.board_to_display_str()
    life.anim_print(240)
