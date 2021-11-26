from manimlib import *

YELLOW_Z = "#e2e1a4"


class Scene(Scene):
    def interact(self):
        self.quit_interaction = False
        self.lock_static_mobject_data()
        try:
            while True:
                self.update_frame()
        except KeyboardInterrupt:
            self.unlock_mobject_data()


class PartScene(Scene):
    CONFIG = {
        "n": 1,
        "title": "",
        "title_color": RED
    }

    def construct(self):
        part = TextMobject(f"Part {self.n}")
        part.scale(1.5)
        part.shift(2 * UP)

        title = TextMobject(self.title, color=self.title_color)
        title.scale(1.5)

        self.play(Write(part))
        self.play(Write(title))
        self.wait()


class ComplexTest(Scene):
    def construct(self):

        a = Sphere()
        self.add(a)
        n = NumberPlane()
        Dot
        # n.prep
        # n.apply_complex_function
        self.embed()
        n.add_updater


class NormalDerivative(Scene):
    LINE_COLOR = YELLOW_Z

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
        dot_kwargs = {
            "color": self.LINE_COLOR
        }
        self.len_of_line = 2

        v = ValueTracker(-1)
        l = self.get_line(-1, **line_kwargs)
        eq = self.get_eq(-1, **eq_kwargs)
        d = self.get_point(-1, **dot_kwargs)

        l.add_updater(lambda l: l.become(
            self.get_line(v.get_value(), **line_kwargs)))
        eq.add_updater(lambda e: e.become(
            self.get_eq(v.get_value(), **eq_kwargs)))
        d.add_updater(lambda d: d.become(
            self.get_point(v.get_value(), **dot_kwargs)))

        self.play(
            Write(axes),
            Write(func),
            Write(label)
        )
        self.play(
            Write(l),
            Write(eq),
            Write(d)
        )
        self.wait()

        self.play(v.increment_value, 5, run_time=10, rate_func=linear)
        self.wait()
        self.embed()

    def get_eq(self, t, **kwargs):
        f_prime = "{:.2f}".format(round(self.deriv(t), 2))
        eq = Tex(r"{{df} \over {dx}} = ",
                 tex_to_color_map={r"f": BLUE}, **kwargs)

        n = DecimalNumber(float(f_prime), color=self.LINE_COLOR)

        n.scale(1.5)
        n.shift(2.5 * UP + 2 * RIGHT)

        eq.scale(1.5)
        eq.shift(2.5 * UP)

        return VGroup(eq, n)

    def get_point(self, t, **kwargs):
        return Dot(self.axes.c2p(*np.array([t, self.func(t), 0])), **kwargs)

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


class IntroduceComplexFunction(Scene):
    plane_opacity = 0.65

    def construct(self):
        c = ComplexPlane()
        c.add_coordinate_labels()

        complex_kwargs = {
            "background_line_style": {
                "stroke_opacity": self.plane_opacity
            }
        }
        c1 = ComplexPlane(x_range=(-3, 3), y_range=(-3, 3), **complex_kwargs)
        c1.add_coordinate_labels()
        c1.axes.set_opacity(self.plane_opacity)
        c1.shift(FRAME_WIDTH/4 * LEFT + 0.5 * DOWN)

        c2 = ComplexPlane(x_range=(-3, 3), y_range=(-3, 3), **complex_kwargs)
        c2.add_coordinate_labels()
        c2.axes.set_opacity(self.plane_opacity)
        c2.shift(FRAME_WIDTH/4 * RIGHT + 0.5 * DOWN)

        input_text = TexText("Input Space", color=YELLOW_Z)
        input_text.scale(1.5)
        input_text.shift(-FRAME_WIDTH/4 * RIGHT + 3.25 * UP)

        output_text = TexText("Output Space", color=YELLOW_Z)
        output_text.scale(1.5)
        output_text.shift(FRAME_WIDTH/4 * RIGHT + 3.25 * UP)

        input_dot = Dot(c1.c2p(1.2, 2.3), color=PURPLE)
        input_dot.set_color(PURPLE)
        input_dot_text = Tex("z")
        input_dot_text.add_updater(
            lambda t: t.become(t.next_to(input_dot, DOWN)))

        output_dot = Dot(c2.c2p(0, 0), color=GREEN)

        def dot_updater(d):
            input_coors = c1.p2c(input_dot.get_center())
            output_coors = self.func(input_coors[0] + input_coors[1]*1j)
            return d.become(Dot(c2.c2p(output_coors.real, output_coors.imag, 0), color=GREEN))

        output_dot.add_updater(dot_updater)
        output_dot_text = Tex("f(z)")
        output_dot_text.add_updater(
            lambda t: t.become(t.next_to(output_dot, DOWN)))

        # self.add(c)
        # self.wait()

        # self.play(Transform(c, c1))

        self.add(c1, c2, input_text, output_text, input_dot,
                 output_dot, input_dot_text, output_dot_text)
        self.embed()

    def func(self, z):
        r = abs(z)
        t = PI/2 if z.real == 0 else np.arctan(z.imag/z.real)
        new_t = 3*t**2 + t + 2
        new_r = 3 * np.sin(r + 6)**2 * np.cos(3 * r + 2)
        return new_r * (np.cos(new_t) + np.sin(new_t) * 1j)


