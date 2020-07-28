from PyQt5.QtCore import QThread
from Worm.WormBlock import WormBlock


class Worm(QThread):

    def __init__(self, main_window, which, mutex_1, mutex_2, update_window_lock):
        super().__init__()
        self.length = 5 + which * 2
        self.which = which
        self.mutex_1 = mutex_1
        self.mutex_2 = mutex_2
        self.main_window = main_window
        self.moving_cnt = 23
        self.update_window_lock = update_window_lock
        self.worm = self.create_worm()

    def create_worm(self):
        offsets = {0: (175, 50), 1: (100, 200), 2: (250, 200)}
        worm_body = [WormBlock(self.main_window, self.which) for i in range(self.length)]

        for i in range(self.length):
            if i < 6: worm_body[i].move(offsets[self.which][0] + i * 25, offsets[self.which][1])
            else: worm_body[i].move(offsets[self.which][0] + 125, offsets[self.which][1] + 25 * (i - 5))

        return worm_body

    def tail_moving(self):
        for i in range(self.length - 1, 0, -1): self.worm[i].move(self.worm[i - 1].pos())

    def common_move(self, amount, worm_head):
        sleep_time = 50 + self.which * 25

        for i in range(amount):
            self.tail_moving()

            if self.moving_cnt < 6: worm_head.move(worm_head.x(), worm_head.y() + 25)
            elif self.moving_cnt < 12: worm_head.move(worm_head.x() + 25, worm_head.y())
            elif self.moving_cnt < 18: worm_head.move(worm_head.x(), worm_head.y() - 25)
            elif self.moving_cnt < 24: worm_head.move(worm_head.x() - 25, worm_head.y())
            if self.moving_cnt == 23: self.moving_cnt = -1

            self.moving_cnt += 1
            self.update_window_lock.lock()
            self.main_window.update()
            self.update_window_lock.unlock()
            self.msleep(sleep_time)

    def moving(self):
        worm_head = self.worm[0]
        breakpoints_offsets = {0: (6, 7), 1: (12, 3), 2: (21, 4)}
        shared_road_len = breakpoints_offsets[self.which][1] + self.length

        self.common_move(breakpoints_offsets[self.which][0], worm_head)
        while True:
            self.mutex_1.lock()
            self.common_move(shared_road_len, worm_head)
            self.mutex_2.unlock()
            self.common_move(24 - shared_road_len, worm_head)

    def run(self) -> None:
        self.moving()
