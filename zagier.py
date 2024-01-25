from manimlib import *
from itertools import product

YELLOW_Z = "#e2e1a4"

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


def get_windmills(n):
    return [
        (x, y, z)
        for (x, y, z) in product(range(1, n), repeat=3)
        if x**2 + 4 * y * z == n
    ]


class GridRectangle(VGroup):
    def __init__(
        self, height, width, freq=1, rect_kwargs={}, line_kwargs={}, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.rect = Rectangle(height=height, width=width, **rect_kwargs)
        self.lines = VGroup()

        for i in np.arange(-height / 2, height / 2, freq):
            self.lines.add(
                Line(LEFT * width / 2, RIGHT * width / 2, **line_kwargs).shift(i * UP)
            )

        for i in np.arange(-width / 2, width / 2, freq):
            self.lines.add(
                Line(UP * height / 2, DOWN * height / 2, **line_kwargs).shift(i * RIGHT)
            )

        self.add(self.rect, self.lines)


class Windmill(VGroup):
    def __init__(
        self,
        x,
        y,
        z,
        freq=1,
        stroke_width=2,
        i_kwargs={"fill_color": "#7e6773", "fill_opacity": 1.0},
        o_kwargs={"fill_color": "#476a64", "fill_opacity": 1.0},
        l_kwargs={},
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.square = GridRectangle(
            x,
            x,
            freq=freq,
            rect_kwargs={"stroke_width": stroke_width, **i_kwargs},
            line_kwargs={"stroke_width": stroke_width, **l_kwargs},
        )
        self.rects = VGroup()

        for i in range(4):
            # curr_vec[0] = 1 if last two bits are 10 or 01 else -1
            # curr_vec[1] = 1 if 2nd last bit is 1 else -1
            curr_vec = np.array(
                [(((i & 1) ^ (i >> 1 & 1)) * 2 - 1), ((i >> 1 & 1) * -2 + 1), 0]
            )

            r = GridRectangle(
                z,
                y,
                freq=freq,
                rect_kwargs={"stroke_width": stroke_width, **o_kwargs},
                line_kwargs={"stroke_width": stroke_width, **l_kwargs},
            )
            r.rotate(i * 90 * DEGREES)
            r.move_to(curr_vec * x / 2)

            r.shift(curr_vec[0] * (i & 1) * z / 2 * RIGHT)
            r.shift(curr_vec[1] * (~i & 1) * z / 2 * UP)

            r.shift(curr_vec[0] * (i & 1) * y / 2 * DOWN)
            r.shift(curr_vec[1] * (~i & 1) * y / 2 * RIGHT)

            self.rects.add(r)

        self.add(self.square, self.rects)


class PartScene(Scene):
    CONFIG = {"n": 1, "title": "Placeholder", "title_color": RED}

    def construct(self):
        self.part = TexText(f"Part {self.n}")
        self.part.scale(1.5)
        self.part.shift(2 * UP)

        self.title = TexText(self.title, color=self.title_color)
        self.title.scale(1.5)

        self.play(Write(self.part))
        self.play(Write(self.title))
        self.wait()


class TitleScene(Scene):
    CONFIG = {"color": None, "text": None}

    def construct(self):
        if self.text is None:
            raise NotImplementedError

        brect = Rectangle(
            height=FRAME_HEIGHT, width=FRAME_WIDTH, fill_opacity=1, color=self.color
        )

        title = TexText(self.text)
        title.scale(1.5)
        title.to_edge(UP)

        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.add(brect)
        self.play(FadeIn(rect, DOWN), Write(title), run_time=2)
        self.wait()


class Recap(TitleScene):
    CONFIG = {"color": "#252626", "text": "What You Just Saw"}


class PartOne(PartScene):
    CONFIG = {"n": 1, "title": "The Involution", "title_color": A_RED}


class OneSentence(Scene):
    def construct(self):
        title = TexText("Zagier's One Sentence Proof", color=A_LAVENDER)
        title.scale(1.5)
        title.shift(3 * UP)

        img = ImageMobject("img/zagier_proof.png")
        img.scale(0.85)

        rect = SurroundingRectangle(img, color=A_LAVENDER, buff=0, stroke_width=8)

        self.play(Write(title))
        self.play(FadeIn(img), Write(rect))
        self.wait()

        self.embed()


class ZagierIntro(Scene):
    def construct(self):
        vectors = [
            FRAME_WIDTH / 4 * LEFT + FRAME_HEIGHT / 4 * UP,
            FRAME_WIDTH / 4 * RIGHT + FRAME_HEIGHT / 4 * UP,
            FRAME_HEIGHT / 4 * DOWN,
        ]
        screens = [
            ScreenRectangle(height=2.75, fill_opacity=1, fill_color=BLACK).move_to(
                vectors[i]
            )
            for i in range(3)
        ]

        texts = ["Simplicity", "Elegance", "Visualization"]
        text_objs = [TexText(texts[i]).next_to(screens[i], UP) for i in range(3)]

        VGroup(*screens, *text_objs).center()
        for i in range(3):
            self.play(FadeIn(screens[i], DOWN))
            self.play(Write(text_objs[i]))
            self.wait(0.25)

        self.embed()


class ZagierIntroVertical(Scene):
    def construct(self):
        b_rect = Rectangle(
            height=FRAME_HEIGHT,
            width=9 / 16 * FRAME_HEIGHT,
            fill_opacity=1,
            fill_color="#252626",
            stroke_width=0,
        )
        self.add(b_rect)

        vectors = [
            ((FRAME_HEIGHT / 2) - (FRAME_HEIGHT / 3.25)) * UP,
            ((FRAME_HEIGHT / 2) - (2 * FRAME_HEIGHT / 3.25)) * UP,
            ((FRAME_HEIGHT / 2) - (3 * FRAME_HEIGHT / 3.25)) * UP,
        ]
        screens = [
            ScreenRectangle(height=1.75, fill_opacity=1, fill_color=BLACK).move_to(
                vectors[i]
            )
            for i in range(3)
        ]

        texts = ["Simplicity", "Elegance", "Visualization"]
        text_objs = [
            TexText(texts[i]).move_to(screens[i]).scale(0.75).shift(1.15 * UP)
            for i in range(3)
        ]

        VGroup(*screens, *text_objs).center()
        for i in range(3):
            self.play(FadeIn(screens[i], DOWN))
            self.play(Write(text_objs[i]))
            self.wait(0.25)

        self.embed()


class Involution(Scene):
    def construct(self):
        # Sinusodal offset to an ellipse to make it less uniform-looking
        def set_bound_curve(t):
            return [5 * np.cos(t), 3 * np.sin(t) + np.sin(0.5 * t), 0]

        set_bound = ParametricCurve(
            set_bound_curve, t_range=(0, 2 * PI), color=A_YELLOW, fill_opacity=0.35
        )
        set_bound.center()

        s_text = Tex("S")
        s_text.scale(3)
        s_text.move_to(set_bound, DL)
        s_text.shift(0.5 * LEFT)

        self.play(Write(set_bound), Write(s_text))

        circles = VGroup(
            Circle(fill_color=RED_E, stroke_color=RED_A, fill_opacity=0.75),
            Circle(fill_color=GREEN_E, stroke_color=GREEN_A, fill_opacity=0.75),
            Circle(fill_color=BLUE_E, stroke_color=BLUE_A, fill_opacity=0.75),
        )

        # Arbritrarly chosen coordinates
        circles[0].move_to(1.5 * LEFT + UP)
        circles[1].move_to(RIGHT + 0.75 * UP)
        circles[2].move_to(0.25 * LEFT + 1.5 * DOWN)

        self.play(Write(circles))
        self.wait()

        circle_move_anims = [
            ApplyMethod(circles[i].move_to, (3.5 * (i - 1) + 1.75) * RIGHT + 2 * UP)
            for i in range(3)
        ]

        self.play(Uncreate(set_bound))
        self.play(*circle_move_anims, ApplyMethod(s_text.move_to, 5 * LEFT + 2 * UP))
        self.wait()

        f_circles = circles.deepcopy()
        f_circles.shift(4 * DOWN)

        f_circles[1].set_fill(color=BLUE_E)
        f_circles[1].set_stroke(color=BLUE_A)

        f_circles[2].set_fill(color=GREEN_E)
        f_circles[2].set_stroke(color=GREEN_A)

        transform_anims = [
            TransformFromCopy(circles[i], f_circles[(i != 0) * (3 - i)])
            for i in range(3)
        ]

        fs_text = Tex(
            "f(S)", tex_to_color_map={"f": A_YELLOW, ")": A_UNKA, "(": A_UNKA}
        )
        fs_text.scale(3)
        fs_text.move_to(5 * LEFT + 2 * DOWN)

        arrows = VGroup()

        for i in range(3):
            start = circles[i].get_center() + 1.25 * DOWN
            end = f_circles[(i != 0) * (3 - i)].get_center() + 1.25 * UP

            arrows.add(
                Arrow(
                    start,
                    end,
                    stroke_width=10,
                    tip_width_ratio=6,
                    stroke_color=A_YELLOW,
                    buff=0,
                )
            )

        self.play(*transform_anims, run_time=6)
        self.play(Write(fs_text), Write(arrows))
        self.bring_to_front(circles, f_circles)
        self.wait()

        inv_title = Tex(
            r"\text{Involution} \leftrightarrow f(f(x)) = x",
            tex_to_color_map={
                r"\leftrightarrow": A_RED,
                "f": A_YELLOW,
                "(": A_UNKA,
                ")": A_UNKA,
            },
        )
        inv_title[1].set_color(A_RED)
        inv_title.scale(1.5)
        inv_title.shift(3.25 * UP)

        all_curr_obj = VGroup(arrows, s_text, fs_text, circles, f_circles)
        self.play(all_curr_obj.shift, 0.5 * DOWN)
        self.play(Write(inv_title))
        self.wait()

        inv_transform_anims = [
            TransformFromCopy(f_circles[i], circles[(i != 0) * (3 - i)])
            for i in range(3)
        ]

        self.play(FadeOut(circles, UP))
        circles.shift(4 * DOWN)

        self.play(f_circles.shift, 4 * UP)
        self.play(*inv_transform_anims, run_time=3)
        self.wait()

        self.play(
            FadeOut(f_circles, UP),
            FadeOut(arrows, UP),
            ApplyMethod(circles.shift, 4 * UP),
        )
        self.wait()

        arrows2 = VGroup()

        for i in range(3):
            start = circles[i].get_center() + 1.25 * DOWN
            end = (
                circles[(i != 2) * (1 - i) + 2 * (i == 2)].get_center()
                + 1.25 * UP
                + 4 * DOWN
            )

            arrows2.add(
                Arrow(
                    start,
                    end,
                    stroke_width=10,
                    tip_width_ratio=6,
                    stroke_color=A_YELLOW,
                    buff=0,
                )
            )

        f_circles2 = circles.deepcopy()
        f_circles2.shift(4 * DOWN)

        f_circles2[1].set_fill(color=RED_E)
        f_circles2[1].set_stroke(color=RED_A)

        f_circles2[0].set_fill(color=GREEN_E)
        f_circles2[0].set_stroke(color=GREEN_A)

        self.play(Write(arrows2[2]), Write(f_circles2[2]))

        b_rect = SurroundingRectangle(
            VGroup(f_circles2[2], arrows2[2], f_circles[2]),
            color=BLUE_E,
            buff=0.15,
            stroke_width=8,
        )
        fixed_text = TexText("Fixed Element", color=BLUE_E)
        fixed_text.scale(1.5)
        fixed_text.move_to(b_rect, LEFT)
        fixed_text.shift(5 * LEFT)

        self.play(Write(b_rect), Write(fixed_text))
        self.wait()

        self.play(Uncreate(b_rect), Uncreate(fixed_text))
        self.wait()

        grp = VGroup(f_circles2[2], circles, fs_text, s_text, arrows2[2])

        self.play(ApplyMethod(grp.scale, 0.5))
        self.play(ApplyMethod(grp.shift, UP))

        ff_text = Tex(
            "f(f(S))", tex_to_color_map={"f": A_YELLOW, ")": A_UNKA, "(": A_UNKA}
        )
        ff_text.scale(1.5)
        ff_text.move_to(fs_text.get_center() + 2 * DOWN)

        arr = arrows2[-1].copy()
        arr.shift(1.75 * LEFT)

        arr2 = arr.copy()
        arr2.shift(2 * DOWN)

        circ = Circle(stroke_color=WHITE)
        circ.scale(0.5)
        circ.move_to(f_circles2[2].get_center() + 1.75 * LEFT)

        q = TexText("?")
        q.scale(1.5)
        q.move_to(circ)

        f_circ = f_circles2[0].copy()
        f_circ.scale(0.5)
        f_circ.move_to(circ.get_center() + 2 * DOWN)

        self.play(Write(ff_text))
        self.play(Write(arr), Write(VGroup(q, circ)))
        self.play(Write(arr2), Write(f_circ))
        self.wait()

        self.play(Uncreate(VGroup(circ, q, ff_text, arr, arr2, f_circ)))
        self.play(grp.shift, DOWN)
        self.play(grp.scale, 2)
        self.play(Write(f_circles2[:-1]), Write(arrows2[:-1]))
        self.wait()

        c = color_gradient([RED_E, GREEN_E, RED_E], 15)
        p_rect = SurroundingRectangle(
            VGroup(*f_circles2[:-1], *arrows2[:-1], *f_circles[:-1]),
            buff=0.15,
            color=c,
            stroke_width=8,
        )
        p_text = Text("Paired Element", gradient=color_gradient([RED_E, GREEN_E], 10))
        p_text.scale(1.5)
        p_text.move_to(p_rect)
        p_text.add_background_rectangle(buff=0.15)

        self.play(ShowCreation(p_rect), Write(p_text))
        self.wait()

        self.embed()


class CommonInvolution(Scene):
    def construct(self):
        input_line = NumberLine()
        input_line.shift(1 * UP)
        input_line.add_numbers(font_size=36)

        x_label = Tex("x", color=A_YELLOW)
        x_label.move_to([-6.5, 1.5, 0])

        output_line = NumberLine()
        output_line.shift(2 * DOWN)
        output_line.add_numbers(font_size=36)

        y_label = Tex("f(x)", tex_to_color_map={"x": A_YELLOW, "f": A_BLUE})
        y_label.move_to([-6.1902, -1.5, 0])

        f_label = Tex("f(x) = -x", tex_to_color_map={"x": A_YELLOW, "f": A_BLUE})
        f_label.scale(1.5)
        f_label.shift(3 * UP)

        self.play(Write(input_line), Write(output_line))
        self.play(Write(x_label), Write(y_label), Write(f_label))

        x_vals, y_vals = [], []
        for x in np.linspace(-8, 8, 129):
            x_vals.append(input_line.n2p(x))
            y_vals.append(output_line.n2p(-x))

        grad = color_gradient([A_PINK, A_GREEN], len(x_vals))
        input_c = DotCloud(x_vals, color=grad)
        output_c = DotCloud(y_vals, color=grad)

        lines = VGroup()

        for i in range(129):
            lines.add(Line(x_vals[i], y_vals[i], color=grad[i], stroke_opacity=0.3))

        self.play(ShowCreation(input_c))
        self.play(TransformFromCopy(input_c, output_c), run_time=5)
        self.play(ShowCreation(lines))
        self.wait()

        lines2 = VGroup()
        for i in range(129):
            lines2.add(
                Line(
                    x_vals[i],
                    y_vals[i],
                    color=grad[len(grad) - i - 1],
                    stroke_opacity=0.3,
                )
            )

        self.play(FadeOut(input_c, UP), FadeOut(lines))
        self.play(ApplyMethod(output_c.shift, 3 * UP))

        input_c.shift(3 * DOWN)
        self.play(TransformFromCopy(output_c, input_c), run_time=3)
        self.play(ShowCreation(lines2))
        self.wait()

        self.embed()


class MoreInvolution(Scene):
    def construct(self):
        color_map = {
            r"\text{paired}": A_PINK,
            "{f}": A_YELLOW,
            "0": A_UNKA,
            "2": A_UNKA,
            "S": A_GREEN,
            r"\text{fixed}": A_PINK,
        }

        eq1 = Tex(
            r"| \text{paired} \ {f} \ S | \equiv 0 \mod 2", tex_to_color_map=color_map
        )
        eq1.scale(2)
        eq1.shift(1.5 * UP)

        eq2 = Tex(
            r"|S| = | \text{fixed} \ {f} \ S | + | \text{paired} \ {f} \ S |",
            tex_to_color_map=color_map,
        )
        eq2.scale(2)
        eq2.shift(1.5 * DOWN)

        eq3 = Tex(
            r"|S| \equiv | \text{fixed} \ {f} \ S | \mod 2", tex_to_color_map=color_map
        )
        eq3.scale(2)
        eq3.shift(1.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(TransformMatchingTex(eq2, eq3))
        self.play(Indicate(eq3))
        self.wait()

        self.embed()


class PartTwo(PartScene):
    CONFIG = {"n": 2, "title": "The Windmill", "title_color": A_AQUA}


class WindmillIntro(Scene):
    def construct(self):
        head_t = Tex(
            r"\text{For all } p = 4k + 1",
            tex_to_color_map={"p": A_GREEN, "k": A_ORANGE, "4": A_UNKA, "1": A_UNKA},
        )
        head_t.scale(2)
        head_t.shift(2.5 * UP)

        bot_t = Tex(
            r"p = a^2 + b^2",
            tex_to_color_map={"p": A_GREEN, "a": A_PINK, "b": A_PINK, "2": A_UNKA},
        )
        bot_t.scale(2)

        self.play(Write(head_t))
        self.play(Write(bot_t))
        self.wait()

        self.play(FadeOut(head_t, UP))
        self.play(bot_t.shift, 3 * UP + FRAME_WIDTH / 4 * LEFT)

        s1 = Square(side_length=4, fill_opacity=0.5, fill_color=A_GREEN)
        s1.shift(FRAME_WIDTH / 4 * LEFT + 0.5 * DOWN)

        s1_lbl = Tex("p").scale(2)
        s1_lbl.move_to(s1)

        self.play(Write(s1), Write(s1_lbl))
        self.wait(1)

        sr1 = Square(side_length=2, fill_color=A_PINK, fill_opacity=0.5)

        r1_lbl = Tex("a^2").scale(2)
        r1_lbl.move_to(sr1)

        r1 = VGroup(sr1, r1_lbl)
        r1.shift(2 * LEFT)

        sr2 = Square(side_length=np.sqrt(12), fill_color=A_PINK, fill_opacity=0.5)

        r2_lbl = Tex("b^2").scale(2)
        r2_lbl.move_to(sr2)

        r2 = VGroup(sr2, r2_lbl)
        r2.shift(RIGHT)

        r_left = VGroup(r1, r2)
        r_left.move_to(s1)

        s1 = VGroup(s1, s1_lbl)

        self.play(Transform(s1, r_left))

        other_t = Tex(
            r"p = x^2 + 4yz",
            tex_to_color_map={
                "p": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "4": A_UNKA,
                "2": A_UNKA,
            },
        )
        other_t.scale(2)
        other_t.shift(FRAME_WIDTH / 4 * RIGHT + 3 * UP)

        s2 = Square(side_length=4, fill_opacity=0.5, fill_color=A_GREEN)
        s2.shift(FRAME_WIDTH / 4 * RIGHT + 0.5 * DOWN)

        s2_lbl = Tex("p").scale(2)
        s2_lbl.move_to(s2)

        self.play(Write(other_t))
        self.play(Write(s2), Write(s2_lbl))
        self.wait(1)

        wind_f = Windmill(2, 1, 3, freq=float("inf"))

        # Positions calculated by moving rects and square relative as desired,
        # then, moving all to FRAME_WIDTH / 4
        wind_f.square.move_to(FRAME_WIDTH / 4 * RIGHT + 1.125 * UP)

        for i in range(4):
            wind_f.rects[i].move_to(ORIGIN + 1.25 * i * RIGHT)
            if i & 1:
                wind_f.rects[i].rotate(90 * DEGREES)

        wind_f.rects.move_to(FRAME_WIDTH / 4 * RIGHT + 1.625 * DOWN)

        sq_lbl = Tex("x^2")
        sq_lbl.scale(2)
        sq_lbl.move_to(wind_f.square)

        wr_lbls = VGroup()
        for i in range(4):
            wr_lbls.add(Tex("yz").move_to(wind_f.rects[i]))

        s2 = VGroup(s2, s2_lbl)
        self.play(Transform(s2, wind_f))
        self.remove(s2)
        self.add(wind_f)

        self.play(Write(sq_lbl), Write(wr_lbls))
        self.wait(1)

        self.play(FadeOut(VGroup(bot_t, s1), UP))
        self.play(other_t.scale, 1 / 1.5)
        self.play(
            ApplyMethod(other_t.shift, FRAME_WIDTH / 4 * LEFT + 0.25 * UP),
            FadeOut(VGroup(sq_lbl, wr_lbls)),
        )

        wind = Windmill(2, 1, 3, freq=float("inf"))
        wind.scale(0.75)
        wind.shift(0.5 * DOWN)

        self.play(Transform(wind_f.square, wind.square))
        self.play(*[Transform(wind_f.rects[i], wind.rects[i]) for i in range(4)])
        self.wait()

        x_label = Tex("x")
        x_label.scale(1.5)

        y_label = Tex("y", color=A_AQUA)
        y_label.scale(1.5)

        z_label = Tex("z", color=A_AQUA)
        z_label.scale(1.5)

        b1 = Brace(wind_f.square, LEFT)
        b1.rotate(180 * DEGREES)
        b1.shift(0.5 * RIGHT)
        b1.put_at_tip(x_label)

        b2 = Brace(wind_f.rects[1], RIGHT)
        b2.put_at_tip(y_label)

        b3 = Brace(wind_f.rects[1], UP)
        b3.put_at_tip(z_label)

        self.play(GrowFromCenter(b1), TransformFromCopy(other_t[2], x_label))
        self.play(GrowFromCenter(b2), TransformFromCopy(other_t[-2], y_label))
        self.play(GrowFromCenter(b3), TransformFromCopy(other_t[-1], z_label))
        self.wait()

        self.embed()


class WindmillDef(Scene):
    def construct(self):
        eq1 = Tex(
            r"W_{n} = \lbrace (x, y, z) \in \mathbb{{N}}^3 \ | \ x^2 + 4yz = {n} \rbrace",
            tex_to_color_map={
                "W": A_YELLOW,
                "{n}": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "3": A_UNKA,
                "4": A_UNKA,
                "{N}": A_LAVENDER,
            },
        )
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        self.play(Write(eq1[:2]))
        self.wait()

        self.play(Write(eq1[2:12]))
        self.wait()

        self.play(Write(eq1[12:]))
        self.wait()

        w_29 = get_windmills(29)

        windmill_stroke_width = 2
        windmills = VGroup()
        # Arbritrarily chosen relative positions
        positions = [-4.825, -1.25, 2, 4.5, 6.375]
        for n, i in enumerate(w_29):
            windmill = Windmill(
                *i,
                l_kwargs={"stroke_width": windmill_stroke_width},
                i_kwargs={
                    "fill_color": A_PINK,
                    "fill_opacity": 0.5,
                    "stroke_width": windmill_stroke_width,
                },
                o_kwargs={
                    "fill_color": A_AQUA,
                    "fill_opacity": 0.5,
                    "stroke_width": windmill_stroke_width,
                },
            )
            windmill.scale(0.25)
            windmill.move_to(positions[n] * RIGHT)
            windmills.add(windmill)
        windmills.center()
        windmills.shift(0.75 * DOWN)

        labels = VGroup(
            *[
                Tex(f"({x}, {y}, {z})").move_to(windmills[i]).shift(2.5 * DOWN)
                for i, (x, y, z) in enumerate(w_29)
            ]
        )

        self.play(Write(windmills[2]), Write(labels[2]))
        for i in range(5):
            if i != 2:
                self.play(Write(windmills[i]), Write(labels[i]))

        b = Brace(windmills, UP)
        t = Tex(r"W_{29}", tex_to_color_map={"W": A_YELLOW, "{29}": A_UNKA})
        b.put_at_tip(t)

        self.play(Write(b), Write(t))
        self.wait()

        self.play(Uncreate(VGroup(b, t, windmills, labels)))

        head_t = Tex(
            r"\text{For all } p = 4k + 1",
            tex_to_color_map={"p": A_GREEN, "k": A_ORANGE, "4": A_UNKA, "1": A_UNKA},
        )
        head_t.scale(1.5)
        head_t.shift(3 * UP)

        eq2 = Tex(
            r"W_{p} = \lbrace (x, y, z) \in \mathbb{{N}}^3 \ | \ x^2 + 4yz = {p} \rbrace",
            tex_to_color_map={
                "W": A_YELLOW,
                "{p}": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "3": A_UNKA,
                "4": A_UNKA,
                "{N}": A_LAVENDER,
            },
        )
        eq2.scale(1.5)
        eq2.shift(1.5 * UP)

        eq3 = Tex(
            r"{p} = x^2 + 4yz",
            tex_to_color_map={
                "{p}": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "4": A_UNKA,
            },
        )
        eq3.scale(1.5)

        self.play(Transform(eq1, eq2))
        self.play(Write(head_t))
        self.wait()

        self.play(TransformMatchingTex(eq2[12:-1], eq3))
        self.wait()

        eq4 = Tex(
            r"{p} = x^2 + 4y^2",
            tex_to_color_map={
                "{p}": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "4": A_UNKA,
            },
        )
        eq4.scale(1.5)
        eq4.shift(3 * DOWN)

        arrow = Arrow(eq3, eq4, stroke_color=A_YELLOW, buff=0.35, stroke_width=16)
        arrow_tex = Tex("y=z", tex_to_color_map={"y": A_AQUA, "z": A_AQUA})
        arrow_tex.scale(1.5)
        arrow_tex.move_to(arrow)
        arrow_tex.shift(1.5 * RIGHT)

        cp = eq3.copy()
        self.play(Write(arrow), Write(arrow_tex))
        self.wait()

        self.play(Transform(cp, eq4))
        self.wait()

        eq5 = Tex(
            r"{p} = x^2 + (2y)^2",
            tex_to_color_map={
                "{p}": A_GREEN,
                "x": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "4": A_UNKA,
            },
        )
        eq5.scale(1.5)
        eq5.shift(3 * DOWN)

        self.play(TransformMatchingTex(cp, eq5))
        self.wait()

        self.embed()


class WindmillOne(Scene):
    def construct(self):
        w_13 = get_windmills(13)

        windmill_stroke_width = 2
        windmills = VGroup()
        # Arbritrarily chosen relative positions
        positions = [-4.825, -1.25, 2]
        for n, i in enumerate(w_13):
            windmill = Windmill(
                *i,
                l_kwargs={"stroke_width": windmill_stroke_width},
                i_kwargs={
                    "fill_color": A_PINK,
                    "fill_opacity": 0.5,
                    "stroke_width": windmill_stroke_width,
                },
                o_kwargs={
                    "fill_color": A_AQUA,
                    "fill_opacity": 0.5,
                    "stroke_width": windmill_stroke_width,
                },
            )
            windmill.scale(0.5)
            windmill.move_to(positions[n] * RIGHT)
            windmills.add(windmill)
        windmills.center()

        labels = VGroup(
            *[
                Tex(f"({x}, {y}, {z})").move_to(windmills[i]).shift(2.5 * DOWN)
                for i, (x, y, z) in enumerate(w_13)
            ]
        )

        title = Tex("W_{13}", tex_to_color_map={"W": A_YELLOW, "{13}": A_GREEN})
        title.scale(1.5)

        b = Brace(windmills, UP)
        b.put_at_tip(title)

        grp = VGroup(windmills, b, labels, title)
        grp.center()

        self.play(Write(title), Write(b))
        for i in range(3):
            self.play(Write(windmills[i]), Write(labels[i]))
        self.wait()

        self.play(Indicate(VGroup(windmills[-1], labels[-1])))
        self.wait()

        eq = Tex(
            r"(1, 1, k)",
            r"\in W_{4k+1}",
            tex_to_color_map={"W": A_YELLOW, "4": A_UNKA, "1": A_UNKA, "k": A_ORANGE},
        )
        eq.scale(1.5)
        eq.shift(3.25 * DOWN)

        self.play(
            ApplyMethod(VGroup(windmills, labels, b, title).shift, 0.5 * UP), Write(eq)
        )
        self.play(Indicate(eq[:7]), Indicate(VGroup(windmills[0], labels[0])))
        self.wait()

        self.embed()


class WindmillProof(Scene):
    def construct(self):
        head_t = Tex(
            r"\text{In }",
            r"{W_{p = 4k}}",
            r"{}_{+}",
            r"{}_{1}",
            r"\text{, (1, 1, k) is the ONLY windmill with } {x} = {y}",
            tex_to_color_map={
                "p": A_GREEN,
                "k": A_ORANGE,
                "4": A_UNKA,
                "1": A_UNKA,
                "{x}": A_PINK,
                "{y}": A_AQUA,
                "{z}": A_AQUA,
                "W": A_YELLOW,
                "{p}": A_GREEN,
            },
        )
        head_t.shift(3.25 * UP)
        self.play(Write(head_t))

        w = Windmill(1, 1, 3)
        w.scale(0.75)
        w.shift(0.8 * DOWN)

        self.play(Write(w))

        self.play(w.rects[0].rotate, 90 * DEGREES)
        self.play(w.rects[0].shift, 2 * LEFT + 0.2 * DOWN)

        b1 = Brace(w.rects[0], RIGHT)
        b2 = Brace(w.square, UP)

        x_label = Tex("x", color=A_PINK)
        x_label.scale(1.5)
        x_label.shift(0.5 * UP)

        self.play(Write(b1), Write(b2), Write(x_label))
        self.wait()

        self.play(
            Uncreate(VGroup(b1, b2, x_label)),
            ApplyMethod(w.rects[0].rotate, -90 * DEGREES),
        )
        self.play(w.rects[0].shift, 2 * RIGHT + 0.2 * UP)
        self.wait()

        w2 = Windmill(1, 1, 3, freq=float("inf"))
        w2.scale(0.75)
        w2.shift(0.8 * DOWN)

        self.play(Transform(w, w2))
        self.wait()

        x, z = ValueTracker(1), ValueTracker(3)
        w.add_updater(
            lambda w: w.become(
                Windmill(x.get_value(), x.get_value(), z.get_value(), freq=float("inf"))
            )
            .scale(0.75)
            .shift(0.8 * DOWN)
        )

        self.play(x.increment_value, 2, rate_func=there_and_back)
        self.play(x.increment_value, -0.75, rate_func=there_and_back)

        self.play(z.increment_value, 0.75, rate_func=there_and_back)
        self.play(z.increment_value, -2, rate_func=there_and_back)

        self.wait()

        w.clear_updaters()
        w3 = Windmill(1, 1, 3)
        w3.scale(0.75)
        w3.shift(0.8 * DOWN + 3.5 * LEFT)

        self.play(Transform(w, w3))

        eq1 = Tex(
            r"\text{Area} = \text{prime } 4{k}+1",
            tex_to_color_map={
                r"\text{Area}": A_LAVENDER,
                r"\text{prime }": A_GREEN,
                "{p}": A_GREEN,
                "{k}": A_ORANGE,
                "4": A_UNKA,
                "1": A_UNKA,
            },
        )
        eq1.move_to(2.5 * RIGHT + 2 * UP)

        eq2 = Tex(
            r"= {x}^2 + 4{x}z",
            tex_to_color_map={
                "{x}": A_PINK,
                "y": A_AQUA,
                "z": A_AQUA,
                "2": A_UNKA,
                "4": A_UNKA,
            },
        )
        eq2.move_to(eq1[1], LEFT)
        eq2.shift(DOWN)

        eq3 = Tex(r"x(x+4z)", tex_to_color_map={"x": A_PINK, "4": A_UNKA, "z": A_AQUA})
        eq3.scale(1.25)
        eq3.move_to(eq2)
        eq3.shift(1.5 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(TransformMatchingTex(eq2[1:].copy(), eq3))
        self.wait()

        eq4 = Tex(
            r"\text{If } {x} \neq 1, \text{ then this provides a}\\ \text{ decomposition of a prime}",
            tex_to_color_map={"{x}": A_PINK, "1": A_UNKA},
        )
        eq4.move_to(eq3)
        eq4.shift(1.5 * DOWN)

        self.play(Write(eq4))
        self.wait()

        self.embed()


class PartThree(PartScene):
    CONFIG = {"n": 3, "title": "The Zagier Map", "title_color": A_LAVENDER}


def get_flip_transform(windmill, flipped):
    windmill_copy = windmill.deepcopy()
    windmill_copy.move_to(flipped)

    return Succession(
        TransformFromCopy(windmill, windmill_copy),
        AnimationGroup(
            *[
                ApplyMethod(windmill_copy.rects[i].rotate, 90 * DEGREES)
                for i in range(4)
            ]
        ),
        AnimationGroup(
            Transform(
                windmill_copy.square,
                flipped.square,
            ),
            *[
                ApplyMethod(
                    windmill_copy.rects[i].move_to,
                    flipped.rects[i],
                )
                for i in range(4)
            ],
        ),
    )


class FlipMap(Scene):
    def construct(self):
        left_w = Windmill(3, 1, 5)
        left_w.scale(0.4)
        left_w.shift(FRAME_WIDTH / 4 * LEFT + 0.5 * UP)

        right_w = Windmill(3, 5, 1)
        right_w.scale(0.4)
        right_w.shift(FRAME_WIDTH / 4 * RIGHT + 0.5 * UP)

        left_t = Tex(
            "(x, y, z)", tex_to_color_map={"x": A_PINK, "y": A_UNKA, "z": A_UNKA}
        )
        left_t.scale(1.5)
        left_t.move_to(FRAME_WIDTH / 4 * LEFT + 3 * DOWN)

        right_t = Tex(
            "(x, z, y)", tex_to_color_map={"x": A_PINK, "y": A_UNKA, "z": A_UNKA}
        )
        right_t.scale(1.5)
        right_t.move_to(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=50,
            max_width_to_length_ratio=10,
        )

        self.play(Write(left_w), Write(left_t))
        self.play(Write(red_arrow))
        self.play(
            get_flip_transform(left_w, right_w),
            TransformMatchingTex(left_t.copy(), right_t),
            run_time=4,
        )
        self.remove(self.mobjects[-2])
        self.add(right_w)
        self.wait()

        left_t_new = Tex(
            "(3, 1, 5)", tex_to_color_map={"3": A_UNKA, "1": A_UNKA, "5": A_UNKA}
        )
        left_t_new.scale(1.5)
        left_t_new.move_to(FRAME_WIDTH / 4 * LEFT + 3 * DOWN)

        right_t_new = Tex(
            "(3, 5, 1)", tex_to_color_map={"3": A_UNKA, "1": A_UNKA, "5": A_UNKA}
        )
        right_t_new.scale(1.5)
        right_t_new.move_to(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(TransformMatchingTex(left_t, left_t_new))
        self.play(TransformMatchingTex(right_t, right_t_new))
        self.wait()

        title = TexText("The Flip Map", color=A_BLUE)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(Write(title))
        self.wait()

        left_w_yz = Windmill(3, 2, 2)
        left_w_yz.scale(0.4)
        left_w_yz.shift(FRAME_WIDTH / 4 * LEFT + 0.5 * UP)

        right_w_yz = Windmill(3, 2, 2)
        right_w_yz.scale(0.4)
        right_w_yz.shift(FRAME_WIDTH / 4 * RIGHT + 0.5 * UP)

        left_t_yz = Tex("(3, 2, 2)", tex_to_color_map={"3": A_UNKA, "2": A_UNKA})
        left_t_yz.scale(1.5)
        left_t_yz.move_to(FRAME_WIDTH / 4 * LEFT + 3 * DOWN)

        right_t_yz = Tex("(3, 2, 2)", tex_to_color_map={"3": A_UNKA, "2": A_UNKA})
        right_t_yz.scale(1.5)
        right_t_yz.move_to(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(
            Transform(left_w, left_w_yz), TransformMatchingTex(left_t_new, left_t_yz)
        )
        self.play(
            Transform(right_w, right_w_yz),
            TransformMatchingTex(right_t_new, right_t_yz),
        )
        self.wait()

        self.embed()


class ZagierMap(Scene):
    def construct(self):
        title = TexText("The Zagier Map", color=A_LAVENDER)
        title.scale(1.5)
        title.shift(3 * UP)

        w_1 = Windmill(3, 5, 1)
        w_1.scale(0.5)

        t_1 = Tex("(3, 5, 1)", tex_to_color_map={"3": A_UNKA, "5": A_UNKA, "1": A_UNKA})
        t_1.scale(1.5)
        t_1.shift(3 * DOWN)

        s = Square(2.5, stroke_width=10, color=A_YELLOW)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=50,
            max_width_to_length_ratio=10,
        )

        self.play(Write(title))
        self.wait()

        self.play(Write(w_1), Write(t_1))
        self.wait()

        self.play(Write(s))
        self.play(Indicate(s))
        self.wait()

        self.play(
            ApplyMethod(w_1.shift, FRAME_WIDTH / 4 * LEFT),
            ApplyMethod(t_1.shift, FRAME_WIDTH / 4 * LEFT),
        )

        w_1_cp = w_1.deepcopy()

        self.add(w_1_cp)
        self.bring_to_front(s)
        self.play(
            Write(red_arrow),
            ApplyMethod(s.shift, FRAME_WIDTH / 4 * RIGHT),
            ApplyMethod(w_1_cp.shift, FRAME_WIDTH / 2 * RIGHT),
        )
        self.wait()

        w_2 = Windmill(5, 1, 1)
        w_2.scale(0.5)
        w_2.shift(FRAME_WIDTH / 4 * RIGHT)

        t_2 = Tex("(5, 1, 1)", tex_to_color_map={"5": A_UNKA, "1": A_UNKA})
        t_2.scale(1.5)
        t_2.shift(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(Indicate(s))
        self.play(
            Transform(w_1_cp.square, w_2.square),
            Uncreate(s),
            TransformMatchingTex(t_1.copy(), t_2),
        )
        self.remove(w_1_cp)
        self.add(w_2)
        self.wait()

        self.play(
            FadeOut(w_2, UP),
            FadeOut(t_1, UP),
            FadeOut(t_2, UP),
            FadeOut(w_1, UP),
            FadeOut(red_arrow, UP),
        )

        w_3 = Windmill(3, 1, 2)
        w_3.scale(0.5)
        w_3.shift(FRAME_WIDTH / 4 * LEFT)

        t_3 = Tex("(3, 1, 2)", tex_to_color_map={"3": A_UNKA, "2": A_UNKA, "1": A_UNKA})
        t_3.scale(1.5)
        t_3.shift(FRAME_WIDTH / 4 * LEFT + 3 * DOWN)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=50,
            max_width_to_length_ratio=10,
        )

        s = Square(1.5, stroke_width=10, color=A_YELLOW)
        s.shift(FRAME_WIDTH / 4 * LEFT)

        self.play(Write(w_3), Write(t_3))
        self.play(Write(red_arrow))
        self.wait()

        self.play(Write(s))
        self.play(Indicate(s))

        w_4 = Windmill(1, 4, 1)
        w_4.scale(0.5)
        w_4.shift(FRAME_WIDTH / 4 * RIGHT)

        w_3_cp = w_3.deepcopy()
        w_3_cp.move_to(w_4)

        t_4 = Tex("(1, 4, 1)", tex_to_color_map={"4": A_UNKA, "1": A_UNKA})
        t_4.scale(1.5)
        t_4.shift(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(TransformFromCopy(w_3, w_3_cp))
        self.play(
            Write(w_4),
            Uncreate(s),
            TransformMatchingTex(t_3.copy(), t_4),
        )
        self.wait()

        self.remove(w_3_cp)
        self.add(w_4)

        self.play(
            ApplyMethod(VGroup(w_3, t_3).shift, FRAME_WIDTH / 2 * RIGHT),
            ApplyMethod(VGroup(w_4, t_4).shift, FRAME_WIDTH / 2 * LEFT),
        )
        self.wait()

        self.play(
            ApplyMethod(VGroup(w_3, t_3).shift, FRAME_WIDTH / 2 * LEFT),
            ApplyMethod(VGroup(w_4, t_4).shift, FRAME_WIDTH / 2 * RIGHT),
        )
        self.wait()

        self.embed()


class ZagierCases(Scene):
    def construct(self):
        cases = [
            r"2y < x",
            r"y < x \land x < 2y",
            r"y = x",
            r"y-z < x \land x < y",
            r"x < y-z",
        ]

        windmills = [
            [[3, 1, 1], [1, 3, 1]],
            [[3, 2, 1], [1, 2, 2]],
            [[3, 3, 1], [3, 3, 1]],
            [[1, 2, 2], [3, 2, 1]],
            [[1, 3, 1], [3, 1, 1]],
        ]

        mapping = [
            r"(x, y, z) \mapsto (x-2y, x+z-y, y)",
            r"(x, y, z) \mapsto (2y-x, y, x+z-y)",
            r"(x, y, z) \mapsto (x, y, z)",
            r"(x, y, z) \mapsto (2y-x, y, x+z-y)",
            r"(x, y, z) \mapsto (x+2z, z, y-x-z)",
        ]

        c_grp, w_grp, m_grp, lines = VGroup(), VGroup(), VGroup(), VGroup()

        for i in range(5):
            wl = Windmill(*windmills[i][0], stroke_width=1).scale(0.25)
            wl.shift((i - 2) * FRAME_WIDTH / 9 * UP + 2.75 * LEFT)
            w_grp.add(wl)

            red_arrow = Arrow(
                1.75 * LEFT + (i - 2) * FRAME_WIDTH / 9 * UP,
                0.75 * LEFT + (i - 2) * FRAME_WIDTH / 9 * UP,
                stroke_color=A_RED,
                stroke_width=7.5,
                max_width_to_length_ratio=50,
            )
            w_grp.add(red_arrow)

            wr = Windmill(*windmills[i][1], stroke_width=1).scale(0.25)
            wr.shift((i - 2) * FRAME_WIDTH / 9 * UP + 0.25 * RIGHT)
            w_grp.add(wr)

            c = Tex(
                cases[i],
                tex_to_color_map={"x": A_PINK, "y": A_AQUA, "z": A_AQUA, "2": A_UNKA},
            )
            c.scale(0.75)
            c.shift((i - 2) * FRAME_WIDTH / 9 * UP + 5.375 * LEFT)
            c_grp.add(c)

            m = Tex(
                mapping[i],
                tex_to_color_map={"x": A_PINK, "y": A_AQUA, "z": A_AQUA, "2": A_UNKA},
            )
            m.scale(0.75)
            m.shift((i - 2) * FRAME_WIDTH / 9 * UP + 4 * RIGHT)
            m_grp.add(m)

        for i in range(4):
            line = Line(10 * LEFT, 10 * RIGHT, stroke_width=0.75)
            line.move_to(((i - 2) * FRAME_WIDTH / 9 + FRAME_WIDTH / 18) * UP)
            lines.add(line)

        left_line = Line(10 * UP, 10 * DOWN, stroke_width=0.75)
        left_line.move_to(3.75 * LEFT)

        right_line = Line(10 * UP, 10 * DOWN, stroke_width=0.75)
        right_line.move_to(1.25 * RIGHT)

        self.play(Write(c_grp), Write(w_grp), Write(m_grp), Write(lines))
        self.wait()

        b_rect = Rectangle(
            width=FRAME_WIDTH, height=FRAME_WIDTH / 9, stroke_color=A_YELLOW
        )
        b_rect.shift(FRAME_WIDTH / 9 * DOWN)

        self.play(Write(b_rect))
        self.wait()

        self.play(Uncreate(b_rect))
        self.wait()

        self.embed()


class ZagierFixed(Scene):
    def construct(self):
        title = Tex(
            r"\text{Fixed Point of Zagier Map }({x}={y})",
            tex_to_color_map={
                "{x}": A_PINK,
                "{y}": A_AQUA,
                "(": WHITE,
                ")": WHITE,
                "=": WHITE,
                r"\text{Fixed Point of Zagier Map }": A_GREY,
            },
        )
        title.scale(1.25)
        title.shift(3 * UP)

        w_1 = Windmill(3, 3, 2)
        w_1.scale(0.5)

        t_1 = Tex("(3, 3, 2)", tex_to_color_map={"3": A_UNKA, "2": A_UNKA})
        t_1.scale(1.5)
        t_1.shift(3 * DOWN)

        s = Square(1.5, stroke_width=10, color=A_YELLOW)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=50,
            max_width_to_length_ratio=10,
        )

        self.play(Write(title))
        self.wait()

        self.play(Write(w_1), Write(t_1))
        self.wait()

        self.play(Write(s))
        self.play(Indicate(s))
        self.wait()

        self.play(
            ApplyMethod(w_1.shift, FRAME_WIDTH / 4 * LEFT),
            ApplyMethod(t_1.shift, FRAME_WIDTH / 4 * LEFT),
        )

        w_1_cp = w_1.deepcopy()

        self.play(
            Write(red_arrow),
            ApplyMethod(w_1_cp.shift, FRAME_WIDTH / 2 * RIGHT),
            ApplyMethod(s.shift, FRAME_WIDTH / 4 * RIGHT),
        )
        self.bring_to_front(s)
        self.wait()

        w_2 = Windmill(3, 3, 2)
        w_2.scale(0.5)
        w_2.shift(FRAME_WIDTH / 4 * RIGHT)

        t_2 = Tex("(3, 3, 2)", tex_to_color_map={"3": A_UNKA, "2": A_UNKA})
        t_2.scale(1.5)
        t_2.shift(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(Write(t_2))
        self.wait()

        self.embed()


class ZagierPrime(Scene):
    def construct(self):
        title = Tex(
            r"\text{Zagier Map has one fixed point on }W_{4k+1}",
            tex_to_color_map={"W": A_YELLOW, "4": A_UNKA, "1": A_UNKA, "k": A_ORANGE},
        )
        title.scale(1.25)
        title.shift(3 * UP)

        w_1 = Windmill(1, 1, 3)
        w_1.scale(0.5)

        t_1 = Tex("(1, 1, k)", tex_to_color_map={"1": A_UNKA, "k": A_ORANGE})
        t_1.scale(1.5)
        t_1.shift(3 * DOWN)

        s = Square(0.5, stroke_width=10, color=A_YELLOW)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=50,
            max_width_to_length_ratio=10,
        )

        self.play(Write(title))
        self.wait()

        self.play(Write(w_1), Write(t_1))
        self.wait()

        self.play(Write(s))
        self.play(Indicate(s))
        self.wait()

        self.play(
            ApplyMethod(w_1.shift, FRAME_WIDTH / 4 * LEFT),
            ApplyMethod(t_1.shift, FRAME_WIDTH / 4 * LEFT),
        )

        w_1_cp = w_1.deepcopy()

        self.play(
            Write(red_arrow),
            ApplyMethod(w_1_cp.shift, FRAME_WIDTH / 2 * RIGHT),
            ApplyMethod(s.shift, FRAME_WIDTH / 4 * RIGHT),
        )
        self.bring_to_front(s)
        self.wait()

        w_2 = Windmill(1, 1, 3)
        w_2.scale(0.5)
        w_2.shift(FRAME_WIDTH / 4 * RIGHT)

        t_2 = Tex("(1, 1, k)", tex_to_color_map={"1": A_UNKA, "k": A_ORANGE})
        t_2.scale(1.5)
        t_2.shift(FRAME_WIDTH / 4 * RIGHT + 3 * DOWN)

        self.play(Write(t_2))
        self.wait()

        self.embed()


class FinalProof(Scene):
    def construct(self):
        text1 = Tex(
            r"\text{For prime } {p} = 4k + 1",
            tex_to_color_map={
                "{p}": A_GREEN,
                "k": A_ORANGE,
                "4": A_UNKA,
                "1": A_UNKA,
            },
        )
        text1.move_to((FRAME_HEIGHT / 2 - FRAME_HEIGHT / 5) * UP, LEFT)

        text2 = Tex(
            r"\text{Zagier Map has one fixed point} \Longrightarrow |W_{p}| \text{ is odd}",
            tex_to_color_map={
                "W": A_YELLOW,
                "{p}": A_GREEN,
                "fixed point": A_LAVENDER,
                "Zagier Map": A_GREY,
                "odd": A_UNKA,
            },
        )
        text2.move_to((FRAME_HEIGHT / 2 - 2 * FRAME_HEIGHT / 5) * UP, LEFT)

        text3 = Tex(
            r"|W_{p}| \text{ is }\text{odd} \Longrightarrow \text{Flip Map}",
            r"\text{ has}",
            r"\text{ odd number of}",
            r"\text{ fixed point}",
            r"\text{s}",
            tex_to_color_map={
                "W": A_YELLOW,
                "{p}": A_GREEN,
                r"\text{Flip Map}": A_BLUE,
                r"\text{odd}": A_UNKA,
            },
        )
        text3.move_to((FRAME_HEIGHT / 2 - 3 * FRAME_HEIGHT / 5) * UP, LEFT)

        text4 = Tex(
            r"|W_{p}| \text{ is }\text{odd} \Longrightarrow \text{Flip Map}",
            r"\text{ has}",
            r"\text{ at least one}",
            r"\text{ fixed point}",
            tex_to_color_map={
                "W": A_YELLOW,
                "{p}": A_GREEN,
                r"\text{Flip Map}": A_BLUE,
                r"\text{odd}": A_UNKA,
            },
        )
        text4.move_to((FRAME_HEIGHT / 2 - 3 * FRAME_HEIGHT / 5) * UP, LEFT)

        text5 = Tex(
            r"|\text{fixed} \ \text{Flip Map} \ W_{p}| \geq 1 \Longrightarrow {p} \text{ is a sum of two squares}",
            tex_to_color_map={
                r"\text{Flip Map}": A_BLUE,
                r"\text{fixed}": A_LAVENDER,
                "{p}": A_GREEN,
                "W": A_YELLOW,
                "1": A_UNKA,
            },
        )
        text5.move_to((FRAME_HEIGHT / 2 - 4 * FRAME_HEIGHT / 5) * UP, LEFT)
        VGroup(text1, text2, text3, text4, text5).shift(6 * LEFT)

        self.play(Write(text1))
        self.wait()

        self.play(Write(text2))
        self.wait()

        self.play(Write(text3))
        self.wait()

        self.play(TransformMatchingTex(text3, text4))
        self.wait()

        self.play(Write(text5))
        self.wait()

        self.embed()


class ErdosBook(Scene):
    def construct(self):
        back = ImageMobject("img/erdos_back.jpg", height=FRAME_HEIGHT)
        # Remove this comment for debugging
        # self.add(back)

        rect = Rectangle(height=0.75, width=2.5, stroke_width=8)
        rect.shift(1.4 * LEFT + 0.625 * UP)

        self.play(Write(rect))

        erdos = ImageMobject("img/paul_erdos.jpeg")
        erdos.shift(4 * RIGHT + 1 * UP)

        erdos_rect = BackgroundRectangle(
            erdos, fill_opacity=0, stroke_width=8, stroke_color=WHITE, stroke_opacity=1
        )
        lines = VGroup(
            Line(rect.get_vertices()[0], erdos_rect.get_vertices()[1], stroke_width=8),
            Line(rect.get_vertices()[3], erdos_rect.get_vertices()[2], stroke_width=8),
        )

        text = TexText("Paul Erdős")
        text.scale(1.5)
        text.move_to(erdos_rect, DOWN)
        text.shift(0.75 * DOWN)

        self.play(Write(erdos_rect), Write(lines), Write(text))
        self.wait()

        self.embed()


class ErdosBookVertical(Scene):
    def construct(self):
        b_rect = Rectangle(
            height=FRAME_HEIGHT,
            width=9 / 16 * FRAME_HEIGHT,
            fill_opacity=1,
            fill_color="#252626",
            stroke_width=0,
        )
        # self.add(b_rect)

        rect = Rectangle(height=0.75, width=2.5, stroke_width=8)
        rect.shift(3 * UP)

        self.play(Write(rect))

        erdos = ImageMobject("img/paul_erdos.jpeg")
        erdos.move_to(rect)
        erdos.shift(4 * DOWN)

        erdos_rect = BackgroundRectangle(
            erdos, fill_opacity=0, stroke_width=8, stroke_color=WHITE, stroke_opacity=1
        )
        lines = VGroup(
            Line(rect.get_vertices()[2], erdos_rect.get_vertices()[1], stroke_width=8),
            Line(rect.get_vertices()[3], erdos_rect.get_vertices()[0], stroke_width=8),
        )

        text = TexText("Paul Erdős")
        text.scale(1.5)
        text.move_to(erdos_rect, DOWN)
        text.shift(0.75 * DOWN)

        self.play(Write(erdos_rect), Write(lines), Write(text))
        self.wait()

        self.embed()


class BookFermat(Scene):
    def construct(self):
        back = ImageMobject("img/fermat_back", height=FRAME_HEIGHT)
        # Remove this comment for debugging
        # self.add(back)

        title = TexText("Fermat's Two Squares Theorem", color=A_LAVENDER)
        title.scale(1.5)
        title.shift(3 * UP)

        rect = BackgroundRectangle(title, buff=SMALL_BUFF)
        title = VGroup(rect, title)

        rect = Rectangle(width=3.5, height=0.5, stroke_width=8)
        rect.shift(1.5 * RIGHT + 1.625 * UP)

        rect_2 = Rectangle(
            width=13.5, height=3, stroke_width=8, fill_color=GREY_D, fill_opacity=1
        )
        rect_2.shift(1.5 * DOWN)

        lines = VGroup(
            Line(rect.get_vertices()[2], rect_2.get_vertices()[1], stroke_width=8),
            Line(rect.get_vertices()[3], rect_2.get_vertices()[0], stroke_width=8),
        )

        eq1 = Tex(
            r"\text{Every prime of the form } {p}=4{k}+1 \text{ can be expressed as a sum of two squares.",
            tex_to_color_map={
                "{p}": A_GREEN,
                "{k}": A_ORANGE,
                "4": A_UNKA,
                "1": A_UNKA,
            },
        )
        eq1.scale(0.8)

        eq2 = Tex(
            r"{13} = 4 \cdot{ {3} }+ 1 ={3}^2 + {2}^2",
            tex_to_color_map={
                "{3}": A_UNKA,
                "{ {3} }": A_ORANGE,
                "^2": GREY_A,
                "{2}": A_UNKA,
                "4": A_UNKA,
                "1": A_UNKA,
                "{13}": A_GREEN,
            },
        )
        eq2.scale(0.8)
        eq2.shift(0.75 * DOWN)

        eq3 = Tex(
            r"29 = 4 \cdot 7 + 1 = 5^2 + {2}^2",
            tex_to_color_map={
                "29": A_GREEN,
                "5": A_UNKA,
                "^2": GREY_A,
                "{2}": A_UNKA,
                "4": A_UNKA,
                "1": A_UNKA,
                "7": A_ORANGE,
            },
        )
        eq3.scale(0.8)
        eq3.shift(1.5 * DOWN)

        VGroup(eq1, eq2, eq3).move_to(rect_2)

        self.play(Write(rect), Write(title))
        self.play(Write(rect_2), Write(lines))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.wait()

        self.embed()


class BookFermatVertical(Scene):
    def construct(self):
        # b_rect = Rectangle(
        #     height=FRAME_HEIGHT,
        #     width=9 / 16 * FRAME_HEIGHT,
        #     fill_opacity=1,
        #     fill_color="#252626",
        #     stroke_width=0,
        # )
        # self.add(b_rect)

        title = TexText("Fermat's Two \\\\ Squares Theorem", color=A_LAVENDER)
        title.scale(1.25)
        title.shift(2.5 * UP)

        rect = BackgroundRectangle(title, buff=SMALL_BUFF)
        title = VGroup(rect, title)

        rect = Rectangle(width=9 / 16 * FRAME_HEIGHT, height=0.5, stroke_width=8)
        rect.shift(1.25 * UP)

        rect_2 = Rectangle(
            width=4.5, height=3, stroke_width=8, fill_color=GREY_D, fill_opacity=1
        )
        rect_2.shift(1.75 * DOWN)

        lines = VGroup(
            Line(rect.get_vertices()[2], rect_2.get_vertices()[1], stroke_width=8),
            Line(rect.get_vertices()[3], rect_2.get_vertices()[0], stroke_width=8),
        )

        eq1 = TexText(
            r"Every prime of the form \\",
            r"${p}$ $=$ $4$${k}$ $+$ $1$ can be expressed \\",
            r"as a sum of two squares. \\ \leavevmode \\",
            r"$13$ $=$ $4$ $\cdot$ ${3}$ $+$ $1$ $=$ $3$$^2$ $+$ $2$$^2$ \\",
            r"$29$ $=$ $4$ $\cdot$ $7$ $+$ $1$ $=$ $5$$^2$ $+$ $2$$^2$ \\",
            tex_to_color_map={
                "${p}$": A_GREEN,
                "${k}$": A_ORANGE,
                "$4$": A_UNKA,
                "$1$": A_UNKA,
                "$13$": A_GREEN,
                "${3}$": A_ORANGE,
                "$^2$": GREY_A,
                "$3$": A_UNKA,
                "$2$": A_UNKA,
                "$4$": A_UNKA,
                "$1$": A_UNKA,
                "$29$": A_GREEN,
                "$5$": A_UNKA,
                "$^2$": GREY_A,
                "$2$": A_UNKA,
                "$4$": A_UNKA,
                "$1$": A_UNKA,
                "$7$": A_ORANGE,
            },
        )
        eq1.scale(0.7)
        eq1.move_to(rect_2)

        self.play(Write(rect), Write(title))
        self.play(Write(rect_2), Write(lines))
        self.play(Write(eq1))
        self.wait()

        self.embed()


class Thumbnail(Scene):
    def construct(self):
        w1 = Windmill(3, 1, 2)
        w1.scale(0.75)
        w1.shift((FRAME_WIDTH / 4 + 0.5) * LEFT)

        w2 = Windmill(1, 4, 1)
        w2.scale(0.75)
        w2.shift((FRAME_WIDTH / 4 + 0.5) * RIGHT)

        red_arrow = Arrow(
            LEFT,
            RIGHT,
            stroke_color=A_RED,
            stroke_width=100,
            max_width_to_length_ratio=35,
            tip_width_ratio=2,
        )

        self.add(w1, w2, red_arrow)
        self.wait()

        self.embed()
