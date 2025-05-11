import unittest
from maze_solver import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_different_sizes(self):
        num_cols = 5
        num_rows = 5
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

        num_cols = 8
        num_rows = 6
        m3 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 20, 20)
        m._break_entrance_and_exit()

        # Check entrance
        self.assertFalse(m._cells[0][0].has_top_wall)

        # Check exit
        self.assertFalse(m._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 20, 20)
        m._break_walls_r(0, 0)
        m._reset_cells_visited()

        for column in m._cells:
            for cell in column:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main() 