class ComplexGraph1_1(Scene):
    def construct(self):
        frame = self.camera.frame
        frame.set_phi(PI/4)
        frame.set_theta(PI/4)

        axes = ThreeDAxes()
        surf = ParametricSurface(
            self.func, u_range=(-4, 4), v_range=(-4, 4), color=PURPLE, opacity=0.75)

        self.play(Write(axes), ShowCreation(surf))
        frame.add_updater(lambda f, dt: f.increment_theta(0.2 * dt))
        self.wait(10)

        self.embed()

    def func(self, u, v):
        return [u, v, np.sin(u) * v]


class ComplexGraph1_2(Scene):
    def construct(self):
        frame = self.camera.frame
        frame.set_phi(PI/4)
        frame.set_theta(3*PI/4)

        axes = ThreeDAxes()
        surf = ParametricSurface(
            self.func, u_range=(-4, 4), v_range=(-4, 4), color=GREEN, opacity=0.75)

        self.play(Write(axes), ShowCreation(surf))
        frame.add_updater(lambda f, dt: f.increment_theta(0.2 * dt))
        self.embed()
        self.wait(10)

    def func(self, u, v):
        return [u, v, 0.5*((0.5 * v) ** 2 + (0.5 * u) ** 3)]


class ComplexGraph2(Scene):
    def construct(self):
        n = NumberPlane(background_line_style={"stroke_opacity": 0.5})
        n.axes.set_opacity(0.5)

        v = VectorField(lambda x, y: [np.cos(
            x)*np.sin(y), np.sin(y) + np.cos(x), 0], n)

        eq = Tex(r"f(x+y{i}) = \cos(x) \sin(y) + (\sin(y) + \cos(x){i}",
                 tex_to_color_map={r"{i}": BLUE})
        beq = BackgroundRectangle(eq, buff=0.2, opacity=1)

        grp = VGroup(beq, eq)
        grp.scale(1.25)
        grp.shift(3 * UP)

        self.play(Write(n))
        self.play(Write(v), Write(grp))
        self.wait()
        self.embed()


class ComplexGraph3(Scene):
    def construct(self):
        axes = ThreeDAxes()

        surf = ParametricSurface(
            lambda u, v: [u, v, abs(0.5 * (u+v*1j)**2)], u_range=(-4, 4), v_range=(-4, 4))
        surf.set_opacity(0.75)
        t_surf = TexturedSurface(surf, "img/z_squared.png")

        frame = self.camera.frame
        frame.add_updater(lambda f, dt: f.increment_theta(0.2 * dt))
        frame.set_theta(5.084)
        frame.set_phi(1.018)

        self.play(Write(axes), ShowCreation(t_surf))
        self.wait(15)


class Part1(PartScene):
    CONFIG = {
        "n": 1,
        "title": "The Real Derivative, revisited",
        "title_color": RED
    }