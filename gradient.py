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


class IntroGraphLeft(Scene):
    def construct(self):
        self.embed()


class IntroGraphRight(Scene):
    def construct(self):
        self.embed()


class PartialExample(Scene):
    def construct(self):
        self.embed()
