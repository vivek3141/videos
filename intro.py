from manim import *


class Intro(Scene):
    def construct(self):
        logo = SVGMobject("files/logo_t.svg")
        self.play(Write(logo))
        self.wait()
