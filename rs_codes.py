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

        BackgroundRectangle

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

        eq6 = Tex("a+", "(-a)", "=", "0", tex_to_color_map={"a": A_PINK})
        eq6.scale(1.5)
        eq6.move_to(eq5, LEFT)
        eq6.shift(2 * DOWN)

        b = Brace(eq6[2:5])
        t_b = b.get_text("Additive inverse", color=A_GREEN)
        t_b.scale(1.5)
        t_b.shift(0.25 * DOWN)

        eq7 = Tex("a+", "(-a)", "\equiv", "0", tex_to_color_map={"a": A_PINK})
        eq7.scale(1.5)
        eq7.move_to(eq6, LEFT)

        self.play(ApplyMethod(eq5.shift, UP))
        self.play(Write(eq6))
        self.wait()

        self.play(Write(b), Write(b_t))
        self.wait()

        self.play(TransformMatchingTex(eq6, eq7))
        self.wait()

        self.embed()