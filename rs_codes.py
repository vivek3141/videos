from manimlib import *

A_AQUA = "#8dd3c7"
A_YELLOW = "#ffffb3"
A_LAVENDER = "#bebada"
A_RED = "#fb8072"
A_BLUE = "#80b1d3"
A_ORANGE = "#fdb462"
A_GREEN = "#b3de69"
A_PINK = "#fccde5"
A_GREY = "#d9d9d9"
A_VIOLET = "#bc80bd"
A_UNKA = "#ccebc5"
A_UNKB = "#ffed6f"


class NumberSquare(VGroup):
    def __init__(self, number, color=RED, opacity=0.5, num_scale=3, side_length=2, square_kwargs={}, tex_kwargs={}, *args, **kwargs):
        VGroup.__init__(self, *args, **kwargs)

        self.sq = Square(side_length=side_length, fill_color=color,
                         fill_opacity=opacity, **square_kwargs)
        self.num = Tex(str(number), **tex_kwargs)
        self.num.scale(num_scale)

        self.add(self.sq, self.num)


class LabelledNumberSquare(NumberSquare):
    def __init__(self, *args, **kwargs):
        NumberSquare.__init__(self, *args, **kwargs)


class RS(Scene):
    def construct(self):
        s = VGroup()
        for i in range(4):
            s_i = NumberSquare(i, [RED_E, RED_D, RED_C][random.randint(0, 2)])
            s.add(s_i.shift(3*i * RIGHT))
        s.center()
        self.embed()


