from manim import *


class LineIntegral(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.8 * np.pi / 2, -0.45 * np.pi)
        surface = ThreeDVMobject
        self.play(ShowCreation(ThreeDAxes))
        self.play(ShowCreation(surface))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(6)

    def func(self, u, v):
        return np.array([
            u,
            v,
            u ** 2 + v ** 2
        ])
