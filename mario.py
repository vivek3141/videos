from manimlib.imports import *
from scipy.optimize import curve_fit


def yx2features(ran=[0, 5], number=100):

    def func(): return ((max(ran) - min(ran) + 1) * np.random.random(number)) + min(ran)
    x1 = np.array(func)
    x2 = np.array(list(map(lambda z: int(z), func())))
    y = np.array([1 if x1[i] > x2[i] else 0 for i in range(number)])
    data = [[x1[i], x2[i]] for i in range(number)]

    return data, y


class NeuralNetworkMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.15,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": LARGE_BUFF,
        "neuron_stroke_color": BLUE,
        "neuron_stroke_width": 3,
        "neuron_fill_color": GREEN,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "edge_propogation_color": YELLOW,
        "edge_propogation_time": 1,
        "max_shown_neurons": 16,
        "brace_for_large_layers": True,
        "average_shown_activation_of_large_layer": True,
        "include_output_labels": False,
    }

    def __init__(self, neural_network, size=0.15):
        VGroup.__init__(self)
        self.layer_sizes = neural_network
        self.neuron_radius = size
        self.add_neurons()
        self.add_edges()

    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size)
            for size in self.layer_sizes
        ])
        layers.arrange_submobjects(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers
        self.add(self.layers)
        if self.include_output_labels:
            self.add_output_labels()

    def get_layer(self, size):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons
        neurons = VGroup(*[
            Circle(
                radius=self.neuron_radius,
                stroke_color=self.neuron_stroke_color,
                stroke_width=self.neuron_stroke_width,
                fill_color=self.neuron_fill_color,
                fill_opacity=0,
            )
            for x in range(n_neurons)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=self.neuron_to_neuron_buff
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = TexMobject("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, neuron1, neuron2):
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.neuron_radius,
            stroke_color=self.edge_color,
            stroke_width=self.edge_stroke_width,
        )

    def add_input_labels(self):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = TexMobject(f"x_{n + 1}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_y(self):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = TexMobject(r"\hat{y}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_weight_labels(self):
        weight_group = VGroup()

        for n, i in enumerate(self.layers[0].neurons):
            edge = self.get_edge(i, self.layers[-1][0])
            text = TexMobject(f"b_{n + 1}", color=RED)
            text.move_to(edge)
            weight_group.add(text)
        self.add(weight_group)


class LinReg(Scene):
    def construct(self):
        xdata = np.linspace(0.25, 5.75, 15)
        ydata = [self.func(i) + 2 * (np.random.random() - 0.5) for i in xdata]

        def f(x, a, b):
            return a * x + b

        theta, _ = curve_fit(f, xdata, ydata)

        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        points = VGroup(
            *[Dot(
                [xdata[i], ydata[i], 0],
                color=BLUE,
                radius=0.75 * DEFAULT_DOT_RADIUS
            ) for i in range(15)]
        )

        line = FunctionGraph(lambda x: f(x, *theta),
                             x_min=0, x_max=6, color=RED)
        dlines = VGroup(
            DashedLine(2.9 * RIGHT, f(2.9, *theta) * UP + 2.9 * RIGHT),
            DashedLine(f(2.9, *theta) * UP, f(2.9, *theta) * UP + 2.9 * RIGHT)
        )

        grp1 = VGroup(axes, points, line)
        grp = VGroup(grp1, dlines)
        grp.center()

        self.play(Write(axes))
        self.play(Write(points), Write(line))
        self.wait()

        xlbl = TextMobject("Plot Size (ft\(^2\))")
        xlbl.shift(3 * DOWN)

        ylbl = TextMobject(r"Market Price (\$)")
        ylbl.rotate(PI/2)
        ylbl.shift(4 * LEFT + 0.5 * UP)

        self.play(grp1.shift, 0.5 * UP)
        dlines.shift(0.5 * UP)
        self.play(FadeInFromDown(xlbl), FadeInFromDown(ylbl))

        lbl = TexMobject(
            f"\\hat{{ \\text{{price}}}} = {round(theta[0], 2)} + {round(theta[1], 2)} \\ \\text{{size}}", color=RED)
        lbl.shift(5 * RIGHT + 2 * UP)
        lbl.scale(0.75)

        ypoint = Dot([0, 0.32, 0], color=YELLOW, radius=0.08)

        self.play(points.set_opacity, 0.5)
        self.play(Write(lbl), Write(dlines), Write(ypoint))
        self.wait()

    @staticmethod
    def func(x):
        return 0.425 * x + 0.785


class LogReg(Scene):
    def construct(self):
        n = 100
        points = []
        colors = []
        c1 = "#99EDCC"
        c2 = "#B85C8C"

        for _ in range(n):
            point = np.random.random(2) * 5.5 + 0.25
            points.append(point)
            colors.append(1 if point[0] > point[1] else 0)

        pointg = VGroup(
            *[Dot([points[i][0], points[i][1], 0], color=c1 if colors[i] else c2) for i in range(len(colors))]
        )
        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=6,
            axis_config={
                "include_tip": False
            }
        )
        line = FunctionGraph(lambda x: x, x_min=0, x_max=6)
        grp = VGroup(axes, pointg, line)
        grp.center()

        self.play(Write(axes))
        self.play(Write(pointg))
        self.wait()

        self.play(ApplyMethod(pointg.set_opacity, 0.5), Write(line))
        self.wait()

        self.play(grp.shift, 3 * LEFT)
        eq1 = TexMobject(r"\hat{y} = ", r"\sigma ( ", r"b_0 + b_1 x ", r")",
                         tex_to_color_map={r"x": GREEN, "y": GOLD, r"\sigma": YELLOW})
        eq1.scale(1.5)
        eq1.shift(3.5 * RIGHT)

        self.play(Write(VGroup(eq1[:3], eq1[5:7])))
        self.wait()

        self.play(FadeInFromDown(VGroup(eq1[3:5], eq1[7])))
        self.wait()

        eq2 = TexMobject(
            r"\sigma ( x ) = \frac{1}{1 + e^{-x}}", tex_to_color_map={r"\sigma": YELLOW})
        eq2.scale(1.5)
        eq2.shift(2.75 * UP)

        self.play(Uncreate(grp))
        self.play(TransformFromCopy(eq1[3], eq2[0]))
        self.play(Write(eq2[1:]))
        self.play(Uncreate(VGroup(eq1)))
        self.wait()

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2,
            axis_config={
                "include_tip": False
            }
        )
        eq = FunctionGraph(lambda x: 2/(1+np.exp(-2*x)),
                           x_min=-3, x_max=3, color=GOLD)
        grp2 = VGroup(axes, eq)
        grp2.scale(2)
        grp2.center()
        grp2.shift(DOWN)

        lbls = VGroup(
            TexMobject("0.5").shift(DOWN),
            TexMobject("1.0").shift(UP)).shift(0.75 * LEFT + 0.2 * UP)

        self.play(Write(grp2))
        self.wait()

        self.play(Write(lbls))
        self.wait()


class LayerToLayer(Scene):
    def construct(self):
        nn = NeuralNetworkMobject([5, 1], 0.2)
        nn.scale(2)
        nn.add_input_labels()
        nn.add_y()
        nn.add_weight_labels()
        nn.shift(0.75 * UP)

        eq = TexMobject(
            r"y = \sigma (b_0 + b_1x_1 + b_2x_2 + b_3x_3 + b_4x_4)")
        eq.scale(1.5)
        eq.shift(3 * DOWN)

        self.play(Write(nn))
        self.play(Write(eq))
        self.wait(2)


class NeuralNetwork(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3], 0.15)
        network.scale(2.5)

        neuron_arrow = Arrow(ORIGIN, 1 * UP)
        neuron_arrow.next_to(network, 1 * UP)

        neuron_text = TextMobject("Each of these circles is a model")
        neuron_text.next_to(neuron_arrow, 1 * UP)

        self.play(Write(network))
        self.play(Write(neuron_arrow), Write(neuron_text))
        self.wait()


class NeuroEvolution(Scene):
    def construct(self):
        n = 3
        m = 1

        shift = [
            m * UP + n * LEFT,
            m * UP,
            m * UP + n * RIGHT,
            m * DOWN + n * LEFT,
            m * DOWN,
            m * DOWN + n * RIGHT
        ]
        scores = [
            "312",
            "434",
            "145",
            "254",
            "332",
            "521"
        ]
        scores2 = [
            "624",
            "512",
            "765",
            "432",
            "332",
            "521"
        ]

        head = TextMobject("Neuroevolution", color=RED)
        head.scale(2)
        head2 = TextMobject("Neuroevolution", color=RED)
        head2.scale(2)
        head2.shift(3 * UP)

        rep = TextMobject("This process is repeated", color=BLUE)
        rep.scale(2)

        one = TextMobject("1994", color=RED)
        one.scale(2)

        survival = TextMobject("Survival of the fittest")
        survival.scale(1.5)
        survival.shift(2 * DOWN)

        net_group = VGroup()
        text_group = VGroup()
        text_group2 = VGroup()

        circle1 = Circle(color=GREEN)
        circle1.shift(shift[5])

        circle2 = Circle(color=GREEN)
        circle2.shift(shift[1])

        circle3 = Circle(color=GREEN)
        circle3.shift(shift[0])

        circle4 = Circle(color=GREEN)
        circle4.shift(shift[2])

        for i in range(6):
            net = NeuralNetworkMobject([2, 3, 2])
            net.shift(shift[i])
            net_group.add(net)

            text = TextMobject(scores[i])
            text.shift(shift[i])
            text.scale(1.5)
            text_group.add(text)

            text2 = TextMobject(scores2[i])
            text2.shift(shift[i])
            text2.scale(1.5)
            text_group2.add(text2)

        self.play(Write(one))
        self.play(Transform(one, head))
        self.play(Write(survival))
        self.wait(0.25)

        self.play(ApplyMethod(one.shift, 3 * UP), Transform(survival, head2))
        self.play(Write(net_group))
        self.wait(0.25)

        self.play(Write(text_group))
        self.wait(0.25)

        self.play(Write(circle1), Write(circle2))
        self.wait(0.25)

        self.play(Transform(circle1, net_group),
                  Uncreate(circle2),
                  Uncreate(text_group),
                  Uncreate(net_group))
        self.wait(0.25)

        self.play(Write(text_group2))
        self.play(Write(circle3), Write(circle4))

        self.wait(0.25)

        self.play(Uncreate(circle1),
                  Uncreate(text_group2),
                  Uncreate(circle3),
                  Uncreate(circle4),
                  Write(rep)
                  )
        self.wait(0.25)
