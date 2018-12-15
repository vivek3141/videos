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
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-5, 6, 2),

    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="y = |x|")
        c = TexMobject("x = 0")
        label_coord = self.input_to_graph_point(0, func_graph)
        c.next_to(label_coord, RIGHT + UP)
        text = TextMobject("y is not differentiable at x=0")
        text.move_to(3 * RIGHT + 2 * DOWN)
        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab), ShowCreation(c))
        self.wait(2)
        self.play(ApplyMethod(func_graph.shift, 2 * LEFT), ApplyMethod(self.axes.shift, 2 * LEFT),
                  ApplyMethod(c.shift, 2 * LEFT), ApplyMethod(graph_lab.shift, 2 * LEFT))
        self.play(Write(text))
        self.wait(2)

    def func_to_graph(self, x):
        return np.abs(x)


class X2(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2),

    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="y = x^2")
        text = TextMobject("y is differentiable everywhere")
        text.move_to(3 * RIGHT + 2 * DOWN)
        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ApplyMethod(func_graph.shift, 2 * LEFT), ApplyMethod(self.axes.shift, 2 * LEFT),
                  ApplyMethod(graph_lab.shift, 2 * LEFT))
        self.play(Write(text))
        self.wait(2)

    def func(self, x):
        return np.power(x, 2)


class Linear(Scene):
    def construct(self):
        g = TextMobject("Estimator and Variance are Linear", color=YELLOW)
        g1 = TextMobject(
            "$V(x+y)=V(x) + V(y)$")
        g2 = TextMobject(
            "$V(\\alpha x) = \\alpha V(x)$")
        g1.move_to(1 * UP)
        g2.move_to(1 * DOWN)
        g1.scale(2)
        g2.scale(2)
        g.scale(1.5)
        self.play(Write(g))
        self.play(ApplyMethod(g.shift, 3.5 * UP))
        self.play(Write(g1))
        self.play(Write(g2))
        self.wait(2)
