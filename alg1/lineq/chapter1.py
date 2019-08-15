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

        self.play(Write(axes), Write(rect), Write(title))
        self.wait()

        self.play(Write(label), ShowCreation(p))
        self.wait()


class Satisfy(Scene):
    def construct(self):
        self.eq = TexMobject(r"2y = 3x + 1")
        self.eq.scale(1.5)
        self.eq.shift(3 * UP)

        self.play(Write(self.eq))
        self.wait()

        m = self.replace(1, 1)

        self.play(Uncreate(m))
        self.wait()

        m = self.replace(1, 2)

    def replace(self, x, y):
        rect = Rectangle(height=2, width=2, color=YELLOW)
        val1 = TexMobject("x = {}".format(x)).shift(0.5 * UP)
        val2 = TexMobject("y = {}".format(y)).shift(0.5 * DOWN)

        r = VGroup(val1, rect, val2)
        r.shift(4 * RIGHT + 2.5 * UP)

        t1 = TexMobject(r"\times")
        t1.shift(2.5 * LEFT)

        t2 = TexMobject(r"\times")
        t2.shift(-0.5 * LEFT)

        e1 = TexMobject("2")
        e1.shift(3 * LEFT)

        e2 = TexMobject("y")
        e2.shift(2 * LEFT)

        e3 = TexMobject("=")
        e3.shift(1 * LEFT)

        e4 = TexMobject("3")
        e4.shift(0 * LEFT)

        e5 = TexMobject("x")
        e5.shift(-1 * LEFT)

        e6 = TexMobject("+")
        e6.shift(-2 * LEFT)

        e7 = TexMobject("1")
        e7.shift(-3 * LEFT)

        group = VGroup(e1, e2, e3, e4, e5, e6, e7, t1, t2)

        rep1 = TexMobject(str(x), color=YELLOW)
        rep1.shift(-1 * LEFT)

        rep2 = TexMobject(str(y), color=YELLOW)
        rep2.shift(2 * LEFT)

        ev1 = TexMobject(str(y * 2))
        ev2 = TexMobject(str(3 * x + 1))

        ev1.shift(1.5 * DOWN + 2 * LEFT)
        ev2.shift(1.5 * DOWN + 0 * RIGHT)

        eve = TexMobject(r"\neq") if y * 2 != 3 * x + 1 else TexMobject(r"=")

        eve.shift(1.5 * DOWN + 1 * LEFT)

        ev = VGroup(ev1, ev2, eve)

        g2 = VGroup(rep1, group, rep2, ev)
        g2.scale(1.5)

        b1 = Brace(VGroup(e4, e5, e6, e7))
        a1 = Arrow(b1.get_tip(), 1.5 * DOWN, color=GREEN)

        b2 = Brace(VGroup(e1, e2))
        a2 = Arrow(b2.get_tip(), 1.5 * DOWN + 3 * LEFT, color=GREEN)

        a = VGroup(a1, b1, a2, b2)

        state = TexMobject(
            r"\text{("+str(x)+r","+str(y) +
            r") does not satisfy the equation }2y = 3x + 11",
            tex_to_color_map={r"2y = 3x + 1": YELLOW, r"("+str(x)+r","+str(y)+r")": GREEN}) if y * 2 != 3 * x + 1 else TexMobject(
                r"\text{("+str(x)+r","+str(y) +
            r") satisfies the equation }2y = 3x + 11",
                tex_to_color_map={r"2y = 3x + 1": YELLOW, r"("+str(x)+r","+str(y)+r")": GREEN})

        state.shift(3.25 * DOWN)

        self.play(Write(r))
        self.wait()

        self.play(Write(group))
        self.wait()

        self.play(Transform(e5, rep1), Transform(e2, rep2))
        self.wait()

        self.play(Write(a))
        self.wait()

        self.play(Write(ev))
        self.wait()

        self.play(Write(state))
        self.wait()

        return VGroup(r, group, a, ev, state)


class LinearEq(Scene):
    def construct(self):
        eqq = TexMobject("2y = x + 1").scale(1.5)
        eqq.shift(2 * RIGHT + 3 * UP)

        rr = BackgroundRectangle(eqq, fill_opacity=1)
        equation = VGroup(rr, eqq)

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )
        f = FunctionGraph(lambda x: 0.5*x + 0.5, x_min=-3, x_max=3, color=BLUE)
        func = VGroup(axes, f)
        func.shift(2 * RIGHT)

        l1 = Line(3 * DOWN, 4 * UP)
        l1.shift(5 * LEFT)

        l2 = Line(7 * LEFT, 3*LEFT)
        l2.shift(3 * UP)

        l3 = Line(3 * DOWN, 4 * UP)
        l3.shift(3 * LEFT)

        l4 = Line(3 * DOWN, 4 * UP)
        l4.shift(7 * LEFT)

        l5 = Line(7 * LEFT, 3*LEFT)
        l5.shift(4 * UP)

        t1 = TexMobject("x")
        t1.shift(6 * LEFT + (3 + 0.5) * UP)

        t2 = TexMobject("y")
        t2.shift(4 * LEFT + (3 + 0.5) * UP)

        table = VGroup(l1, l2, t1, t2, l3, l4, l5)

        for i in range(-3, 3):
            l = Line(7 * LEFT, 3*LEFT)
            l.shift(i * UP)

            t = TexMobject(str(i))
            t.shift(6 * LEFT + (i + 0.5) * UP)
            table.add(l)
            table.add(t)

        table.shift(0.5 * DOWN + 1 * RIGHT)

        self.play(Write(axes), Write(equation))
        self.wait()

        self.play(Write(table))
        self.wait()

        self.plot(0)
        self.plot(1)
        self.plot(-1)

        self.plot(2)
        self.plot(-2)
        self.plot(-3)

        self.play(Write(f))
        self.wait()

    def plot(self, x):
        y = x * 0.5 + 0.5
        p = Circle(radius=0.1,  color=YELLOW,
                   fill_opacity=1).shift(x * RIGHT + y * UP)
        p.shift(2 * RIGHT)

        t = TexMobject(str(y))
        t.shift(3 * LEFT + x * UP)

        self.play(Write(t))
        self.play(Write(p))
        self.wait()
