from manimlib.imports import *


class Grid(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.m = m
        self.n = n
        self.s_width = s_width
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
                pos = s_width * \
                    np.array([x - m/2 + (1 if y % 2 == 0 else 0) + 0.5,
                              y - n/2 + 0.5,
                              0])
                rect = Rectangle(
                    width=s_length,
                    height=s_width,
                    fill_opacity=0.6,
                    color=WHITE)
                rect.shift(pos)
                self.add(rect)


class DominoGrid(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, dt=0.6, perm=None, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        self.dt = dt
        self.add_rect(2, 3)

    def add_rect(self, pos1, pos2):
        rect = Rectangle(
            width=(2*self.s_width-self.dt),
            height=self.s_width-self.dt,
            fill_opacity=1,
            stroke_color=WHITE,
            color=PURPLE).shift(
            [self.s_width * np.array([pos1 - self.m/2 + 1, pos2 - self.n/2 + 0.5, 0])])
        self.add(rect)


class DominoTest(Scene):
    def construct(self):
        grid = DominoGrid(4, 4, s_width=1.5, s_length=1.5)
        #grid = Chessboard(4, 4, s_width=1.5, s_length=1.5)
        self.play(ShowCreation(grid))
