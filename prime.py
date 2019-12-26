from manimlib.imports import *
from scipy.special import expi


class PrimeMethods:
    def count_prime(self, x):
        counter = 0

        for i in range(2, int(x)):
            if self.isPrime(i):
                counter += 1

        return counter

    def isPrime(self, x):
        for i in range(2, int(x/2) + 1):
            if x % i == 0:
                return False
        return True

    def pnt(self, x):
        return self.count_prime(x)/(x/math.log(x))

    def pnt_li(self, x):
        return self.count_prime(x)/expi(math.log(x))


class PrimeFuncGraph(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 500,
        "y_min": 0,
        "x_max": 3000,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$\pi(x)$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.count_prime,
            color=PINK,
        )

        self.play(Write(f1))
        self.wait()


class PNTGraph(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 2,
        "y_min": 0,
        "x_max": 1000,
        "x_min": 0.001,
        "y_tick_frequency": 1,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": r"$\frac{\pi(x)}{x/ \ln (x)}$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.pnt,
            color=RED,
        )

        self.play(Write(f1))
        self.wait()


class PNTGraph2(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 2,
        "y_min": 0,
        "x_max": 1000,
        "x_min": 0.001,
        "y_tick_frequency": 1,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.pnt,
            color=RED,
        )
        f2 = self.get_graph(
            self.pnt_li,
            color=YELLOW,
        )

        lbl1 = TexMobject(
            r"\frac{\pi(x)}{x / \ln (x)}").shift(2 * UP).scale(0.75)
        lbl2 = TexMobject(r"\frac{\pi(x)}{Li(x)}").shift(1 * DOWN).scale(0.75)

        l1 = VGroup()
        self.freq = 0.33*self.x_tick_frequency
        for i in range(1, int(self.x_max/self.freq), 2):
            l1.add(
                self.get_graph(
                    lambda x: 1,
                    x_min=i * self.freq,
                    x_max=(i+1) * self.freq,
                    color=WHITE,
                    stroke_width=0.5 * DEFAULT_STROKE_WIDTH
                )
            )

        self.play(
            Write(f1),
            Write(f2),
            Write(lbl1),
            Write(lbl2),
            Write(l1)
        )
        self.wait()
