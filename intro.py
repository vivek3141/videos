from manim import *


class Intro(Scene):
    def construct(self):
        logo = SVGMobject("file/logo.svg")
        self.play(Write(logo))
        self.wait(2)
