from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Green's Theorem")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(Write(title), Write(rect))
        self.wait()

        #self.play()
