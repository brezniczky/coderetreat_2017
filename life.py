#!/usr/bin/python


# list of lists as a board
# a single list of rows * cols elemenets
# a pandas dataframe


class GameOfLife():

    def __init__(self): #, rows, cols):
        self.resize(0, 0)

    def resize(self, rows, cols):
        self._board = [([0] * cols)] * rows

    def get_rows(self):
        return len(self._board)

    def get_cols(self):
        return len(self.board[0])



"""
print "this always happens"

if __name__ == "__main__":
    print "hello"
"""
