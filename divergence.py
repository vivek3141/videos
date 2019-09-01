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

        n = VGroup(
            *[self.n(t)
              for t in np.arange(-1.9, 2.001, 0.5)]
        )
        field = VGroup(axes, f)

        lbl = TexMobject(r"\hat{n}")
        lv = Vector([0, 1, 0], color=GREEN)
        lv.center()
        lbl.shift(0.25 * RIGHT)
        lv.shift(0.25 * LEFT)
        lr = Rectangle(height=1.5, width=1.5)
        nll = VGroup(lr, lv, lbl)
        nll.shift(5 * RIGHT + 3 * UP)

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

        field2 = VGroup(axes2, f2)
        field2.set_fill(opacity=0.5)
        field2.set_stroke(opacity=0.5)

        axes3 = Axes(
            x_min=-5,
            x_max=5,
            y_min=-5,
            y_max=5,
            number_line_config={"include_tip": False, }
        )
        f3 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )

        field3 = VGroup(axes3, f3)
        field3.set_fill(opacity=0.5)
        field3.set_stroke(opacity=0.5)

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

        self.play(Write(n), Uncreate(field), Write(nll))
        self.wait()

        self.play(ShowCreation(field3), Uncreate(nll))
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
            field3.set_fill(opacity=opacity)
            n.set_fill(opacity=opacity)

        focus()

        self.play(ll1.move_to, ORIGIN)
        self.play(ApplyMethod(ll1.scale, 3))

        self.wait()

        w = ll1.get_width()
        h = ll1.get_height()

        line1 = Line((w/2 - 1) * LEFT, (w/2) * RIGHT,
                     color=YELLOW, stroke_width=6).shift(h/2 * DOWN)
        lbl1 = TexMobject(r"\Delta s")
        lbl1.shift((h/2 + 1) * DOWN)
        lbl1.scale(1.5)

        lbl2 = TexMobject(r"F \Delta t")
        lbl2.shift((w/2 + 1) * LEFT)
        lbl2.scale(1.5)

        lbv = Vector([0, h, 0], color=GREEN).shift(h/2 * DOWN + (w/2) * RIGHT)

        lbl3 = TexMobject(r"F \Delta t \cdot \hat{n}")
        lbl3.shift((w/2 + 1.5) * RIGHT)
        lbl3.scale(1.5)

        hhead = TexMobject(
            r"\text{Area} = (F \cdot \hat{n})(\Delta t)(\Delta s)")
        rhead = BackgroundRectangle(hhead, color=BLACK, fill_opacity=1)
        head = VGroup(rhead, hhead)
        head.scale(1.5)
        head.shift(3 * UP)

        hhead2 = TexMobject(
            r"\text{Area per unit time} = (F \cdot \hat{n})(\Delta s)")
        rhead2 = BackgroundRectangle(hhead2, color=BLACK, fill_opacity=1)
        head2 = VGroup(rhead2, hhead2)
        head2.scale(1.5)
        head2.shift(3 * UP)

        self.play(ShowCreation(line1), Write(lbl1))
        self.wait()

        self.play(Write(lbl2))
        self.wait()

        self.play(TransformFromCopy(v2, lbv))
        self.play(Write(lbl3))
        self.wait()

        self.play(Write(head))
        self.wait()

        self.play(Transform(head, head2))
        self.wait()

        a = VGroup(*self.mobjects)

        self.play(Uncreate(a))

        feq = TexMobject(r"\text{Flow rate over C} = \int_C (\vec{F} \cdot \hat{n}) \ ds",
                         tex_to_color_map={r"\text{Flow rate over C}": BLUE}).scale(2)

        feq2 = TexMobject(r"\text{Flux} = \int_C (\vec{F} \cdot \hat{n}) \ ds",
                          tex_to_color_map={r"\text{Flux}": BLUE}).scale(2)

        self.play(Write(feq))
        self.wait()

        self.play(Transform(feq, feq2))
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

    def n(self, t):
        vect = np.array([
            -3*t**2 + 4,
            -4*t,
            0
        ])
        mag = math.sqrt(vect[0] ** 2 + vect[1] ** 2)
        v = Vector((1/mag) * vect, color=GREEN).shift(self.func(t)
                                                      [0] * RIGHT + self.func(t)[1] * UP)
        return v

    @staticmethod
    def func2(t, a=9.6):
        return np.array([
            a*(1-2*t**2-0.4),
            a*(t**3-4*t-2.03),
            0
        ])


