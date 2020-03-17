from manimlib.imports import *


class Grid(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.m = m
        self.n = n
        self.s_width = s_width
        for x in range(0, m + 1):
            self.add(Line(
                s_width * np.array([x - m/2, -n/2, 0]),
                s_width * np.array([x - m/2, n/2, 0]))
            )
        for y in range(0, n + 1):
            self.add(Line(
                s_length * np.array([-m/2, y - n/2, 0]),
                s_length * np.array([m/2, y - n/2, 0]))
            )


class Chessboard(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        for x in range(0, m, 2):
            for y in range(0, n):
                pos = s_width * \
                    np.array([x - m/2 + (1 if y % 2 == 0 else 0) + 0.5,
                              y - n/2 + 0.5,
                              0])
                rect = Rectangle(
                    width=s_length,
                    height=s_width,
                    fill_opacity=0.6,
                    color=WHITE)
                rect.shift(pos)
                self.add(rect)


class DominoGrid(Grid):
    def __init__(self, m, n, s_width=1, s_length=1, dt=0.5, perm=None, **kwargs):
        Grid.__init__(self, m, n, s_width=s_width, s_length=s_length, **kwargs)
        self.colors = [TEAL, MAROON, GREEN]
        self.dt = dt
        if perm is not None:
            for n, i in enumerate(perm):
                self.add(self.get_rect(
                    *sorted([2 * n if (n // (self.m/2)) % 2 == 0 else 2 * n + 1, i])))

    def get_perm(self, perm):
        rects = VGroup()
        for n, i in enumerate(perm):
            rects.add(self.get_rect(
                *sorted([2 * n if (n // (self.m/2)) % 2 == 0 else 2 * n + 1, i])))
        return rects

    def get_rect(self, pos1, pos2):
        if pos1 // self.m == pos2 // self.m:
            rect = Polygon(
                self.get_point(pos1) + np.array([-self.dt, self.dt, 0]),
                self.get_point(pos2) + np.array([self.dt, self.dt, 0]),
                self.get_point(pos2) - np.array([-self.dt, self.dt, 0]),
                self.get_point(pos1) - np.array([self.dt, self.dt, 0]),
                fill_opacity=1,
                stroke_color=WHITE,
                color=self.colors[pos1 % len(self.colors)]
            )
        else:
            rect = Polygon(
                self.get_point(pos1) + np.array([self.dt, self.dt, 0]),
                self.get_point(pos2) + np.array([self.dt, -self.dt, 0]),
                self.get_point(pos2) - np.array([self.dt, self.dt, 0]),
                self.get_point(pos1) - np.array([self.dt, -self.dt, 0]),
                fill_opacity=1,
                stroke_color=WHITE,
                color=self.colors[pos1 % len(self.colors)]
            )
        return rect

    def get_point(self, n):
        return self.s_width * np.array([n % self.m - self.s_width, self.s_width - n // self.n, 0])


class Tilings(Scene):
    def construct(self):
        grid = DominoGrid(4, 4, s_width=1.5, s_length=1.5)
        rects1 = grid.get_perm((4, 1, 9, 3, 12, 6, 14, 11))

        rects2 = grid.get_perm((0, 1, 6, 3, 4, 9, 12, 11))[1:]
        rects2.add(grid.get_rect(14, 15))
        rects2.add(grid.get_rect(0, 1).shift(1.5 * LEFT))

        rects3 = grid.get_perm((4, 1, 9, 3, 12, 6, 14, 11))
        rects4 = grid.get_perm((1, 3, 9, 11, 4, 6, 12, 14))
        rects5 = grid.get_perm((1, 3, 4, 6, 9, 11, 12, 14))

        m = TexMobject("M")
        m.shift(4 * LEFT)
        m.scale(1.5)

        n = TexMobject("N")
        n.shift(3.5 * DOWN)
        n.scale(1.5)

        cross = VGroup()
        cross.add(Line(3.5 * UP + 3.5 * RIGHT, 3.5 * DOWN +
                       3.5 * LEFT, color=RED, stroke_width=8))
        cross.add(Line(3.5 * UP + 3.5 * LEFT, 3.5 * DOWN +
                       3.5 * RIGHT, color=RED, stroke_width=8))

        self.play(ShowCreation(grid))
        self.play(FadeInFromDown(m), FadeInFromDown(n))
        self.wait()

        self.play(Write(rects1))
        self.wait()

        self.play(Transform(rects1, rects2))
        self.play(ShowCreation(cross))
        self.wait()

        self.play(Uncreate(cross))
        self.play(Transform(rects1, rects3))
        self.wait()

        self.play(Transform(rects1, rects4))
        self.wait()

        self.play(Transform(rects1, rects5))
        self.wait()

        group = VGroup(grid, rects1, m, n)
        self.play(group.shift, 2 * LEFT)

        eq = TexMobject(r"M \cdot N \text{ is even}", tex_to_color_map={
                        r"M \cdot N": BLUE})
        eq.scale(1.5)
        eq.shift(4 * RIGHT)

        self.play(Write(eq))
        self.wait()


class Recursion(Scene):
    def construct(self):
        title = TextMobject("Fibonacci Sequence", color=TEAL)
        title.scale(2)
        title.shift(3 * UP)

        n1 = TexMobject("1").scale(3)
        n2 = TexMobject("1").scale(3)

        n1.shift(3 * LEFT)
        n2.shift(0 * LEFT)

        grp = VGroup(n1, n2)

        n3 = TexMobject("2").scale(3)
        n3.shift(3 * RIGHT)

        self.play(Write(title))
        self.play(Write(grp))
        self.wait()

        self.play(TransformFromCopy(grp, n3))
        self.wait()

        grp.add(n3)

        self.play(Uncreate(n1))
        self.play(grp.shift, 3 * LEFT)

        n4 = TexMobject("3").scale(3)
        n4.shift(3 * RIGHT)

        self.play(TransformFromCopy(grp, n4))
        self.wait()

        grp.add(n4)

        self.play(Uncreate(n2))
        self.play(grp.shift, 3 * LEFT)

        n5 = TexMobject("5").scale(3)
        n5.shift(3 * RIGHT)

        self.play(TransformFromCopy(grp, n5))
        self.wait()

        grp.add(n5)

        self.play(Uncreate(grp))

        eq = TexMobject(r"F_n = F_{n-1} + F_{n-2}")
        eq.scale(2.5)

        self.play(FadeInFromDown(eq))
        self.wait()


class TwoByNExample(Scene):
    def construct(self):
        grid = DominoGrid(5, 2, s_width=1.5, s_length=1.5)
        rects = VGroup()
        for i in np.arange(-3, 3.1, 1.5):
            rect = Rectangle(
                width=1,
                height=2.5,
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            ).shift(i * RIGHT)
            rects.add(rect)

        self.play(ShowCreation(grid))
        self.wait()

        self.play(Write(rects))
        self.wait()


class Tmn(Scene):
    def construct(self):
        eq = TexMobject(r"T(m, n)", tex_to_color_map={r"m": RED, r"n": GREEN})
        eq.scale(2)
        eq.shift(3 * LEFT)

        arrow = Arrow(LEFT, RIGHT, color=TEAL)
        text = TextMobject(r"Number of ways \\ to tile M x N",
                           tex_to_color_map={r"M": RED, r" N": GREEN})
        text.scale(1.25)
        text.shift(3.5 * RIGHT)

        self.play(FadeInFromDown(eq))
        self.play(FadeInFromDown(arrow))
        self.play(FadeInFromDown(text))


class TwoByN(Scene):
    def construct(self):
        eq = TexMobject(r"T(2, n)", r"= T(2, n-1)", r"+ T(2, n-2)",
                        tex_to_color_map={r"-2": RED, r"-1": RED, r"n": GREEN})
        eq.scale(1.5)
        eq.shift(3 * UP)

        grid = DominoGrid(5, 2, s_width=1.5, s_length=1.5)
        rect = Rectangle(
            width=1,
            height=2.5,
            fill_opacity=1,
            stroke_color=WHITE,
            color=PURPLE
        ).shift(3 * RIGHT)

        rect2 = Rectangle(
            width=5.5,
            height=2.5,
            fill_opacity=1,
            stroke_color=WHITE,
            color=GRAY
        ).shift(0.75 * LEFT)

        self.play(FadeInFromDown(eq[:3]))
        self.play(Write(grid))
        self.wait()

        self.play(Write(rect))
        self.play(Write(rect2))
        self.wait()

        text1 = TexMobject("T(2, n-1)")
        text1.scale(1.5)
        text1.shift(0.75 * LEFT)

        self.play(FadeInFromDown(text1))
        self.play(FadeInFromDown(eq[3:7]))
        self.wait()

        rects = VGroup(
            Rectangle(
                width=2.5,
                height=1,
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            ).shift(2.25 * RIGHT + 0.75 * UP),
            Rectangle(
                width=2.5,
                height=1,
                fill_opacity=1,
                stroke_color=WHITE,
                color=PURPLE
            ).shift(2.25 * RIGHT - 0.75 * UP)
        )

        self.play(Uncreate(rect2), Uncreate(text1))
        self.play(Transform(rect, rects))

        rect3 = Rectangle(
            width=4,
            height=2.5,
            fill_opacity=1,
            stroke_color=WHITE,
            color=GRAY
        ).shift(1.5 * LEFT)

        text2 = TexMobject("T(2, n-2)")
        text2.scale(1.5)
        text2.shift(1.5 * LEFT)

        self.play(Write(rect3))
        self.play(FadeInFromDown(text2))
        self.play(FadeInFromDown(eq[7:]))
        self.wait()

        fib = TexMobject(
            r"T(2, n) = F_{n + 1}", tex_to_color_map={r"n": GREEN, r"F": TEAL})
        fib.scale(1.5)
        fib.shift(2.5 * DOWN)

        rect = BackgroundRectangle(
            fib, buff=MED_SMALL_BUFF, color=YELLOW, stroke_opacity=1, stroke_width=6, fill_opacity=0)

        self.play(FadeInFromDown(fib))
        self.play(Write(rect))
        self.wait()


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


class NewTopics(Scene):
    def construct(self):
        tree = TreeMobject((1, 2, 4))
        tree.rotate(PI/2, axis=IN)
        tree.shift(3 * LEFT + UP)

        g = TextMobject(r"Graph Theory")
        g.scale(1.25)
        g.shift(3 * LEFT + 2 * DOWN)

        l = TextMobject(r"Linear Algebra")
        l.scale(1.25)
        l.shift(3 * RIGHT + 2 * DOWN)

        matrix = TexMobject(
            r"\begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \end{bmatrix}")
        matrix.scale(1.5)
        matrix.shift(3 * RIGHT + UP)

        self.play(Write(tree), Write(matrix))
        self.play(FadeInFromDown(g), FadeInFromDown(l))
        self.wait()


class GridGraph(VGroup):
    def __init__(self, m, n, s_width=1, **kwargs):
        VGroup.__init__(self, **kwargs)

        self.m = m
        self.n = n
        self.s_width = s_width

        self.colors = [TEAL, MAROON, GREEN]
        self.bw = ["#FFE9B3", "#4E7C4C"]

        self.circles = VGroup()
        self.lines = VGroup()

        for i in range(m):
            self.lines.add(
                Line(self.get_point(m * i), self.get_point(m * i + n - 1))
            )

        for i in range(n):
            self.lines.add(
                Line(self.get_point(i), self.get_point(i + m * (n - 1)))
            )

        for i in range(0, m * n):
            self.circles.add(
                Circle(radius=0.15, color=self.colors[i % len(self.colors)], fill_opacity=1).shift(
                    self.get_point(i))
            )

        self.add(self.lines, self.circles)

    def get_point(self, n):
        return self.s_width * np.array([n % self.m - self.s_width, self.s_width - n // self.n, 0])

    def get_edge(self, pos1, pos2, color=RED):
        return Line(self.get_point(pos1), self.get_point(pos2), color=color, stroke_width=8)

    def get_perm(self, perm):
        edges = VGroup()
        for n, i in enumerate(perm):
            edges.add(self.get_edge(
                *sorted([2 * n if (n // (self.m/2)) % 2 == 0 else 2 * n + 1, i])))
        return edges

    def set_black_white(self):
        for i in range(self.m * self.n):
            c = self.bw[i % 2] if (
                i // self.m) % 2 == 0 else self.bw[(i + 1) % 2]
            self.circles[i].set_fill(color=c)
            self.circles[i].set_stroke(color=c)


class GridGraphIntro(Scene):
    def construct(self):
        g = GridGraph(4, 4, s_width=1.5)
        g2 = GridGraph(4, 4, s_width=1.5)
        g2.set_stroke(opacity=0.2)

        grid = Grid(4, 4, s_width=1.5, s_length=1.5)
        grid1 = Grid(4, 4, s_width=1.5, s_length=1.5)
        grid1.set_stroke(opacity=0.1)

        self.play(Write(grid))
        self.wait()

        self.play(Transform(grid, grid1))
        self.play(Write(g))
        self.wait()

        edges1 = g.get_perm((4, 1, 9, 3, 12, 6, 14, 11))
        edges2 = g.get_perm((1, 3, 9, 11, 4, 6, 12, 14))
        edges3 = g.get_perm((1, 3, 4, 6, 9, 11, 12, 14))

        self.play(Uncreate(grid))
        self.play(Transform(g, g2))
        self.play(Write(edges1))
        self.wait()

        self.play(Transform(edges1, edges2))
        self.wait()

        self.play(Transform(edges1, edges3))
        self.wait()


class PerfectBipartiteGraph(VGroup):
    def __init__(self, n=3, w=1.5, p=1.5, vertex_color=BLUE, line_color=WHITE, radius=0.3, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.n = n
        self.line_color = line_color

        self.vertices = [None for i in range(2 * n)]
        self.lines = VGroup()

        for i in range(n):
            self.vertices[i] = Circle(
                radius=radius,
                color=vertex_color,
                fill_opacity=1,
                fill_color=BLACK).shift(w * LEFT + i * p * DOWN)

            self.vertices[i + n] = Circle(
                radius=radius,
                color=vertex_color,
                fill_opacity=1,
                fill_color=BLACK).shift(w * RIGHT + i * p * DOWN)

        self.add(*self.vertices)
        self.center()

    def add_edge(self, v1, v2):
        self.add_to_back(
            Line(self.vertices[v1].get_center(),
                 self.vertices[v2].get_center())
        )

    def get_edge(self, v1, v2):
        return (
            Line(self.vertices[v1].get_center(),
                 self.vertices[v2].get_center())
        )

    def add_perm(self, perm):
        for n, i in enumerate(perm):
            for x in i:
                self.lines.add(self.get_edge(n, x + self.n))
        self.add_to_back(self.lines)


class BipartiteGraphs(Scene):
    def construct(self):
        b1 = PerfectBipartiteGraph()
        b1.add_perm([[0, 1, 2] for i in range(3)])

        b2 = PerfectBipartiteGraph()
        b2.add_perm([[1], [2], [0]])

        b1.shift(2.5 * LEFT)
        b2.shift(2.5 * RIGHT)

        title = TextMobject("Bipartite Graphs", color=GOLD)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.play(Write(b1), Write(b2))
        self.wait()


class GridGraphBipartite(Scene):
    def construct(self):
        g = GridGraph(4, 4, s_width=1.5)
        g2 = GridGraph(4, 4, s_width=1.5)
        g2.set_black_white()

        g3 = GridGraph(4, 4, s_width=1.5)
        g3.set_black_white()
        g3.lines.set_opacity(0.3)

        self.play(Write(g))
        self.wait()

        self.play(Transform(g, g2))
        self.wait()

        labels = VGroup()

        for i in range(8):
            w = TexMobject(fr"W_{i}")
            b = TexMobject(fr"B_{i}")
            if (i // (2)) % 2 == 0:
                wpos = 2 * i
                bpos = 2 * i + 1
            else:
                wpos = 2 * i + 1
                bpos = 2 * i

            w.move_to(g.circles[wpos], UP)
            b.move_to(g.circles[bpos], UP)
            labels.add(w, b)

        labels.shift(0.5 * UP)

        self.play(Transform(g, g3))
        self.play(FadeInFromDown(labels))
        self.wait()


class Matrix(VGroup):
    def __init__(self, vals, p=0.5, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.m = len(vals)
        self.n = len(vals[0])
        self.nums = VGroup()

        l1 = Line(ORIGIN, self.m * DOWN).shift(p * LEFT).shift(0.45 * UP)
        l2 = Line(0.45 * UP, 0.45 * UP + 0.22 * RIGHT).shift(p * LEFT)
        l3 = Line(0.45 * UP, 0.45 * UP + 0.22 *
                  RIGHT).shift(p * LEFT + (self.m) * DOWN)

        l4 = Line(ORIGIN,
                  self.m * DOWN).shift((self.m - 1) * RIGHT).shift(0.45 * UP + p * RIGHT)
        l5 = Line(0.45 * UP, 0.45 * UP + 0.22 *
                  LEFT).shift((self.m - 1 + p) * RIGHT)
        l6 = Line(0.45 * UP, 0.45 * UP + 0.22 *
                  LEFT).shift((self.m - 1 + p) * RIGHT + self.m * DOWN)

        lines = VGroup(l1, l2, l3, l4, l5, l6)

        for x in range(self.m):
            for y in range(self.n):
                t = TexMobject(str(vals[x][y])).shift(y * RIGHT + x * DOWN)
                self.nums.add(t)

        self.add(self.nums)
        self.add(lines)

        self.center()


class AdjacencyMatrix(Scene):
    def construct(self):
        vals = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        mat = Matrix(vals)

        graph = PerfectBipartiteGraph()
        graph.add_perm([[1], [2], [0]])

        self.add(mat)
