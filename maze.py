import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2, self.win)
                column.append(cell)
            self._cells.append(column)
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append((-1, 0))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append((0, -1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append((0, 1))

            if not directions:
                self._draw_cell(i, j)
                return

            di, dj = random.choice(directions)
            ni, nj = i + di, j + dj

            if di == -1:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif di == 1:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            elif dj == -1:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            elif dj == 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False

            self._break_walls_r(ni, nj)

    def _break_entrance_and_exit(self):
        # Break the entrance at the top-left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Break the exit at the bottom-right cell
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        # Check if we are at the end cell
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # Directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                if not self._cells[ni][nj].visited:
                    if (di == -1 and not self._cells[i][j].has_left_wall) or \
                       (di == 1 and not self._cells[i][j].has_right_wall) or \
                       (dj == -1 and not self._cells[i][j].has_top_wall) or \
                       (dj == 1 and not self._cells[i][j].has_bottom_wall):

                        self._cells[i][j].draw_move(self._cells[ni][nj])

                        if self._solve_r(ni, nj):
                            return True

                        self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)

        return False 