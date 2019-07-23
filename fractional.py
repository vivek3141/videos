from manimlib.imports import *
import scipy.special
from mpmath import differint
from sympy import Float
import mpmath as mp


class Intro(Scene):
    def construct(self):
        f = ParametricFunction(
            self.func,
            t_min=0,
            t_max=1.75,
            color=GREEN
        )
        curve = ParametricFunction(
            self.func,
            t_min=0.1,
            t_max=0.9,
            color=RED,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        axes = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        line = Line(ORIGIN + 0.01 * UP, 1 * RIGHT + 0.01 * UP,
                    stroke_width=DEFAULT_STROKE_WIDTH*1.25, color=RED)
        line.shift(1.3125 * UP)

        fun = VGroup(axes, f)

        func = VGroup(fun, line, curve)
        func.scale(2.5)
        func.shift(2 * LEFT + 1 * DOWN)

        eq1 = TexMobject(r"\frac{dy}{dx}")
        eq1.scale(2)
        eq1.shift(4 * RIGHT)

        eq2 = TexMobject(r"\frac{d^2y}{dx^2}")
        eq2.scale(2)
        eq2.shift(4 * RIGHT)

        self.play(Write(fun))
        self.wait()

        self.play(Write(eq1), Write(line))
        self.wait()

        self.play(Transform(eq1, eq2), Transform(line, curve))
        self.wait()

    @staticmethod
    def func(t):
        return np.array([
            t,
            t**4 - 2*t**3 + t + 1,
            0
        ])


class NDeriv(Scene):
    def construct(self):
        eq1 = TexMobject(r"\frac{d^nf}{dx^n}")
        eq1.scale(2)

        eq2 = TexMobject(r"\left (\frac{d}{dx} ... \frac{d}{dx}\right )", "f")
        eq2.scale(2)

        b = Brace(eq2[0])
        t = b.get_text("n times").scale(1.5)

        t1 = TextMobject("Only for positive integers",
                         tex_to_color_map={"integers": YELLOW})
        t1.scale(1.5)
        t1.shift(3 * UP)

        self.play(Write(eq1))
        self.wait()

        self.play(Transform(eq1, eq2), Write(b), Write(t))
        self.wait()

        self.play(Write(t1))
        self.wait()


class FracConfus(Scene):
    def construct(self):
        eq = TexMobject(r"\frac{d^{\frac{1}{2}}f}{dx^{{\frac{1}{2}}}} =  \ ?")
        eq.scale(3)

        self.play(Write(eq))
        self.wait()


class MultipleDeriv(Scene):
    def construct(self):
        title = TexMobject(r"\text{What does } \frac{d^nf}{dx^n} \text{ mean?}",
                           tex_to_color_map={r"\frac{d^nf}{dx^n}": YELLOW}
                           )
        title.scale(2)

        title2 = TexMobject(r"\text{What does } \frac{d^nf}{dx^n} \text{ mean?}",
                            tex_to_color_map={r"\frac{d^nf}{dx^n}": YELLOW}
                            )
        title2.shift(3 * UP)

        eq = TexMobject(
            r"\frac{d^nf}{dx^n}=", r"\left (\frac{d}{dx} ... \frac{d}{dx}\right )", r"f")
        eq.scale(1.5)

        b = Brace(eq[1])
        t = b.get_text("n times").scale(1.5)

        eq1 = VGroup(eq, b, t)

        f1 = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=0,
            t_max=math.sqrt(2),
            color=RED,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a1 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func1 = VGroup(a1, f1)
        func1.scale(1.5)
        func1.shift(4.5 * LEFT + 1 * DOWN)

        f2 = ParametricFunction(
            lambda t: np.array([t, 2*t, 0]),
            t_min=0,
            t_max=1,
            color=BLUE,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a2 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func2 = VGroup(a2, f2)
        func2.scale(1.5)
        func2.shift(3 * RIGHT + 1 * DOWN)

        a = Arrow(1 * LEFT, 1 * RIGHT, color=GREEN)
        a.scale(1.5)

        t = TexMobject(r"\frac{d}{dx}")
        t.shift(1 * UP)

        arr = VGroup(a, t)

        self.play(Write(title))
        self.wait()

        self.play(Transform(title, title2))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Uncreate(eq1))
        self.play(Write(func1))
        self.wait()

        self.play(Write(arr))
        self.play(TransformFromCopy(func1, func2))
        self.wait()


class MultipleInt(Scene):
    def construct(self):
        a = 20

        eq1 = TexMobject(r"If(x) = \int_0^x f(t) dt",
                         )
        eq1.scale(1.25)
        eq1.shift(2.5 * UP)

        eq2 = TexMobject(
            r"(I^3f)(x)=\int_0^x\left[\int_0^t \left(\int_0^s f(u)\,du\right)\, ds \right]\,dt")
        eq2.scale(1.25)
        eq2.shift(2.5 * UP)

        f1 = ParametricFunction(
            lambda t: np.array([t, a*t**2, 0]),
            t_min=-0.205,
            t_max=0.205,
            color=RED,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a1 = Axes(
            x_min=-1,
            x_max=1,
            y_min=-1,
            y_max=1,
            number_line_config={
                "include_tip": False,
            }
        )

        func1 = VGroup(a1, f1)
        func1.scale(1.5)
        func1.shift(3 * LEFT + 1 * DOWN)

        f2 = ParametricFunction(
            lambda t: np.array([t, a*t**3 / 3, 0]),
            t_min=-0.5,
            t_max=0.5,
            color=BLUE,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a2 = Axes(
            x_min=-1,
            x_max=1,
            y_min=-1,
            y_max=1,
            number_line_config={
                "include_tip": False,
            }
        )

        func2 = VGroup(a2, f2)
        func2.scale(1.5)
        func2.shift(3 * RIGHT + 1 * DOWN)

        f3 = ParametricFunction(
            lambda t: np.array([t, a*t**5 / (5*4*3), 0]),
            t_min=-1,
            t_max=1,
            color=YELLOW,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a3 = Axes(
            x_min=-1,
            x_max=1,
            y_min=-1,
            y_max=1,
            number_line_config={
                "include_tip": False,
            }
        )
        func3 = VGroup(a3, f3)
        func3.scale(1.5)
        func3.shift(3 * RIGHT + 1 * DOWN)

        a = Arrow(0.5 * LEFT, 0.5 * RIGHT, color=GREEN).scale(1.5)
        a.shift(1 * DOWN)

        t = TexMobject(r"\int")
        t2 = TexMobject(r"\iiint")

        arr = VGroup(a, t)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(func1))
        self.wait()

        self.play(Write(arr))
        self.play(TransformFromCopy(func1, func2))
        self.wait()

        self.play(Transform(eq1, eq2),
                  Uncreate(func2), Transform(t, t2),
                  )
        self.wait()

        self.play(TransformFromCopy(func1, func3))
        self.wait()


class CauchyFormula(Scene):
    def construct(self):
        title = TextMobject(
            "Cauchy's formula for repeated integration", color=GREEN)
        title.scale(1.25)
        title.shift(2.5 * UP)

        eq = TexMobject(
            r"I^n f(x) = \frac{1}{(n-1)!} \int_{a}^{x} (x-t)^{n-1} f(t) dt",
        )
        eq.scale(1.5)

        eq1 = TexMobject(
            r"I^n f(x) = \frac{1}{(n-1)!} \int_{a}^{x} (x-t)^{n-1} f(t) dt")
        eq1.shift(2.5 * UP + 1.5 * LEFT)

        eq2 = TexMobject(
            r"g(x) = \int_0^x (x-t) f(t) dt")
        eq2.scale(1.5)

        eq3 = TexMobject(
            r"g(x) = x\int_0^x f(t)\,dt - \int_0^x tf(t)\, dt")
        eq3.scale(1.5)

        eq4 = TexMobject(
            r"g'(x) = \left[\int_0^x f(t)\,dt +xf(x)\right]- xf(x)")
        eq4.scale(1.5)

        eq5 = TexMobject(
            r"g'(x) = \int_0^x f(t)\,dt")
        eq5.scale(1.5)

        eq6 = TexMobject(
            r"g'(x) = If(x)")
        eq6.scale(1.5)

        eq7 = TexMobject(
            r"g(x) = g(x) - g(0)")
        eq7.scale(1.5)

        eq8 = TexMobject(
            r"g(x) = \int_0^x g'(t)\,dt")
        eq8.scale(1.5)

        eq9 = TexMobject(
            r"g(x) = I^2f(x)")
        eq9.scale(1.5)

        r = Rectangle(height=2, width=5, color=YELLOW,
                      stroke_width=2 * DEFAULT_STROKE_WIDTH)

        t1 = TexMobject(r"n=2")
        r1 = Rectangle(height=1, width=2, color=RED)
        t = VGroup(t1, r1)
        t.shift(5 * RIGHT + 2.5 * UP)

        t2 = TexMobject(r"n=2").shift(0.5 * UP)
        t3 = TexMobject(r"g(0) = 0").shift(0.5 * DOWN)
        r2 = Rectangle(height=2, width=2, color=RED)
        tt = VGroup(t3, r2, t2)
        tt.shift(5 * RIGHT + 2.5 * UP)

        self.play(
            Write(title),
            Write(eq)
        )
        self.wait()

        self.play(
            Uncreate(title),
            Transform(eq, eq1)
        )
        self.play(Write(t))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Transform(eq2, eq3))
        self.wait()

        self.play(Transform(eq2, eq4))
        self.wait()

        self.play(Transform(eq2, eq5))
        self.wait()

        self.play(Transform(eq2, eq6))
        self.wait()

        self.play(ApplyMethod(eq2.shift, 3 * DOWN))
        self.play(
            Transform(t, tt),
            Write(eq7)
        )
        self.wait()

        self.play(Transform(eq7, eq8))
        self.wait()

        self.play(Transform(eq7, eq9))
        self.wait()

        self.play(Write(r))
        self.wait()


class Challenge(Scene):
    def construct(self):
        title = TextMobject("Challenge", color=GREEN)
        title.scale(2)
        title.shift(3.5 * UP)

        eq1 = TexMobject(r"\text{Show that}")
        eq2 = TexMobject(
            r"I^n f(x) = \frac{1}{(n-1)!} \int_{a}^{x} (x-t)^{n-1} f(t) dt")
        eq3 = TexMobject(r"\text{for } n \in \mathbb{N}")

        hint1 = TexMobject(r"\text{Hint: Use Binomial Theorem}")
        hint2 = TexMobject(
            r"(x+y)^n = \sum_{k=0}^{k=n} \left ( ^n_k \right ) x^{n-k}y^k")
        hint1.shift(1 * DOWN)
        hint2.shift(2.5 * DOWN)

        eq1.shift(2 * UP)
        eq2.shift(1 * UP)
        eq3.shift(0 * DOWN)

        self.add(title)
        self.add(eq1)
        self.add(eq2)
        self.add(eq3)
        self.add(hint1)
        self.add(hint2)
        self.wait()


class GammaFunc(Scene):
    CONFIG = {
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1.25,
        "p_color": YELLOW,
        "p_width": 0.1
    }

    def construct(self):
        f1 = ParametricFunction(
            self.func,
            t_min=-4.99,
            t_max=-4.01,
            color=self.g_color,
            stroke_width=self.g_width
        )
        f2 = ParametricFunction(
            self.func,
            t_min=-3.99,
            t_max=-3.01,
            color=self.g_color,
            stroke_width=self.g_width
        )
        f3 = ParametricFunction(
            self.func,
            t_min=-2.99,
            t_max=-2.01,
            color=self.g_color,
            stroke_width=self.g_width
        )
        f6 = ParametricFunction(
            self.func,
            t_min=-1.99,
            t_max=-1.01,
            color=self.g_color,
            stroke_width=self.g_width
        )
        f4 = ParametricFunction(
            self.func,
            t_min=-0.99,
            t_max=-0.01,
            color=self.g_color,
            stroke_width=self.g_width
        )
        f5 = ParametricFunction(
            self.func,
            t_min=0.01,
            t_max=4,
            color=self.g_color,
            stroke_width=self.g_width
        )

        a1 = Axes(
            x_min=-5,
            x_max=5,
            y_min=-4,
            y_max=4,
            number_line_config={
                "include_tip": False,
            }
        )

        p1 = Circle(radius=self.p_width, color=self.p_color, fill_opacity=1).shift(
            1 * RIGHT + 1 * UP)
        p2 = Circle(radius=self.p_width, color=self.p_color, fill_opacity=1).shift(
            2 * RIGHT + 1 * UP)
        p3 = Circle(radius=self.p_width, color=self.p_color, fill_opacity=1).shift(
            3 * RIGHT + 2 * UP)
        p = VGroup(p1, p2, p3)

        rect = Rectangle(height=8, width=10.5, stroke_width=self.g_width)
        gfunc = VGroup(a1, f1, f2, f3, f4, f5, f6, rect)
        g = VGroup(p, gfunc)

        g.scale(0.8)
        g.shift(0.7 * DOWN)

        title = TexMobject(r"\text{Gamma Function }\Gamma (x)", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        title2 = TextMobject(r"Challenge 2", color=GREEN)
        title2.scale(1.5)
        title2.shift(3 * UP)

        eq1 = TextMobject(r"Show that")
        eq2 = TexMobject(
            r"\Gamma(n) = \int_0^{\infty} e^{-t}t^{n-1} dt")
        eq2.scale(1.5)
        eq3 = TexMobject(r"\text{for } n \in \mathbb{N}")

        hint1 = TexMobject(r"\text{Hint: Integration by parts}")

        hint1.shift(3 * DOWN)

        eq1.shift(2 * UP)
        eq2.shift(2 * LEFT)
        eq3.shift(2 * DOWN)

        self.play(Write(gfunc), Write(title))
        self.wait()

        self.play(Write(p))
        self.wait()

        self.play(ApplyMethod(gfunc.scale, 0.4), Uncreate(p))
        self.play(ApplyMethod(gfunc.shift, 0.7 * UP + 4 * RIGHT))
        self.play(Write(eq2))
        self.wait()

        self.play(Transform(title, title2))
        self.play(Write(eq1), Write(eq3), Write(hint1))
        self.wait()

    @staticmethod
    def func(t):
        val = float(scipy.special.gamma(t))
        if val < 0:
            val = np.maximum(val, -4)
        elif val > 0:
            val = np.minimum(val, 4)
        else:
            val = 0
        return np.array([
            t,
            val,
            0,

        ], dtype=float)


class FractionalIntegral(Scene):
    def construct(self):
        title = TextMobject(
            "Fractional Integrals", color=YELLOW)
        title.scale(1.25)
        title.shift(2.5 * UP)

        eq1 = TexMobject(
            r"I^n f(x) = \frac{1}{(n-1)!} \int_{a}^{x} (x-t)^{n-1} f(t) dt",
        )
        eq1.scale(1.5)

        eq2 = TexMobject(
            r"I^n f(x) = \frac{1}{\Gamma(n-1)} \int_{a}^{x} (x-t)^{n-1} f(t) dt",
            tex_to_color_map={r"\Gamma(n-1)": BLUE}
        )
        eq2.scale(1.5)

        eq3 = TexMobject(r"\text{for } n \in \mathbb{C}, \text{Re}(n) > 0")
        eq3.shift(2 * DOWN)
        eq3.scale(1.5)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(title), Transform(eq1, eq2))
        self.wait()

        self.play(Write(eq3))
        self.wait()


class FracProperty(Scene):
    def construct(self):
        pass


class DifferIntegralOLD(Scene):
    CONFIG = {
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        f1 = ParametricFunction(
            lambda t: np.array([t, 0.5*t**2, 0]),
            t_min=0,
            t_max=math.sqrt(6),
            color=PINK,
            stroke_width=self.g_width
        )
        f2 = ParametricFunction(
            lambda t: np.array([t, 1, 0]),
            t_min=0,
            t_max=4,
            color=RED,
            stroke_width=self.g_width
        )

        a1 = Axes(
            x_min=0,
            x_max=4,
            y_min=0,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )
        f = ParametricFunction(
            lambda t: np.array([t, t, 0]),
            t_min=0,
            t_max=3,
            color=GREEN,
            stroke_width=self.g_width
        )

        # f.scale(1.5)
        # f.shift(1.5 * DOWN + 2.5 * LEFT)

        fs = VGroup(a1, f1, f2, f)
        fs.scale(1.5)
        fs.shift(1.5 * DOWN + 2.5 * LEFT)

        line1 = Line(1 * LEFT, 0 * RIGHT, color=PINK,
                     stroke_width=self.g_width).shift(1 * UP + 1.5 * LEFT)
        line2 = Line(1 * LEFT, 0 * RIGHT, color=GREEN,
                     stroke_width=self.g_width).shift(0 * UP + 1.5 * LEFT)
        line3 = Line(1 * LEFT, 0 * RIGHT, color=RED,
                     stroke_width=self.g_width).shift(1 * DOWN + 1.5 * LEFT)

        t1 = TexMobject(r"\int f(x)dx = \frac{1}{2}x^2").shift(
            1 * UP + 0.5 * RIGHT)
        t2 = TexMobject(r"f(x) = x").shift(0.5 * RIGHT)
        t3 = TexMobject(r"\frac{d}{dx} f(x) = 1").shift(1 * DOWN + 0.5 * RIGHT)

        rect = Rectangle(height=4, width=6)

        legend = VGroup(line1, line2, line3, t1, t2, t3, rect).scale(0.5)
        legend.shift(2.5 * UP + 5 * RIGHT)

        self.play(Write(fs))
        self.play(Write(legend))
        self.wait()

        self.play(ShowCreation(f))
        self.wait()

        self.play(UpdateFromAlphaFunc(f, self.f_update),
                  rate_func=there_and_back, run_time=4)
        self.wait()

    @staticmethod
    def _func(t):
        return t

    def func(self, t):
        return np.array([
            t,
            self._func(t),
            0
        ])

    def f_update(self, ff, dt):
        a = interpolate(-1, 1, dt)
        f = ParametricFunction(
            lambda t: np.array(
                [t, self.dint(t, a), 0]),
            t_min=0,
            t_max=math.sqrt(6),
            color=GREEN,
            stroke_width=self.g_width
        )
        point = 1.5 * DOWN + 2.5 * LEFT
        f.shift(point)
        f.scale(1.5, about_point=point)

        ff.become(f)

    def dint(self, x, a, k=1):
        return (scipy.special.gamma(k+1)/scipy.special.gamma(k-a+1)) * (x**(k-a))


class DifferIntegral(GraphScene):
    CONFIG = {
        "y_max": 3,
        "y_min": 0,
        "x_max": 4,
        "x_min": 0,
        "y_tick_frequency": 5,
        "axes_color": BLUE,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            lambda t:  0.5*t**2,
            color=PINK,
        )
        f2 = self.get_graph(
            lambda t: 1,
            color=RED,
        )
        f = self.get_graph(
            lambda t: t,
            color=GREEN,
        )

        line1 = Line(1 * LEFT, 0 * RIGHT, color=PINK,
                     stroke_width=self.g_width).shift(1 * UP + 1.5 * LEFT)
        line2 = Line(1 * LEFT, 0 * RIGHT, color=GREEN,
                     stroke_width=self.g_width).shift(0 * UP + 1.5 * LEFT)
        line3 = Line(1 * LEFT, 0 * RIGHT, color=RED,
                     stroke_width=self.g_width).shift(1 * DOWN + 1.5 * LEFT)

        t1 = TexMobject(r"\int f(x)dx = \frac{1}{2}x^2").shift(
            1 * UP + 0.5 * RIGHT)
        t2 = TexMobject(r"f(x) = x").shift(0.5 * RIGHT)
        t3 = TexMobject(r"\frac{d}{dx} f(x) = 1").shift(1 * DOWN + 0.5 * RIGHT)

        rect = Rectangle(height=4, width=6)

        legend = VGroup(line1, line2, line3, t1, t2, t3, rect).scale(0.5)
        legend.shift(2.5 * UP + 5 * RIGHT)

        self.play(Write(f1), Write(f2))
        self.play(Write(legend))
        self.wait()

        self.play(ShowCreation(f))
        self.wait()

        self.play(UpdateFromAlphaFunc(f, self.f_update1),
                  rate_func=there_and_back, run_time=2)
        self.play(UpdateFromAlphaFunc(f, self.f_update2),
                  rate_func=there_and_back, run_time=2)
        self.wait()

    def f_update1(self, ff, dt):
        a = interpolate(0, 1, dt)
        f = self.get_graph(
            lambda t: self.dint(t, a),
            color=GREEN,
        )

        ff.become(f)

    def f_update2(self, ff, dt):
        a = interpolate(0, -1, dt)
        f = self.get_graph(
            lambda t: self.dint(t, a),
            color=GREEN,
        )

        ff.become(f)

    def dint(self, x, a, k=1):
        return (scipy.special.gamma(k+1)/scipy.special.gamma(k-a+1)) * (x**(k-a))


class RLProperty(Scene):
    def construct(self):
        title = TextMobject("Properties of R-L Integrals", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        eq1 = TexMobject(r"1. I^{a+b} = I^aI^bf")
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(r"2. \frac{d}{dx} I^{a+1} = I^a")
        eq2.scale(1.5)
        eq2.shift(1.5 * DOWN)

        eq3 = TextMobject("1st fundamental theorem of calculus", color=RED)
        eq3.shift(3 * DOWN)

        rect = Rectangle(width=5, height=2, color=YELLOW,
                         stroke_width=1.25 * DEFAULT_STROKE_WIDTH)
        rect.shift(1.5 * DOWN)

        self.play(
            Write(eq1),
            Write(eq2),
            Write(title)
        )
        self.wait()

        self.play(Write(rect))
        self.play(Write(eq3))
        self.wait()


class CeilFunc(Scene):
    def construct(self):
        func = VGroup(
            FunctionGraph(
                lambda x: math.ceil(x),
                x_min=0,
                x_max=0.99
            ),
            FunctionGraph(
                lambda x: math.ceil(x),
                x_min=1.01,
                x_max=1.99
            ),
            FunctionGraph(
                lambda x: math.ceil(x),
                x_min=2.01,
                x_max=2.99
            ),
            FunctionGraph(
                lambda x: math.ceil(x),
                x_min=3.01,
                x_max=3.99
            ),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                1 * UP + 0 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                1 * UP + 1 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                2 * UP + 1 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                2 * UP + 2 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                3 * UP + 2 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                3 * UP + 3 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                4 * UP + 3 * RIGHT),
            Circle(radius=0.1, color=WHITE, fill_opacity=1).shift(
                4 * UP + 4 * RIGHT),

        )
        axes = Axes(
            x_min=0,
            x_max=4,
            y_min=0,
            y_max=4,
            number_line_config={
                "include_tip": False,
            }
        )
        f = VGroup(axes, func)
        f.scale(1.25)
        f.center()
        f.shift(0.5 * DOWN)

        title = TexMobject(r"\text{ceil}(x) = \lceil x \rceil", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        examples = TexMobject(
            r"\text{ceil}(4.1) = 5 \\", r"\text{ceil}(4.6) = 5 \\", r"\text{ceil}(4.0) = 4 \\",
            tex_to_color_map={r"\text{ceil}": GREEN})
        examples.scale(1.5)
        examples.shift(3.5 * RIGHT)

        self.play(Write(f), Write(title))
        self.wait()

        self.play(
            ApplyMethod(title.shift, 2 * LEFT),
            ApplyMethod(f.shift, 2 * LEFT)
        )
        self.play(
            Write(examples)
        )
        self.wait()


class FracNo(Scene):
    def construct(self):
        eq = TexMobject(r"\frac{d^n}{dx^n} = I^{-n}")
        eq.scale(1.5)

        c = VGroup(
            Line(UP + LEFT, DOWN + RIGHT, color=RED),
            Line(UP + RIGHT, DOWN + LEFT, color=RED),
        )

        e = VGroup(eq, c)

        er = TexMobject(
            r"\Gamma(x) \text{ is not defined for }n < 0", color=RED)
        er.scale(1.5)
        er.shift(2 * DOWN)

        self.play(Write(eq))
        self.wait()

        self.play(Write(c))
        self.play(Write(er))
        self.wait()


class FracDeriv(Scene):
    def construct(self):
        eq1 = TexMobject(r"\frac{d^nf}{dx^n}(I^nf(t)) = f(t)")
        eq1.scale(1.5)

        rect = Rectangle(width=7, height=2, color=YELLOW,
                         stroke_width=1.25 * DEFAULT_STROKE_WIDTH)

        t1 = TexMobject(
            r"\text{We are trying to preserve this}", color=RED)
        t1.scale(1.5)
        t1.shift(2 * DOWN)

        eq2 = TexMobject(
            r"D^n f = \frac{d^{\lceil n \rceil}}{dx^{\lceil n \rceil}} \left(I^{\lceil n \rceil - n} f \right)")
        eq2.scale(1.5)

        eq3 = TexMobject(
            r"D^n f(x) = \frac{1}{\Gamma(\lceil n \rceil - n)} \frac{d}{dx^{\lceil n \rceil}} \int_{a}^{x} (x-t)^{\lceil n \rceil - n -1} f(t) dt}")
        eq3.scale(1)

        title1 = TextMobject("Fractional Derivative", color=BLUE)
        title1.scale(1.5)
        title1.shift(2 * UP)

        title2 = TextMobject(
            "Left Riemann-Liouville Fractional Derivative", color=BLUE)
        title2.scale(1)
        title2.shift(2 * UP)

        self.play(Write(eq1))
        self.play(
            Write(rect),
            Write(t1)
        )
        self.wait()

        self.play(
            Uncreate(eq1),
            Uncreate(rect),
            Uncreate(t1)
        )
        self.play(
            Write(eq2),
            Write(title1)
        )
        self.wait()

        self.play(
            Transform(eq2, eq3),
            Transform(title1, title2)
        )
        self.wait()


class DifferEquation(Scene):
    def construct(self):
        eq1 = TexMobject(r"D^a f").shift(1 * UP)
        eq2 = TexMobject(r"f").shift(0 * UP)
        eq3 = TexMobject(r"I^{|a|}").shift(-1 * UP)

        eq1.align_to(eq2, LEFT)
        eq3.align_to(eq2, LEFT)

        t1 = TexMobject(r"\text{if } a > 0").shift(1 * UP + 2 * RIGHT)
        t2 = TexMobject(r"\text{if } a = 0").shift(0 * UP + 2 * RIGHT)
        t3 = TexMobject(r"\text{if } a < 0").shift(-1 * UP + 2 * RIGHT)

        t1.align_to(t2, LEFT)
        t3.align_to(t2, LEFT)

        e = VGroup(eq1, eq2, eq3)
        t = VGroup(t1, t2, t3)
        et = VGroup(e, t)

        b = Brace(et, LEFT)
        bt = b.get_tex(r"J^af = ")
        eq = VGroup(et, b, bt)

        eq.scale(1.5)
        eq.center()
        eq.shift(0.5 * DOWN)

        title = TextMobject("Differintegral Operator", color=YELLOW)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(Write(eq), Write(title))
        self.wait()


class Cycloid(ParametricFunction):
    CONFIG = {
        "point_a": 3*LEFT+2*UP,
        "radius": 2,
        "end_theta": np.pi,
        "density": 5*DEFAULT_POINT_DENSITY_1D,
        "color": YELLOW
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        ParametricFunction.__init__(self, self.pos_func, **kwargs)

    def pos_func(self, t):
        T = t*self.end_theta
        return self.point_a + self.radius * np.array([
            T - np.sin(T),
            np.cos(T) - 1,
            0
        ])


class TChroneAnim(Scene):
    def construct(self):
        title = TextMobject("Tautochrone problem", color=GREEN)
        title.shift(3 * UP)
        title.scale(1.5)

        self.cyc = Cycloid(stroke_width=1.25 *
                           DEFAULT_STROKE_WIDTH, color=GRAY)

        c1 = Circle(radius=0.2, color=BLUE, fill_opacity=1, stroke_color=WHITE)
        c1.shift(3*LEFT+2*UP)

        c2 = Circle(radius=0.2, color=RED, fill_opacity=1,  stroke_color=WHITE)
        pos = self.cyc.pos_func(0.5)
        c2.move_to(pos[0] * RIGHT + pos[1] * UP)

        c3 = Circle(radius=0.2, color=GREEN,
                    fill_opacity=1,  stroke_color=WHITE)
        pos = self.cyc.pos_func(0.75)
        c3.move_to(pos[0] * RIGHT + pos[1] * UP)

        l1 = Line(3*LEFT+2*UP, 3*LEFT+2*DOWN, color=GRAY,
                  stroke_width=1.25 * DEFAULT_STROKE_WIDTH)
        l2 = Line(3*LEFT+2*DOWN, 3*RIGHT+2*DOWN, color=GRAY,
                  stroke_width=1.25 * DEFAULT_STROKE_WIDTH)

        self.play(
            Write(self.cyc),
            Write(l1),
            Write(l2),
            Write(title)
        )
        self.play(
            Write(c1),
            Write(c2),
            Write(c3)
        )
        self.wait()

        self.play(
            UpdateFromAlphaFunc(c1, lambda c, dt: self.update(c, dt, start=0)),
            UpdateFromAlphaFunc(
                c2, lambda c, dt: self.update(c, dt, start=0.5)),
            UpdateFromAlphaFunc(
                c3, lambda c, dt: self.update(c, dt, start=0.75)),
            rate_func=linear, run_time=2
        )
        self.wait()

    def update(self, c, dt, start=0):
        a = interpolate(start, 1, dt)
        pos = self.cyc.pos_func(a)
        c.move_to(pos[0] * RIGHT + pos[1] * UP)


class Nonlocality(Scene):
    def construct(self):
        title1 = TextMobject("Nonlocality", color=YELLOW)
        title1.scale(2)
        title1.shift(3 * UP)

        exp1 = TexMobject(r"D^n \text{ also depends on }a")
        exp1.scale(1.25)
        exp1.shift(2 * DOWN)

        eq1 = TexMobject(
            r"D^n_a f(x) = \frac{1}{\Gamma(\lceil n \rceil - n)} \frac{d}{dx^{\lceil n \rceil}} \int_{a}^{x} (x-t)^{\lceil n \rceil - n -1} f(t) dt}")
        eq1.scale(1)

        rect1 = Rectangle(height=0.3, width=0.3, color=RED,
                          stroke_width=DEFAULT_STROKE_WIDTH*1.25)
        rect1.shift(5.175 * LEFT + 0.15 * DOWN)

        rect2 = Rectangle(height=0.3, width=0.3, color=RED,
                          stroke_width=DEFAULT_STROKE_WIDTH*1.25)
        rect2.shift(0.85 * RIGHT + 0.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(rect1), Write(rect2))
        self.play(Write(title1), Write(exp1))
        self.wait()


class Locality(Scene):
    def construct(self):

        title = TexMobject(r"\frac{d^nf}{dx^n} \text{ only depends on } x",
                           tex_to_color_map={r"\frac{d^nf}{dx^n}": YELLOW}
                           )
        title.shift(3 * UP)

        title2 = TexMobject(r"\frac{d^nf}{dx^n} \text{ has Locality}", color=RED)
        title2.shift(3 * DOWN)
        title2.scale(1.25)

        f1 = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=0,
            t_max=math.sqrt(2),
            color=RED,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a1 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func1 = VGroup(a1, f1)
        func1.scale(1.5)
        func1.shift(4.5 * LEFT + 1 * DOWN)

        f2 = ParametricFunction(
            lambda t: np.array([t, 2*t, 0]),
            t_min=0,
            t_max=1,
            color=BLUE,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a2 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func2 = VGroup(a2, f2)
        func2.scale(1.5)
        func2.shift(3 * RIGHT + 1 * DOWN)

        a = Arrow(1 * LEFT, 1 * RIGHT, color=GREEN)
        a.scale(1.5)

        t = TexMobject(r"\frac{d}{dx}")
        t.shift(1 * UP)

        arr = VGroup(a, t)

        self.play(Write(title))
        self.wait()

        self.play(Write(func1))
        self.wait()

        self.play(Write(arr))
        self.play(TransformFromCopy(func1, func2))
        self.wait()

        self.play(Write(title2))
        self.wait()

class Formulas(Scene):
    def construct(self):
        eq1 = TexMobject(r"D^a(x^n) = \frac{\Gamma(n+1)}{\Gamma(n+1-a)}x^{n-a}")
        eq1.scale(1)
        eq1.shift(3 * UP)

        eq2 = TexMobject(r"D^{\frac{1}{2}} (1) = \frac{1}{\sqrt{\pi t}}")
        eq2.scale(1)
        eq2.shift(1 * UP)

        eq3 = TexMobject(r"D^{\frac{1}{2}} (1) = \frac{1}{\sqrt{\pi t}}")
        eq3.scale(1)
        eq3.shift(1 * DOWN)

        eq4 = TexMobject(r"D^{\frac{1}{2}} (1) = \frac{1}{\sqrt{\pi t}}")
        eq4.scale(1)
        eq4.shift(3 * DOWN)



        self.play(Write(eq1))
        self.wait()
