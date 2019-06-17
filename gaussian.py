from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pass


class GaussianVisual(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2
            v_max=2
        ).scale(2)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])
