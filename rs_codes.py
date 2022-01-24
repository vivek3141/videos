from ast import SetComp
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

        self.embed()
        # s.move_to(UP)
        # eq1 = Tex("3 + 3 \equiv 1 \mod 5",
        #           tex_to_color_map={"3": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
        # eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        # add(eq1)
        # eq1.scale(1.5)
        # eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        # t.move_to(1.5 * UP)
        # s.move_to(1.5 * UP)
        # remove(s[0])
        # add(s[0])
        # remove(s[1])
        # add(s[1])
        # remove(eq1)
        # eq1 = Tex(
        #     "3 + 3 = 6", tex_to_color_map={"3": A_ORANGE, "6": A_ORANGE, "5": A_AQUA})
        # eq1.scale(1.5)
        # eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        # add(eq1)
        # eq2 = Tex("3 + 3 \equiv 1 \mod 5",
        #           tex_to_color_map={"3": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
        # add(eq2)
        # eq2.scale(1.5)
        # eq2.move_to(0 * UP + 0.5 * LEFT, RIGHT)
        # eq1.move_to(eq2, LEFT)
        # remove(eq2)
        # cp = eq1.copy()
        # play(TransformMatchingTex(eq1, eq2))
        # remove(eq1[3])
        # remove(eq1[2])
        # remove(eq2[2])
        # remove(eq2[3])
        # add(eq2[2])
        # play(Indicate(eq2[3]))
        # play(Indicate(eq2[3], scale_factor=2))
        # play(Indicate(eq2[3], scale_factor=1.5))
        # play(s.move_to, 4 * RIGHT + UP)
        # c = Circle(radius=2)
        # add(c)
        # c.next_to(t, DOWN)
        # c.next_to(s, DOWN)
        # play(s.move_to, 4 * RIGHT + 1.5 * UP)
        # c.next_to(s, DOWN)
        # c.set_color(A_GREY)
        # np.linspace(90, 450)
        # np.linspace(90, 450, 5)
        # np.linspace(90, 450, 6)
        # for t in np.linspace(90, 450, 6):
        #     x = 2 * np.cos(t)
        # for i, t in enumerate(np.linspace(-3 * PI/2, PI/2, 6)[:-1]):
        #     x, y = 2 * np.cos(t), 2 * np.sin(t)
        #     grp.add(Tex(str(i)).move_to([x, y, 0]))
        # grp = VGroup()
        # for i, t in enumerate(np.linspace(-3 * PI/2, PI/2, 6)[:-1]):
        #     x, y = 2 * np.cos(t), 2 * np.sin(t)
        #     grp.add(Tex(str(i)).move_to([x, y, 0]))
        # add(grp)
        # grp.move_to(c.get_center())
        # for i, t in enumerate(np.linspace(-3 * PI/2, PI/2, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(1.5).move_to([x, y, 0]))
        # remove(grp)
        # grp = VGroup()
        # for i, t in enumerate(np.linspace(-3 * PI/2, PI/2, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(1.5).move_to([x, y, 0]))
        # add(grp)
        # grp.move_to(c.get_center())
        # cent = c.get_center()
        # remove(grp)
        # grp = VGroup()
        # for i, t in enumerate(np.linspace(-3 * PI/2, PI/2, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(
        #         1.5).move_to(cent).shift([x, y, 0]))
        # add(grp)
        # for i, t in enumerate(np.linspace(PI/2, PI/2 + 2*PI, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(
        #         1.5).move_to(cent).shift([x, y, 0]))
        # remove(grp)
        # grp = VGroup()
        # for i, t in enumerate(np.linspace(PI/2, PI/2 + 2*PI, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(
        #         1.5).move_to(cent).shift([x, y, 0]))
        # add(grp)
        # for i, t in enumerate(np.linspace(PI/2, PI/2 - 2*PI, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(
        #         1.5).move_to(cent).shift([x, y, 0]))
        # remove(grp)
        # grp = VGroup()
        # for i, t in enumerate(np.linspace(PI/2, PI/2 - 2*PI, 6)[:-1]):
        #     x, y = 1.5 * np.cos(t), 1.5 * np.sin(t)
        #     grp.add(Tex(str(i), color=A_ORANGE).scale(
        #         1.5).move_to(cent).shift([x, y, 0]))
        # add(grp)
        # remove(s[1])
        # add(s[1])
        # for i in range(1, 10, 2):
        #     remove(s[i])
        # remove(s[3])
        # remove(s[2])
        # remove(s[3])
        # remove(s[4])
        # remove(s[5])
        # remove(s[6])
        # remove(s[7])
        # 1, 4
        # remove(s[8])
        # add(s)
        # for i in range(1, 17, 3):
        #     remove(s[i])
        # add(s)
        # for i in range(1, 16, 3):
        #     remove(s[i])
        # add(s)
        # remove(s[13])
        # remove(s[10])
        # add(s)
        # add(s)
        # for i in range(1, 14, 3):
        #     remove(s[i])
        # add(s)
        # remove(grp)
        # s_num = list(range(1, 14, 3))
        # anims = []
        # for i in range(4):
        #     anims.append(TransformFromCopy(s[s_num[i]], grp[i]))
        # play(Transform(*anims), run_time=5)
        # play(*anims, run_time=5)
        # remove(grp)
        # s_num
        # for i in range(5):
        #     anims.append(TransformFromCopy(s[s_num[i]], grp[i]))
        # anims = []
        # for i in range(5):
        #     anims.append(TransformFromCopy(s[s_num[i]], grp[i]))
        # anims
        # play(*anims, run_time=5)
        # self.embed()
