from sys import exit, argv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize, QMutex
from Path.Path import Path
from Worm.Worm import Worm


class ThreadsExample(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(475, 450))
        self.setWindowTitle("Thread Example")
        self.threads = []
        update_window_lock = QMutex()
        worms_mutex = [QMutex() for i in range(3)]
        self.create_paths()
        self.create_worms(update_window_lock, worms_mutex)
        self.show()

    def create_worms(self, update_window_lock, worms_mutex):
        worms_mutex[0].lock()
        worms_mutex[1].lock()

        for i in range(3):
            self.threads.append(Worm(self, i, worms_mutex[i], worms_mutex[(i + 1) % 3], update_window_lock))
            self.threads[i].start()

    def create_paths(self):
        Path(self)

    def closeEvent(self, event):
        for worm in self.threads: worm.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    mainWin = ThreadsExample()
    exit(app.exec_())
