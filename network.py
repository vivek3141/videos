from manim import *


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

    def __init__(self, neural_network, size, **kwargs):
        VGroup.__init__(self, **kwargs)
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

    def get_active_layer(self, layer_index, activation_vector):
        layer = self.layers[layer_index].deepcopy()
        self.activate_layer(layer, activation_vector)
        return layer

    def activate_layer(self, layer, activation_vector):
        n_neurons = len(layer.neurons)
        av = activation_vector

        def arr_to_num(arr):
            return (np.sum(arr > 0.1) / float(len(arr))) ** (1. / 3)

        if len(av) > n_neurons:
            if self.average_shown_activation_of_large_layer:
                indices = np.arange(n_neurons)
                indices *= int(len(av) / n_neurons)
                indices = list(indices)
                indices.append(len(av))
                av = np.array([
                    arr_to_num(av[i1:i2])
                    for i1, i2 in zip(indices[:-1], indices[1:])
                ])
            else:
                av = np.append(
                    av[:n_neurons / 2],
                    av[-n_neurons / 2:],
                )
        for activation, neuron in zip(av, layer.neurons):
            neuron.set_fill(
                color=self.neuron_fill_color,
                opacity=activation
            )
        return layer

    def activate_layers(self, input_vector):
        activations = self.neural_network.get_activation_of_all_layers(input_vector)
        for activation, layer in zip(activations, self.layers):
            self.activate_layer(layer, activation)

    def deactivate_layers(self):
        all_neurons = VGroup(*it.chain(*[
            layer.neurons
            for layer in self.layers
        ]))
        all_neurons.set_fill(opacity=0)
        return self

    def get_edge_propogation_animations(self, index):
        edge_group_copy = self.edge_groups[index].copy()
        edge_group_copy.set_stroke(
            self.edge_propogation_color,
            width=1.5 * self.edge_stroke_width
        )
        return [ShowCreationThenDestruction(
            edge_group_copy,
            run_time=self.edge_propogation_time,
            submobject_mode="lagged_start"
        )]

    def add_output_labels(self):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = TexMobject(str(n))
            label.set_height(0.75 * neuron.get_height())
            label.move_to(neuron)
            label.shift(neuron.get_width() * RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_input_labels(self):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = TexMobject(f"x_{n}")
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
