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
        "title_color": A_AQUA
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

        self.embed()


class CommonInvolution(Scene):
    def construct(self):
        pass