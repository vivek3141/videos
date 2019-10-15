from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pass


class Revolution(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        f1 = FunctionGraph(lambda x: 1/x, x_min=0.1)
        f2 = FunctionGraph(lambda x: 1/x, x_max=-0.1, x_min=-10)
        func = VGroup(f1, f2)
        func2 = FunctionGraph(lambda x: 1/x, x_min=1)

        surface = ParametricSurface(
            self.surface,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=0.001,
            checkerboard_colors=[eval(key) for key in COLOR_MAP.keys()],
            fill_color=YELLOW,
            stroke_color=YELLOW
        )

        self.play(Write(func), Write(axes))
        self.wait()

        self.play(Transform(f1, func2), Uncreate(f2), Write(surface))
        self.wait()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.remove(f1)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(
            UpdateFromAlphaFunc(surface, self.update_f),
            rate_func=linear,
            run_time=2
        )

        self.play(Uncreate(axes), surface.center)
        self.wait(5)

    def update_f(self, c, dt):
        a = interpolate(0.1, 2*PI, dt)
        s = ParametricSurface(
            self.surface,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=a,
            checkerboard_colors=[eval(key) for key in COLOR_MAP.keys()],
            color=YELLOW,
            fill_color=YELLOW,
        )
        c.become(s)

    @staticmethod
    def surface(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])


class Volume(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[eval(key) for key in COLOR_MAP.keys()],

        )
        surface.center()

        disk = ParametricSurface(
            self.disk,
            u_min=0,
            u_max=2*PI,
            v_min=-1/3,
            v_max=1/3,
            checkerboard_colors=[RED, ORANGE],
        )

        disk2 = ParametricSurface(
            self.disk2,
            u_min=0,
            u_max=2*PI,
            v_min=-2.5,
            v_max=2.5,
            checkerboard_colors=[RED, ORANGE],
        )

        circle = VGroup(
            ParametricFunction(
                self.circle,
                t_min=0,
                t_max=2*PI,
                color=YELLOW,
                stroke_width=0.5*DEFAULT_STROKE_WIDTH
            ),
            ParametricFunction(
                lambda t: np.array([0, 0, t]),
                t_min=0,
                t_max=2.5,
                color=YELLOW,
                stroke_width=2*DEFAULT_STROKE_WIDTH
            )
        )

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.begin_ambient_camera_rotation()
        self.wait()

        surface.set_fill(opacity=0.5)
        surface.set_stroke(opacity=0.5)
        self.wait()

        self.play(Write(disk))
        self.wait()

        self.stop_ambient_camera_rotation()
        self.play(Uncreate(surface))

        self.move_camera(
            phi=90 * DEGREES,
            theta=0 * DEGREES,
        )

        self.play(Transform(disk, disk2))
        self.wait()

        self.play(Write(circle))
        self.wait()

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])

    @staticmethod
    def disk(u, v):
        return np.array([
            -2,
            v*np.cos(u),
            v*np.sin(u)
        ])

    @staticmethod
    def disk2(u, v):
        return np.array([
            0,
            v*np.cos(u),
            v*np.sin(u)
        ])

    @staticmethod
    def circle(t, r=2.5):
        return r*np.array([
            0,
            np.cos(t),
            np.sin(t)
        ])


class VolumeEval(Scene):
    def construct(self):
        eq1 = TexMobject(
            r"\int_1^{\infty} \pi \left( \frac{1}{x} \right)^2 dx",
            tex_to_color_map={r"\left( \frac{1}{x} \right)^2": RED})
        eq1.scale(1.5)

        eq2 = TexMobject(
            r"\lim_{t \rightarrow \infty} \int_1^{t} \pi \left( \frac{1}{x} \right)^2 dx",
            tex_to_color_map={r"\left( \frac{1}{x} \right)^2": RED})
        eq2.scale(1.5)

        eq3 = TexMobject(
            r"= \pi \lim_{t \rightarrow \infty} \left ( \frac{-1}{x} \right ) \Big |_1^t",
            tex_to_color_map={r"\left( \frac{1}{x} \right)^2": RED})
        eq3.scale(1.5)

        eq4 = TexMobject(
            r"= \pi \lim_{t \rightarrow \infty} \frac{-1}{t} + 1",
            tex_to_color_map={r"\left( \frac{1}{x} \right)^2": RED})
        eq4.scale(1.5)
        eq4.shift(2.5 * DOWN)

        ans = TexMobject(r"\pi")
        ans.scale(1.5)
        ans.shift(2.5 * DOWN)

        rect = Rectangle(height=1, width=1, color=YELLOW)
        rect.shift(2.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Transform(eq1, eq2))
        self.wait()

        self.play(eq1.shift, 2.5 * UP)
        self.wait()

        self.play(Write(eq3))
        self.wait()

        self.play(Write(eq4))
        self.wait()

        self.play(Transform(eq4, ans), Write(rect))
        self.wait()


class Horn(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[eval(key) for key in COLOR_MAP.keys()],
            stroke_opacity=0
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
