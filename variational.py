from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        axes = Axes(
            x_min=-1,
            x_max=2,
            y_min=-1,
            y_max=2
        )
        self.play(Write(axes))


