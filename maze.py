import random
from time import sleep

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self._cells: list[list[Cell]] = []
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        if win:
            self._win: Window | None = win
        else:
            self._win = None
        if seed is not None:
            self._seed: int | None = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            col_cells: list[Cell] = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                print(f"{i}, {j}")

    def _draw_cell(self, i, j) -> None:
        if self._win is None:
            return
        x1: int = self._x1 + i * self._cell_size_x
        y1: int = self._y1 + j * self._cell_size_y
        x2: int = x1 + self._cell_size_x
        y2: int = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.15)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j) -> None:
        self._cells[i][j]._visited = True
        while True:
            temp: list = []
            not_visited: list = [self._cells[0][0], self._cells[0][0]]
