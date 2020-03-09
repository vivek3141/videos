from manimlib.imports import *



class Table(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1):
        for x in range(0, m):
            for y in range(0, n):
                self.add()


class DominoScene(Scene):
    CONFIG = {
        "m": 4,
        "n": 4,
        "s_width": 1,
        "s_length": 1
    }
    def construct(self):
        self.table = VGroup()