class ModularIntro(Scene):
    def construct(self):
        title = TexText("Modular Arithmetic", color=A_YELLOW)
        title.shift(3 * UP)
        title.scale(1.5)

        self.play(Write(title))
        self.wait()

        s = Text("{0, 1, 2, 3, 4}", t2c={str(i): A_ORANGE for i in range(5)})
        s.scale(1.5)
        s.move_to(1.5 * UP)

        ff = Tex(
            r"(+, -, \cross, \olddiv) \mod {p}", tex_to_color_map={"{p}": A_AQUA})
        ff.scale(1.5)

        self.play(title.shift, 3.5 * LEFT)

        ff.next_to(title, RIGHT)
        ff.shift(0.5 * RIGHT)

        self.play(Write(ff))
        self.wait()

        self.play(Write(s))
        self.wait()

        eq1 = Tex(
            "3 + 3 = 6", tex_to_color_map={"3": A_ORANGE, "6": A_ORANGE, "5": A_AQUA})
        eq1.scale(1.5)

        eq2 = Tex("3 + 3 \equiv 1 \mod 5",
                  tex_to_color_map={"3": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
        eq2.scale(1.5)

        eq2.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        eq1.move_to(eq2, LEFT)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

        self.play(Indicate(eq2[3], scale_factor=1.5))
        self.wait()

        self.play(s.move_to, 4 * RIGHT + 1.5 * UP)

        c = Circle(radius=2, stroke_color=A_GREY)
        c.next_to(s, DOWN)

        c_nums = VGroup()

        for i, t in enumerate(np.linspace(PI/2, PI/2 - 2*PI, 6)[:-1]):
            x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)

            t = Tex(str(i), color=A_ORANGE)
            t.scale(1.5)
            t.move_to(c.get_center())
            t.shift(x * RIGHT + y * UP)

            c_nums.add(t)

        self.play(Write(c))

        anims = []
        s_num = range(1, 14, 3)

        for i in range(5):
            anims.append(TransformFromCopy(s[s_num[i]], c_nums[i]))

        self.play(*anims, run_time=5)
        self.wait()

        self.play(
            Uncreate(s),
            ApplyMethod(
                VGroup(c, c_nums).move_to, 4 * RIGHT + 0.5 * DOWN)
        )

        eq3 = Tex(
            "4 + 3 \equiv 2 \mod 5",
            tex_to_color_map={
                "2": A_ORANGE, "3": A_ORANGE,
                "4": A_ORANGE, "5": A_AQUA
            }
        )
        eq3.scale(1.5)
        eq3.move_to(eq2, LEFT)

        self.play(FadeOut(eq2, UP), FadeIn(eq3, UP))

        b_rects = VGroup()

        for num in c_nums:
            b = SurroundingRectangle(num, color="#f5fd62", buff=0.15)
            b_rects.add(b)

        b1 = SurroundingRectangle(eq3[0], color="#f5fd62", buff=0.15)

        self.play(Write(b1))
        self.wait()

        for i in range(4, 8):
            self.play(Transform(b1, b_rects[i % 5]))
            self.wait(0.5)

        self.wait(1)

        eq4 = Tex(
            "1 - 3 \equiv 3 \mod 5",
            tex_to_color_map={
                "1": A_ORANGE, "3": A_ORANGE,
                "5": A_AQUA
            }
        )
        eq4.scale(1.5)
        eq4.move_to(eq3, LEFT)

        self.play(FadeOut(eq3, UP), FadeIn(eq4, UP), Uncreate(b1))
        self.wait()

        b1 = SurroundingRectangle(eq4[0], color="#f5fd62", buff=0.15)

        self.play(Write(b1))
        self.wait()

        for i in range(6, 2, -1):
            self.play(Transform(b1, b_rects[i % 5]))
            self.wait(0.5)

        self.wait(1)

        self.play(Uncreate(b1))
        self.wait()

        eq5 = Tex(
            "1 + (-3) \equiv 3 \mod 5",
            tex_to_color_map={
                "1": A_ORANGE, "3": A_ORANGE,
                "5": A_AQUA
            }
        )
        eq5.scale(1.5)
        eq5.move_to(eq4, LEFT)

        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()

        eq6 = Tex("a", "+", "(-a)", "=", "0", tex_to_color_map={"a": A_PINK})
        eq6.scale(1.5)
        eq6.move_to(eq5, LEFT)
        eq6.shift(DOWN)

        b = Brace(eq6[2:5])
        t_b = b.get_text("Additive inverse", color=A_GREEN)
        t_b.scale(1.5)
        t_b.shift(0.25 * DOWN)

        eq7 = Tex("a", "+", "(-a)", "\equiv", "0", "\mod 5",
                  tex_to_color_map={"a": A_PINK, "5": A_AQUA})
        eq7.scale(1.5)
        eq7.move_to(eq6, LEFT)

        self.play(ApplyMethod(eq5.shift, UP))
        self.play(Write(eq6))
        self.wait()

        self.play(Write(b), Write(t_b))
        self.wait()

        self.play(TransformMatchingTex(eq6, eq7))
        self.wait()

        eq8 = Tex("3", "+", "(-3)", "\equiv", r"0 \mod 5",
                  tex_to_color_map={"3": A_ORANGE, "5": A_AQUA})
        eq8.scale(1.5)
        eq8.move_to(eq7, LEFT)

        eq9 = Tex("3", "+", "2", "\equiv", r"0 \mod 5",
                  tex_to_color_map={"3": A_ORANGE, "2": A_ORANGE, "5": A_AQUA})
        eq9.scale(1.5)
        eq9.move_to(eq7, LEFT)

        n = Tex("2", color=A_ORANGE)
        n.scale(1.5)
        n.move_to([-4.09011112, -0.94835368, 0])

        self.play(FadeOut(VGroup(eq7, t_b, b), DOWN))
        self.wait()

        grp = VGroup(eq5[1][2], eq5[2])
        grp2 = VGroup(eq8[2][1], eq8[3])

        eq8_2 = eq8[2]
        eq8.remove(eq8[2], eq8[3])

        self.play(TransformFromCopy(grp, grp2))
        self.wait()

        self.play(Write(VGroup(eq8_2[0], eq8)))
        self.wait()

        self.play(Transform(grp2, n))
        self.wait()

        cp = n.copy()
        cp.move_to(grp)

        self.play(Transform(grp, cp), TransformFromCopy(n, cp))
        self.play(Uncreate(VGroup(eq8, grp2, eq8_2)),
                  ApplyMethod(VGroup(eq5, cp).shift, DOWN))
        self.wait()

        self.play(FadeOut(VGroup(eq5, cp), UP))
        self.wait()

        eq10 = Tex(
            "2 \cdot 3 = 6", tex_to_color_map={"2": A_ORANGE, "3": A_ORANGE, "6": A_ORANGE, "5": A_AQUA})
        eq10.scale(1.5)

        eq11 = Tex("2 \cdot 3 \equiv 1 \mod 5",
                   tex_to_color_map={"2": A_ORANGE, "3": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
        eq11.scale(1.5)

        eq11.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        eq10.move_to(eq11, LEFT)

        self.play(Write(eq10))
        self.wait()

        self.play(TransformMatchingTex(eq10, eq11))
        self.wait()

        eq12 = Tex(r"2+2+2 \equiv 1 \mod 5",
                   tex_to_color_map={"2": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
        eq12.scale(1.5)
        eq12.move_to(eq11, LEFT)
        eq12.shift(1.5 * DOWN)

        self.play(ApplyMethod(eq11.shift, 0.5 * UP))
        self.wait(0.5)

        b1 = SurroundingRectangle(eq11[0], color="#f5fd62", buff=0.15)

        self.play(TransformFromCopy(eq11[0:3], eq12[:5]), Write(eq12[5:]))
        self.wait()

        self.play(Write(b1))
        self.wait()

        self.play(Indicate(eq12[0], scale_factor=1.5))
        self.play(Transform(b1, b_rects[2]))

        for i in range(1, 3):
            self.play(Indicate(eq12[2*(i-1)+1:2*i+1], scale_factor=1.5))
            for j in range(3):
                self.play(Transform(b1, b_rects[(2*i + j) % 5]))
            self.wait()

        self.play(Uncreate(VGroup(b1, eq11, eq12)))
        self.wait()

        eq13 = Tex(r"a", r" \cdot ", r"a^{-1} ", r"\equiv 1 \mod 5",
                   tex_to_color_map={"a": A_PINK, "5": A_AQUA, "1": A_ORANGE})
        eq13.scale(1.5)
        eq13.move_to(0.25 * LEFT, RIGHT)

        b = Brace(eq13[2:5])

        b_t = b.get_text("Multiplicative Inverse", color=A_GREEN)
        b_t.scale(1.25)
        b_t.shift(0.5 * DOWN + 1.5 * RIGHT)

        self.play(Write(eq13))
        self.wait()

        self.play(Write(b), Write(b_t))
        self.wait()

        self.play(ApplyMethod(VGroup(eq13, b, b_t).shift, DOWN))
        self.wait()

        eq14 = Tex("4", r" \olddiv", "2 \equiv 4 \cdot 2^{-1} \mod 5", tex_to_color_map={
                   "5": A_AQUA, "4": A_ORANGE, "2": A_ORANGE, "1": A_ORANGE})
        eq14.scale(1.5)
        eq14.move_to(eq13, LEFT)
        eq14.shift(2 * UP)

        eq15 = Tex("4", r" \olddiv", "2 \equiv 4 \cdot 3 \mod 5", tex_to_color_map={
                   "5": A_AQUA, "4": A_ORANGE, "2": A_ORANGE, "3": A_ORANGE})
        eq15.scale(1.5)
        eq15.move_to(eq14, LEFT)
        eq15.shift(0.07 * DOWN)

        eq16 = Tex("4", r" \olddiv", "2 \equiv 2 \mod 5", tex_to_color_map={
            "5": A_AQUA, "4": A_ORANGE, "2": A_ORANGE, "3": A_ORANGE})
        eq16.scale(1.5)
        eq16.move_to(eq15, LEFT)

        self.play(Write(eq14))
        self.wait()

        self.play(Transform(eq14[5:], eq15[5:]))
        self.wait()

        self.play(Transform(eq14[4:], eq16[4:]))
        self.wait()

        self.play(Uncreate(VGroup(c, eq14, b, b_t, eq13, c, c_nums)))
        self.wait()

        l1 = Line(10 * LEFT, 10 * RIGHT)
        l1.move_to(2 * UP)

        l2 = Line(2 * UP, 10 * DOWN)

        l3 = Line(10 * LEFT, 10 * RIGHT)
        l3.move_to(0.75 * UP)

        title1 = TexText("Addition", color=A_GREEN)
        title1.scale(1.25)
        title1.move_to(FRAME_WIDTH/4 * LEFT + 1.375 * UP)

        title2 = TexText("Multiplication", color=A_GREEN)
        title2.scale(1.25)
        title2.move_to(FRAME_WIDTH/4 * RIGHT + 1.3 * UP)

        m = {"a": A_PINK, "b": A_PINK, "p": A_AQUA}

        def create_eq(eq, n, direction):
            return Tex(eq, tex_to_color_map=m if n < 3 else {**m, "c": A_PINK}).shift(FRAME_WIDTH/4 * direction + (n-1) * 0.75 * DOWN)

        add_eqs = VGroup()
        add_tex = [
            "(a + b) + c \equiv a + (b + c)",
            "a + b \equiv b + a",
            "a(b+c) \equiv ab+ac",
            "a + 0 \equiv a \equiv 0 + a",
            "a + (-a) \equiv 0 \equiv (-a) + a"
        ]

        mul_eqs = VGroup()
        mul_tex = [
            "(ab)c \equiv a(bc)",
            "ab \equiv ba",
            "(a+b)c \equiv ac + bc",
            r"a \cdot 1 \equiv a \equiv 1 \cdot a",
            r"aa^{-1} \equiv 1 \equiv a^{-1} a; a \neq 0",
        ]

        for i in range(5):
            add_eqs.add(create_eq(add_tex[i] + r" \mod p", i+1, LEFT))
            mul_eqs.add(create_eq(mul_tex[i] + r" \mod p", i+1, RIGHT))

        self.play(Write(l1), Write(l2), Write(l3))

        self.play(Write(title1))
        self.play(Write(add_eqs))

        self.play(Write(title2))
        self.play(Write(mul_eqs))

        self.wait()

        self.embed()


class LagrangeIntro(Scene):
    CONFIG = {
        "fade_opacity": 0.15,
        "curve_opacity": 1
    }

    def construct(self):
        x_vals = [1, 3, 4]
        y_vals = [2, 2, -1]
        coors = [(x_vals[i], y_vals[i]) for i in range(3)]

        colors = [A_RED, A_YELLOW, A_BLUE]

        curve_kwargs = {
            "stroke_width": 6,
            "stroke_opacity": self.curve_opacity
        }

        axes = Axes(
            x_range=(0, 5),
            y_range=(-3, 3),
            axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 6},
            y_axis_config={"stroke_width": 6}
        )

        points = VGroup()
        labels = VGroup()
        offsets = [0.5 * RIGHT, 0.5 * LEFT, 0.75 * LEFT]

        for i, (x, y) in enumerate(coors):
            d = Dot(
                axes.c2p(x, y),
                radius=2 * DEFAULT_DOT_RADIUS, color=A_GREEN
            )

            t = Tex(f"({x}, {y})")
            t.next_to(d, DOWN)
            t.shift(offsets[i])

            points.add(d)
            labels.add(t)

        labels_cp = labels.copy()

        c = ParametricCurve(
            lambda t: axes.c2p(t, self.func(t)),
            t_range=(0, 5), stroke_width=6, color=A_GREEN
        )

        eq = Tex(
            "p(x) = -x^2 + 4x - 1",
            tex_to_color_map={"p": A_GREEN, "x": A_PINK}
        )
        eq.scale(1.5)
        eq.shift(3.25 * UP)

        grp = VGroup(axes, c, points, labels)

        self.play(Write(axes), Write(points), Write(labels))
        self.wait()

        self.play(Write(c))
        self.wait()

        self.play(ApplyMethod(grp.shift, 0.5 * DOWN))
        self.play(Write(eq))
        self.wait()

        self.play(FadeOut(VGroup(eq, c)), ApplyMethod(grp.shift, 0.5 * UP))

        def l1(x): return (x-3)*(x-4)/6
        l1_c = ParametricCurve(
            lambda t: axes.c2p(t, l1(t)),
            t_range=(0, 5), color=colors[0], stroke_width=6,
            stroke_opacity=self.curve_opacity
        )
        l1_cp = l1_c.copy()
        l1_cp.set_stroke(opacity=self.fade_opacity)

        def l2(x): return (x-1)*(x-4)/-2
        l2_c = ParametricCurve(
            lambda t: axes.c2p(t, l2(t)),
            t_range=(0, 5), color=colors[1], stroke_width=6,
            stroke_opacity=self.curve_opacity
        )
        l2_cp = l2_c.copy()
        l2_cp.set_stroke(opacity=self.fade_opacity)

        def l3(x): return (x-1)*(x-3)/3
        l3_c = ParametricCurve(
            lambda t: axes.c2p(t, l3(t)),
            t_range=(0, 5), color=colors[2], stroke_width=6,
            stroke_opacity=self.curve_opacity
        )
        l3_cp = l3_c.copy()
        l3_cp.set_stroke(opacity=self.fade_opacity)

        l_c = VGroup(l1_c, l2_c, l3_c)
        l_cp = l_c.deepcopy()
        l_faded = VGroup(l1_cp, l2_cp, l3_cp)

        self.play(
            Write(l_c),
        )
        self.wait()

        def hide_all_but(idx):
            anims = []

            for i in range(3):
                if i != idx:
                    anims.append(Transform(l_c[i], l_faded[i]))

            self.play(*anims)

        def show_all():
            anims = []

            for i in range(3):
                anims.append(Transform(l_c[i], l_cp[i]))

            self.play(*anims)

        def one_hot(x_val, curve_index):
            return 1 if x_val == x_vals[curve_index] else 0

        def show_curve(curve_index):
            points.set_opacity(self.fade_opacity)

            hide_all_but(curve_index)

            points_0 = VGroup()

            for x in x_vals:
                points_0.add(
                    Dot(axes.c2p(x, one_hot(x, curve_index)),
                        radius=0.1, color=colors[curve_index])
                )

            labels_0 = VGroup()

            for i in range(3):
                labels_0.add(
                    Tex(f"({x_vals[i]}, {one_hot(x_vals[i], curve_index)})"
                        ).next_to(points_0[i], UP)
                )

            self.play(Write(points_0), Transform(labels, labels_0))
            self.wait()

            self.play(Indicate(labels[curve_index]))
            self.wait()

            self.play(Transform(labels, labels_cp),
                      ApplyMethod(points.set_opacity, 1),
                      Uncreate(points_0))
            show_all()

            self.wait()

        show_curve(0)
        show_curve(1)
        show_curve(2)

        eq1 = Tex(
            "l_1(x)", "=", "(x-3)", "(x-4)",
            tex_to_color_map={"x": A_PINK, "l_1": A_RED,
                              "3": A_ORANGE, "4": A_ORANGE}
        )
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        eq2 = Tex(
            "l_1(x)", "=", r"{{1} \over {6}}", "(x-3)", "(x-4)",
            tex_to_color_map={"x": A_PINK, "l_1": A_RED,
                              "{1}": A_ORANGE, "{6}": A_ORANGE,
                              "3": A_ORANGE, "4": A_ORANGE}
        )
        eq2.scale(1.5)
        eq2.shift(3 * UP)

        def p(x): return 2*l1(x) + 2*l2(x) - 1*l3(x)

        eq3 = Tex(r"p(x) =", r" 2 \cdot l_1(x)", r" + 2 \cdot ", r"l_2(x)", r" + (-1) \cdot ", r"l_3(x)",
                  tex_to_color_map={"l_1": A_RED, "l_2": A_YELLOW, "l_3": A_BLUE, "x": A_PINK, "p": A_GREEN})
        eq3.shift(3.25 * UP)
        eq3.scale(1.5)

        def func(t):
            return axes.c2p(t, p(t))

        self.play(Uncreate(l_c))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

        self.play(TransformFromCopy(eq2, l_cp[0]))
        self.wait()

        self.play(FadeOut(VGroup(eq2[4:], l_cp[0], l_c[0])))

        grp2 = VGroup(axes, points, labels)
        c.shift(0.5 * DOWN)
        l_cp.shift(0.5 * DOWN)

        self.play(
            ApplyMethod(grp2.shift, 0.5 * DOWN),
            ReplacementTransform(eq2[:4], eq3[5:9])
        )

        def func_lc_1(t):
            return axes.c2p(t, 2 * l1(t))

        def func_lc_2(t):
            return axes.c2p(t, 2*l1(t) + 2*l2(t))

        def func_lc_3(t):
            return axes.c2p(t, 2*l1(t) + 2*l2(t) + -1*l3(t))

        color_avg = rgb_to_hex((hex_to_rgb(A_RED) + hex_to_rgb(A_YELLOW))/2)

        lc_1 = ParametricCurve(func_lc_1, t_range=(
            0, 5), color=colors[0], **curve_kwargs)
        lc_2 = ParametricCurve(func_lc_2, t_range=(
            0, 5), color=color_avg, **curve_kwargs)
        lc_3 = ParametricCurve(func_lc_3, t_range=(
            0, 5), color=A_GREEN, **curve_kwargs)

        self.play(Write(eq3[:4]))
        self.wait()

        self.play(TransformFromCopy(eq3[5:9], l_cp[0]))
        self.wait()

        self.play(Write(eq3[4]))
        self.bring_to_front(eq3[:9], points, labels)
        self.play(Indicate(eq3[4]))
        self.play(Transform(l_cp[0], lc_1), ApplyMethod(
            points[0].set_color, A_RED), run_time=3.5)
        self.wait()

        self.play(Write(eq3[9:14]))
        self.play(Indicate(eq3[9:14]))

        self.play(Transform(l_cp[0], lc_2), ApplyMethod(
            points[:2].set_color, color_avg), run_time=3.5)
        self.wait()

        self.play(Write(eq3[14:]))
        self.play(Indicate(eq3[14:]))
        self.play(Transform(l_cp[0], lc_3), ApplyMethod(
            points.set_color, A_GREEN), run_time=3.5)
        self.wait()

        self.play(TransformMatchingTex(eq3, eq))
        self.wait()

        self.embed()

    def func(self, x):
        return -x**2 + 4*x - 1


class LagrangeUnique(Scene):
    def construct(self):
        dots = Tex(r".\\.\\.\\")

        p1 = Tex(
            "(x_{1}, y_{1})",
            tex_to_color_map={"1": A_ORANGE, "x": A_PINK, "y": A_GREEN}
        )
        p1.scale(1.5)
        p1.shift(1.75 * UP)

        p2 = Tex(
            "(x_{n}, y_{n})",
            tex_to_color_map={"n": A_ORANGE, "x": A_PINK, "y": A_GREEN}
        )
        p2.scale(1.5)
        p2.shift(1.5 * DOWN)

        axes = Axes(x_range=(0, 5), y_range=(-3, 3), axis_config={
                    "include_tip": False}, x_axis_config={"stroke_width": 6}, y_axis_config={"stroke_width": 6})

        coors = [[i+np.random.random(), 6*np.random.random()-3]
                 for i in range(5)]

        points = VGroup()
        labels = VGroup()

        for i, (x, y) in enumerate(coors):
            points.add(
                Dot(axes.c2p(x, y), color=A_ORANGE, radius=2*DEFAULT_DOT_RADIUS)
            )
            labels.add(
                Tex(f"(x_{{{i+1}}}, y_{{{i+1}}})",
                    tex_to_color_map={
                        str(i+1): A_ORANGE,
                        "x": A_PINK, "y": A_GREEN}
                    ).next_to(points[i], DOWN)
            )

        self.play(Write(axes))
        self.play(Write(points), Write(labels))
        self.wait()

        grp1 = VGroup(axes, points, labels)

        grp2 = VGroup(dots, p1, p2)
        grp2.shift(4 * RIGHT)

        l = Line(10 * UP, 10 * DOWN)
        l.shift(2 * RIGHT)

        self.play(Transform(grp1, grp2))
        self.play(Write(l))
        self.wait()

        l1 = Line(10 * LEFT, 2 * RIGHT)
        l1.shift(2.25 * UP)

        l2 = Line(10 * LEFT, 2 * RIGHT)
        l2.shift(0.7 * DOWN)

        eq1 = Tex(
            "p(x_i)", "=", "q(x_i)", "= y_i",
            tex_to_color_map={"p": A_LAVENDER, "q": A_AQUA,
                              "y": A_GREEN, "i": A_ORANGE, "x": A_PINK}
        )
        eq1.scale(1.5)
        eq1.move_to(2.5 * LEFT + 3 * UP)

        eq2 = Tex("r(x)", "=", "p(x)", "-", "q(x)",
                  tex_to_color_map={"x": A_PINK, "p": A_LAVENDER, "q": A_AQUA, "r": A_RED})
        eq2.scale(1.5)
        eq2.next_to(eq1, DOWN).shift(0.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformFromCopy(eq1[:4], eq2[5:9]), TransformFromCopy(
            eq1[6:10], eq2[10:]), Write(eq2[:5]), Write(eq2[9]), run_time=2)
        self.play(Write(l1))
        self.wait()

        eq3 = Tex(r"\mathrm{deg} \ r(x)", r"\leq n-1", tex_to_color_map={"r": A_RED,
                  "x": A_PINK, r"\mathrm{deg}": A_YELLOW, "n": A_ORANGE, "1": A_ORANGE})
        eq3.scale(1.5)
        eq3.next_to(eq2, DOWN).shift(0.5 * DOWN)

        self.play(TransformFromCopy(eq2[:4], eq3[1:5]), Write(
            eq3[0]), Write(eq3[5:]), run_time=2)
        self.wait()

        eq4 = Tex(r"r(x_i) = p(x_i) - q(x_i)", tex_to_color_map={
            "i": A_ORANGE, "p": A_LAVENDER,
            "q": A_AQUA, "x": A_PINK, "y": A_GREEN, "r": A_RED}
        )
        eq4.scale(1.5)
        eq4.next_to(eq3, DOWN).shift(0.65 * DOWN)

        eq4_1 = Tex(r"r(x_i)", "= 0", tex_to_color_map={
                    "i": A_ORANGE, "r": A_RED, "x": A_PINK})
        eq4_1.scale(1.5)
        eq4_1.move_to(eq4, LEFT)

        self.play(Write(l2))
        self.play(Write(eq4))
        self.wait()

        self.play(Transform(eq4[5:], eq4_1[5]))
        self.play(ApplyMethod(eq4.shift, (eq3.get_center()
                  [1] - eq4.get_center()[1]) * RIGHT))
        self.wait()

        eq5 = Tex(r"\mathrm{deg} \ r(x)", r"=n", tex_to_color_map={
                  "r": A_RED, "x": A_PINK, r"\mathrm{deg}": A_YELLOW, "n": A_ORANGE, "1": A_ORANGE})
        eq5.scale(1.5)
        eq5.next_to(eq4, DOWN).shift(0.5 * DOWN)

        self.play(Write(eq5))
        self.wait()

        self.embed()


class FinitePoly(Scene):
    def construct(self):
        eq = Tex(r"f(x) = x^2 + 2 \mod 5",
                 tex_to_color_map={"5": A_ORANGE, "2": A_YELLOW, "x": A_PINK, "f": A_GREEN})
        eq.scale(1.5)
        eq.shift(3.25 * UP)

        axes = Axes(
            x_range=(0, 4), y_range=(0, 4),
            axis_config={"include_tip": False}, x_axis_config={"stroke_width": 6}, y_axis_config={"stroke_width": 6}
        )
        axes.add_coordinate_labels()

        self.play(Write(eq))
        self.play(Write(axes))
        self.wait()

        points = VGroup()

        for x in range(0, 5):
            y = (x**2 + 2) % 5
            obj = Dot(axes.c2p(x, y), color=A_RED,
                      radius=2 * DEFAULT_DOT_RADIUS)
            points.add(obj)

        self.play(Write(points))
        self.wait()

        self.embed()


class RSCodes(Scene):
    def construct(self):
        shades = ["#fc998e", "#fb8d80", "#fb8072", "#e27367", "#c9665b"]
        numbers = [2, 4, 3, 1, "?", "?"]
        numbers2 = [2, 4, 3, 1, 0, "?"]

        c = [2, 4, 0, 4, 1, 3]

        s = VGroup()
        for i in range(4):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1.5, num_scale=2)
            s.add(s_i.shift(2*i * RIGHT))
        s.center()

        self.play(Write(s))
        self.wait()

        s2 = VGroup()
        for i in range(6):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s2.add(s_i.shift(1.5*i * RIGHT))
        s2.center()

        b1 = Brace(s2[-2:])
        t1 = b1.get_tex("k = 2", tex_to_color_map={
                        "k": A_YELLOW, "2": A_ORANGE})
        t1.scale(1.5)
        t1.shift(0.25 * DOWN)

        self.play(ReplacementTransform(s, s2[:5]), Write(s2[5:]))
        self.play(GrowFromCenter(b1), Write(t1))
        self.wait()

        labels = VGroup()
        for i, obj in enumerate(s2):
            t = Tex(str(i+1), color=A_YELLOW)
            t.next_to(obj, UP)
            t.scale(1.25)
            labels.add(t)
        labels.shift(0.25 * UP)

        labels2 = VGroup()
        for i, obj in enumerate(s2):
            t = Tex(f"m_{str(i+1)}",
                    tex_to_color_map={str(i+1): A_YELLOW, "m": A_PINK})
            t.next_to(obj, UP)
            t.scale(1.25)
            labels2.add(t)
        labels2.shift(0.25 * UP)
        labels2_cp = labels2.deepcopy()

        self.play(Write(labels))
        self.wait()

        self.play(Transform(labels, labels2))
        self.wait()

        b2 = Brace(labels, UP)
        t2 = b2.get_tex(r"p > m_i", tex_to_color_map={
                        "p": A_GREEN, "m": A_PINK, "i": A_YELLOW})

        self.play(GrowFromCenter(b2), Write(t2))
        self.wait()

        self.play(Uncreate(b2), Uncreate(t2))
        self.wait()

        s_cp, s_cp2 = s2.deepcopy(), s2.deepcopy()
        for i, x in enumerate(np.linspace(3, -3, 6)):
            s_cp[i].move_to(x * UP)
        s_cp.shift(3 * RIGHT)

        eqs = VGroup()
        for i, x in enumerate(np.linspace(3, -3, 6)):
            t = Tex(f"f({i}) = m_{i+1}" if i < 4 else f"m_{i+1} = f({i})", tex_to_color_map={
                    "f": A_GREEN, "x": A_PINK, "m": A_PINK, str(i): A_YELLOW, str(i+1): A_YELLOW})
            t.move_to(x * UP)
            t.scale(1.25)
            eqs.add(t)

        self.play(Uncreate(VGroup(b1, t1, labels[-1], labels[-2])))
        self.play(
            Transform(s2, s_cp),
            ReplacementTransform(
                labels[:-2],
                VGroup(*[eq[-2:] for eq in eqs])[:-2]
            )
        )
        self.play(Write(VGroup(*[eq[:-2] for eq in eqs[:-2]])))
        self.wait()

        axes = Axes(
            x_range=(0, 4), y_range=(-2, 6), axis_config={"include_tip": False},
            width=6, x_axis_config={"stroke_width": 3}, y_axis_config={"stroke_width": 3}
        )
        axes.shift(3 * RIGHT)

        curve = ParametricCurve(lambda t: axes.c2p(
            t, self.f(t)), t_range=(0, 5), color=A_GREEN)

        dots = VGroup()
        point_lbl = VGroup()

        for i in range(4):
            dots.add(Dot(axes.c2p(i, numbers[i]), color=A_GREEN))
            point_lbl.add(Tex(f"({i}, {numbers[i]})", tex_to_color_map={str(i): A_ORANGE, str(
                numbers[i]): A_ORANGE}).move_to(dots[i], DOWN).add_background_rectangle(buff=0.1))
        point_lbl.shift(0.75 * DOWN)
        eqs[-2:].shift(5 * LEFT)

        self.play(VGroup(eqs[:-2], s2).shift, 5 * LEFT)
        self.play(Write(axes))
        self.wait()

        self.play(TransformFromCopy(eqs[:-2], dots))
        self.play(Write(point_lbl))
        self.wait()

        self.bring_to_front(point_lbl)
        self.play(Write(curve))
        self.bring_to_front(point_lbl)
        self.wait()

        self.play(Write(eqs[-2:]))
        self.wait()

        self.play(Uncreate(VGroup(axes, curve, point_lbl, dots)))

        s_cp2.shift(2 * RIGHT)

        t1, t2 = Tex("f(4)"), Tex("f(5)")

        t1.move_to(s_cp2[-2])
        t2.move_to(s_cp2[-1])

        s_cp2[-1].remove(s_cp2[-1].num)
        s_cp2[-2].remove(s_cp2[-2].num)

        s_cp2[-1].num = t2
        s_cp2[-1].add(s_cp2[-1].num)

        s_cp2[-2].num = t1
        s_cp2[-2].add(s_cp2[-2].num)

        labels2_cp.shift(2 * RIGHT)

        l = Line(10 * UP, 10 * DOWN)
        l.shift(3 * LEFT)

        self.play(Transform(s2, s_cp2), Write(labels2_cp), Write(l))

        r1 = BackgroundRectangle(VGroup(labels2_cp[-2], s_cp2[-2]), buff=0.15)
        r2 = BackgroundRectangle(VGroup(labels2_cp[1], s_cp2[1]), buff=0.15)

        self.play(ShowCreation(r1), ShowCreation(r2))
        self.wait()

        self.play(Uncreate(VGroup(eqs, l)))

        s_cp, labels2_cp2 = s2.deepcopy(), labels2_cp.deepcopy()

        for i, x in enumerate(np.linspace(3, -3, 6)):
            labels2_cp2[i].move_to(x * UP)
            s_cp[i].move_to(x * UP)

        s_cp.shift(6 * LEFT)
        labels2_cp2.shift(4.5 * LEFT)

        axes = Axes(
            x_range=(0, 6), y_range=(-2, 6),
            axis_config={"include_tip": False}, x_axis_config={"stroke_width": 3},
            y_axis_config={"stroke_width": 3}, width=9
        )
        axes.shift(2 * RIGHT)

        r1_2 = BackgroundRectangle(
            VGroup(labels2_cp2[-2], s_cp[-2]), buff=0.15)
        r2_2 = BackgroundRectangle(VGroup(labels2_cp2[1], s_cp[1]), buff=0.15)

        self.play(
            Transform(s2, s_cp),
            Transform(labels2_cp, labels2_cp2),
            Transform(r1, r1_2), Transform(r2, r2_2)
        )

        coors = [(0, 2), (2, 3), (3, 1), (5, 2)]

        dots, labels = VGroup(), VGroup()
        for x, y in coors:
            dots.add(Dot(axes.c2p(x, y), color=A_GREEN))
            labels.add(
                Tex(f"({x}, {y})", tex_to_color_map={str(x): A_ORANGE, str(y): A_ORANGE}
                    ).move_to(dots[-1], DOWN).shift(0.25 * DOWN).add_background_rectangle(buff=0.1))
        labels.shift(0.5 * DOWN)

        curve = ParametricCurve(lambda t: axes.c2p(
            t, self.f(t)), t_range=(0, 6), color=A_GREEN)

        self.play(Write(axes))

        left = [0, 2, 3, 5]
        grp = VGroup(*self.get_indices(labels2_cp, left))

        self.play(TransformFromCopy(grp, dots))
        self.play(Write(labels))
        self.wait()

        self.play(Write(curve))
        self.bring_to_front(labels)

        x = ValueTracker(0)
        d = Dot(radius=2*DEFAULT_DOT_RADIUS, color=A_YELLOW)

        def point_updater(point):
            new_point = point.move_to(
                axes.c2p(x.get_value(), self.f(x.get_value())))
            point.become(new_point)

        l1 = Line()

        def dash_updater_x(line):
            point = axes.c2p(x.get_value(), self.f(x.get_value()))
            new_line = Line(axes.c2p(0, self.f(x.get_value())),
                            point, stroke_opacity=0.5)
            line.become(new_line)
            self.bring_to_back(line)

        l2 = Line()

        def dash_updater_y(line):
            point = axes.c2p(x.get_value(), self.f(x.get_value()))
            new_line = Line(axes.c2p(x.get_value(), 0),
                            point, stroke_opacity=0.5)
            line.become(new_line)
            self.bring_to_back(line)

        self.play(Write(d))
        d.add_updater(point_updater)
        l1.add_updater(dash_updater_x)
        l2.add_updater(dash_updater_y)
        self.wait()

        lbl = Tex(f"(1, 4)", tex_to_color_map={"1": A_ORANGE, "4": A_ORANGE}).move_to(
            Point(axes.c2p(1, 4)), DOWN).shift(0.25 * UP).add_background_rectangle(buff=0.1)

        self.play(Indicate(VGroup(d, labels[0][1:])))
        self.play(TransformFromCopy(d, s_cp[0]))
        self.wait()

        self.play(x.increment_value, 1, run_time=3)
        self.play(Write(lbl))
        self.play(Indicate(VGroup(d, lbl[1:])))
        self.play(TransformFromCopy(d, s_cp[1]), Uncreate(r2))
        self.wait()

        self.play(x.increment_value, 1, run_time=3)
        self.play(Indicate(VGroup(d, labels[1][1:])))
        self.play(TransformFromCopy(d, s_cp[2]))
        self.wait()

        self.play(x.increment_value, 1, run_time=3)
        self.play(Indicate(VGroup(d, labels[2][1:])))
        self.play(TransformFromCopy(d, s_cp[3]))

        s = VGroup()
        for i in range(4):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s.add(s_i.shift(1.5*i * RIGHT))
        s.center()
        s.move_to(3 * UP)

        m = {"{5}": A_ORANGE, **{str(i): A_YELLOW for i in list(
            range(5)) + list(range(6, 10)) + [56]}, "f": A_GREEN, "x": A_PINK}

        eq = Tex(r"f(x) = 2x^3 + 2 \mod {{5}}", tex_to_color_map=m)
        eq.scale(1.5)
        eq.shift(1.5 * UP)

        eqs, eqs2 = VGroup(), VGroup()
        for i, y in enumerate(numbers[:-2]):
            mod_eq = Tex(rf"f({i}) = {2*i**3 + 2} \mod {{5}}",
                         tex_to_color_map=m)
            mod_eq.scale(1.5)
            mod_eq.move_to(6 * LEFT, LEFT)
            mod_eq.shift(i * DOWN)
            eqs.add(mod_eq)

            mod_eq2 = Tex(
                rf"f({i}) = {(2*i**3+2)%5} \mod {{5}}", tex_to_color_map=m)
            mod_eq2.scale(1.5)
            mod_eq2.move_to(6 * LEFT, LEFT)
            mod_eq2.shift(i * DOWN)
            eqs2.add(mod_eq2)

        remove_grp = VGroup(
            axes, d, curve, dots, lbl,
            labels2_cp2, labels, labels2_cp, s_cp, *s2[-2:],
            l1, l2)

        self.play(Uncreate(remove_grp))
        self.remove(*self.mobjects[:2])
        self.wait()

        self.play(Transform(s2[:-2], s))
        self.wait()

        self.play(Write(eq))
        self.wait()

        self.play(Write(eqs[0]))
        self.wait(1)

        self.play(Write(eqs[1]))
        self.wait(1)

        self.play(Write(eqs[2]))
        self.play(TransformMatchingTex(eqs[2], eqs2[2]))
        self.wait(1)

        self.play(Write(eqs[3]))
        self.play(TransformMatchingTex(eqs[3], eqs2[3]))
        self.wait(1)

        eqs_right1 = Tex(r"f(4) = 0 \mod 5", tex_to_color_map={
                         "5": A_ORANGE, "0": A_YELLOW, "4": A_YELLOW, "f": A_GREEN})
        eqs_right1.scale(1.5)
        eqs_right1.move_to(6*LEFT+FRAME_WIDTH/2*RIGHT, LEFT)

        eqs_right2 = Tex(r"f(5) = 2 \mod {{5}}", tex_to_color_map={
                         r"5": A_YELLOW, "{5}": A_ORANGE, "2": A_YELLOW, "4": A_YELLOW, "f": A_GREEN})
        eqs_right2.scale(1.5)
        eqs_right2.move_to(6*LEFT+FRAME_WIDTH/2*RIGHT + 1 * DOWN, LEFT)

        s_11 = VGroup()
        for i in range(5):
            s_i = NumberSquare(
                numbers[i], shades[c[i]], side_length=1, num_scale=1.5)
            s_11.add(s_i.shift(1.5*i * RIGHT))
        s_11.center()
        s_11.shift(3 * UP)

        s = s2[:-2]
        self.play(Transform(s, s_11[:-1]), Write(s_11[-1]))

        s_12 = NumberSquare(0, shades[c[4]], side_length=1, num_scale=1.5)
        s_12.move_to(s_11[-1])

        self.play(TransformFromCopy(eqs_right1[4], s_12), Uncreate(s_11[-1]))

        s_21 = VGroup()
        for i in range(6):
            s_i = NumberSquare(
                numbers2[i], shades[c[i]], side_length=1, num_scale=1.5)
            s_21.add(s_i.shift(1.5*i * RIGHT))
        s_21.center()
        s_21.shift(3 * UP)

        s_22 = NumberSquare(2, shades[c[5]], side_length=1, num_scale=1.5)
        s_22.move_to(s_21[-1])

        self.play(Transform(VGroup(*s, s_12), s_21[:-1]), Write(s_21[-1]))
        self.play(TransformFromCopy(eqs_right2[4], s_22), Uncreate(s_21[-1]))

        self.embed()

    @staticmethod
    def get_indices(arr, indices):
        return [arr[i] for i in indices]

    @staticmethod
    def f(x):
        return 1/3 * x**3 - 5/2 * x**2 + 25/6 * x + 2
