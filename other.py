from manimlib.imports import *


class LinEQ(Scene):
    def construct(self):
        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )
        f = FunctionGraph(lambda x: 0.5*x + 1, x_min=-3, x_max=3)
        func = VGroup(axes, f)

        self.play(Write(func))


class Intro(Scene):
    def construct(self):
        logo = SVGMobject("files/logo_t.svg")
        self.play(Write(logo))
        self.wait()


class ElectricField(ThreeDScene):

    def construct(self):
        OPACITY = 0.1
        line0 = Line(3 * DOWN + 0.5 * LEFT, 2 *
                     DOWN + 0.5 * LEFT, stroke_width=8)
        line1 = Line(2 * DOWN + 0.5 * LEFT, 2 *
                     DOWN + 2 * LEFT, stroke_width=8)
        line3 = Line(2 * UP + 2 * LEFT, 2 * UP + 2 * RIGHT, stroke_width=8)
        line4 = Line(2 * UP + 2 * RIGHT, 2 * DOWN + 2 * RIGHT, stroke_width=8)
        line2 = Line(2 * DOWN + 2 * LEFT, 2 * UP + 2 * LEFT, stroke_width=8)
        line5 = Line(2 * DOWN + 2 * RIGHT, 2 * DOWN +
                     0.5 * RIGHT, stroke_width=8)
        line6 = Line(2 * DOWN + 0.5 * RIGHT, 3 *
                     DOWN + 0.5 * RIGHT, stroke_width=8)

        line02 = Line(3 * DOWN + 0.5 * LEFT, 2 *
                      DOWN + 0.5 * LEFT, stroke_width=8)
        line12 = Line(2 * DOWN + 0.5 * LEFT, 2 *
                      DOWN + 2 * LEFT, stroke_width=8)
        line32 = Line(2 * UP + 2 * LEFT, 2 * UP + 2 * RIGHT, stroke_width=8)
        line42 = Line(2 * UP + 2 * RIGHT, 2 * DOWN + 2 * RIGHT, stroke_width=8)
        line22 = Line(2 * DOWN + 2 * LEFT, 2 * UP + 2 * LEFT, stroke_width=8)
        line52 = Line(2 * DOWN + 2 * RIGHT, 2 * DOWN +
                      0.5 * RIGHT, stroke_width=8)
        line62 = Line(2 * DOWN + 0.5 * RIGHT, 3 *
                      DOWN + 0.5 * RIGHT, stroke_width=8)

        line00 = Line(3 * DOWN + 0.5 * LEFT, 2 * DOWN +
                      0.5 * LEFT, stroke_opacity=OPACITY)
        line10 = Line(2 * DOWN + 0.5 * LEFT, 2 * DOWN +
                      2 * LEFT, stroke_opacity=OPACITY)
        line30 = Line(2 * UP + 2 * LEFT, 2 * UP + 2 *
                      RIGHT, stroke_opacity=OPACITY)
        line40 = Line(2 * UP + 2 * RIGHT, 2 * DOWN +
                      2 * RIGHT, stroke_opacity=OPACITY)
        line20 = Line(2 * DOWN + 2 * LEFT, 2 * UP +
                      2 * LEFT, stroke_opacity=OPACITY)
        line50 = Line(2 * DOWN + 2 * RIGHT, 2 * DOWN +
                      0.5 * RIGHT, stroke_opacity=OPACITY)
        line60 = Line(2 * DOWN + 0.5 * RIGHT, 3 * DOWN +
                      0.5 * RIGHT, stroke_opacity=OPACITY)

        arrow = Arrow(ORIGIN, 1 * UP, color=RED)
        arrow.move_to(line2, 1 * LEFT)

        circle = Circle()
        circle.rotate(np.pi / 4, axis=X_AXIS)
        circle.shift(2 * LEFT)

        head = TextMobject("Isolate segment 1", color=BLUE)
        head.scale(1.25)
        head.shift(3 * UP)

        head3 = TextMobject("Do the same for every other segment", color=BLUE)
        head3.scale(1.25)
        head3.shift(3 * UP)

        head2 = TextMobject("Find the direction of magnetic field at A, B, C, D\\\\only using this current",
                            color=GREEN)
        head2.scale(1.25)
        head2.shift(3 * DOWN)

        self.play(Write(line0))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.play(Write(line6))

        self.wait()

        self.play(Write(arrow))
        self.play(Write(circle))

        self.wait()

        self.play(Write(head))

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line60),
        )

        self.wait()
        self.play(Write(head2))

        self.wait()

        self.play(Transform(head, head3))
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line32),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line60),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line42),
            Transform(line5, line50),
            Transform(line6, line60),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line52),
            Transform(line6, line60),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line62),
        )
        self.wait()


class Test(Scene):
    def construct(self):
        sin1 = ParametricFunction(lambda t: np.array(
            [t, np.sin(t), 0]), t_min=0, t_max=6 * PI, color=GREEN)
        sin1.shift(7 * LEFT)

        sin2 = ParametricFunction(lambda t: np.array(
            [t, -np.sin(t), 0]), t_min=0, t_max=6 * PI, color=GREEN)
        sin2.shift(7 * LEFT)

        sin11 = ParametricFunction(lambda t: np.array(
            [t, np.sin(t), 0]), t_min=0, t_max=6 * PI, color=GREEN)
        sin11.shift(7 * LEFT)

        self.play(Write(sin1))
        for i in range(5):
            self.play(Transform(sin1, sin2))
            self.play(Transform(sin1, sin11))