class FluxExample(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-3,
            y_max=3,
            number_line_config={"include_tip": False, }
        )
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-3, 4, 1)
              ]
        )

        field = VGroup(axes, f)

        c = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2*PI,
            stroke_width=1.5 * DEFAULT_STROKE_WIDTH,
        )

        curve = c

        field.set_fill(opacity=0.75)
        field.set_stroke(opacity=0.75)

        rect = Rectangle(height=8, width=12)

        grp = VGroup(field, curve, rect)
        grp.scale(0.35)

        grp.shift(3 * LEFT + 2.3 * UP)

        eq1 = TexMobject(r"\text{Find} \int_C (\vec{F} \cdot \hat{n}) \ ds")
        eq1.shift(3 * RIGHT + 3 * UP)

        eq2 = TexMobject(r"F = \langle xy + x, x + y \rangle")
        eq2.shift(3 * RIGHT + 2 * UP)

        eq3 = TexMobject(r"C = \langle \cos(t), \sin(t) \rangle")
        eq3.shift(3 * RIGHT + 1 * UP)

        eq4 = TexMobject(
            r"\int_C \vec{F} \cdot d\vec{r} = \int_a^b F(r(t)) \ || r'(t) || \ dt")
        eq4.shift(0 * UP)

        eq5 = TexMobject(
            r"\int_C (\vec{F} \cdot \hat{n}) \ ds = \int_a^b (F(r(t)) \cdot \hat{n}(r(t)) )\ || r'(t) || \ dt")
        eq5.shift(1.5 * DOWN)

        eq6 = TexMobject(
            r"\int_C (\vec{F} \cdot \hat{n}) \ ds = \int_0^{2\pi} " +
            r"\begin{bmatrix}\cos(t)\sin(t) + \cos(t) \\ \cos(t) + " +
            r"\sin(t) \end{bmatrix} \cdot \begin{bmatrix}\cos(t) \\ \sin(t)\end{bmatrix} \text{d}t")
        eq6.shift(1.5 * DOWN)

        eq7 = TexMobject(r"= 2 \pi")
        eq7.shift(3 * DOWN)

        r1 = Rectangle(height=1, width=2, color=YELLOW)
        r1.shift(3 * DOWN)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2), Write(eq3))
        self.play(ShowCreation(field), Write(rect))
        self.play(Write(curve))
        self.wait()

        self.play(Write(eq4))
        self.wait()

        self.play(Write(eq5))
        self.wait()

        self.play(Transform(eq5, eq6))
        self.wait()

        self.play(Write(eq7))
        self.play(Write(r1))
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
            math.cos(t),
            math.sin(t),
            0
        ])


class DivTwoEq(Scene):
    def construct(self):
        eq = TexMobject(r"\oint_C (\vec{F} \cdot \hat{n}) \ ds = \iint_R \nabla \cdot \vec{F} \ dA",
                        tex_to_color_map={r"\vec{F}": YELLOW, r"C": GREEN, r"R": BLUE, r"\nabla": RED})
        eq.scale(1.5)

        title = TextMobject("2D Divergence Theorem", color=PURPLE)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(Write(eq), Write(title))
        self.wait()


class DivDemo(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0.1
    }

    def construct(self):
        axes_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -4,
            "y_max": 4,
            "number_line_config": {
                "include_tip": False,
            },
        }
        axes = Axes(**axes_config)
        f1 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.field1, prop=0)
                for x in np.arange(-5, 5, 1)
                for y in np.arange(-4, 5, 1)
              ]
        )
        c = Circle(fill_color=RED, fill_opacity=0.25, color=WHITE, radius=1)
        field1 = VGroup(axes, f1, c)
        field1.scale(0.6)

        axes = Axes(**axes_config)
        f2 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.field2, prop=0)
                for x in np.arange(-5, 5, 1)
                for y in np.arange(-4, 5, 1)
              ]
        )

        c = Circle(fill_color=RED, fill_opacity=0.25, color=WHITE, radius=1)
        field2 = VGroup(axes, f2, c)
        field2.scale(0.6)

        axes = Axes(**axes_config)
        f3 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.field3, prop=0)
                for x in np.arange(-5, 6, 1)
                for y in np.arange(-4, 5, 1)
              ]
        )

        c = Circle(fill_color=RED, fill_opacity=0.25, color=WHITE, radius=1)
        field3 = VGroup(axes, f3, c)
        field3.scale(0.6)

        t1 = TexMobject(r"\nabla \cdot \textbf{F} > 0",
                        tex_to_color_map={">": YELLOW})
        t1.shift(3 * UP)
        b1 = BackgroundRectangle(t1, color=BLACK, fill_opacity=1)
        text1 = VGroup(b1, t1)

        t2 = TexMobject(r"\nabla \cdot \textbf{F} < 0",
                        tex_to_color_map={"<": YELLOW})
        t2.shift(3 * UP)
        b2 = BackgroundRectangle(t2, color=BLACK, fill_opacity=1)
        text2 = VGroup(b2, t2)

        t3 = TexMobject(r"\nabla \cdot \textbf{F} > 0",
                        tex_to_color_map={">": YELLOW})
        t3.shift(3 * UP)
        b3 = BackgroundRectangle(t3, color=BLACK, fill_opacity=1)
        text3 = VGroup(b3, t3)

        self.play(Write(field1))
        self.wait()

        self.play(Write(text1))
        self.wait()

        self.play(
            Transform(field1, field2),
            Transform(text1, text2)
        )
        self.wait()

        self.play(
            Transform(field1, field3),
            Transform(text1, text3)
        )
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
    def field1(x, y):
        return np.array([
            x,
            y
        ])

    @staticmethod
    def field2(x, y):
        return np.array([
            -x,
            -y
        ])

    @staticmethod
    def field3(x, y):
        return np.array([
            x + 6,
            0
        ])


