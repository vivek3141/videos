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
            lambda t:  0.5*t**2,
            color=PINK,
        )

        self.play(Write(f1))
        self.wait()
    
    