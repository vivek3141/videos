from manimlib.imports import *


class Intro(Scene):
    CONFIG = {"default_riemann_start_color": BLUE,
              "default_riemann_end_color": GREEN,
              "area_opacity": 0.8,
              "num_rects": 50, }

    def construct(self):
        f = ParametricFunction(
            function=self.func,
            t_min=-3,
            t_max=3,
            color=BLUE
        )

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        rect = self.get_riemann_sums(self.func)
        rect.scale(1.95)
        rect.shift(2.4 * DOWN)

        func = VGroup(axes, f)
        func.scale(2)
        func.shift(2 * DOWN)

        eq1 = TexMobject(r"f(x) = e^{-x^2}")
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        eq2 = TexMobject(r"\int_{-\infty}^{\infty} e^{-x^2} \ dx = \sqrt{\pi}")
        eq2.scale(1.5)
        eq2.shift(3 * UP)

        self.play(Write(func))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Write(rect), Transform(eq1, eq2))
        self.wait()

    @staticmethod
    def get_riemann_sums(func, dx=0.01, x=(-3, 3), color=RED):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[1]
            rect = Rectangle(height=h, width=dx, color=color,
                             stroke_opacity=0.3, fill_opacity=0.3)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects

    def func(self, t):
        return np.array([t, np.exp(-t**2), 0])


class DefiniteIntegral(Scene):
    def construct(self):
        graph = ParametricFunction(
            function=lambda t: np.array([t, t ** 2, 0]),
            t_min=-1,
            t_max=2,
            color=RED
        )
        axes = Axes(
            x_min=-1,
            x_max=3,
            y_min=0,
            y_max=4
        )

        rects = self.get_riemann_sums(lambda t: np.array([t, t ** 2, 0]))
        func = VGroup(graph, axes, rects)
        func.shift(3.5 * LEFT + 2 * DOWN)

        eq1 = TexMobject(r"\int_1^2 x^2 dx")
        eq1.shift(1.5 * RIGHT + 3 * UP)

        eq2 = TexMobject(r"= \frac{x^3}{3} \Big|_1^2")
        eq2.shift(1.5 * RIGHT + 1 * UP)

        eq3 = TexMobject(r"= \frac{2^3}{3} - \frac{1^3}{3}")
        eq3.shift(1.5 * RIGHT + 1 * DOWN)

        eq4 = TexMobject(r"= \frac{7}{3}")
        eq4.shift(1.5 * RIGHT + 3 * DOWN)

        self.play(Write(eq1), Write(func))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))

        self.wait()

    @staticmethod
    def get_riemann_sums(func, dx=0.01, x=(1, 2), color=GREEN):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[1]
            rect = Rectangle(height=h-dx, width=dx, color=color,
                             stroke_opacity=0.3, fill_opacity=0.3)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects


class Nonelem(Scene):
    def construct(self):
        eq = TexMobject(r"\int e^{-x^2} dx")
        eq.scale(1.5)

        brace = Brace(eq)
        text = brace.get_text("Nonelementary")

        self.play(Write(eq))
        self.play(Write(brace))



class GaussianVisual(ThreeDScene):
    def construct(self):
        s = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        )

        axes = ThreeDAxes(
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        conf = {"fill_color": ORANGE,
                "fill_opacity": 1.0,
                "checkerboard_colors": [ORANGE, RED],
                "stroke_color": RED,
                "stroke_width": 0.5, }

        const = self.func(0, 1)[-1]
        cyln = ParametricSurface(
            self.cyln,
            u_min=0,
            u_max=2*PI,
            v_min=0,
            v_max=const,
            **conf
        ).scale(2)

        surface = VGroup(axes, s)
        surface.scale(2)

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

        # self.begin_ambient_camera_rotation()
        # self.wait(5)

        s.set_style(fill_opacity=0.25,
                    stroke_opacity=0.25)
        self.play(Write(cyln))
        self.wait()

        # self.begin_ambient_camera_rotation()
        # self.wait(5)

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])

    def cyln(self, u, v):
        return np.array([
            np.cos(u),
            np.sin(u),
            v
        ])
