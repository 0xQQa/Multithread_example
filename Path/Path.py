from PyQt5.QtWidgets import QWidget
from Path.PathBlock import PathBlock


class Path(QWidget):

    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.draw_path()

    def draw_path(self, ):
        for i in range(13):
            PathBlock(self.main_window).move(75 + 25 * i, 200)
            PathBlock(self.main_window).move(75 + 25 * i, 350)

        for i in range(6):
            PathBlock(self.main_window).move(75, 225 + 25 * i)
            PathBlock(self.main_window).move(150 + 25 * i, 50)
            PathBlock(self.main_window).move(150, 50 + 25 * i)
            PathBlock(self.main_window).move(225, 225 + 25 * i)
            PathBlock(self.main_window).move(300, 50 + 25 * i)
            PathBlock(self.main_window).move(375, 225 + 25 * i)
