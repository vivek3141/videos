from manimlib import *


class Scene(Scene):
    def interact(self):
        self.quit_interaction = False
        self.lock_static_mobject_data()
        try:
            while True:
                self.update_frame()
        except KeyboardInterrupt:
            self.unlock_mobject_data()


class ComplexTest(Scene):
    def construct(self):

        a = Sphere()
        self.add(a)
        n = NumberPlane()
        # n.prep
        # n.apply_complex_function
        self.embed()
        n.add_updater


class NormalDerivative(Scene):
    LINE_COLOR = "#e2e1a4"

    def construct(self):
        axes = Axes(x_range=(-2, 5), y_range=(0, 5))
        self.axes = axes

        func = axes.get_graph(self.func, color=BLUE)
        label = axes.get_graph_label(func, label=r"f(x)")

        line_kwargs = {
            "color": self.LINE_COLOR
        }
        eq_kwargs = {

        }
        self.len_of_line = 2

        v = ValueTracker(-1)
        l = self.get_line(-1, **line_kwargs)
        eq = self.get_eq(-1, **eq_kwargs)

        l.add_updater(lambda l: l.become(self.get_line(v.get_value(), **line_kwargs)))
        eq.add_updater(lambda e: e.become(self.get_eq(v.get_value(), **eq_kwargs)))

        self.add(axes, func, label, l, eq)
        self.embed()
    
    def get_eq(self, t, **kwargs):
        f_prime = "{:.2f}".format(round(self.deriv(t), 2))
        eq = Tex(r"{{df} \over {dx}} = ", tex_to_color_map={r"f": BLUE}, **kwargs)

        n = DecimalNumber(float(f_prime), color=self.LINE_COLOR)
        n.move_to(eq)
        n.shift(1.25 * RIGHT)

        eq = VGroup(eq, n)
        eq.scale(1.5)
        eq.shift(2.5 * UP)

        return eq
        

    def get_line(self, t, **kwargs):
        f_prime = self.deriv(t)
        theta = np.arctan(f_prime)
        center = np.array([t, self.func(t), 0])

        p1 = self.len_of_line/2 * \
            np.array([np.cos(theta), np.sin(theta), 0]) + center
        p2 = -self.len_of_line/2 * \
            np.array([np.cos(theta), np.sin(theta), 0]) + center

        return Line(self.axes.c2p(*p1), self.axes.c2p(*p2), **kwargs)

    def func(self, x):
        x -= 1
        return 0.1 * (x**4 - x**3 - 6*x**2) + 2.5

    def deriv(self, x):
        return 0.5 + 0.6 * x - 1.5 * x**2 + 0.4 * x**3
