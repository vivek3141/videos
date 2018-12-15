from manim import *


class Intro(Scene):
    def construct(self):
        text = TextMobject("Why do we use Mean Squared Error?", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(1.5)
        self.play(Write(text))


class CostFunction(Scene):
    def construct(self):
        text = TextMobject("Cost Function", color=YELLOW)
        text2 = TextMobject("not", color=RED)
        eq2 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} |h_\\theta (x^{(i)}) - y^{(i)}| $")
        eq1 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} (h_\\theta (x^{(i)}) - y^{(i)})^2 $")
        text.scale(2)
        eq1.scale(2.5)
        eq2.scale(2.5)
        text2.scale(2)
        eq2.move_to(3 * DOWN)
        text.move_to(3 * UP)
        self.play(Write(text))
        self.play(Transform(text, eq1))
        self.play(ApplyMethod(text.shift, 3 * UP))
        self.play(Write(text2))
        self.play(Write(eq2))
        self.wait(2)


class GradientDescent(Scene):
    def construct(self):
        g = TextMobject("Gradient Descent", color=YELLOW)
        g1 = TextMobject(
            "$\\Theta_0 = \\Theta_0 - \\alpha \\frac{\\partial}{\\partial \\Theta_0} J(\\Theta_0, \\Theta_1)$")
        g2 = TextMobject(
            "$\\Theta_1 = \\Theta_1 - \\alpha \\frac{\\partial}{\\partial \\Theta_1} J(\\Theta_0, \\Theta_1)$")
        text = TextMobject("$\\alpha$ is the learning rate")
        text.move_to(3 * DOWN)
        g1.move_to(1 * UP)
        g2.move_to(1 * DOWN)
        g1.scale(2)
        g2.scale(2)
        g.scale(2.5)
        self.play(Write(g))
        self.play(ApplyMethod(g.shift, 3.5 * UP))
        self.play(Write(g1))
        self.play(Write(g2))
        self.play(Write(text))
        self.wait(2)


class AbsX(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),

    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
