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
            Write(rect)
        )
        self.wait(2)


class InputANN(Scene):
    def construct(self):
        mario = SVGMobject("files/mario.svg")
        a = Arrow(LEFT, RIGHT, color=RED)

        nn = SVGMobject("files/nn.svg")
        nn.move_to(2.5 * RIGHT)

        head = TextMobject("Artificial Neural Network", color=BLUE)
        head.move_to(2 * UP)
        head.scale(1.5)

        foot = TextMobject("Recommender System", color=RED)
        foot.move_to(2 * DOWN)
        foot.scale(1.5)

        self.play(Write(mario))
        self.play(ApplyMethod(mario.shift, 2.5 * LEFT), Write(a))
        self.play(Write(nn))
        self.wait(2)

        self.play(Write(head))
        self.wait(2)

        self.play(Write(foot))
        self.wait(2)


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
            label = TexMobject("y")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_weight_labels(self):
        weight_group = VGroup()

        for n, i in enumerate(self.layers[0].neurons):
            edge = self.get_edge(i, self.layers[-1][0])
            text = TexMobject(f"w_{n + 1}", color=RED)
            text.move_to(edge)
            weight_group.add(text)
        self.add(weight_group)


class NeuralNetwork(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3], 0.15)
        network.scale(2.5)

        neuron_arrow = Arrow(ORIGIN, 1 * UP)
        neuron_arrow.next_to(network, 1 * UP)

        neuron_text = TextMobject("Neurons")
        neuron_text.next_to(neuron_arrow, 1 * UP)

        input_arrow = Arrow(1 * LEFT, ORIGIN, color=BLUE)
        input_arrow.next_to(network, 2 * LEFT)

        input_text = TextMobject("Inputs", color=BLUE)
        input_text.next_to(input_arrow, 1 * UP)

        output_arrow = Arrow(ORIGIN, 1 * RIGHT, color=RED)
        output_arrow.next_to(network, 2 * RIGHT)

        output_text = TextMobject("Outputs", color=RED)
        output_text.next_to(output_arrow, 1 * UP)

        weight_arrow = Arrow(2 * LEFT, 2 * LEFT + 2 * DOWN)

        weight_text = TextMobject("Weights")
        weight_text.next_to(weight_arrow, 1 * DOWN)

        brace = Brace(VGroup(network), DOWN)
        text = brace.get_text("Bias")

        self.play(Write(network))
        self.wait(2)

        self.play(Write(neuron_arrow), Write(neuron_text))
        self.wait(2)

        self.play(Write(input_arrow), Write(input_text))
        self.wait(2)

        self.play(Write(output_arrow), Write(output_text))
        self.wait(2)

        self.play(Write(weight_arrow), Write(weight_text))
        self.wait(2)

        self.play(Write(brace), Write(text))
        self.wait(2)


class Sigmoid(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": 3 * DOWN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Sigmoid")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.sigmoid, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"\sigma (x) = max(x, \alpha x)", color=WHITE)
        graph_lab.scale(0.75)

        brace = Brace(VGroup(func_graph), LEFT)
        b_text = brace.get_tex(r"0 < \sigma (x) < 1")

        self.play(Write(func_graph))
        self.play(Write(graph_lab))
        self.play(Write(text))

        self.play(Write(brace), Write(b_text))
        self.wait(2)

    def sigmoid(self, x):
        return 1 / (1 + math.e ** (-x))


class Relu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": GREEN,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(Write(func_graph))
        self.play(Write(graph_lab))
        self.play(Write(text))
        self.wait(2)

    @staticmethod
    def relu(x):
        return max(x, 0)


class LeakyRelu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Leaky ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.leaky_relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(Write(func_graph))
        self.play(Write(graph_lab))
        self.play(Write(text))
        self.wait(2)

    @staticmethod
    def leaky_relu(x):
        return max(x, x / 4)


class SoftMax(GraphScene):
    def construct(self):
        equation = TexMobject(r"\sigma (x_j) = \frac{e^{x_j}}{\sum _i {e^{x_i}}")
        head = TextMobject("Softmax", color=GREEN)

        equation.scale(2)
        head.scale(2)
        head.move_to(2 * UP)

        self.play(Write(head))
        self.play(Write(equation))
        self.wait(2)


class LayerToLayer(Scene):
    def construct(self):
        nn = NeuralNetworkMobject([5, 1], 0.2)
        nn.scale(2)
        nn.add_input_labels()
        nn.add_y()
        nn.add_weight_labels()
        nn.shift(0.75 * UP)

        eq = TexMobject(r"y = \sigma (w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4)")
        eq.scale(1.5)
        eq.shift(3 * DOWN)

        self.play(Write(nn))
        self.play(Write(eq))
        self.wait(2)


