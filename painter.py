from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        fig = PiCreature()

        self.play(Write(fig))
        self.wait()


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
            tex_to_color_map={
                r"\left( \frac{1}{x} \right)^2": RED,
                r"\pi": GREEN,
                r"_1^t": BLUE
            }
        )
        eq1.scale(1.5)

        eq2 = TexMobject(
            r"\lim_{t \rightarrow \infty} \int_1^{t} \pi \left( \frac{1}{x} \right)^2 dx",
            tex_to_color_map={
                r"\left( \frac{1}{x} \right)^2": RED,
                r"\pi": GREEN,
                r"_1^{t}": BLUE
            }
        )
        eq2.scale(1.5)

        eq3 = TexMobject(
            r"= \pi \lim_{t \rightarrow \infty} \left ( \frac{-1}{x} \right ) \Big |_1^t",
            tex_to_color_map={
                r"\left ( \frac{-1}{x} \right )": RED,
                r"\pi": GREEN,
                r"_1^t": BLUE
            }
        )
        eq3.scale(1.5)

        eq4 = TexMobject(
            r"= \pi \lim_{t \rightarrow \infty} \frac{-1}{t} + 1",
            tex_to_color_map={
                r"\left( \frac{1}{x} \right)^2": RED,
                r"\pi": GREEN,
                r"_1^t": BLUE
            }
        )
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


class SurfaceArea(ThreeDScene):
    def construct(self):
        frustum = ParametricSurface(
            self.frustum,
            u_min=0,
            u_max=2*PI,
            v_min=1,
            v_max=3,
            checkerboard_colors=[]
        )

        horn = ParametricSurface(
            self.horn,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[eval(key) for key in COLOR_MAP.keys()],
            stroke_opacity=0
        )
        """
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.begin_ambient_camera_rotation()

        self.play(Write(horn))
        self.wait()

        self.play(Write(frustum))
        self.wait()

        self.play(Uncreate(horn))
        """
        self.play(frustum.center)
        self.play(frustum.rotate, 0)
        # self.wait()
        # self.stop_ambient_camera_rotation()

        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES)
        self.play(frustum.scale, 2)
        # self.wait()

        l = Line(2.2*LEFT, 2*RIGHT, color=YELLOW, stroke_width=1.5 *
                 DEFAULT_STROKE_WIDTH).shift(0.667*UP)

        l2 = Line(0.667*UP, 2.1*UP, color=RED, stroke_width=1.5 *
                  DEFAULT_STROKE_WIDTH).shift(2.2*LEFT)

        l3 = Line(2*RIGHT, 2.2*LEFT + 2.1*UP, color=PURPLE, stroke_width=1.5 *
                  DEFAULT_STROKE_WIDTH)

        self.play(Write(l))
        self.wait()

        self.play(Write(l2))
        self.wait()

        self.play(Write(l3))
        self.wait()

    @staticmethod
    def frustum(u, v, r=1/3):
        return np.array([
            -v-1,
            r*v*np.cos(u),
            r*v*np.sin(u),
        ])

    @staticmethod
    def horn(u, v):
        return np.array([
            u-5,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])


