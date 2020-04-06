from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        axes = Axes(
            x_min=-2,
            x_max=4,
            y_min=-2,
            y_max=4,
            number_line_config={"include_tip": False}
        )

        f = FunctionGraph(
            self.func,
            x_min=-2,
            x_max=4
        )

        s = [-0.904, 0.904, 3.528]

        lbl = TexMobject("f(x)", color=YELLOW).move_to(f, RIGHT)
        xlbl = TexMobject("x").shift(4.5 * RIGHT)
        ylbl = TexMobject("y").shift(4.5 * UP)

        lines = VGroup(*[self.get_lines(i) for i in s])
        graph = VGroup(axes, f, lbl, xlbl, ylbl)

        grp = VGroup(graph, lines)
        grp.move_to(2.5 * LEFT)

        self.play(Write(graph))
        self.wait()

        head1 = TextMobject("Local min/max", color=GOLD_B)
        head1.shift(3.5 * RIGHT + 2.5 * UP)
        head1.scale(1.25)

        self.play(Write(head1))

        eq1 = TexMobject("f'(x) = 0")
        eq1.scale(1)
        eq1.shift(3.5 * RIGHT + 1 * UP)

        self.wait()

        brect = BackgroundRectangle(
            eq1, buff=0.25, stroke_opacity=1, fill_opacity=0, stroke_width=6, color=BLUE)

        self.play(Write(eq1))
        self.play(Write(brect), Write(lines))
        self.wait()

    def func(self, x):
        return x * np.sin(np.cos(x)) + 2

    def get_lines(self, point):
        ret = VGroup()
        ret.add(DashedLine(ORIGIN, self.func(point) * UP,
                           dash_length=0.1, stroke_opacity=0.7).shift(point * RIGHT))
        ret.add(Line(0.75 * LEFT, 0.75 * RIGHT,
                     color=BLUE).shift([point, self.func(point), 0]))

        return ret
