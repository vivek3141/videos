from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Introduction to Linear Equations")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(Write(title), Write(rect))
        self.wait()

        self.play(Uncreate(title), Uncreate(rect))
        self.wait()

        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )

        f1 = FunctionGraph(lambda x: x)
        f2 = FunctionGraph(lambda x: 3*x, color=RED)

        self.play(Write(axes), Write(f1), Write(f2))
        self.wait()


class SlopeCalc(Scene):
    def construct(self):
        eqt = TexMobject("y=0.5x+1").scale(1.5)
        eqt.shift(3 * UP)

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-2,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )
        f = ParametricFunction(
            lambda t: np.array([t, 0.5*t+1, 0]),
            t_min=-3,
            t_max=3,
            color=BLUE
        )
        eq = VGroup(axes, f).shift(1 * DOWN)

        self.play(Write(eqt))
        self.wait()

        self.play(Write(eq))
        self.wait()

        self.play(eq.shift, 2 * RIGHT)

        self.plot(2)
        self.plot(1)

        eq1 = TexMobject(r"\Delta x = 2 - 1 = 1")
        eq1.scale(1.25)
        eq1.shift(3 * LEFT + 2 * UP)

        eq2 = TexMobject(r"\Delta y = 2 - 1.5 = 0.5")
        eq2.scale(1.25)
        eq2.shift(3 * LEFT + 1 * UP)

        eq3 = TexMobject(r"\frac{\Delta y}{\Delta x} = 0.5")
        eq3.scale(1.25)
        eq3.shift(4 * LEFT - 2 * UP)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Write(eq3))
        self.wait()

        r = Rectangle(height=2, width=3, color=YELLOW).shift(4 * LEFT - 2 * UP)
        t = TextMobject("Slope", color=GREEN).scale(1.5)
        t.shift(1 * LEFT + 2 * DOWN)

        self.play(Write(r), Write(t))
        self.wait()

    def plot(self, x):
        y = x * 0.5 + 1

        p = Circle(radius=0.1,  color=YELLOW,
                   fill_opacity=1).shift(x * RIGHT + y * UP)
        p.shift(2 * RIGHT + 1 * DOWN)

        t = TexMobject(r"({},{})".format(str(x), str(y)))
        t.shift((x + 2) * RIGHT + (y - 0.25) * UP)

        self.play(Write(t))
        self.play(Write(p))
        self.wait()


class NegativeSlope(Scene):
    def construct(self):
        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-5,
            y_max=5,
            number_line_config={
                "include_tip": False,
            }
        )

        f1 = FunctionGraph(lambda x: -0.5*x + 1, color=PURPLE)

        self.play(Write(axes), Write(f1))
        self.wait()


class LinearEq(Scene):
    def construct(self):
        title = TextMobject("Equation of a Line", color=PINK).scale(1.5)
        title.shift(2.5 * UP)

        eq = TexMobject(
            r"y = mx + b", tex_to_color_map={r"m": BLUE, r"b": GREEN})
        eq.scale(3)

        exp = TexMobject(r"m = \text{Slope}", tex_to_color_map={
                         r"m": BLUE}).scale(1.5)
        exp.shift(2 * DOWN)

        self.play(Write(title), Write(eq), Write(exp))
        self.wait()


class Example(Scene):
    def construct(self):
        t = TexMobject("y = mx+b")
        t.scale(1.5)
        t.shift(3 * UP)

        given = TexMobject(r"m = 2 \\ (1,1)", tex_to_color_map={r"m": BLUE})
        given.shift(4 * RIGHT + 3 * UP)

        eq1 = TexMobject("y = 2x+b")
        eq1.scale(1.5)
        eq1.shift(2 * UP)

        eq1 = TexMobject("y = 2x+b")
        eq1.scale(1.5)
        eq1.shift(2 * UP)

        eq2 = TexMobject(r"1 = 2 \cdot 1+b")
        eq2.scale(1.5)
        eq2.shift(0 * UP)

        eq3 = TexMobject(r"b = -1")
        eq3.scale(1.5)
        eq3.shift(-1 * UP)

        eq4 = TexMobject(r"y=2x-1")
        eq4.scale(1.5)
        eq4.shift(-2 * UP)

        self.play(Write(t))
        self.wait()

        self.play(Write(given))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Write(eq3))
        self.wait()

        self.play(Write(eq4))
        self.wait()
