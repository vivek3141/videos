from manimlib.imports import *

maxn = 10


def func(x, b=0.1):
    y = 0
    for i in range(1, maxn):
        y += np.cos((b ** i) * PI * x) / (3 ** i)
    return y


class Visualization(Scene):
    def construct(self):
        t = ValueTracker(0.1)
        f = FunctionGraph(func, color=GOLD).scale(5)
        axes = Axes(
            x_min=-15,
            x_max=15,
            y_min=-15,
            y_max=15,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": True,
                "exclude_zero_from_default_numbers": True,
            },
        )
        f.add_updater(lambda x: x.become(
            FunctionGraph(lambda x: func(x, t.get_value()), color=GOLD).scale(5)))

        self.play(Write(f))
        self.play(t.increment_value, 4.9,  run_time=3, rate_func=linear)
        self.wait()
