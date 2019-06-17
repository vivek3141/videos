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
        func = VGroup(f, axes)

        self.play(Write(func))


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
