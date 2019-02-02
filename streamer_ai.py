from manim import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Super Mario NEAT")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)
        self.play(
            FadeInFromDown(title),
            ShowCreation(rect)
        )
        self.wait(2)


class InputANN(Scene):
    def construct(self):
        mario = SVGMobject("files/mario.svg")
        a = Arrow(LEFT, RIGHT, color=RED)
        nn = SVGMobject("files/nn.svg")
        nn.move_to(2.5 * RIGHT)
        self.play(ShowCreation(mario))
        self.play(ApplyMethod(mario.shift, 2.5 * LEFT), ShowCreation(a))
        self.play(ShowCreation(nn))
        self.wait(2)
