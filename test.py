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

    def test_set_cell_32_23(self):
        # captures the bug incurred with developing the
        # implementation for rule testing test case change request
        self._tested.resize((5, 5))
        self._tested.set_is_alive(2, 3, True)
        self._tested.set_is_alive(3, 2, True)
        self.assertTrue(
            self._tested.get_board() ==
            [[False, False, False, False, False],
             [False, False, False, False, False],
             [False, False, False, True, False],
             [False, False, True, False, False],
             [False, False, False, False, False]]
        )

    def test_set_cell_sets_True(self):
        self._tested.resize((2, 2))  # that should be a setup thing
        self._tested.set_is_alive(1, 1, True)
        self.assertTrue(
            self._tested.get_board() == [[False, False],
                                         [False, True]]
        )

    def test_board_as_display_at(self):
        self._tested.resize((1, 1))
        self.assertEqual(
            self._tested.get_board_as_display_at(0, 0),
            " "
        )

    def test_board_as_display_at_2(self):
        self._tested.resize([2, 2])
        self._tested.set_is_alive(1, 1, True)
        self.assertEqual(
            self._tested.get_board_as_display_at(1, 1),
            "*"
        )

    def test_board_as_display_at_3(self):
        self._tested.resize([2, 2])
        self._tested.set_is_alive(0, 0, True)
        self.assertEqual(
            self._tested.get_board_as_display_at(0, 0),
            "*"
        )

    def test_print_board_all_empty(self):
        self._tested.resize((1, 1))
        self.assertEqual(
            self._tested.board_to_display_str(),
            " \n"
        )

    def test_print_board_one_live(self):
        self._tested.resize((1, 1))
        self._tested.set_is_alive(0, 0, True)
        self.assertEqual(
            self._tested.board_to_display_str(),
            "*\n"
        )

    def test_print_board_twobytwo(self):
        self._tested.resize((2, 2))
        self.assertEqual(
            self._tested.board_to_display_str(),
            "  \n  \n"
        )

    def test_print_board_twobytwo_2(self):
        self._tested.resize((3, 2))
        self._tested.set_is_alive(2, 1, True)
        self.assertEqual(
            self._tested.board_to_display_str(),
            "  \n  \n *\n"
        )

    def test_will_it_live(self):
        self._tested.resize((5, 5))
        self._tested.set_is_alive(3, 3, False)
        self.assertEquals(
            # cell with no neighbors stays dead
            self._tested.will_it_live(3, 3),
            False
        )

    def test_will_it_live_corner(self):
        self._tested.resize((3, 3))
        self._tested.set_is_alive(0, 0, True)
        self.assertEquals(
            # cell with no neighbors stays dead
            # (assume cells outside the board are dead)
            self._tested.will_it_live(0, 0),
            False
        )

    def test_will_it_live_with_5_neighbors_live_cell(self):
        self._tested.resize((5, 5))
        self._tested.set_is_alive(3, 3, True)
        self._tested.set_is_alive(2, 3, True)
        self._tested.set_is_alive(3, 2, True)
        self._tested.set_is_alive(4, 3, True)
        self._tested.set_is_alive(3, 4, True)
        self._tested.set_is_alive(4, 4, True)
        self.assertEquals(
            # 3. live cell with 3+ neighbours dies
            self._tested.will_it_live(3, 3),
            False
        )


if __name__ == "__main__":
    unittest.main()
