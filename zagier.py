from manimlib import *

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


class PartScene(Scene):
    CONFIG = {
        "n": 1,
        "title": "",
        "title_color": RED
    }

    def construct(self):
        self.part = TexText(f"Part {self.n}")
        self.part.scale(1.5)
        self.part.shift(2 * UP)

        self.title = TexText(self.title, color=self.title_color)
        self.title.scale(1.5)

        self.play(Write(self.part))
        self.play(Write(self.title))
        self.wait()


class PartOne(PartScene):
    CONFIG = {
        "n": 1,
        "title": "The Involution",
        "title_color": A_RED
    }


class Involution(Scene):
    def construct(self):
        # Sinusodal offset to an ellipse to make it less uniform-looking
        def set_bound_curve(t):
            return [5 * np.cos(t), 3 * np.sin(t) + np.sin(0.5 * t), 0]

        set_bound = ParametricCurve(
            set_bound_curve,
            t_range=(0, 2 * PI),
            color=A_YELLOW,
            fill_opacity=0.35
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
            Circle(fill_color=BLUE_E, stroke_color=BLUE_A, fill_opacity=0.75)
        )

        # Arbritrarly chosen coordinates
        circles[0].move_to(1.5 * LEFT + UP)
        circles[1].move_to(RIGHT + 0.75 * UP)
        circles[2].move_to(0.25 * LEFT + 1.5 * DOWN)

        self.play(Write(circles))
        self.wait()

        circle_move_anims = [
            ApplyMethod(circles[i].move_to,
                        (3.5 * (i - 1) + 1.75) * RIGHT + 2 * UP)
            for i in range(3)
        ]

        self.play(Uncreate(set_bound))
        self.play(
            *circle_move_anims,
            ApplyMethod(s_text.move_to, 5 * LEFT + 2 * UP)
        )
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
            "f(S)",
            tex_to_color_map={"f": A_YELLOW, ")": A_UNKA, "(": A_UNKA}
        )
        fs_text.scale(3)
        fs_text.move_to(5 * LEFT + 2 * DOWN)

        arrows = VGroup()

        for i in range(3):
            start = circles[i].get_center() + 1.25 * DOWN
            end = f_circles[(i != 0) * (3 - i)].get_center() + 1.25 * UP

            arrows.add(Arrow(start, end, stroke_width=10,
                       tip_width_ratio=6, stroke_color=A_YELLOW, buff=0))

        self.play(
            *transform_anims,
            run_time=6
        )
        self.play(
            Write(fs_text),
            Write(arrows)
        )
        self.bring_to_front(circles, f_circles)
        self.wait()

        inv_title = Tex(
            r"\text{Involution} \leftrightarrow f(f(x)) = x",
            tex_to_color_map={r"\leftrightarrow": A_RED,
                              "f": A_YELLOW, "(": A_UNKA, ")": A_UNKA}
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
        self.play(
            *inv_transform_anims,
            run_time=3
        )
        self.wait()

        self.play(
            FadeOut(f_circles, UP), FadeOut(arrows, UP),
            ApplyMethod(circles.shift, 4 * UP)
        )
        self.wait()

        arrows2 = VGroup()

        for i in range(3):
            start = circles[i].get_center() + 1.25 * DOWN
            end = circles[(i != 2) * (1 - i) + 2 * (i == 2)
                          ].get_center() + 1.25 * UP + 4 * DOWN

            arrows2.add(Arrow(start, end, stroke_width=10,
                              tip_width_ratio=6, stroke_color=A_YELLOW, buff=0))

        f_circles2 = circles.deepcopy()
        f_circles2.shift(4 * DOWN)

        f_circles2[1].set_fill(color=RED_E)
        f_circles2[1].set_stroke(color=RED_A)

        f_circles2[0].set_fill(color=GREEN_E)
        f_circles2[0].set_stroke(color=GREEN_A)

        self.play(Write(arrows2[2]), Write(f_circles2[2]))
        self.wait()

        grp = VGroup(f_circles2[2], circles, fs_text, s_text, arrows2[2])

        self.play(ApplyMethod(grp.scale, 0.5))
        self.play(ApplyMethod(grp.shift, UP))

        ff_text = Tex(
            "f(f(S))",
            tex_to_color_map={"f": A_YELLOW, ")": A_UNKA, "(": A_UNKA})
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

        f_label = Tex(
            "f(x) = -x", tex_to_color_map={"x": A_YELLOW, "f": A_BLUE})
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
            lines.add(
                Line(
                    x_vals[i], y_vals[i],
                    color=grad[i],
                    stroke_opacity=0.3
                )
            )

        self.play(ShowCreation(input_c))
        self.play(TransformFromCopy(input_c, output_c), run_time=5)
        self.play(ShowCreation(lines))
        self.wait()

        lines2 = VGroup()
        for i in range(129):
            lines2.add(
                Line(
                    x_vals[i], y_vals[i],
                    color=grad[len(grad)-i-1],
                    stroke_opacity=0.3
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
            r"\text{paired}": A_PINK, "{f}": A_YELLOW,
            "0": A_UNKA, "2": A_UNKA, "S": A_GREEN,
            r"\text{fixed}": A_PINK
        }

        eq1 = Tex(
            r"| \text{paired} \ {f} \ S | \equiv 0 \mod 2",
            tex_to_color_map=color_map
        )
        eq1.scale(2)
        eq1.shift(1.5 * UP)

        eq2 = Tex(
            r"|S| = | \text{fixed} \ {f} \ S | + | \text{paired} \ {f} \ S |",
            tex_to_color_map=color_map
        )
        eq2.scale(2)
        eq2.shift(1.5 * DOWN)

        eq3 = Tex(
            r"|S| \equiv | \text{fixed} \ {f} \ S | \mod 2",
            tex_to_color_map=color_map
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
    CONFIG = {
        "n": 2,
        "title": "The Windmill",
        "title_color": A_AQUA
    }


class GridRectangle(VGroup):
    def __init__(self, height, width,
                 freq=1, rect_kwargs={},
                 line_kwargs={}, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rect = Rectangle(height=height, width=width, **rect_kwargs)
        self.lines = VGroup()

        for i in np.arange(-height/2, height/2, freq):
            self.lines.add(
                Line(LEFT*width/2, RIGHT*width/2, **line_kwargs).shift(i*UP)
            )

        for i in np.arange(-width/2, width/2, freq):
            self.lines.add(
                Line(UP*height/2, DOWN*height/2, **line_kwargs).shift(i*RIGHT)
            )

        self.add(self.rect, self.lines)


class Windmill(VGroup):
    def __init__(self, x, y, z, freq=1, 
                 i_kwargs={"fill_color": A_PINK, "fill_opacity": 0.5}, 
                 o_kwargs={"fill_color": A_AQUA, "fill_opacity": 0.5},
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.square = GridRectangle(x, x, freq=freq, rect_kwargs=i_kwargs)
        self.rects = VGroup()

        s_boundaries = []
        

        for i in range(4):
            # curr_vec[0] = 1 if last two bits are 10 or 01 else -1
            # curr_vec[1] = 1 if 2nd last bit is 1 else -1
            curr_vec = np.array([
                (((i & 1) ^ (i >> 1 & 1)) * 2 + -1),
                ((i >> 1 & 1) * -2 + 1),
                0
            ])

            r = GridRectangle(z, y, freq=freq, rect_kwargs=o_kwargs)
            r.rotate(i * 90 * DEGREES)
            r.move_to(curr_vec * x/2)

            r.shift(curr_vec[0] * (i & 1) * z/2 * RIGHT)
            r.shift(curr_vec[1] * (~i & 1) * z/2 * UP)

            r.shift(curr_vec[0] * (i & 1) * y/2 * DOWN)
            r.shift(curr_vec[1] * (~i & 1) * y/2 * RIGHT)

            self.rects.add(r)

        self.add(self.square, self.rects)
        

class WindmillIntro(Scene):
    def construct(self):
        head_t = Tex(r"\text{For all } p = 4k + 1", tex_to_color_map={"p": A_GREEN, "k": A_ORANGE, "4": A_UNKA, "1": A_UNKA})
        head_t.scale(2)
        head_t.shift(2.5 * UP)

        bot_t = Tex(r"p = a^2 + b^2", tex_to_color_map={"p": A_GREEN, "a": A_PINK, "b": A_PINK, "2": A_UNKA})
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

        other_t = Tex(r"p = x^2 + 4yz", tex_to_color_map={"p": A_GREEN, "x": A_PINK, "y": A_AQUA, "z": A_AQUA, "4": A_UNKA, "2": A_UNKA})
        other_t.scale(2)
        other_t.shift(FRAME_WIDTH/4 * RIGHT + 3 * UP)

        s2 = Square(side_length=4, fill_opacity=0.5, fill_color=A_GREEN)
        s2.shift(FRAME_WIDTH/4 * RIGHT + 0.5 * DOWN)

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
        
        self.play(Transform(VGroup(s2, s2_lbl), wind_f))
        self.play(Write(sq_lbl), Write(wr_lbls))
        self.wait(1)
        
        self.play(FadeOut(VGroup(bot_t, s1), UP))
        self.play(
            ApplyMethod(other_t.shift, FRAME_WIDTH / 4 * LEFT),
            FadeOut(VGroup(sq_lbl, wr_lbls))
        )

        wind = Windmill(2, 1, 3, freq=float("inf"))
        wind.scale(0.75)
        wind.rotate(45 * DEGREES)

        self.play(Transform(wind_f.square, wind.square))
        self.play(*[Transform(wind_f.rects[i], wind.rects[i]) for i in range(4)])
        self.wait()

        self.embed()