class BackProp(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3])
        network.scale(2)

        back = Arrow(2.5 * UP + 1 * RIGHT, 2.5 * UP + 1 * LEFT, color=RED)
        text = TextMobject("Backpropagation")
        text.shift(3 * UP)

        self.play(Write(network))
        self.play(Write(back), Write(text))
        self.wait(2)


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
        self.wait(2)

        self.play(ApplyMethod(one.shift, 3 * UP), Transform(survival, head2))
        self.play(Write(net_group))
        self.wait(2)

        self.play(Write(text_group))
        self.wait(2)

        self.play(Write(circle1), Write(circle2))
        self.wait(2)

        self.play(Transform(circle1, net_group),
                  Uncreate(circle2),
                  Uncreate(text_group),
                  Uncreate(net_group))
        self.wait(2)

        self.play(Write(text_group2))
        self.play(Write(circle3), Write(circle4))

        self.wait(2)

        self.play(Uncreate(circle1),
                  Uncreate(text_group2),
                  Uncreate(circle3),
                  Uncreate(circle4),
                  Write(rep)
                  )
        self.wait(2)


class TWEANN(Scene):
    def construct(self):
        network1 = NeuralNetworkMobject([3, 4, 3])
        network2 = NeuralNetworkMobject([2, 3, 3])
        network3 = NeuralNetworkMobject([4, 2, 3])
        network4 = NeuralNetworkMobject([3, 2, 3])

        f = 2
        network1.scale(f)
        network2.scale(f)
        network3.scale(f)
        network4.scale(f)

        sub = TextMobject("Topology and Weight Evolving Artificial Neural Networks")
        head = TextMobject("TWEANNs", color=BLUE)
        head.scale(1.5)

        head.shift(3.5 * UP)
        sub.shift(2.5 * UP)

        sub2 = TextMobject("Neuroevolution of Augmenting Topologies")
        head2 = TextMobject("NEAT", color=RED)
        head2.scale(1.5)

        head2.shift(3.5 * UP)
        sub2.shift(2.5 * UP)

        self.play(Write(head), Write(sub))
        self.play(Write(network1))
        self.wait()

        self.play(Transform(network1, network2))
        self.wait()

        self.play(Transform(network1, network3))
        self.wait()

        self.play(Transform(network1, network4))
        self.wait()

        self.play(Transform(sub, sub2), Transform(head, head2))
        self.wait(2)


class Commentary(Scene):
    def construct(self):
        head = TextMobject("Commentary")
        head.scale(2)

        node1 = TextMobject("Thanking")
        node1.scale(1.5)
        node1.shift(3 * LEFT + 2 * DOWN)

        node2 = TextMobject("Actual Commentary")
        node2.scale(1.5)
        node2.shift(3 * RIGHT + 2 * DOWN)

        l1 = Line(1 * UP, ORIGIN, color=GREEN)
        l2 = Line(3 * RIGHT, 3 * LEFT, color=GREEN)
        l3 = Line(3 * RIGHT, 3 * RIGHT + 1 * DOWN, color=GREEN)
        l4 = Line(3 * LEFT, 3 * LEFT + 1 * DOWN, color=GREEN)

        self.play(Write(head))
        self.wait(2)
        self.play(ApplyMethod(head.shift, 2 * UP))
        self.play(Write(l1), Write(l2))
        self.play(Write(l3), Write(l4))
        self.play(Write(node1), Write(node2))
        self.wait(2)


class StreamLabs(Scene):
    def construct(self):
        streamlabs = SVGMobject("files/streamlabs.svg", color=BLUE)
        api = TextMobject("API", color=BLUE)

        streamlabs.shift(2 * LEFT)
        api.shift(2 * RIGHT)
        api.scale(2)
        streamlabs.scale(2)

        self.play(Write(streamlabs), Write(api))
        self.wait(2)


