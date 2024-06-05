from cell import Cell
from graphics import Window
from maze import Maze


def main() -> None:
    num_rows = 6
    num_cols = 8
    margin = 150
    screen_x = 800
    screen_y = 600
    cell_size_x: int = (screen_x - 2 * margin) // num_cols
    cell_size_y: int = (screen_y - 2 * margin) // num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()
