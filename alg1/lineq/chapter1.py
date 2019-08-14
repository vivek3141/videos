from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Linear Equations", color=RED)
        title.scale(2)

        eq1 = TexMobject("2y = 3x + 2").scale(1.5).shift(2 * LEFT + 1 * UP)
        eq2 = TexMobject("y = x + 3").scale(1.5).shift(3 * LEFT + 1 * DOWN)
        eq3 = TexMobject("3y + 2x = 1").scale(1.5).shift(2 * LEFT + 3 * DOWN)

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )
        f = FunctionGraph(lambda x: 0.5*x + 1, x_min=-3, x_max=3)
        func = VGroup(axes, f)

        func.shift(2 * RIGHT + 1 * DOWN)

        self.play(Write(title))
        self.wait()

        self.play(title.shift, 3 * UP)
        self.wait()

        self.play(Write(func), Write(eq1), Write(eq2), Write(eq3))
        self.wait()


class Cartesian(Scene):
    def construct(self):
        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
                "include_numbers": True,
            },
            y_axis_config={
                "include_numbers": False,
            },
        )

        p = Circle(radius=0.1,  color=YELLOW,
                   fill_opacity=1).shift(3 * RIGHT + 2 * UP)
        label = TextMobject("P")
        label.shift(3.5 * RIGHT + 2 * UP)

        title = TextMobject("Cartesian System", color=ORANGE)
        title.scale(1.5)
        title.shift(3 * UP)

        rect = BackgroundRectangle(title, fill_opacity=1)

        self.play(Write(axes), Write(rect), Write(title) )
        self.wait()

        self.play(Write(label), ShowCreation(p))
        self.wait()