# eq1 = Tex(r"(+, -, \cross, \olddiv)")
# add(eq1)
# eq1.scale(2)
# eq1 = Tex(r"(+, -, \cross, \olddiv) \mod {p}", tex_to_color_map={"{p}": A_AQUA})
# remove(self.mobjects[-1])
# add(eq1)
# eq1.scale(1.5)
# eq1.shift(UP)
# eq1.move_to(1 * UP + 1 * RIGHT, LEFT)
# eq1.move_to(1 * UP + 1 * RIGHT, RIGH)
# eq1.move_to(1 * UP + 1 * RIGHT, RIGHT)
# title.shift(LEFT)
# title.shift(LEFT)
# title.shift(LEFT)
# eq1.next_to(title, RIGHT)
# eq1.shift(0.5 * RIGHT)
# title.shift(0.5 * LEFT)
# eq1.shift(0.5 * LEFT)
# arrow = Arrow(ORIGIN, 0.25 * RIGHT)
# add(arrow)
# remove(arrow)
# s = Tex("{0, 1, 2, 3, 4}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# add(s)
# s = Tex(r"\{ 0, 1, 2, 3, 4 \}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# remove(self.mobjects[-1])
# s = Tex(r"\{0, 1, 2, 3, 4\}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# s1 = Tex(r"\{")
# s1 = Tex(r"\{ \}")
# add(s1)
# s1 = Tex(r"\{")
# remove(self.mobjects[-1])
# Set
# Matrix
# List
# eq = Tex(r"\{", *3*["\\quad \\\\"], r"\}")
# eq = Tex(r"\{" + 3*"\\quad \\\\" + "\}")
# add(eq)
# eq = Tex(r"\{" + 3*"\\quad \\" + "\}")
# remove(self.mobjects[-1])
# eq = Tex(r"\{" + 3*r"\quad" + r"\}")
# add(eq)
# eq1 = Tex("3")
# eq1 = Tex("3,")
# eq1.next_to(eq[0])
# add(eq1)
# eq1.next_to(eq[-1])
# eq1.next_to(eq[0])
# remove(eq1)
# remove(eq)
# s = Tex(r"\{")
# s = TexTextr(r"\{")
# s = TexText(r"\{")
# s = TexText(r"$\{$")
# s = TexText(r"$\{ \}$")
# add(s)
# remove(s)
# s = Tex()
# Brakcet
# Bracket
# GavinBelson
# s = Tex("negros123")
# s = Tex("{")
# add(s)
# s = Tex("\{")
# s = Tex(r"\{")
# %clear
# s = Tex(r"\{ \}")
# add(s)
# remove(s)
# %clear
# s = TexText(r"{0, 1, 2, 3, 4}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# add(s)
# s = TexText(r"\{ 0, 1, 2, 3, 4 \\}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# s = TexText(r"\{ 0, 1, 2, 3, 4 \}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# s = TexText("{1, 2, 3, 4}")
# add(s)
# remove(s)
# remove(s)
# remove(self.mobjects[-1])
# s = TexText(r"\{ 0, 1, 2, 3, 4 \}", tex_to_color_map={str(i): A_ORANGE for i in range(5)})
# s1 = SingleStringTex("{")
# add(s1)
# s1 = SingleStringTex(r"\{")
# %clear
# %clear
# t = Text("{")
# add(t)
# t = Text("{ 0, 1, 2, 3, 4 }")
# add(t)
# remove(self.mobjects[-1])
# remove(self.mobjects[-1])
# add(t)
# t = Text("{0, 1, 2, 3, 4}")
# remove(self.mobjects[-1])
# add(t)
# t = Text("{0, 1, 2, 3, 4}", tex_to_color_map={})
# t = Text("{0, 1, 2, 3, 4}", tex_to_color_map={"1": A_ORANGE})
# add(t)
# remove(t)
# remove(self.mobjects[-1])
# add(t)
# remove(t)
# t = Text("{0, 1, 2, 3, 4}", t2c={"1": A_ORANGE})
# add(t)
# t = Text("{0, 1, 2, 3, 4}", t2c={str(i): A_ORANGE for i in range(5)})
# add(t)
# remove(t)
# remove(t)
# remove(self.mobjects[-1])
# add(t)
# t = Text("{0, 1, 2, 3, 4}", t2c={str(i): A_ORANGE for i in range(5)})
# remove(self.mobjects[-1])
# add(t)
# t.scale(1.5)
# t.move_to(RIGHT + UP)
# t.move_to(2 * RIGHT + UP)
# t.move_to(3 * RIGHT + UP)
# t.move_to(4 * RIGHT + UP)
# c = Circle(radius=3)
# add(c)
# remove(c)
# c = Circle(radius=2)
# add(c)
# c.next_to(t, DOWN)
# t.move_to(4 * RIGHT + 1.5 * UP)
# c.next_to(t, DOWN)
# remove(c)
# t.move_to(1.5 * UP)
# eq1
# eq1 = Tex("3 + 3 \equiv 1 \mod 5")
# add(eq1)
# eq1.scale(1.5)
# eq1.move_to(0 * UP + 2 * LEFT, RIGHT)
# eq1.move_to(0 * UP + 3 * LEFT, RIGHT)
# eq1.move_to(0 * UP + 1 * LEFT, RIGHT)
# eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
# remove(eq1)
# eq1 = Tex("3 + 3 \equiv 1 \mod 5", tex_to_color_map={"3": A_ORANGE, "1": A_ORANGE, "5": A_AQUA})
# eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
# add(eq1)
# eq1.scale(1.5)
# eq1.move_to(0 * UP + 0.5 * LEFT, RIGHT)
# np.linspace(0, 2 * PI, 5)
# for t in np.linspace(0, 2*PI, 5):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
# for t in np.linspace(0, 2*PI, 5):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
# for t in np.linspace(0, 2*PI, 5):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
# for t in np.linspace(0, 2*PI, 5):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
# for t in np.linspace(0, 2*PI, 5):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
# grp = VGroup()
# for i, t in enumerate(np.linspace(0, 2*PI, 5)):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
#     grp.add(Tex(str(i)).move_to([x, y, 0]))
# add(grp)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# for i, t in enumerate(np.linspace(0, 2*PI, 6))[:-1]:
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
#     grp.add(Tex(str(i)).move_to([x, y, 0]))
# for i, t in enumerate(np.linspace(0, 2*PI, 6)[:-1]):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
#     grp.add(Tex(str(i)).move_to([x, y, 0]))
# remove(self.mobjects[-1])
# grp = VGroup()
# for i, t in enumerate(np.linspace(0, 2*PI, 6)[:-1]):
#     z = np.exp(t*1j)
#     x, y = z.real, z.imag
#     grp.add(Tex(str(i)).move_to([x, y, 0]))
# add(grp)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# grp.shift(RIGHT)
# remove(grp)
# np.linspace(90, 450, 5)
# np.linspace(90, 450, 6)
#         self.embed()
