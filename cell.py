from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is not None:
            if self.has_left_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "#d9d9d9")
            if self.has_right_wall:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
            else:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "#d9d9d9")
            if self.has_top_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "#d9d9d9")
            if self.has_bottom_wall:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if self._win is not None:
            color = "gray" if undo else "red"
            start_x = (self._x1 + self._x2) // 2
            start_y = (self._y1 + self._y2) // 2
            end_x = (to_cell._x1 + to_cell._x2) // 2
            end_y = (to_cell._y1 + to_cell._y2) // 2
            self._win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), color) 