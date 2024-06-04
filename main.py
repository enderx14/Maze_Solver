from graphics import Cell, Line, Point, Window


def main() -> None:
    win = Window(800, 600)
    # win.draw_line(Line(Point(50, 50), Point(400, 400)), "red")
    first = Cell(win)
    first.draw(100, 300, 200, 400)
    second = Cell(win)
    # second.has_left_wall = False
    second.draw(300, 300, 500, 400)
    first.draw_move(second)
    third = Cell(win)
    third.has_bottom_wall = False
    third.has_top_wall = False
    third.draw(100, 100, 200, 200)
    # c1 = Cell(win)
    # c1.has_left_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_right_wall = False
    # c2.draw(125, 125, 200, 200)

    # c3 = Cell(win)
    # c3.has_bottom_wall = False
    # c3.draw(225, 225, 250, 250)

    # c4 = Cell(win)
    # c4.has_top_wall = False
    # c4.draw(300, 300, 500, 500)

    # c1.draw_move(c2)
    win.wait_for_close()


main()
