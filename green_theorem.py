from manim import *


class Diagram(Scene):
    def construct(self):
        pass


class GreenTheoremVisual(Scene):
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
        r_config = {"x_min": -3,
                    "x_max": 3,
                    "y_min": 0,
                    "y_max": 0.01,
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
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
        )

        field = VGroup(axes, f)
        field.scale(0.6)

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
        curve.scale(0.6)

        r_axes = Axes(**r_config)
        c2 = ParametricFunction(
            self.line_evaluated,
            t_min=-3,
            t_max=3,
            color=RED
        )
        func = VGroup(r_axes)
        func.shift(3 * DOWN + 2 * LEFT)

        
        self.f = VGroup()
        self.a = VGroup()

        """ self.play(Write(integral))

        self.play(ApplyMethod(integral.scale, 0.5))
        self.play(ApplyMethod(integral.shift, 3 * UP))
 """
        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

        """   self.play(Uncreate(integral), ApplyMethod(field.shift, 1 * UP), ApplyMethod(curve.shift, 1 * UP))
        self.wait() """

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

    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "r"):
            dt = self.frame_duration

            t = self.t
            d_point = (self.func(t + dt) - self.func(t)) * 0.6 * RIGHT + ((dt * 0.6) * UP)

            self.r.shift(d_point)
            self.r_.put_start_and_end_on(self.r_.get_start(), (self.r_prime(t) * 0.6) + self.r_.get_start())

            self.fr.put_start_and_end_on(self.fr.get_start(), (self.f_r(t) * 0.25) + self.fr.get_start())
            self.v2.put_start_and_end_on(self.v2.get_start(), (self.func(t) * 0.25) + self.v2.get_start())

            l2 = Line(
                (3 - self.line_evaluated(t)[1]) * DOWN + (2 - t) * LEFT,
                3 * DOWN + (2 - t) * LEFT,
                color=YELLOW,
                stroke_width=dt
            )
            self.a.add(l2)
            self.add(
                l2
            )

            l1 = Line(
                (3 - self.line_evaluated(t)[1]) * DOWN + (2 - t) * LEFT,
                (3 - self.line_evaluated(t + dt)[1]) * DOWN + (2 - t - dt) * LEFT,
                color=RED,
                stroke_width=8
            )
            self.f.add(l1)
            self.add(
                l1
            )

            if self.t >= 3:
                del self.r
            self.t = self.t + dt
