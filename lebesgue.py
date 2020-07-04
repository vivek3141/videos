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
        grp = VGroup(axes, f)
        grp.center()
        self.add(grp)
