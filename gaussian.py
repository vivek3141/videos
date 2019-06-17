from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        f = ParametricFunction(
            function=lambda t: np.array([t, np.exp(-t**2), 0]),
            t_min=-3,
            t_max=3,
            color=BLUE
        )
        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2
        )
        func = VGroup(axes, f)
        func.scale(2)

        eq = TexMobject(r"\int_{-\infty}^{\infty} e^{-x^2} \ dx = \sqrt{pi}")
        eq.scale(1.5)
        eq.shift(3 * UP)

        self.play(Write(func))
        self.wait()
        self.play(Write(eq))
        self.wait()


class GaussianVisual(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        ).scale(2)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])
