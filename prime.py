from manimlib.imports import *


class PrimeMethods:
    def count_prime(self, x):
        counter = 0

        for i in range(int(x)):
            if self.isPrime(i):
                counter += 1

        return counter

    def isPrime(self, x):
        for i in range(2, int((x+1)/2)):
            if x % i == 0:
                return False
        return True

    def pnt(self, x):
        return self.count_prime(x)/(x/math.log(x))


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
