import unittest
from life import GameOfLife


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        self._tested = GameOfLife()

    def test_initializes_with_empty_board(self):
        self.assertTrue(self._tested.get_size() == (0, 0))

    def test_get_size_returns_correct_values_after_resize(self):
        self._tested.resize((5, 5))
        self.assertTrue(self._tested.get_size() == (5, 5))

    def test_get_size_returns_correct_values_after_resize_2(self):
        self._tested.resize((3, 5))
        self.assertTrue(self._tested.get_size() == (3, 5))

    def test_resize_initializes_with_dead_cells(self):
        self._tested.resize((2, 3))
        self.assertTrue(
            self._tested.get_board() == [[False, False, False],
                                         [False, False, False]]
        )

    def test_set_cell_sets_True(self):
        self._tested.resize((2, 2))  # that should be a setup thing
        self._tested.set_is_alive(1, 1, True)
        self.assertTrue(
            self._tested.get_board() == [[False, False],
                                         [False, True]]
        )


if __name__ == "__main__":
    unittest.main()
