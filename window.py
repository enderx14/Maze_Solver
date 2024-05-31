from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.running_status: bool = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.running_status = True
        while self.running_status:
            self.redraw()

    def close(self) -> None:
        self.running_status = False