class SurfaceEval(Scene):
    def construct(self):
        eq1 = TexMobject(
            r"\int_{1}^{\infty} 2\pi\frac{1}{x}ds",
            tex_to_color_map={
                r"\frac{1}{x}": RED,
                r"ds": YELLOW,
                r"2\pi": GREEN,
                r"_1^t": BLUE
            }
        )
        eq1.scale(1.5)

        eq1b = TexMobject(
            r"\int_{1}^{\infty} 2\pi\frac{1}{x} \sqrt{1+\left ( \frac{-1}{x^2} \right )^2} dx",
            tex_to_color_map={
                r"\frac{1}{x}": RED,
                r"2\pi": GREEN,
                r"_1^t": BLUE,
                r"\sqrt{1+\left ( \frac{-1}{x^2} \right )^2}": YELLOW
            }
        )
        eq1b.scale(1.5)

        eq2 = TexMobject(
            r"\int_{1}^{\infty} 2\pi\frac{1}{x} \sqrt{1+\left ( \frac{-1}{x^2} \right )^2} dx \geq \int_{1}^{\infty} 2\pi\frac{1}{x}dx",
            tex_to_color_map={
                r"\frac{1}{x}": RED,
                r"2\pi": GREEN,
                r"_1^t": BLUE,
                r"\sqrt{1+\left ( \frac{-1}{x^2} \right )^2}": YELLOW
            }
        )
        eq2.scale(1.5)

        eq2b = TexMobject(
            r"\int_{1}^{\infty} 2\pi\frac{1}{x}dx",
            tex_to_color_map={
                r"\frac{1}{x}": RED,
                r"2\pi": GREEN,
                r"_1^t": BLUE,
                r"\sqrt{1+\left ( \frac{-1}{x^2} \right )^2}": YELLOW
            }
        )
        eq2b.scale(1.5)

        eq2c = TexMobject(
            r"\lim_{t \rightarrow \infty} \int_{1}^{t} 2\pi\frac{1}{x}dx",
            tex_to_color_map={
                r"\frac{1}{x}": RED,
                r"2\pi": GREEN,
                r"_{1}^{t}": BLUE,
                r"\sqrt{1+\left ( \frac{-1}{x^2} \right )^2}": YELLOW
            }
        )
        eq2c.scale(1.5)

        eq3 = TexMobject(
            r"= 2\pi \lim_{t \rightarrow \infty} \ln(x) \Big |_1^t",
            tex_to_color_map={
                r"\left ( \frac{-1}{x} \right )": RED,
                r"2\pi": GREEN,
                r"_1^t": BLUE
            }
        )
        eq3.scale(1.5)

        eq4 = TexMobject(
            r"= 2\pi \lim_{t \rightarrow \infty} \ln(t)",
            tex_to_color_map={
                r"\left( \frac{1}{x} \right)^2": RED,
                r"2\pi": GREEN,
                r"_1^t": BLUE
            }
        )
        eq4.scale(1.5)
        eq4.shift(2.5 * DOWN)

        ans = TexMobject(r"\infty")
        ans.scale(1.5)
        ans.shift(2.5 * DOWN)

        rect = Rectangle(height=1, width=1, color=YELLOW)
        rect.shift(2.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Transform(eq1, eq1b))
        self.wait()

        self.play(Transform(eq1, eq2))
        self.wait()

        self.play(Transform(eq1, eq2b))
        self.wait()

        self.play(Transform(eq1, eq2c))
        self.wait()

        self.play(eq1.shift, 2.5 * UP)
        self.wait()

        self.play(Write(eq3))
        self.wait()

        self.play(Write(eq4))
        self.wait()

        self.play(Transform(eq4, ans), Write(rect))
        self.wait()


class TwoConverge(Scene):
    def construct(self):
        line = NumberLine(
            include_numbers=True,
            x_min=-5,
            x_max=10,
            unit_size=6,
            tick_frequency=0.25,
            decimal_number_config={
                "num_decimal_places": 1,
            },
            scale_factor=0.5,
        )

        line.numbers = [DecimalNumber(number=i.number*0.5)
                        for i in line.numbers]

        line.add_numbers()
        line.shift(6 * LEFT)

        s = Line(6*LEFT, ORIGIN, stroke_width=2 *
                 DEFAULT_STROKE_WIDTH, color=YELLOW)

        eq1 = TexMobject(r"\sum_{n=1}^{\infty} \frac{1}{2^n}")
        eq1.shift(2 * UP)
        eq1.scale(1.5)

        eq2 = TexMobject(r"\sum_{n=1}^{\infty} \frac{1}{2^n} = 1")
        eq2.shift(2 * UP)
        eq2.scale(1.5)

        self.play(Write(line))
        self.play(Write(eq1))

        for i in range(1, 10):
            val = sum([1/(2**n) for n in range(i)])
            s = Line(6*LEFT, 6*LEFT + 6*val*RIGHT, stroke_width=2 *
                     DEFAULT_STROKE_WIDTH, color=YELLOW)
            self.add(s)
            self.wait(0.5)

        self.wait()

        self.play(Transform(eq1, eq2))
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
        self.begin_ambient_camera_rotation(rate=0.04)
        self.wait(20)

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])


class Torricelli(Scene):
    def construct(self):
        text = TextMobject("Evangelista Torricelli")
        text.scale(2)
        self.play(Write(text))
        self.wait()


class TextScene(Scene):
    def construct(self):
        text = TexMobject(self.text)
        text.scale(2)
        self.play(Write(text))
        self.wait()


class OneX(TextScene):
    CONFIG = {"text": r"\frac{1}{x}"}


class VDisk(TextScene):
    CONFIG = {"text": r"V = \pi \left( \frac{1}{x} \right) ^2 dx"}


class SFrustum(TextScene):
    CONFIG = {"text": r"S = 2\pi r l"}
