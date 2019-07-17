from manimlib.imports import *
import scipy.special


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
        "g_width": DEFAULT_STROKE_WIDTH*1.25
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
            y_min=-5,
            y_max=5,
            number_line_config={
                "include_tip": False,
            }
        )

        gfunc = VGroup(a1, f1, f2, f3, f4, f5)

        self.play(Write(gfunc))
        self.wait()

    @staticmethod
    def func(t):
        val = float(scipy.special.gamma(t))
       # if not np.isfinite(val):
       #     val = 5
        if val < 0:
            val = np.maximum(val, -5)
        elif val > 0:
            val = np.minimum(val, 5)
        else:
            val = 0
        return np.array([
            t,
            val,
            0,

        ], dtype=float)
