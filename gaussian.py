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
            rect = Rectangle(height=h, width=dx, color=color, stroke_opacity=0.3, fill_opacity=0.3)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects

    def func(self, t):
        return np.array([t, np.exp(-t**2), 0])


class GaussianVisual(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        ).scale(2)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])