class DivTwoVisual(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        axes_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "number_line_config": {"include_tip": False},
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

        n = VGroup(
            *[self.n(t)
              for t in np.arange(-1.9, 2.001, 0.5)]
        )

        axes2 = Axes(**axes_config)
        f2 = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
                for x in np.arange(-5, 5, 1)
                for y in np.arange(-5, 5, 1)
              ]
        )
        f2.set_fill(opacity=0.5)
        f2.set_stroke(opacity=0.5)

        field2 = VGroup(axes, f2)

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
        surface.set_stroke(opacity=0.5)

        curve = VGroup(label, c)

        eq0 = self.getEq(r"\int_C (\vec{\text{F}} \cdot \hat{n}) \ ds")
        eq1 = self.getEq(r"\int_C (\vec{\text{F}} \cdot \hat{n}) \ ds = "
                         + r"\int_{C_1} (\vec{\text{F}} \cdot \hat{n}) \ ds + "
                         + r"\int_{C_2} (\vec{\text{F}} \cdot \hat{n}) \ ds",
                         tex_map={r"{C_1}": RED, r"{C_2}": GREEN})
        eq2 = self.getEq(
            r"\int_{C_r} (\vec{\text{F}} \cdot \hat{n}) \ ds \approx \nabla \cdot \vec{\text{F}} |r|")
        eqf = self.getEq(
            r"\int_C (\vec{\text{F}} \cdot \hat{n}) \ ds = \iint_D \nabla \cdot \vec{\text{F}} \ \text{dA}")

        t1 = [1.225]

        c1 = VGroup(
            *[Line(-self.func(t)[1]*UP, self.func(t)[1] *
                   UP, color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2).shift(self.func(t)[0]*RIGHT) for t in t1],
            ParametricFunction(
                self.func,
                t_min=1.22,
                t_max=2,
                color=RED,
                stroke_width=DEFAULT_STROKE_WIDTH*2
            ),
            ParametricFunction(
                self.func,
                t_min=-2,
                t_max=-1.22,
                color=RED,
                stroke_width=DEFAULT_STROKE_WIDTH*2
            ),
            TexMobject(r"\text{C}_1", color=RED).shift(
                2 * LEFT + 1.5 * UP).scale(1.5)

        )
        c2 = VGroup(
            *[Line(-self.func(t)[1]*UP, self.func(t)[1] *
                   UP, color=GREEN, stroke_width=DEFAULT_STROKE_WIDTH*2).shift(self.func(t)[0]*RIGHT) for t in t1],

            ParametricFunction(
                self.func,
                t_min=-1.22,
                t_max=1.22,
                color=GREEN,
                stroke_width=DEFAULT_STROKE_WIDTH*2
            ),
            TexMobject(r"\text{C}_2", color=GREEN).shift(
                2 * RIGHT + 1.5 * UP).scale(1.5)
        )

        table2 = VGroup()

        for t in np.arange(0, 2, 0.05):
            y = self.func(t)[1]
            x = self.func(t)[0]
            roots = [i for i in np.roots(
                [1, 0, -4, -x]) if 2 >= i.real >= -2 and i.imag == 0]

            l1 = Line(-y*UP, y * UP, color=RED).shift(x*RIGHT)
            if len(roots) >= 2:
                l2 = Line(self.func(roots[0])[
                    0]*RIGHT, self.func(roots[1])[0] * RIGHT, color=RED).shift(self.func(roots[0])[1]*UP)

            table2.add(l1, l2)

        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

        self.play(Write(n))
        self.wait()

        self.play(Transform(field, field2))
        self.wait()

        self.play(Write(eq0))
        self.wait()

        self.play(Uncreate(eq0), Write(c1))
        self.wait()

        self.play(Write(c2))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Uncreate(eq1), Uncreate(c1), Uncreate(c2), Write(table2))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Uncreate(table2), Uncreate(eq2), Write(surface))
        self.wait()

        self.play(Write(eqf))
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

    def getEq(self, eq, tex_map={}):
        eq1 = TexMobject(eq, tex_to_color_map=tex_map)
        back = BackgroundRectangle(eq1, color=BLACK, fill_opacity=1)
        eq0 = VGroup(back, eq1)
        eq0.shift(3 * UP)

        return eq0

    @staticmethod
    def vect(x, y):
        return np.array([
            x*y+x,
            x+y,
            0
        ])

    def n(self, t):
        vect = np.array([
            -3*t**2 + 4,
            -4*t,
            0
        ])
        mag = math.sqrt(vect[0] ** 2 + vect[1] ** 2)
        v = Vector((1/mag) * vect, color=GREEN).shift(self.func(t)
                                                      [0] * RIGHT + self.func(t)[1] * UP)
        return v