class API(Scene):
    def construct(self):
        api = TextMobject("API", color=RED)
        full = TextMobject("Application Programming Interface", color=RED)

        api.scale(2)
        full.scale(1.5)

        server = SVGMobject("files/server.svg")
        monitor = SVGMobject("files/monitor.svg")

        server.shift(3.5 * RIGHT)
        monitor.shift(3.5 * LEFT)

        arrow = Arrow(2.5 * LEFT, 2.5 * RIGHT, color=BLUE)

        mes = TextMobject("API", color=GREEN)
        mes.scale(1.25)
        mes.shift(1.5 * LEFT + 0.5 * UP)

        self.play(Write(api))
        self.play(Transform(api, full))
        self.play(ApplyMethod(api.shift, 3 * UP))

        self.wait(2)

        self.play(Write(monitor), Write(server), Write(arrow))
        self.play(Write(mes))

        self.play(ApplyMethod(mes.shift, 3 * RIGHT))
        self.play(ApplyMethod(mes.shift, 3 * LEFT))

        self.play(ApplyMethod(mes.shift, 3 * RIGHT))
        self.play(ApplyMethod(mes.shift, 3 * LEFT))

        self.wait(2)


class SocketAPI(Scene):
    def construct(self):
        head = TextMobject("Socket API", color=ORANGE)
        head.scale(2)
        head.shift(1 * UP)

        foot = TextMobject("Collection of Socket Commands", color=YELLOW)
        foot.scale(1.25)
        foot.shift(1 * DOWN)

        socket = TextMobject("Once a client accepts the connection, a socket is created")
        socket.shift(3 * DOWN)

        desc = TextMobject("The client gets pinged every time an event occurs")
        desc.shift(3 * UP)

        brace = Brace(foot, UP)

        client = SVGMobject("files/monitor.svg")
        server = SVGMobject("files/server.svg")

        server.shift(3.5 * RIGHT)
        client.shift(3.5 * LEFT)

        arrow1 = Arrow(2.5 * LEFT + 0.5 * UP, 2.5 * RIGHT + 0.5 * UP, color=BLUE)
        arrow2 = Arrow(2.5 * RIGHT + 0.5 * DOWN, 2.5 * LEFT + 0.5 * DOWN, color=BLUE)

        self.play(Write(head))
        self.play(Write(foot), Write(brace))

        self.wait(2)

        self.play(Uncreate(head), Uncreate(foot), Uncreate(brace))

        self.play(Write(client), Write(server))
        self.play(Write(arrow1), Write(arrow2))
        self.play(Write(socket))

        self.wait(2)

        self.play(Write(desc))
        self.wait(2)


class GTTS(Scene):
    def construct(self):
        google = SVGMobject("files/search.svg", color=ORANGE)
        google.shift(3 * LEFT)

        gtts = TextMobject("Text to speech")
        gtts.scale(1.5)
        gtts.shift(1 * RIGHT)

        tmp = TextMobject("/tmp = RAM", tex_to_color_map={"/tmp": YELLOW, "RAM": RED})
        tmp.scale(1.5)
        tmp.shift(2 * DOWN)

        self.play(Write(google), Write(gtts))
        self.play(Write(tmp))
        self.wait(2)


class CGame(Scene):
    def construct(self):
        opt = BulletedList("Markov Chains", "Recurrent Neural Networks", "Choosing from list")
        opt.scale(2)

        self.play(Write(opt))
        for i in range(3):
            self.play(opt.fade_all_but, i)
            self.wait(2)
        self.play(opt.reset)
        self.wait(2)


# Title class to reuse
class TitleScene(Scene):
    CONFIG = {
        "title": "test",
        "color": RED,
    }

    def construct(self):
        title = TextMobject(self.title, color=self.color)
        title.scale(2)

        self.play(Write(title))
        self.wait(2)


class ANNTitle(TitleScene):
    CONFIG = {
        "title": "Artificial Neural Network",
        "color": RED,
    }


class LayerTitle(TitleScene):
    CONFIG = {
        "title": "Going from Layer to Layer",
        "color": ORANGE,
    }


class TrainingTitle(TitleScene):
    CONFIG = {
        "title": "Training a Network",
        "color": YELLOW,
    }


class OtherTitle(TitleScene):
    CONFIG = {
        "title": "Other Ways of Learning",
        "color": GREEN,
    }


class SocketTitle(TitleScene):
    CONFIG = {
        "title": "Socket APIs",
        "color": BLUE,
    }


class GitHub(Scene):
    def construct(self):
        logo = SVGMobject("files/github-logo.svg")
        logo.shift(1 * LEFT)

        star = SVGMobject("files/star.svg")
        star.shift(1 * RIGHT)

        source = TextMobject("Source Code")
        source.shift(2 * DOWN + 2 * LEFT)

        arrow = Arrow(2 * DOWN + 2 * RIGHT, 3 * DOWN + 2 * RIGHT)

        self.play(Write(source), Write(arrow))
        self.play(Write(logo), Write(star))
        self.wait(2)
