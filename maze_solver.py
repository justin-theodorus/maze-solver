from tkinter import Tk, BOTH, Canvas
import time
import random
from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 40, 40, win, seed=0)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main() 