class IntP1(GraphScene):
    CONFIG = {
        "x_max": 4,
        "x_labeled_nums": list(range(-1, 5)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 2.5,
        "y_labeled_nums": list(range(5, 20, 5)),
        "n_rect_iterations": 6,
        "default_right_x": 3,
        "func": lambda x: 0.1*math.pow(x-2, 2) + 1,
    }

    def construct(self):
        ftc = TexMobject(r"\int_a^b f'(x) \ dx = f(b) - f(a)")
        ftc.shift(3 * UP)

        self.play(Write(ftc))
        self.setup_axes()
        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))

        self.graph = graph
        rect = self.get_riemann_rectangles(
            self.graph,
            x_min=1,
            x_max=self.default_right_x,
            dx=0.004,
            stroke_width=4*0.004,
        )
        foreground_mobjects = [self.axes, self.graph]

        self.play(
            DrawBorderThenFill(
                rect,
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
            *list(map(Animation, foreground_mobjects))
        )

        self.wait()


class DivThreeEq(Scene):
    def construct(self):
        eq = TexMobject(r"\oiint_S \vec{F} \cdot d \vec{S} = \iiint_V \nabla \times \vec{F} \,dV",
                        tex_to_color_map={r"\vec{F}": YELLOW, r"S": GREEN, r"V": BLUE, r"\nabla": RED})
        eq.scale(1.5)

        title = TextMobject("3D Divergence Theorem", color=PURPLE)
        title.scale(1.5)
        title.shift(3 * UP)

        title2 = TextMobject("Gauss' Theorem", color=ORANGE)
        title2.shift(2 * UP)

        self.play(Write(eq), Write(title), Write(title2))
        self.wait()


class IntP2(ThreeDScene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        s = Sphere()

        n = VGroup(
            *[self.n(*self.func(u, v))
              for u in np.arange(0, PI, 0.2)
              for v in np.arange(0, TAU, 0.2)]
        )

        axes = ThreeDAxes(
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        surface = VGroup(axes, s)
        surface.scale(2)

        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP + z * OUT, self.vect, prop=0, opacity=0.5)
                for x in np.arange(-5, 6, 1)
                for y in np.arange(-5, 6, 1)
                for z in np.arange(-3, 4, 1)
              ]
        )

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.play(Write(f))
        self.play(Write(n))

        self.begin_ambient_camera_rotation()
        self.wait(10)

    def func(self, u, v):
        return [
            np.cos(v) * np.sin(u),
            np.sin(v) * np.sin(u),
            np.cos(u)
        ]

    def vect(self, x, y, z):
        return np.array([
            y, x, z
        ])

    def n(self, x, y, z):
        vect = np.array([
            x,
            y,
            z
        ])

        mag = math.sqrt(vect[0] ** 2 + vect[1] ** 2 + vect[2] ** 2)
        v = Vector(
            (0.5/mag) * vect,
            color=GREEN,
            stroke_width=DEFAULT_STROKE_WIDTH).shift(2*x * RIGHT + 2*y * UP + 2*z * OUT)
        return v

    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y, z = point[:]
        func = f(x, y, z)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2 + func[2] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0, 0])
        func = func / 1.5
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
            v.set_stroke(opacity=opacity)
        return v
