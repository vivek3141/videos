from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Green's Theorem")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        eq = TexMobject(r"\oiint_S \vec{F} \cdot d \vec{S} = \iiint_V \nabla \times \vec{F} \,dV",
                        tex_to_color_map={r"S": BLUE, r"\vec{F}": YELLOW,
                                          r"\nabla": RED, r"V": GREEN})
        eq.scale(1.5)

        title2 = TextMobject("Divergence Theorem", color=PURPLE)
        title2.scale(1.5)
        title2.shift(3 * UP)

        self.play(
            FadeInFromDown(title),
            Write(rect)
        )
        self.wait()

        self.play(
            Uncreate(rect),
            Uncreate(title)
        )
        self.play(
            Write(eq),
            Write(title2)
        )
        self.wait()


class FluxIntegral(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        eq1 = TexMobject(r"\int_C \vec{F} \cdot \hat{n} \ \text{d}s")
        eq1.scale(1.5)

        t1 = TextMobject("Flux Integral", color=BLUE)
        t1.scale(1.5)
        t1.shift(3 * UP)

        eq2 = TexMobject(r"\int_C \vec{F} \cdot \hat{n} \ \text{d}s")
        eq2.shift(3 * UP)

        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-5,
            y_max=5,
            number_line_config={"include_tip": False, }
        )
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )
        field = VGroup(axes, f)

        axes2 = Axes(
            x_min=-5,
            x_max=5,
            y_min=-5,
            y_max=5,
            number_line_config={"include_tip": False, }
        )
        f2 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )

        field2 = VGroup(axes, f2)
        field2.set_fill(opacity=0.5)
        field2.set_stroke(opacity=0.5)

        curve = ParametricFunction(
            self.func,
            t_min=-2,
            t_max=2,
            color=YELLOW_E
        )

        a = 9.6
        c1 = ParametricFunction(
            lambda t: np.array([a*(1-2*t**2-0.4), a*(t**3-4*t-2.03), 0]),
            t_min=-0.6,
            t_max=-0.5,
            color=YELLOW_E
        )

        c2 = ParametricFunction(
            self.func2,
            t_min=-0.58,
            t_max=-0.51,
            color=YELLOW_E
        )

        b = Brace(c2, LEFT)
        b.rotate(0.6187171549725232)
        b.shift(0.75 * RIGHT)
        t = b.get_tex(r"\Delta s")

        p1 = self.func2(-0.58)
        p2 = self.func2(-0.52)

        v1 = Vector(np.array([0.5, 0.75, 0]), color=RED).shift(
            p1[0]*RIGHT + p1[1]*UP)
        v2 = Vector(np.array([0.5, 0.75, 0]), color=RED).shift(
            p2[0]*RIGHT + p2[1]*UP)

        r = Rectangle(
            height=3,
            width=4,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )

        p = Polygon(
            np.array([0.5, 0.75, 0])+p1[0]*RIGHT + p1[1]*UP,
            np.array([0.5, 0.75, 0])+p2[0]*RIGHT + p2[1]*UP,
            p2[0]*RIGHT + p2[1]*UP,
            p1[0]*RIGHT + p1[1]*UP,
            color=BLUE,
            fill_opacity=0.75,
            stroke_opacity=0.75
        )

        ll1 = VGroup(p, v1, v2)
        ll2 = VGroup(r, c1, b, t)
        r1 = VGroup(ll2, ll1)

        r1.shift(2.5 * RIGHT + 1.5 * DOWN)

        point = 2 * UP + 2.474606757 * RIGHT
        p1 = 0.125 * UP + 0.125 * RIGHT
        p2 = 0.125 * UP + 0.125 * LEFT

        l1 = Line(0.5 * RIGHT, point-p1, stroke_width=1*DEFAULT_STROKE_WIDTH)
        l2 = Line(4.5 * RIGHT, point-p2, stroke_width=1*DEFAULT_STROKE_WIDTH)

        r2 = Rectangle(
            height=0.25,
            width=0.25,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_width=1*DEFAULT_STROKE_WIDTH
        )
        r2.shift(point)

        zoom = VGroup(r2, l1, l2, r1)

        self.play(Write(eq1), Write(t1))
        self.wait()

        self.play(Uncreate(t1), Transform(eq1, eq2))

        self.play(ShowCreation(field), Uncreate(eq1))
        self.wait()

        self.play(Transform(field, field2), Write(curve))
        self.wait()

        self.play(
            Write(zoom)
        )
        self.wait()

        self.play(
            ApplyMethod(ll1.rotate, -0.6187171549725232 + (PI/2)),
            Uncreate(b),
            Uncreate(t)
        )

        def focus(opacity=0.1):
            for i in self.mobjects:
                i.set_stroke(opacity=opacity)
            v1.set_stroke(opacity=1)
            v2.set_stroke(opacity=1)
            field.set_fill(opacity=opacity)

        focus()

        self.play(ll1.move_to, ORIGIN)
        self.play(ApplyMethod(ll1.scale, 3))

        b1 = Brace(ll1, DOWN)

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
    def vect(x, y):
        return np.array([
            x*y+x,
            x+y,
            0
        ])

    @staticmethod
    def func(t):
        return np.array([
            1 - 2*t**2 + 2,
            t**3 - 4*t,
            0
        ])

    @staticmethod
    def func2(t, a=9.6):
        return np.array([
            a*(1-2*t**2-0.4),
            a*(t**3-4*t-2.03),
            0
        ])

    


