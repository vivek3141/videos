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

        axes = Axes(**axes_config)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
        )

        field = VGroup(axes, f)
        # field.scale(0.6)

        axes2 = Axes(**axes_config)
        f2 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0).set_fill(opacity=0.5)
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
        )

        field2 = VGroup(axes, f2)
        # field2.scale(0.6)

        c = ParametricFunction(
            self.func,
            t_min=-2,
            t_max=2,
        )
        c.set_stroke(opacity=0.75)
        label = TextMobject("C")
        label.shift(3 * LEFT)
        label.scale(2)

        surface = ParametricSurface(
            self.surface,
            u_min=-2,
            u_max=2,
            v_min=-1,
            v_max=1,
            fill_color=BLUE,
            checkerboard_colors=[BLUE, BLUE],
            stroke_color=BLUE
        ).set_fill(opacity=0.5)

        curve = VGroup(label, c)

        eq = TexMobject(
            r"\int_C \vec{\text{F}} \bullet \text{d}\vec{\text{r}}")
        back = BackgroundRectangle(eq, color=BLACK, fill_opacity=1)
        eq0 = VGroup(back, eq)
        eq0.shift(3 * UP)

        eq = TexMobject(
            r"\int_C \vec{\text{F}} \bullet \text{d}\vec{\text{r}} = \int_{C_1} \vec{\text{F}} \bullet \text{d}\vec{\text{r}} + \int_{C_2} \vec{\text{F}} \bullet \text{d}\vec{\text{r}}")
        back = BackgroundRectangle(eq, color=BLACK, fill_opacity=1)
        eq1 = VGroup(back, eq)
        eq1.shift(3 * UP)

        eq = TexMobject(
            r"\int_{C_r} \vec{\text{F}} \bullet \text{d}\vec{\text{r}} = \nabla \times \vec{\text{F}} \|r\|")
        back = BackgroundRectangle(eq, color=BLACK, fill_opacity=1)
        eq2 = VGroup(back, eq)
        eq2.shift(3 * UP)

        eq = TexMobject(
            r"\int_C \vec{\text{F}} \bullet \text{d}\vec{\text{r}} = \iint_D \nabla \times \vec{\text{F}} \ \text{dA}")
        back = BackgroundRectangle(eq, color=BLACK, fill_opacity=1)
        eqf = VGroup(back, eq)
        eqf.shift(3 * UP)

        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

        self.play(Transform(field, field2))
        self.wait()

        #self.play(Write(surface))
        #self.wait()

        self.play(Write(eq0))
        self.wait()

        self.play(Transform(eq0, eq1))
        self.wait()

        self.play(Transform(eq0, eq2))
        self.wait()

        self.play(Transform(eq0, eqf))
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
            1 - 2*t**2 + 2,
            t**3 - 4*t,
            0
        ])

    @staticmethod
    def surface(t, v):
        return np.array([
            1 - 2*t**2 + 2,
            v*(t**3 - 4*t),
            0
        ])

    @staticmethod
    def vect(x, y):
        return np.array([
            y,
            x,
            0
        ])
