from manim import *


class Intro(Scene):
    def construct(self):
        text = TextMobject("Why do we use Mean Squared Error?", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(1.5)
        self.play(Write(text))


class CostFunction(Scene):
    def construct(self):
        text = TextMobject("Cost Function", tex_to_color_map={"Cost Function": YELLOW})
        text2 = TextMobject("not", tex_to_color_map={"not": RED})
        eq2 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} |h_\\theta (x^{(i)}) - y^{(i)}| $")
        eq1 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} (h_\\theta (x^{(i)}) - y^{(i)})^2 $")
        text.scale(2)
        eq1.scale(2.5)
        eq2.scale(2.5)
        eq2.move_to(3 * DOWN)
        text.move_to(3 * UP)
        self.play(Write(text))
        self.play(Transform(text, eq1))
        self.play(ApplyMethod(text.shift, 3 * UP))
        self.play(Write(text2))
        self.play(Write(eq2))
        self.wait(2)
