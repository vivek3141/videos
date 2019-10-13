from manimlib.imports import *


class Intro(Scene):
    pass


class Revolution(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        func = FunctionGraph(lambda x: 1/x)

        self.play(Write(axes))
        self.play(Write(func))


class Horn(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI
        )
        surface.center()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])
