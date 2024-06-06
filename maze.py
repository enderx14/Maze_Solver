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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            col_cells: list[Cell] = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                # print(f"{i}, {j}")

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

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j]._visited = True
        while True:
            directions: dict[str, list] = {}
            if i != 0:
                directions["left"] = [i - 1, j]
            if j != 0:
                directions["top"] = [i, j - 1]
            if i != self._num_cols - 1:
                directions["right"] = [i + 1, j]
            if j != self._num_rows - 1:
                directions["bottom"] = [i, j + 1]
            mydict: dict[str, list[int]] = {
                k: v
                for k, v in directions.items()
                if self._cells[v[0]][v[1]]._visited == False
            }
            if not mydict:
                self._draw_cell(i, j)
                return
            chosen: str = random.choice(list(mydict.keys()))
            if chosen == "right":
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[i + 1][j].has_left_wall = False
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)
            if chosen == "left":
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                self._cells[i - 1][j].has_right_wall = False
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1, j)
            if chosen == "top":
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                self._cells[i][j - 1].has_bottom_wall = False
                self._draw_cell(i, j - 1)
                self._break_walls_r(i, j - 1)
            if chosen == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._cells[i][j + 1].has_top_wall = False
                self._draw_cell(i, j + 1)
                self._break_walls_r(i, j + 1)

    def _reset_cells_visited(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False

    def solve(self) -> bool:
        if self._solve_r(0, 0):
            return True
        else:
            return False

    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        self._cells[i][j]._visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if (
            j != 0
            and not self._cells[i][j - 1]._visited
            and not self._cells[i][j - 1].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if (
            j != self._num_rows - 1
            and not self._cells[i][j + 1]._visited
            and not self._cells[i][j + 1].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        if (
            i != self._num_cols - 1
            and not self._cells[i + 1][j]._visited
            and not self._cells[i + 1][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            i != 0
            and not self._cells[i - 1][j]._visited
            and not self._cells[i - 1][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        return False
