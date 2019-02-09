from manim import *


class Intro(Scene):
    def construct(self):
        li = TextMobject("Line Integral", color=BLUE)
        li.scale(2)

        int2 = TexMobject(r"\int_C\overrightarrow{\textbf{F}} \bullet \textbf{d} \overrightarrow{\textbf{r}}")
        int2.scale(1.5)

        int1 = TexMobject(r"\int_C f(x,y) ds")
        int1.scale(1.5)

        int3 = TexMobject(r"\int_C \textbf{P}dx + \textbf{Q}dy")
        int3.scale(1.5)

        uses = BulletedList(
            "Work",
            "Center of mass",
            "Faraday's Law",
            "Ampere's Law",
            "..."
        )

        self.play(Write(li))
        self.wait()
        self.play(ApplyMethod(li.shift, 3 * UP))

        self.play(Write(int1))
        self.wait()

        self.play(Transform(int1, int2))
        self.wait()

        self.play(Transform(int1, int3))
        self.wait()

        self.play(Uncreate(int1))
        self.play(Write(uses))

        self.wait(2)


class LineIntegralScalar(ThreeDScene):

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

        curve = ParametricFunction(
            self.c,
            t_min=-1,
            t_max=1,
        )

        curve_p = ParametricFunction(
            self.c_project,
            t_min=-1,
            t_max=1
        )

        surface.scale(2)
        axes = ThreeDAxes(**t_config)
        axes.scale(2.5)

        point1 = Point(self.c(-1))
        point2 = Point(self.c(1))

        text = TextMobject("C")
        text.scale(1.5)
        text.move_to(curve, 4 * RIGHT + 3 * DOWN)

        area = self.get_riemann_sums(self.c_project, dx=0.005)

        self.play(Write(integral))

        self.play(ApplyMethod(integral.scale, 0.5))
        self.play(ApplyMethod(integral.shift, 3 * UP))

        self.play(ShowCreation(axes))
        self.play(ShowCreation(surface))
        self.play(ShowCreation(curve), Write(text))
        self.play(Uncreate(integral), Uncreate(text))
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.begin_ambient_camera_rotation()
        self.wait(6)

        self.stop_ambient_camera_rotation()
        self.move_camera(np.pi / 2, -np.pi / 2)
        self.play(Transform(curve, curve_p), Uncreate(surface))
        self.play(ShowCreation(area), ShowCreation(curve_p))

        self.wait(3)

        self.move_camera(0, -np.pi / 2)
        self.play(Uncreate(axes), Uncreate(curve), Uncreate(area), Uncreate(curve_p))

        self.play(Write(integral2))

        self.wait()

        self.play(Transform(integral2, sol))
        self.wait(6)

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

    def c_project(self, t):
        return np.array([
            t,
            0,
            self.func(t, t ** 3)[-1]
        ])

    @staticmethod
    def get_riemann_sums(func, dx=0.2, x=(-1, 1), color=RED):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[-1]
            rect = Rectangle(height=h, width=dx, color=color)
            rect.shift(i * RIGHT + (h / 2) * OUT)
            rect.rotate(np.pi / 2, axis=X_AXIS)
            rect.rotate(-np.pi / 2, axis=Z_AXIS)
            rects.add(rect)

        return rects
