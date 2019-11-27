from manimlib.imports import *


class PrimeFuncGraph(GraphScene):
    CONFIG = {
        "y_max": 100,
        "y_min": 0,
        "x_max": 20,
        "x_min": 0,
        "y_tick_frequency": 5,
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

    @staticmethod
    def count_prime(x):
        x = int(x)
        counter = 0

        for i in range(x):
            if isPrime(i):
                counter += 1

        return counter

    @staticmethod
    def isPrime(x):
        for i in range(2, int((x+1)/2)):
            if x % i == 0:
                return False
        return True
