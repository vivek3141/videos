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
        integral2 = TexMobject(r"\int_C f(x,y) ds")
        integral2.scale(2)

        sol = TexMobject(r"\int_a^b f(x(t), y(t)) \sqrt{(\frac{dx}{dt})^2+(\frac{dy}{dt})^2}dt")
        sol.scale(1.5)

        surface = ParametricSurface(
            self.func,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1,
            fill_color=RED,
            checkerboard_colors=[RED, ORANGE]

        )

        plane = ParametricSurface(
            self.plane,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1,
            fill_color=RED,
            checkerboard_colors=[RED, RED]

        )

        curve = ParametricFunction(
            self.c,
            t_min=-1,
            t_max=1,
        )

        surface.scale(2)
        axes = ThreeDAxes(**t_config)
        axes.scale(2.5)

        point1 = Point(self.c(-1))
        point2 = Point(self.c(1))

        text = TextMobject("C")
        text.scale(1.5)
        text.move_to(curve, 4 * RIGHT + 3 * DOWN)

        #self.play(Write(integral))

        #self.play(ApplyMethod(integral.scale, 0.5))
        #self.play(ApplyMethod(integral.shift, 3 * UP))

        self.play(ShowCreation(axes))
        # self.play(ShowCreation(surface))
        # self.play(ShowCreation(curve), Write(text))
        # self.play(Uncreate(integral), Uncreate(text))
        # self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        #
        # self.begin_ambient_camera_rotation()
        # self.wait(6)
        #
        # self.stop_ambient_camera_rotation()
        self.move_camera(np.pi/2, -np.pi/2)

        self.wait()
        #self.play(Uncreate(surface))
        self.play(ShowCreation(plane), ShowCreation(curve))
        self.wait(3)

        # self.move_camera(0, -np.pi/2)
        # self.play(Uncreate(axes), Uncreate(curve))
        #
        # self.play(Write(integral2))
        #
        # self.wait()
        #
        # self.play(Transform(integral2, sol))
        # self.wait(6)

    @staticmethod
    def func(x, y):
        return np.array([
            x,
            y,
            0.5 * (math.cos(5 * x) + math.sin(5 * y))
        ])

    def c(self, t):
        return np.array([
            t,
            t ** 3,
            self.func(t, t ** 3)[-1]
        ])

    def plane(self, x, y):
        return np.array([
            x,
            0,
            self.func(x, y)[-1]
        ])




