from manimlib import *
from manimlib.once_useful_constructs.graph_scene import GraphScene

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


class Intro(Scene):
    def construct(self):
        self.interact()
        l = Line(10 * UP, 10 * DOWN)

        title1 = TexText("Single Variable")
        title1.scale(1.5)
        title1.move_to(FRAME_WIDTH/4 * LEFT + 3.5 * UP, UP)

        title2 = TexText("Multivariable")
        title2.scale(1.5)
        title2.move_to(FRAME_WIDTH/4 * RIGHT + 3.5 * UP, UP)

        self.play(FadeIn(title1, DOWN), FadeIn(title2, DOWN), Write(l))

        self.embed()


class IntroGraphLeft(GraphScene):
    CONFIG = {
        "x_max": 4,
        "x_labeled_nums": list(range(-1, 5)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 2.5,
        "y_labeled_nums": list(range(5, 20, 5)),
        "n_rect_iterations": 1,
        "default_right_x": 3,
        "func": lambda x: 0.1*math.pow(x-2, 2) + 1,
        "y_axis_label": "",
    }

    def construct(self):
        self.setup_axes()

        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))
        self.graph = graph

        rects = VGroup()
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects.add(rect)

        self.play(
            DrawBorderThenFill(
                rects[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect in rects[1:]:
            self.play(
                Transform(
                    rects[0], rect,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )
            self.wait()

        t = TexText("Riemann Integration")
        t.scale(1.5)
        t.shift(3 * UP)

        self.play(FadeIn(t, DOWN))
        self.wait()


class IntroGraphRight(Scene):
    def construct(self):
        self.embed()


class PartialExample(Scene):
    def construct(self):
        self.embed()