class Setup(Scene):
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
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )

        field = VGroup(axes, f)
        # field.scale(0.6)

        c = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2*PI,
            stroke_width=1.5 * DEFAULT_STROKE_WIDTH,
        )

        curve = c

        field.set_fill(opacity=0.75)
        field.set_stroke(opacity=0.75)

        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

        # self.play(Write(surface))
        # self.wait()

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
    def vect(x, y):
        return np.array([
            x*y+x,
            x+y,
            0
        ])

    @staticmethod
    def func(t):
        return np.array([
            math.cos(t),
            math.sin(t),
            0
        ])

    @staticmethod
    def surface(t, v):
        return np.array([
            1 - 2*t**2 + 2,
            v*(t**3 - 4*t),
            0
        ])


class Test(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        a = 9.6
        c1 = ParametricFunction(
            lambda t: np.array([a*(1-2*t**2-0.4), a*(t**3-4*t-2.03), 0]),
            t_min=-0.6,
            t_max=-0.5,
            color=YELLOW_E
        )

        c2 = ParametricFunction(
            self.func2,
            t_min=-0.58,
            t_max=-0.51,
            color=YELLOW_E
        )

        b = Brace(c2, LEFT)
        b.rotate(-0.9520791718223733 + (PI/2))
        b.shift(0.75 * RIGHT)
        t = b.get_tex(r"\Delta s")

        p1 = self.func2(-0.58)
        p2 = self.func2(-0.52)

        v1 = Vector(np.array([0.5, 0.75, 0]), color=RED).shift(
            p1[0]*RIGHT + p1[1]*UP)
        v2 = Vector(np.array([0.5, 0.75, 0]), color=RED).shift(
            p2[0]*RIGHT + p2[1]*UP)

        r = Rectangle(
            height=3,
            width=4,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        p = Polygon(
            np.array([0.5, 0.75, 0])+p1[0]*RIGHT + p1[1]*UP,
            np.array([0.5, 0.75, 0])+p2[0]*RIGHT + p2[1]*UP,
            p2[0]*RIGHT + p2[1]*UP,
            p1[0]*RIGHT + p1[1]*UP,
            color=BLUE,
            fill_opacity=0.75,
            stroke_opacity=0.75)
        l1 = VGroup(p, v1, v2)
        l2 = VGroup(r, c1, b, t)
        r1 = VGroup(l2, l1)

        # r1.shift(2.5 * RIGHT + 1.5 * DOWN)

        self.play(Write(r1))
        self.wait()

        self.play(ApplyMethod(
            l1.rotate, -0.6187171549725232 + (PI/2)), Uncreate(l2))

        self.play(l1.center, ApplyMethod(l1.scale, 2))

        self.wait()

    @staticmethod
    def func2(t, a=9.6):
        return np.array([
            a*(1-2*t**2-0.4),
            a*(t**3-4*t-2.03),
            0
        ])

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
    def vect(x, y):
        return np.array([
            x*y+x,
            x+y,
            0
        ])

    @staticmethod
    def func(t):
        return np.array([
            1 - 2*t**2 + 2,
            t**3 - 4*t,
            0
        ])
