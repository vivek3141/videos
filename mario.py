from manim import *


class Sigmoid(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": 2.5 * DOWN,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2),

    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = \sigma (x)")
        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.wait(10)

    @staticmethod
    def func_to_graph(x):
        return 1 / (1 + np.exp(-x))


class SigmoidEq(Scene):
    def construct(self):
        text = TexMobject(r"\sigma (x) = \frac{1}{1 + e^{-x}}", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(4)
        self.play(Write(text))
        self.wait(10)
