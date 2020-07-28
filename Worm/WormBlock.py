from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QLabel


class WormBlock(QLabel):

    def __init__(self, main_window, which):
        super().__init__(main_window)
        self.setPixmap(QPixmap(24, 24))
        color = '#' + str(hex(0xFF << which * 8))[2:].zfill(6)
        self.pixmap().fill(QColor(color))
