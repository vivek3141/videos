from manimlib.imports import *


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

        fun = VGroup(f, axes)

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

        func1 = VGroup(f1, a1)
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

        func2 = VGroup(f2, a2)
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
        c = 20

        eq1 = TexMobject(r"If(x) = \int_0^x f(t) dt",
                         )
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        eq2 = TexMobject(
            r"(I^3f)(x)=\int_0^x\left[\int_0^t \left(\int_0^s f(u)\,du\right)\, ds \right]\,dt")
        eq2.scale(1.5)
        eq2.shift(3 * UP)

        f1 = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=-1,
            t_max=1,
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

        func1 = VGroup(f1, a1)
        func1.scale(1.5)
        func1.shift(3 * LEFT + 1 * DOWN)

        f2 = ParametricFunction(
            lambda t: np.array([t, t**3 / 3, 0]),
            t_min=-1,
            t_max=1,
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

        func2 = VGroup(f2, a2)
        func2.scale(1.5)
        func2.shift(3 * RIGHT + 1 * DOWN)

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
                  Uncreate(func2), Transform(t, t2))
        self.wait()
