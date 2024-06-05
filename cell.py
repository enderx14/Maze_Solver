from graphics import Line, Point, Window


class Cell:
    def __init__(self, window: Window | None = None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1: int | None = None
        self.__y1: int | None = None
        self.__x2: int | None = None
        self.__y2: int | None = None
        self._visited: bool = False
        if window:
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
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

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
