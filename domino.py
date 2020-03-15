from manimlib.imports import *


class Grid(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.m = m
        self.n = n
        self.s_width = s_width
        for x in range(0, m + 1):
            self.add(Line(
                s_width * np.array([x - m/2, -n/2, 0]),
                s_width * np.array([x - m/2, n/2, 0]))
            )
        for y in range(0, n + 1):
            self.add(Line(
                s_length * np.array([-m/2, y - n/2, 0]),
                s_length * np.array([m/2, y - n/2, 0]))
            )


class Chessboard(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        for x in range(0, m, 2):
            for y in range(0, n):
                pos = s_width * \
                    np.array([x - m/2 + (1 if y % 2 == 0 else 0) + 0.5,
                              y - n/2 + 0.5,
                              0])
                rect = Rectangle(
                    width=s_length,
                    height=s_width,
                    fill_opacity=0.6,
                    color=WHITE)
                rect.shift(pos)
                self.add(rect)


class DominoGrid(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, dt=0.5, perm=None, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        self.dt = dt
        if perm is not None:
            for n, i in enumerate(perm):
                self.add(self.get_rect(
                    *sorted([2 * n if (n // (self.m/2)) % 2 == 0 else 2 * n + 1, i])))

    def get_perm(self, perm):
        rects = VGroup()
        for n, i in enumerate(perm):
            rects.add(self.get_rect(
                *sorted([2 * n if (n // (self.m/2)) % 2 == 0 else 2 * n + 1, i])))
        return rects

    def get_rect(self, pos1, pos2):
        if pos1 // self.m == pos2 // self.m:
            rect = Polygon(
                self.get_point(pos1) + np.array([-self.dt, self.dt, 0]),
                self.get_point(pos2) + np.array([self.dt, self.dt, 0]),
                self.get_point(pos2) - np.array([-self.dt, self.dt, 0]),
                self.get_point(pos1) - np.array([self.dt, self.dt, 0]),
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            )
        else:
            rect = Polygon(
                self.get_point(pos1) + np.array([self.dt, self.dt, 0]),
                self.get_point(pos2) + np.array([self.dt, -self.dt, 0]),
                self.get_point(pos2) - np.array([self.dt, self.dt, 0]),
                self.get_point(pos1) - np.array([self.dt, -self.dt, 0]),
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            )
        return rect

    def get_point(self, n):
        return self.s_width * np.array([n % self.m - self.s_width, self.s_width - n // self.n, 0])


class Tilings(Scene):
    def construct(self):
        grid = DominoGrid(4, 4, s_width=1.5, s_length=1.5)
        rects1 = grid.get_perm((4, 1, 9, 3, 12, 6, 14, 11))

        rects2 = grid.get_perm((0, 1, 6, 3, 4, 9, 12, 11))[1:]
        rects2.add(grid.get_rect(14, 15))
        rects2.add(grid.get_rect(0, 1).shift(1.5 * LEFT))

        rects3 = grid.get_perm((4, 1, 9, 3, 12, 6, 14, 11))
        rects4 = grid.get_perm((1, 3, 9, 11, 4, 6, 12, 14))
        rects5 = grid.get_perm((1, 3, 4, 6, 9, 11, 12, 14))

        m = TexMobject("M")
        m.shift(4 * LEFT)
        m.scale(1.5)

        n = TexMobject("N")
        n.shift(3.5 * DOWN)
        n.scale(1.5)

        cross = VGroup()
        cross.add(Line(3.5 * UP + 3.5 * RIGHT, 3.5 * DOWN +
                       3.5 * LEFT, color=RED, stroke_width=8))
        cross.add(Line(3.5 * UP + 3.5 * LEFT, 3.5 * DOWN +
                       3.5 * RIGHT, color=RED, stroke_width=8))

        self.play(ShowCreation(grid))
        self.play(FadeInFromDown(m), FadeInFromDown(n))
        self.wait()

        self.play(Write(rects1))
        self.wait()

        self.play(Transform(rects1, rects2))
        self.play(ShowCreation(cross))
        self.wait()

        self.play(Uncreate(cross))
        self.play(Transform(rects1, rects3))
        self.wait()

        self.play(Transform(rects1, rects4))
        self.wait()

        self.play(Transform(rects1, rects5))
        self.wait()

        group = VGroup(grid, rects1, m, n)
        self.play(group.shift, 2 * LEFT)

        eq = TexMobject(r"M \cdot N \text{ is even}", tex_to_color_map={
                        r"M \cdot N": BLUE})
        eq.scale(1.5)
        eq.shift(4 * RIGHT)

        self.play(Write(eq))
        self.wait()


class Recursion(Scene):
    def construct(self):
        title = TextMobject("Fibonacci Sequence", color=TEAL)
        title.scale(2)
        title.shift(3 * UP)

        n1 = TexMobject("1").scale(3)
        n2 = TexMobject("1").scale(3)

        n1.shift(3 * LEFT)
        n2.shift(0 * LEFT)

        grp = VGroup(n1, n2)

        n3 = TexMobject("2").scale(3)
        n3.shift(3 * RIGHT)

        self.play(Write(title))
        self.play(Write(grp))
        self.wait()

        self.play(TransformFromCopy(grp, n3))
        self.wait()

        grp.add(n3)

        self.play(Uncreate(n1))
        self.play(grp.shift, 3 * LEFT)

        n4 = TexMobject("3").scale(3)
        n4.shift(3 * RIGHT)

        self.play(TransformFromCopy(grp, n4))
        self.wait()

        grp.add(n4)

        self.play(Uncreate(n2))
        self.play(grp.shift, 3 * LEFT)

        n5 = TexMobject("5").scale(3)
        n5.shift(3 * RIGHT)

        self.play(TransformFromCopy(grp, n5))
        self.wait()

        grp.add(n5)

        self.play(Uncreate(grp))

        eq = TexMobject(r"F_n = F_{n-1} + F_{n-2}")
        eq.scale(2.5)

        self.play(FadeInFromDown(eq))
        self.wait()


class TwoByNExample(Scene):
    def construct(self):
        grid = DominoGrid(5, 2, s_width=1.5, s_length=1.5)
        rects = VGroup()
        for i in np.arange(-3, 3.1, 1.5):
            rect = Rectangle(
                width=1,
                height=2.5,
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            ).shift(i * RIGHT)
            rects.add(rect)

        self.play(ShowCreation(grid))
        self.wait()

        self.play(Write(rects))
        self.wait()


class Tmn(Scene):
    def construct(self):
        eq = TexMobject(r"T(m, n)", tex_to_color_map={r"m": RED, r"n": GREEN})
        eq.scale(2)
        eq.shift(3 * LEFT)

        arrow = Arrow(LEFT, RIGHT, color=TEAL)
        text = TextMobject(r"Number of ways \\ to tile M x N",
                           tex_to_color_map={r"M": RED, r" N": GREEN})
        text.scale(1.25)
        text.shift(3.5 * RIGHT)

        self.play(FadeInFromDown(eq))
        self.play(FadeInFromDown(arrow))
        self.play(FadeInFromDown(text))


class TwoByN(Scene):
    def construct(self):
        grid = DominoGrid(5, 2, s_width=1.5, s_length=1.5)
        rect = Rectangle(
            width=1,
            height=2.5,
            fill_opacity=1,
            stroke_color=WHITE,
            color=PURPLE
        ).shift(3 * RIGHT)

        rect2 = Rectangle(
            width=5.5,
            height=2.5,
            fill_opacity=1,
            stroke_color=WHITE,
            color=GRAY
        ).shift(0.75 * LEFT)

        self.play(Write(grid))
        self.play(Write(rect))
        self.play(Write(rect2))
