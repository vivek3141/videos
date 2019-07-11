from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        f = ParametricFunction(
            self.func,
            t_min=0,
            t_max=1.75,
            color=GREEN
        )
        axes = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func = VGroup(axes, f)
        func.scale(2.5)
        func.shift(2 * LEFT)

        eq1 = TexMobject(r"\frac{dy}{dx}")
        eq1.scale(1.5)
        eq1.shift(2 * RIGHT)

        eq2 = TexMobject(r"\frac{d^2y}{dx^2}")
        eq2.scale(1.5)
        eq2.shift(2 * RIGHT)

        self.play(Write(func))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Transform(eq1, eq2))
        self.wait()

    @staticmethod
    def func(t):
        return np.array([
            t,
            t**4 - 2*t**3 + t + 1,
            0
        ])
