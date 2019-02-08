from manim import *


class LineIntegral(ThreeDScene):

    def construct(self):
        ThreeDConfig = {
            "x_min": -1,
            "x_max": 1,
            "y_min": -1,
            "y_max": 1,
            "z_axis_config": {},
            "z_min": -1,
            "z_max": 1,
            "z_normal": DOWN,
            "num_axis_pieces": 20,
            "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
        }
        self.set_camera_orientation(0.8 * np.pi / 2, -0.45 * np.pi)
        surface = ParametricSurface(
            self.func,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1
        )
        surface.scale(2)
        self.play(ShowCreation(ThreeDAxes(**ThreeDConfig).scale(3)))
        self.play(ShowCreation(surface))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(6)

    @staticmethod
    def func(x, y):
        return np.array([
            x,
            y,
            x * y ** 3 - y * x ** 3
        ])
