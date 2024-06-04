from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running_status: bool = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running_status = True
        while self.__running_status:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__running_status = False

    def draw_line(self, line, color: str = "black") -> None:
        line.draw(self.__canvas, color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1: Point = point1
        self.point2: Point = point2

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, window: Window) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1: int | None = None
        self.__y1: int | None = None
        self.__x2: int | None = None
        self.__y2: int | None = None
        self.__win: Window = window

    def draw(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:

        if self.__x1 and self.__x2 and self.__y1 and self.__y2:
            p1: Point = Point(
                int((self.__x1 + self.__x2) / 2), int((self.__y1 + self.__y2) / 2)
            )
        else:
            raise ValueError("Cell points are undefined")
        if to_cell.__x1 and to_cell.__x2 and to_cell.__y1 and to_cell.__y2:
            p2: Point = Point(
                int((to_cell.__x1 + to_cell.__x2) / 2),
                int((to_cell.__y1 + to_cell.__y2) / 2),
            )
        else:
            raise ValueError("Cell points are undefined")
        line: Line = Line(p1, p2)
        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ) -> None:
        self.x1: int = x1
        self.y1: int = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self.win: Window = win

    def _create_cells(self) -> None:
        self._cells: list[list]