class BannerE(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):

        axes_config = {"x_min": -5,
                       "x_max": 5,
                       "y_min": -5,
                       "y_max": 5,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = Axes(**axes_config)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, lambda x, y: np.array([y, x]), prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )

        field = VGroup(axes, f)

        c = ParametricFunction(
            self.func,
            t_min=-3,
            t_max=3,
        )
        c.set_stroke(opacity=0.75)
        label = TextMobject("C")
        label.shift(2 * LEFT)
        label.scale(2)

        curve = VGroup(label, c)

        everything = VGroup(field, curve)
        everything.scale(0.7)

        text = TextMobject("Multivariable Calculus")
        text.scale(2.5)
        rect = BackgroundRectangle(
            text, buff=MED_LARGE_BUFF, color=BLACK, fill_opacity=1, stroke_opacity=1)
        t = VGroup(rect, text)

        self.play(Write(everything), Write(t))
        self.wait()

    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y = point[:2]
        func = f(x, y)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0])
        func = func / 1.5
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
        return v

    @staticmethod
    def func(t):
        return np.array([
            2 * np.arctan(t),
            t,
            0
        ])

    def f_r(self, t):
        r = self.func(t)
        return np.array([
            r[1],
            r[0],
            0
        ])

    @staticmethod
    def line_evaluated(x):
        r_derivative = np.array([2 / (1 + x ** 2), 1])
        f_r = np.array([x, 2 * np.arctan(x)])

        return np.array([
            x,
            0.25 * np.dot(f_r, r_derivative),
            0
        ])

    @staticmethod
    def r_prime(x):
        r_d = np.array([2 / (1 + x ** 2), 1, 0])
        return r_d


class FTC(GraphScene):
    CONFIG = {
        "x_max": 4,
        "x_labeled_nums": list(range(-1, 5)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 2.5,
        "y_labeled_nums": list(range(5, 20, 5)),
        "n_rect_iterations": 1,
        "default_right_x": 3,
        "func": lambda x: 0.1*math.pow(x-2, 2) + 1,
    }

    def construct(self):
        ftc = TexMobject(r"\int_a^b f'(x) \ dx = f(b) - f(a)")
        ftc.shift(3 * UP)

        self.play(Write(ftc))
        self.setup_axes()
        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))

        self.graph = graph
        dx = 0.2
        rect = self.get_riemann_rectangles(
            self.graph,
            x_min=0,
            x_max=self.default_right_x,
            dx=dx,
            stroke_width=4*dx,
        )
        foreground_mobjects = [self.axes, self.graph]

        self.play(
            DrawBorderThenFill(
                rect,
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
            *list(map(Animation, foreground_mobjects))
        )

        self.wait()


class TypeT(Scene):
    def construct(self):
        text1 = TextMobject("Animated").scale(3).shift(0.75 * UP)
        text2 = TextMobject(r"Math and CS").scale(1.5).shift(0.75 * DOWN)

        self.play(Write(text1), Write(text2))


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
        text = TexMobject(
            r"\sigma (x) = \frac{1}{1 + e^{-x}}", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(4)
        self.play(Write(text))
        self.wait(10)


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
        text = TexMobject(
            r"\sigma (x) = \frac{1}{1 + e^{-x}}", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(4)
        self.play(Write(text))
        self.wait(10)


class Outro(Scene):
    CONFIG = {"s": 0.5}

    def construct(self):
        text = TextMobject("Thanks for Watching").scale(2)

        ghub = SVGMobject(file_name="files/github-logo.svg")
        ghub.shift(5 * LEFT + 2.5 * DOWN)
        ghub.scale(self.s)

        ghub_text = TextMobject("/vivek3141")
        ghub_text.shift(3 * LEFT + 2.5 * DOWN)

        insta = SVGMobject(file_name="files/instagram-logo.svg")
        insta.shift(1*RIGHT + 2.5*DOWN)
        insta.scale(self.s)

        twitter = SVGMobject(file_name="files/twitter.svg")
        twitter.shift(2.5*RIGHT + 2.5*DOWN)
        twitter.scale(self.s)

        text2 = TextMobject("/vcubingx")
        text2.shift(2.5*DOWN + 4.5 * RIGHT)

        text.move_to(3 * UP)

        self.play(
            Write(text),
            Write(ghub),
            Write(twitter),
            Write(insta),
            Write(ghub_text),
            Write(text2)
        )
        self.wait(10)


class UpdateOpacity(Scene):
    def construct(self):
        circle = Circle(color=RED, fill_opacity=1, radius=2)
        self.play(Write(circle))

        self.play(UpdateFromAlphaFunc(circle, self.update),
                  rate_func=smooth, run_time=4)

    def update(self, circle, dt):
        opacity = interpolate(1, 0, dt)
        new_circ = Circle(color=RED, fill_opacity=opacity, radius=2)
        circle.become(new_circ)
