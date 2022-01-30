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
        self.num.scale(3)

        self.add(self.sq, self.num)


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

        self.embed()
