from manimlib.imports import *


class Grid(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        VGroup.__init__(self, **kwargs)
        for x in range(0, m + 1):
            self.add(Line(
                s_width * np.array([x - m/2, -n/2, 0]),
                s_width * np.array([x - m/2, n/2, 0]))
            )
        for y in range(0, n + 1):
            self.add(Line(
                s_length * np.array([-m/2, y - n/2, 0]),
                s_length * np.array([m/2, y - n/2, 0]))
            )


class Chessboard(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        for x in range(0, m, 2):
            for y in range(0, n):
                rect = Rectangle(width=s_length, height=s_width, fill_opacity=0.6, color=WHITE).shift(
                    [s_width * np.array([x - m/2 + (1 if y % 2 == 0 else 1/3) * s_width, y - n/2 + s_width/3, 0])])
                self.add(rect)


class DominoScene(Scene):
    CONFIG = {
        "m": 4,
        "n": 4,
        "s_width": 1.5,
        "s_length": 1.5,
        "dt": 0.6,
    }

    def construct(self):
        self.table = Chessboard(
            self.m, self.n, s_width=self.s_width, s_length=self.s_length)
        self.add(self.table)
        for x in range(0, self.m, 2):
            for y in range(0, self.n):
                rect = Rectangle(width=(2*self.s_width-self.dt), height=self.s_width-self.dt, fill_opacity=1, stroke_color=WHITE, color=PURPLE).shift(
                    [self.s_width * np.array([x - self.m/2 + self.s_length/1.5, y - self.n/2 + self.s_width/3, 0])])
                self.add(rect)
