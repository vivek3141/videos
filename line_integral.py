from manim import *


class LineIntegral(ThreeDScene):

    def construct(self):
        t_config = {
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
            "number_line_config": {
                "include_tip": False,
            },
        }

        integral = TexMobject(r"\int_C f(x,y) ds")
        integral.scale(2)

        surface = ParametricSurface(
            self.func,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1
        )
        curve = ParametricFunction(
            self.c
        )

        surface.scale(2)
        axes = ThreeDAxes(**t_config)
        axes.scale(2.5)

        self.play(Write(integral))

        self.play(ApplyMethod(integral.scale, 0.5))
        self.play(ApplyMethod(integral.shift, 3 * UP))

        self.play(ShowCreation(axes))
        # self.play(ShowCreation(surface))
        self.play(ShowCreation(curve))
        self.play(Uncreate(integral))
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.begin_ambient_camera_rotation()
        self.wait(6)

    @staticmethod
    def func(x, y):
        return np.array([
            x,
            y,
            x * y ** 3 - y * x ** 3
        ])

    @staticmethod
    def c(t):
        return np.array([
            t,
            t ** 3,
            t + 1
        ])
