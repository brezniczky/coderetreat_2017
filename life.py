class GameOfLife():

    def __init__(self):
        self.resize((0, 0))

    def get_size(self):
        h = len(self._board)
        return h, 0 if h == 0 else len(self._board[0])

    def resize(self, size):
        self._board = [[False] * size[1] for y in range(size[0])]

    def get_board(self):
        return self._board

    def set_is_alive(self, x, y, is_alive):
        print self._board
        self._board[x][y] = is_alive
