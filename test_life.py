import unittest  # ~ junit, dunit
from life import GameOfLife


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        self._tested = GameOfLife()

    def test_initially_empty(self):
        self.assertTrue(self._tested.get_rows() == 0)

    def test_resize(self):
        self._tested.resize(5, 5)
        self.assertTrue(self._tested.get_rows() == 5)
        self.assertTrue(self._tested.get_cols() == 5)


if __name__ == "__main__":
    unittest.main()
