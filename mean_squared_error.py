from manim import *

V_COLOR = YELLOW
W_COLOR = MAROON_B
SUM_COLOR = PINK


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
        g = TextMobject("Estimator and Variance are Linear", color=GREEN)
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


class InnerProduct(Scene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "point_charge_loc": 0.5 * RIGHT - 1.5 * UP,
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        vector = Vector(1 * UP + 3 * RIGHT, color=RED)
        vector2 = Vector(2 * UP + 1 * RIGHT, color=BLUE)
        projected = Vector(1.73768398521 * RIGHT + 0.57922769775 * UP, color=GREEN)
        full_projected = Vector(4.73768398521 * RIGHT + 1.57922769775 * UP, color=BLUE)
        self.wait(0.25)
        self.play(ShowCreation(vector))
        self.play(ShowCreation(vector2))
        self.wait(2)
        self.play(Transform(vector2, projected))
        self.play(ApplyMethod(vector2.shift, 1 * UP, 3 * RIGHT))
        self.wait(2)
        self.play(Transform(vector2, full_projected), Transform(vector, full_projected))
        self.wait(3)


class InnerProperties(Scene):
    def construct(self):
        g = TextMobject("Inner Product = $<x, y>$", color=BLUE)
        g1 = TextMobject(
            "$<x, y> = \\overline{<y, x>}$").scale(1.5)
        g2 = TextMobject(
            "$<x+y, y> = <x, y> + <y, y>$").scale(1.5)
        g3 = TextMobject(
            "$<\\alpha x, y> = \\alpha<x,y>$").scale(1.5)
        g4 = TextMobject(
            "$<x, x> \\geq 0$").scale(1.5)
        g5 = TextMobject(
            "$<x, x> = 0 \\Longleftrightarrow x = 0$").scale(1.5)
        g1.move_to(2.5 * UP)
        g2.move_to(1.25 * UP + 1.5 * RIGHT)
        g3.move_to(1.5 * RIGHT)
        g4.move_to(1.25 * DOWN + 2 * RIGHT)
        g5.move_to(2.5 * DOWN + 2 * RIGHT)
        g.scale(1.5)
        b1 = Brace(VGroup(g2, g3), LEFT)
        b2 = Brace(VGroup(g4, g5), LEFT)
        t1 = b1.get_text("Linearity")
        t2 = b2.get_text("Positive-definiteness")
        self.play(Write(g))
        self.play(ApplyMethod(g.shift, 3.5 * UP))
        self.play(Write(g1))
        self.play(Write(b1), Write(g2), Write(g3), Write(t1))
        self.play(Write(b2), Write(g4), Write(g5), Write(t2))
        self.wait(2)


class Outro(Scene):
    def construct(self):
        text = TextMobject("Thanks for Watching").scale(2)
        text.move_to(3 * UP)
        self.play(Write(text))
        self.wait(10)
