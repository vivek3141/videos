from manimlib.imports import *


class IntroQuote(Scene):
    def construct(self):
        quote = TextMobject("""
        I have to pay a certain sum, which I have collected in my pocket.
        I take the bills and coins out of my pocket and give them to the 
        creditor in the order I find them until I have reached the total 
        sum. This is the Riemann integral. But I can proceed differently. 
        After I have taken all the money out of my pocket I order the bills 
        and coins according to identical values and then I pay the 
        several heaps one after the other to the creditor. This is my integral.""")
        quote.scale(0.75)
        author = TextMobject("- Henri Lebesgue", color=YELLOW)
        author.shift(2 * DOWN + 3 * RIGHT)
        self.play(Write(quote))
        self.play(Write(author))
        self.wait(5)


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
        "y_axis_label": "",
    }

    def construct(self):
        self.setup_axes()

        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))
        self.graph = graph

        rects = VGroup()

        for dx in np.arange(0.2, 0.05, -0.05):
            rect = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects.add(rect)

        self.play(
            DrawBorderThenFill(
                rects[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect in rects[1:]:
            self.play(
                Transform(
                    rects[0], rect,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )
            self.wait()

        t = Text("Riemann Integration")
        t.scale(1.5)
        t.shift(3 * UP)

        self.play(FadeInFromDown(t))
        self.wait()


class Problems(Scene):
    def construct(self):
        title = Text(
            "Problems with Riemann Integration", color=PURPLE)
        title.scale(1.25)
        title.shift(3 * UP)

        l = BulletedList("Higher Dimensions", "Continuitiy",
                         dot_color=BLUE, buff=0.75*LARGE_BUFF)
        l.scale(1.5)
        l.shift(0.25*DOWN)

        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        self.play(l.fade_all_but, 0)
        self.wait()

        self.play(l.fade_all_but, 1)
        self.wait()


class HigherDim(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -3.5,
            "z_max": 3.5,
        }
        axes = ThreeDAxes(**axis_config)
        cubes = VGroup()

        for x in np.arange(-5, 5.1, 0.5):
            for y in np.arange(-5, 5.1, 0.5):
                z = np.sin(x) + np.cos(y)
                p = Prism(dimensions=[0.5, 0.5, z])
                p.shift([x, y, z/2])
                cubes.add(p)

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(axes))
        self.play(Write(cubes))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(30)


class PieceWise(Scene):
    def construct(self):
        axes = Axes(
            x_min=-1,
            x_max=5,
            y_min=-1,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )
        f = VGroup(
            FunctionGraph(lambda x: 2, x_min=0, x_max=2.5),
            FunctionGraph(lambda x: 4, x_min=2.5, x_max=5)
        )
        r1 = self.get_riemann_sums(lambda x: 2)

        grp = VGroup(axes, f, r1)
        grp.center()

        self.play(Write(axes), Write(f))
        self.wait()

        self.play(Write(r1))
        self.wait()

        r = Rectangle(height=1.9, width=1, stroke_opacity=1,
                      fill_opacity=1, stroke_color=DARK_BLUE, fill_color=BLUE,)
        r.next_to(r1[-1], RIGHT).shift(0.25 * LEFT)

        h = ValueTracker(1.9)

        def update(rect):
            r = Rectangle(height=h.get_value(), width=1, stroke_opacity=1,
                          fill_opacity=1, stroke_color=DARK_BLUE, fill_color=BLUE,)
            r.next_to(r1[-1], RIGHT).shift(0.25 * LEFT +
                                           (h.get_value() - 1.9)/2 * UP)
            rect.become(r)

        r.add_updater(update)

        self.play(Write(r))
        self.play(h.increment_value, 2, rate_func=there_and_back, run_time=3)
        self.wait()

    def get_riemann_sums(self, func, dx=1, x=(0.5, 2.5), color=RED):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)
            rect = Rectangle(height=h-0.1, width=dx, stroke_color=DARK_BLUE, fill_color=BLUE,
                             stroke_opacity=1, fill_opacity=1)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects


class IRFunc(Scene):
    def construct(self):
        eq = TexMobject(
            r"f(x) = \begin{cases} 0 & x \text{ is rational} \\ 1 & x \text{ is irrational} \end{cases}")
        eq.scale(1.5)

        self.play(Write(eq))
        self.wait()

        self.play(eq.scale, 0.5)
        self.play(eq.shift, 3 * UP)
        self.wait()


class IRGraph(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 1,
        "x_labeled_nums": list(range(0, 2)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 1,
        "y_labeled_nums": list(range(0, 2)),
        "func": lambda x: 1,
        "y_axis_label": "",
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func)
        self.wait()

        dx = 0.005
        rects = self.get_riemann_rectangles(
            graph,
            x_min=0,
            x_max=1,
            dx=dx,
            stroke_width=2,
        )

        self.play(
            DrawBorderThenFill(
                rects,
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()


class IRExp(Scene):
    def construct(self):
        num = TexMobject("0.", "123", "123123...")
        num.scale(3)

        self.play(FadeInFromDown(num[0]))
        self.wait()

        self.play(FadeInFromDown(num[1]))
        self.wait()

        b = Brace(num[2], color=YELLOW)
        t = b.get_tex("P = (0.1)^n")

        br = VGroup(b, t)

        self.play(Write(num[2]))
        self.play(Write(br))
        self.wait()

        axes = Axes(
            x_min=-1,
            x_max=1,
            y_min=0,
            y_max=1,
            axis_config={
                "include_tip": False
            }
        )
        f = FunctionGraph(lambda x: 0.1 * math.pow(0.1, x),
                          x_min=-1, x_max=1, color=TEAL)

        func = VGroup(axes, f)
        func.shift(2 * UP + 3 * LEFT)
        func.scale(2)

        eq = TexMobject(r"\lim_{n \rightarrow \infty} 0.1^n = 0")
        eq.scale(1.5)
        eq.shift(2 * UP + 3 * RIGHT)

        self.play(Write(func))
        self.play(Write(eq))
        self.wait()


class Integ(Scene):
    def construct(self):
        eq = TexMobject(r"\int_0^1 f(x) dx = 1")
        eq.scale(2)
        self.play(Write(eq))


class LebesguePart(Scene):
    def construct(self):
        title = TextMobject("Lebesgue Integration", color=GOLD)
        title.scale(2)

        self.play(Write(title))
        self.wait()


class HenriLebesgue(Scene):
    def construct(self):
        img = ImageMobject("./img/henri.jpg")
        img.scale(2.5)
        img.shift(1 * UP)
        eq = TextMobject(r"Henri Lebesgue").scale(1.5).shift(2.5 * DOWN)

        self.play(FadeInFromDown(img))
        self.play(Write(eq))
        self.wait()


class LebesgueIntegral(Scene):
    CONFIG = {
        "func": lambda x: -0.9 * (x - 2.5) ** 2 + 2.5,
    }

    def construct(self):
        axes = Axes(
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )
        f = FunctionGraph(self.func, x_min=0.833, x_max=4.167,
                          color=WHITE, stroke_width=2)
        func = VGroup(axes, f)
        rects = self.get_lebesgue_rectangles()
        self.add(axes, rects, f)

    def get_lebesgue_rectangles(self, dx=0.2, y=(0, 2.75)):
        rects = VGroup()
        y_range = np.arange(y[0], y[1], dx)
        colors = color_gradient([WHITE, RED], len(y_range))
        for color, y in zip(colors, y_range):
            x = abs(2.5 - ((((y + dx) - 2.5)/(-0.9))**(1/2) + 2.5))
            rect = Rectangle(height=dx, width=2*x, stroke_color=BLACK,  fill_color=color,
                             stroke_opacity=1, fill_opacity=1, stroke_width=2*dx)
            rect.shift([2.5, y+dx/2, 0])
            rects.add(rect)

        return rects
