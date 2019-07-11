from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        f = ParametricFunction(
            func,
            t_min=0,
            t_max=1,
            color=GREEN
        )
        axes = Axes(
            x_min=-1,
            x_max=3,
            y_min=0,
            y_max=4,
            number_line_config={
                "include_tip": False,
            }
        )

        func = VGroup(axes, f)
        self.play(Write(func))

    def func(t):
        return np.array([
            t,
            t**4 - 2*t**3 + t + 1,
            0
        ])
