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

        self.play(Write(title))
        self.wait()

        self.play(Transform(title, title2))
        self.wait()
