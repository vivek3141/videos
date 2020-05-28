from manimlib.imports import *

maxn = 10


def func(x, b=3):
    y = 0
    for i in range(1, maxn):
        y += np.cos((b ** i) * PI * x) / (3 ** i)
    return y


class Graph(Scene):
    def construct(self):
        t = ValueTracker(0.1)
        f = FunctionGraph(func, color=GOLD).scale(5)
        axes = Axes(
            x_min=-15,
            x_max=15,
            y_min=-15,
            y_max=15,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": True,
                "exclude_zero_from_default_numbers": True,
            },
        )
        f.add_updater(lambda x: x.become(
            FunctionGraph(lambda x: func(x, t.get_value()), color=GOLD).scale(5)))

        self.play(Write(f))
        self.play(t.increment_value, 4.9,  run_time=3, rate_func=linear)
        self.wait()


class Secant(MovingCameraScene):
    CONFIG = {
        "x1": -0.4,
        "x2": -2.0,
        "down": 13.5
    }

    def construct(self):
        f = FunctionGraph(lambda x: self.f_s(x, scale=17) - self.down,
                          color=GOLD, stroke_opacity=0.5)

        self.play(Write(f))
        self.wait()
        p1 = Dot(fill_opacity=1, color=YELLOW)
        p1.shift([self.x1, self.f_s(self.x1) - self.down, 0])

        t = ValueTracker(-2)

        p2 = Dot(fill_opacity=1, color=YELLOW)
        p2.shift([t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        p2.add_updater(lambda x: x.become(
            Dot(fill_opacity=1, color=YELLOW).shift(
                [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        ))

        line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                    [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        line.scale(100)

        def line_update(l):
            line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                        [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
            line.scale(100)
            l.become(line)

        line.add_updater(line_update)

        self.play(Write(line), Write(p1), Write(p2))
        self.wait()

        self.play(t.increment_value, 1.5,  run_time=3, rate_func=linear)
        self.wait()

        grp = VGroup(f, line, p1, p2)
        self.remove(p1, p2)

        width = p1.get_width()*5

        self.play(
            self.camera_frame.set_width, width,
            self.camera_frame.move_to, p1
        )
        p1.scale(0.05)
        d = Dot(radius=0.05 * DEFAULT_DOT_RADIUS,
                color=YELLOW, point=p2.get_center())
        d.add_updater(lambda x: x.become(
            Dot(fill_opacity=1, radius=0.05 * DEFAULT_DOT_RADIUS, color=YELLOW).shift(
                [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        ))

        self.add(p1, d)
        self.wait()
        self.play(t.increment_value, 0.09, run_time=3, rate_func=linear)
        self.wait()

    def f_s_point(self, x, scale, point):
        def f(x): return self.f_s(x) - self.down
        def g(x): return f(x - point) - f(point)
        def z(x): return scale * g((1 / scale) * x)
        def ans(x): return z(x + point) + f(point)
        return ans(x)

    @staticmethod
    def func(x, b=3):
        x *= 1/10
        y = 0
        for i in range(1, maxn):
            y += np.cos((b ** i) * PI * x) / (2 ** i)
        return y

    def f_s(self, x, scale=17):
        x *= 1/scale
        return scale * self.func(x)


def anti_func(x, b=3):
    y = 0
    for i in range(1, maxn):
        y += (1 / (9 ** i * PI)) * np.sin(3 ** i * PI * x)
        # y += -((b ** i) * PI) * np.sin((b ** i) * PI * x) / 3 ** i
        #y += np.cos((b ** i) * PI * x) / (3 ** i)
    return y


class AntiDerivative(Scene):
    def construct(self):
        r_axes = axes = Axes(
            x_min=0,
            x_max=6,
            y_min=-1,
            y_max=1,
            axis_config={"include_tip": False}
        )
        r_axes.shift(3 * LEFT)
        # r_axes.set_opacity(0.5)

        c2 = ParametricFunction(
            self.w_func,
            t_min=0,
            t_max=6,
            color=RED,
        ).shift(3 * LEFT)

        fgrp = VGroup(r_axes, c2)
        fgrp.shift(1.5 * DOWN)

        t = ValueTracker(0)

        grp = VGroup()

        def updater(x):
            rect = self.get_rect(t.get_value())
            x.add_to_back(rect)
            self.bring_to_back(x)
        grp.add_updater(updater)

        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=-1,
            y_max=1,
            axis_config={"include_tip": False}
        )

        def updater2(x):
            f = FunctionGraph(self.anti, x_min=-0.01, x_max=t.get_value())
            f.shift(3 * LEFT + 1.5 * UP)
            x.become(f)

        f2 = FunctionGraph(self.anti, x_min=0, x_max=6)
        f2.add_updater(updater2)

        grp2 = VGroup(axes, f2)
        grp2.shift(3 * LEFT + 1.5 * UP)

        self.play(Write(fgrp), Write(grp))
        self.play(Write(axes), Write(f2))
        self.bring_to_back(grp)
        self.wait()
        self.play(t.increment_value, 6,  run_time=6, rate_func=linear)
        self.wait()

    def anti(self, x, dx=0.1):
        return 20 * anti_func(x / 5)

    @staticmethod
    def w_func(t):
        return [t, 2.5 * func(t / 5), 0]

    def get_rect(self, t, dx=0.025):
        y = self.w_func(t)[1]
        pairity = -1 if y < 0 else (0 if y == 0 else 1)

        return Line(
            ORIGIN,
            pairity * (abs(y) - dx) * UP,
            stroke_width=8,
            stroke_opacity=0.75,
            color=BLUE_E
        ).set_opacity(0.75).shift(3 * LEFT + 1.5 * DOWN + (t * RIGHT))


class TestScene(Scene):
    def construct(self):
        l = Line(ORIGIN, 2 * RIGHT)

        

