from manimlib.imports import *


def coupon(N):
    return N * sum([1/i for i in range(1, N+1)])


class TreeMobject(VGroup):
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
            for i, n1 in enumerate(l1.neurons):
                n2 = l2.neurons[2*i]
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
                n2 = l2.neurons[2*i+1]
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

    def add_labels(self, layer, labels):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[layer].neurons):
            label = TexMobject(labels[n])
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_branch_labels(self, labels, move=(RIGHT, LEFT)):
        weight_group = VGroup()

        for n, i in enumerate(self.layers[1].neurons):
            edge = self.get_edge(i, self.layers[0].neurons[0])
            text = TextMobject(labels[n], color=RED)
            text.move_to(edge, move[n] * 2)
            weight_group.add(text)
        self.add(weight_group)


class Intro(Scene):
    def construct(self):
        cards = VGroup()
        m = [5, 2, -2, -5]
        for i in range(1, 5):
            cards.add(
                ImageMobject(
                    f"./img/card{i}.jpg"
                ).shift(m[i-1] * LEFT).scale(1.5)
            )
        cards.add(TexMobject("...").scale(2))
        cards.shift(1 * UP)

        for i in range(0, 4):
            self.play(FadeInFromDown(cards[i]), run_time=0.5)

        self.play(Write(cards[4]))
        l = Line(6.1 * LEFT, 6.1 * RIGHT).shift(0.75 * DOWN)

        b = Brace(l)
        lbl = b.get_tex("N").scale(1.5).shift(0.25 * DOWN).set_color(TEAL)
        brace = VGroup(b, lbl)
        cards.add(brace)

        self.play(Write(brace))
        self.wait()

        self.play(cards.shift, 1 * UP)

        q = TextMobject(r"How many draws to get all \( N \) cards?",
                        tex_to_color_map={r"\( N \)": TEAL})
        q.scale(1.5)
        q.shift(2.5 * DOWN)

        self.play(Write(q))
        self.wait()

        q2 = TextMobject(r"Expected value of number of draws to get all \( N \) cards",
                         tex_to_color_map={r"Expected value": GOLD, r"\( N \)": TEAL})
        q2.scale(1.1)
        q2.shift(2.5 * DOWN)

        self.play(Transform(q, q2))
        self.wait()


class ExpectedValue(Scene):
    def construct(self):
        title = TextMobject("Expected value", color=GOLD)
        title.scale(1.5)
        title.shift(3 * UP)

        title2 = TextMobject("Expected value", "= predicted outcome", tex_to_color_map={
                             "Expected value": GOLD})
        title2.scale(1.5)
        title2.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.wait()

        self.play(Transform(title, title2[0]))
        self.play(FadeInFromDown(title2[1]))
        self.wait()

        tree = TreeMobject([1, 2])
        tree.add_labels(1, [r"\text{H}", r"\text{T}"])
        tree.scale(3)
        tree.shift(4 * LEFT + 0 * DOWN)

        lbl1 = TexMobject(r"x_1 = + \$ 10", r"\cdot p_1 = 0.5", tex_to_color_map={
                          r"x_1": BLUE, r"+ \$ 10": GREEN, r"p_1": ORANGE, r"0.5": GREEN})
        lbl1.scale(1)
        lbl1.shift(1 * UP + 1 * RIGHT)

        lbl2 = TexMobject(r"x_2 = - \$ 5", r"\cdot p_2 = 0.5", tex_to_color_map={
                          r"x_2": BLUE, r"- \$ 5": GREEN, r"p_2": ORANGE, r"0.5": GREEN})
        lbl2.scale(1)
        lbl2.shift(1 * DOWN + 1 * RIGHT)

        self.play(Write(tree))
        self.wait()

        self.play(FadeInFromDown(lbl1))
        self.play(FadeInFromDown(lbl2))
        self.wait()

        ans1 = TextMobject(r"\( = 5 \)", alignment="").scale(1.5)
        ans2 = TextMobject(r"\( = -2.5 \)", alignment="").scale(1.5)

        ans1.shift(1 * UP + 4.4 * RIGHT)
        ans2.shift(1 * DOWN + 5 * RIGHT)

        self.play(Write(ans1))
        self.play(Write(ans2))
        self.wait()

        line = Line(3.5 * RIGHT, 6.5 * RIGHT)
        line.shift(2 * DOWN)

        self.play(Write(line))

        ans = TexMobject(r"E[{x}] = \sum x_i p_i = ", r"2.5", tex_to_color_map={
                         r"E": GOLD, r"{x}": BLUE, r"x_i": BLUE, r"p_i": ORANGE}).scale(1.5)
        ans.shift(3 * DOWN + 2.1 * RIGHT)

        self.play(Write(ans[-1]))

        brect = BackgroundRectangle(
            ans[-1], color=YELLOW, buff=0.2, fill_opacity=0, stroke_opacity=1, stroke_width=4)
        self.play(Write(brect))
        self.wait()

        self.play(FadeInFromDown(ans[:-1]))
        self.wait()


