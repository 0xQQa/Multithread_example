from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QLabel


class PathBlock(QLabel):

    def __init__(self, central_widget):
        super().__init__(central_widget)
        self.setPixmap(QPixmap(24, 24))
        self.pixmap().fill(QColor(0, 0, 0))
