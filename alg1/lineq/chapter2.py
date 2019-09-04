from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Introduction to Linear Equations")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(Write(title), Write(rect))
        self.wait()

        self.play(Uncreate(title), Uncreate(rect))
        self.wait()