class Tails(Scene):
    def construct(self):
        eq1 = TexMobject(
            r"\left ( \frac{1}{2} \right )",
            r"\left ( \frac{1}{2} \right )",
            r"\left ( \frac{1}{2} \right )"
        ).scale(2)

        eq1[:2].set_color_by_gradient(RED, ORANGE)
        eq1[2].set_color(YELLOW, GOLD)

        b1 = Brace(eq1[:2])
        l1 = b1.get_tex(r"\text{tails}")
        brace1 = VGroup(b1, l1)

        b2 = Brace(eq1[-1])
        l2 = b2.get_tex(r"\text{heads}")
        brace2 = VGroup(b2, l2)

        self.play(Write(eq1))
        self.play(Write(brace1), Write(brace2))
        self.wait()

        ans = TexMobject(r"=  \frac{1}{8}")
        ans.scale(2)
        ans.shift(3.2 * RIGHT)

        self.play(
            ApplyMethod(eq1.shift, 1.3 * LEFT),
            ApplyMethod(brace1.shift, 1.3 * LEFT),
            ApplyMethod(brace2.shift, 1.3 * LEFT)
        )
        self.play(FadeInFromDown(ans))
        self.wait()


class Bernoulli(Scene):
    def construct(self):
        title = TextMobject("Bernoulli Trial", color=TEAL)
        title.scale(1.5)
        title.shift(3 * UP)

        b = BulletedList(
            "Trial is independent", "Trial has two outcomes", "Probability of success doesn't change",
            dot_scale_factor=5).scale(1.5)

        self.play(Write(title))
        self.play(Write(b))
        self.wait()

        for i in range(0, 3):
            self.play(b.fade_all_but, i)
            self.wait()

        self.play(b.reset)
        self.wait()

class RollingDice(VGroup):
    def __init__(self, *args, **kwargs):
        VGroup.__init__(*args, **kwargs)
        


class ExpectBern(Scene):
    def construct(self):
        d = RollingDice()
        self.add(d)
        d.roll()


class Asymptote(Scene):
    CONFIG = {
        "max_n": 77,
        "skip": 4,
        "x_min": -6,
        "x_max": 6,
        "buff": 0.4
    }

    def construct(self):
        rects = VGroup()
        width = (abs(self.x_min) + abs(self.x_max)) / (self.max_n / self.skip)

        for i in range(int(self.max_n/self.skip)):
            height = 0.1 * coupon(i)
            lbl = TexMobject(str(self.skip * i))
            rects.add(
                Rectangle(
                    width=width - self.buff,
                    height=0.1*coupon(i),
                    fill_opacity=1,
                ).shift([i * width + self.x_min, - 4 + height / 2, 0]
                        ).set_color_by_gradient(RED, BLUE)
            )
            rects.add(
                lbl.next_to(rects[-1], DOWN)
            )

        rects.shift(1 * UP)

        self.play(Write(rects))
        self.wait()
