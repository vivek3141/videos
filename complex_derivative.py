from manimlib import *

YELLOW_Z = "#e2e1a4"

A_AQUA = "#8dd3c7"
A_YELLOW = "#ffffb3"
A_LAVENDER = "#bebada"
A_RED = "#fb8072"
A_BLUE = "#80b1d3"
A_ORANGE = "#fdb462"
A_GREEN = "#b3de69"
A_PINK = "#fccde5"
A_GREY = "#d9d9d9"
A_VIOLET = "#bc80bd"
A_UNKA = "#ccebc5"
A_UNKB = "#ffed6f"

INPUT_C = A_PINK
OUTPUT_C = A_GREEN


class PartScene(Scene):
    CONFIG = {
        "n": 1,
        "title": "",
        "title_color": RED
    }

    def construct(self):
        part = TexText(f"Part {self.n}")
        part.scale(1.5)
        part.shift(2 * UP)

        title = TexText(self.title, color=self.title_color)
        title.scale(1.5)

        self.play(Write(part))
        self.play(Write(title))
        self.wait()


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


class RealDerivative(NormalDerivative):
    LINE_COLOR = YELLOW_Z

    def construct(self):
        def check(obj):
            self.remove(obj)
            self.wait(0.5)
            self.add(obj)
        axes = Axes(x_range=(-2, 5), y_range=(0, 5))
        self.axes = axes

        func = axes.get_graph(self.func, color=BLUE)
        label = axes.get_graph_label(func, label=r"f(x)")

        line_kwargs = {
            "color": self.LINE_COLOR
        }
        dx_line_kwargs = {
            "color": INPUT_C
        }
        dy_line_kwargs = {
            "color": OUTPUT_C
        }
        eq_kwargs = {

        }
        dot_kwargs = {
            "color": self.LINE_COLOR
        }
        self.len_of_line = 2

        v = ValueTracker(1.5)
        dx = ValueTracker(1)

        def dx_line_updater(line):
            x, dx_v = v.get_value(), dx.get_value()
            p1 = axes.c2p(x, self.func(x))
            p2 = axes.c2p(x+dx_v, self.func(x))
            return line.become(Line(p1, p2, **dx_line_kwargs))

        def dy_line_updater(line):
            x, dx_v = v.get_value(), dx.get_value()
            p1 = axes.c2p(x+dx_v, self.func(x))
            p2 = axes.c2p(x+dx_v, self.func(x+dx_v))
            return line.become(Line(p1, p2, **dy_line_kwargs))

        p1, p2 = VMobject(), VMobject()
        p1.add_updater(lambda p: p.become(
            self.get_point(v.get_value(), **dot_kwargs)))
        p2.add_updater(lambda p: p.become(self.get_point(
            v.get_value() + dx.get_value(), **dot_kwargs)))

        dx_line, dy_line = VMobject(), VMobject()
        dx_line.add_updater(dx_line_updater)
        dy_line.add_updater(dy_line_updater)

        dx_text = Tex("dx", tex_to_color_map={
                      "x": INPUT_C}).next_to(dx_line, UP)
        dy_text = Tex("dy", tex_to_color_map={
                      "y": OUTPUT_C}).next_to(dy_line, RIGHT)

        eq = Tex(
            r"f'(x) = {{d}y \over {d}x}",
            isolate=["{d}", "'(x)"],
            tex_to_color_map={"x": INPUT_C, "f'": BLUE, "y": OUTPUT_C}
        )
        # isolate=["f'(x)", "{dy}", "{dx}"])

        eq.scale(1.5)
        eq.shift(2.5 * UP)

        self.play(
            Write(axes),
            Write(func),
            Write(label)
        )
        self.play(
            Write(dx_line),
            Write(dx_text),
            Write(p1)
        )
        self.wait()

        self.play(
            Write(dy_line),
            Write(dy_text),
            Write(p2)
        )
        self.wait()

        self.play(
            Write(eq)
        )

        dx_text.add_updater(lambda d: d.next_to(dx_line, UP))
        dy_text.add_updater(lambda d: d.next_to(dy_line, RIGHT))

        self.play(dx.increment_value, -1, run_time=10, rate_func=linear)
        self.wait()

        eq2 = Tex(
            "{d}y = f'(x) \cdot {d}x",
            isolate=["{d}", "'(x)"],
            tex_to_color_map={"x": INPUT_C, "f'": BLUE, "y": OUTPUT_C}
        )
        eq2.shift(2.5 * UP)
        eq2.scale(1.5)

        self.play(TransformMatchingTex(eq, eq2))
        self.wait()

        grp = VGroup(*[i for i in self.mobjects if i not in [eq2,
                     axes] and isinstance(i, VMobject)])
        self.play(Uncreate(grp))
        self.wait()

        input_line = NumberLine()
        input_line.shift(1 * UP)
        input_line.add_numbers(font_size=36)

        x_label = Tex("x", color=INPUT_C)
        x_label.move_to([-6.5, 1.5, 0])

        output_line = NumberLine()
        output_line.shift(2 * DOWN)
        output_line.add_numbers(font_size=36)

        y_label = Tex("y=f(x)", tex_to_color_map={
                      "f": BLUE, "y": OUTPUT_C, "x": INPUT_C})
        y_label.move_to([-5.75, -1.5, 0])

        input_dot, output_dot = Dot(color=INPUT_C), Dot(color=OUTPUT_C)
        output_dot.add_updater(lambda d: d.become(
            Dot(output_line.n2p(self.t_func(input_line.p2n(
                input_dot.get_center()))), color=OUTPUT_C)
        ))
        input_dot.move_to(input_line.n2p(-6))

        self.play(
            ReplacementTransform(axes.x_axis, input_line),
            ReplacementTransform(axes.y_axis, output_line)
        )
        self.play(
            ApplyMethod(eq2.shift, 0.25 * UP),
            Write(x_label),
            Write(y_label)
        )
        self.wait()

        dx = ValueTracker(1)

        dx_vec = Vector([1, 0], stroke_color=INPUT_C, stroke_width=8)
        dx_vec.move_to(input_line.n2p(1.5), aligned_edge=LEFT)
        dx_vec.add_updater(
            lambda v: v.become(
                Vector(
                    [dx.get_value(), 0], stroke_color=INPUT_C, stroke_width=8
                ).move_to(input_line.n2p(1.5), aligned_edge=LEFT)
            )
        )

        dx_label = Tex("dx", tex_to_color_map={"x": INPUT_C})
        dx_label.add_updater(lambda l: l.move_to(dx_vec, DOWN).shift(0.3 * UP))

        dy_vec = Vector([1.5 * 2 * dx.get_value(), 0],
                        stroke_color=OUTPUT_C, stroke_width=8)
        dy_vec.add_updater(
            lambda v: v.become(
                Vector(
                    [1.5*2*dx.get_value(), 0], stroke_color=OUTPUT_C, stroke_width=8
                ).move_to(output_line.n2p(1.5**2), aligned_edge=LEFT)
            )
        )

        dy_label = Tex(
            "dy = f'(x) \cdot {dx}",
            tex_to_color_map={"x": INPUT_C, "f'": BLUE, "y": OUTPUT_C}
        )
        dy_label.add_updater(lambda l: l.move_to(dy_vec, DOWN).shift(0.3 * UP))

        self.play(
            Write(dx_vec), Write(dx_label)
        )
        self.play(
            Write(dy_vec), Write(dy_label)
        )
        self.wait()

        self.play(
            dx.increment_value, -0.9, run_time=7.5, rate_func=linear
        )
        self.wait()

        self.play(
            Uncreate(dx_vec), Uncreate(dx_label),
            Uncreate(dy_vec), Uncreate(dy_label)
        )
        self.play(
            Write(input_dot),
            Write(output_dot)
        )
        self.play(
            ApplyMethod(input_dot.move_to, input_line.n2p(6)),
            run_time=5,
            rate_func=linear
        )
        self.wait()

        self.play(
            Uncreate(input_dot),
            Uncreate(output_dot)
        )
        self.wait()

        x_vals = [[x, input_line.n2p(0)[1], 0]
                  for x in np.linspace(-FRAME_WIDTH/2, FRAME_WIDTH/2, 100)]
        y_vals = [[x[0]**2, output_line.n2p(0)[1], 0] for x in x_vals]

        input_c = DotCloud(x_vals, color=INPUT_C)
        output_c = DotCloud(y_vals, color=OUTPUT_C)

        eq32 = Tex("dy = 2x \cdot {dx}", tex_to_color_map={
            "x": INPUT_C, "f'": BLUE, "y": OUTPUT_C})
        eq32.shift(2.75 * UP)
        eq32.scale(1.5)

        x_label2 = Tex("x^2", tex_to_color_map={"x": INPUT_C})
        x_label2.move_to([-6.5, 1.5, 0])

        y_label2 = Tex("y=x^2", tex_to_color_map={
                       "f": BLUE, "y": OUTPUT_C, "x": INPUT_C})
        y_label2.move_to([-6.25, -1.5, 0])

        self.play(
            Transform(eq2, eq32),
            Transform(x_label, x_label2),
            Transform(y_label, y_label2)
        )
        self.wait()

        self.play(ShowCreation(input_c))
        self.wait()

        self.play(TransformFromCopy(input_c, output_c), run_time=5)
        self.wait()

        grad = color_gradient([INPUT_C, OUTPUT_C], 10)

        lines = VGroup()

        for i in range(100):
            lines.add(Line(x_vals[i], y_vals[i], color=INPUT_C))

        lines.set_opacity(0.3)
        lines.set_color(grad)

        self.bring_to_back(lines)
        self.play(ShowCreation(lines), run_time=5)
        self.wait()

        self.embed()

    def create_vector_dot_cloud(self, points, **kwargs):
        dot_cloud = VGroup()

        for point in points:
            dot_cloud.add(Dot(point, **kwargs))

        return dot_cloud

    def get_eq(self, t, **kwargs):
        f_prime = "{:.2f}".format(round(self.deriv(t), 2))
        eq = Tex(r"{{d {y}} \over {d {x}}} = ",
                 tex_to_color_map={r"{y}": BLUE, r"{x}": YELLOW}, **kwargs)

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

    def t_func(self, x):
        return np.sin(2*x + 3) * np.cos(x**2) + 0.5*x


class IntroComplexDeriv(Scene):
    CONFIG = {
        "plane_opacity": 0.65,
        "x": 1.5,
        "y": 2,
        "vec_opacity": 0.75
    }

    def construct(self):
        complex_kwargs = {
            "background_line_style": {
                "stroke_opacity": self.plane_opacity
            }
        }
        c1 = ComplexPlane(x_range=(-3, 3), y_range=(-3, 3), **complex_kwargs)
        c1.add_coordinate_labels()
        c1.coordinate_labels.set_opacity(self.plane_opacity)
        c1.axes.set_opacity(self.plane_opacity)
        c1.shift(FRAME_WIDTH/4 * LEFT + 0.5 * DOWN)

        c2 = ComplexPlane(x_range=(-3, 3), y_range=(-3, 3), **complex_kwargs)
        c2.add_coordinate_labels()
        c2.coordinate_labels.set_opacity(self.plane_opacity)
        c2.axes.set_opacity(self.plane_opacity)
        c2.shift(FRAME_WIDTH/4 * RIGHT + 0.5 * DOWN)

        input_text = TexText("Input Space", color=YELLOW_Z)
        input_text.scale(1.5)
        input_text.shift(-FRAME_WIDTH/4 * RIGHT + 3.25 * UP)

        output_text = TexText("Output Space", color=YELLOW_Z)
        output_text.scale(1.5)
        output_text.shift(FRAME_WIDTH/4 * RIGHT + 3.25 * UP)

        input_dot = Dot(c1.c2p(self.x, self.y), color=PURPLE)
        input_dot.set_color(A_PINK)

        input_dot_text = Tex("z", color=A_PINK)
        input_dot_text.add_background_rectangle()
        input_dot_text.add_updater(
            lambda t: t.become(t.next_to(input_dot, DOWN)))

        output_dot = Dot(c2.c2p(0, 0), color=A_GREEN)

        def dot_updater(d):
            input_coors = c1.p2c(input_dot.get_center())
            output_coors = self.func(input_coors[0] + input_coors[1]*1j)
            return d.become(Dot(c2.c2p(output_coors.real, output_coors.imag, 0), color=A_GREEN))

        output_dot.add_updater(dot_updater)

        output_dot_text = Tex("f(z)", tex_to_color_map={
                              r"z": A_PINK, "f": A_GREEN})
        output_dot_text.add_background_rectangle()
        output_dot_text.add_updater(
            lambda t: t.become(t.next_to(output_dot, DOWN)))

        self.play(
            Write(c1), Write(input_text)
        )
        self.play(
            Write(c2), Write(output_text)
        )
        self.wait()

        self.play(
            Write(input_dot), Write(input_dot_text)
        )
        self.play(
            Write(output_dot), Write(output_dot_text)
        )
        self.wait()

        def path_func(t): return c1.c2p(1.5*np.sin((3*PI)/4*t), -t)
        path = ParametricCurve(path_func, t_range=(-2, 2))

        self.play(
            MoveAlongPath(input_dot, path), run_time=10, rate_func=there_and_back
        )
        self.wait()

        z = [self.x, self.y]
        z_deriv = self.f_deriv(self.x + self.y*1j)

        f_z = self.func(self.x + self.y*1j)
        f_z = [f_z.real, f_z.imag]

        img_vecs = VGroup()
        vecs = VGroup()

        for t in np.linspace(0, 2*PI, 15)[:-1]:
            z_0 = np.exp(t*1j)
            x_0, y_0 = 0.75 * z_0.real, 0.75 * z_0.imag

            f_z0 = 0.5 * z_0 * z_deriv
            f_x0, f_y0 = f_z0.real, f_z0.imag

            v_0 = self.get_vec(
                c1, [x_0, y_0], stroke_color=A_PINK, stroke_opacity=self.vec_opacity)
            f_v0 = self.get_vec(
                c2, [f_x0, f_y0], stroke_color=A_GREEN, stroke_opacity=self.vec_opacity)

            v_0.move_to(c1.c2p(*z), aligned_edge=[-x_0, -y_0, 0])
            f_v0.move_to(c2.c2p(*f_z), aligned_edge=[-f_x0, -f_y0, 0])

            vecs.add(v_0)
            img_vecs.add(f_v0)

        vecs_cp = vecs.copy()
        img_vecs_cp = img_vecs.copy()

        input_dot_text.non_time_updaters, output_dot_text.non_time_updaters = [], []

        self.bring_to_front(input_dot_text)
        self.play(Write(vecs), ApplyMethod(input_dot_text.shift, 0.5 * DOWN))
        self.bring_to_front(input_dot_text)
        self.wait()

        self.bring_to_front(output_dot_text)
        self.play(
            TransformFromCopy(vecs, img_vecs),
            ApplyMethod(output_dot_text.shift, 0.3 * DOWN),
            run_time=7
        )
        self.bring_to_front(output_dot_text)
        self.wait()

        self.play(
            Uncreate(vecs[:4]), Uncreate(vecs[5:]),
            Uncreate(img_vecs[:4]), Uncreate(img_vecs[5:]),
            ApplyMethod(vecs[4].set_opacity, 1),
            ApplyMethod(img_vecs[4].set_opacity, 1),
            ApplyMethod(output_dot_text.shift, 0.3 * UP),
            ApplyMethod(input_dot_text.shift, 0.5 * UP)
        )

        dz_label = Tex("dz", tex_to_color_map={"z": A_PINK})
        dz_label.add_background_rectangle()
        dz_label.move_to(vecs[4], UP)
        dz_label.shift(0.5 * RIGHT)

        df_label = Tex("df", tex_to_color_map={"f": A_GREEN})
        df_label.add_background_rectangle()
        df_label.move_to(img_vecs[4])
        df_label.shift(0.6 * UP)

        self.play(
            Write(dz_label), Write(df_label)
        )
        self.wait()

        eq = Tex("df = f'(z) \cdot dz", tex_to_color_map={
                 "f": A_GREEN, "z": A_PINK, "'": A_GREEN})
        eq.add_background_rectangle()
        eq.scale(1.5)
        eq.shift(2.75 * DOWN)

        cp = img_vecs[4].copy()

        self.play(Write(eq))
        self.wait()

        self.play(TransformFromCopy(vecs[4], cp), run_time=5)
        self.remove(cp)
        self.wait()

        self.bring_to_front(dz_label, input_dot_text)
        self.play(
            Write(vecs_cp), Uncreate(vecs),
            ApplyMethod(dz_label.shift, [0.5, 0.25, 0]),
            ApplyMethod(input_dot_text.shift, 0.5 * DOWN)
        )
        self.bring_to_front(dz_label, input_dot_text)
        self.wait()

        self.bring_to_front(output_dot_text, df_label)
        self.play(
            TransformFromCopy(vecs_cp, img_vecs_cp),
            Uncreate(img_vecs),
            ApplyMethod(df_label.shift, 0.1 * UP),
            ApplyMethod(output_dot_text.shift, 0.3 * DOWN),
            run_time=5
        )
        self.bring_to_front(output_dot_text, df_label)
        self.wait()

        eq2 = Tex(
            r"f'(z) = 1.15 e^{\frac{2 \pi}{5} i}",
            tex_to_color_map={
                "f'": A_GREEN,
                "z": A_PINK,
                r"\frac{2 \pi}{5}": YELLOW_Z,
                "1.15": YELLOW_Z}
        )
        eq2.scale(1.5)
        eq2.add_background_rectangle()
        eq2.shift(2.75 * DOWN)

        self.play(
            ApplyMethod(eq.shift, 1.25 * UP),
            Write(eq2)
        )
        self.wait()

        eq3 = Tex(
            "f'(z) = 0.38 - 1.09i",
            tex_to_color_map={
                "f'": A_GREEN, "z": A_PINK,
                "0.38": YELLOW_Z, "1.09": YELLOW_Z}
        )
        eq3.add_background_rectangle()
        eq3.scale(1.5)
        eq3.shift(2.75 * DOWN)

        self.play(
            Transform(eq2, eq3)
        )
        self.wait()

        self.play(Uncreate(eq2), ApplyMethod(eq.shift, 1.25 * DOWN))
        self.wait()

        img_vecs2 = VGroup()

        f_M = np.array([
            [1/2, -np.sqrt(3)],
            [np.sqrt(3)/2, 1]
        ])

        for t in np.linspace(0, 2*PI, 15)[:-1]:
            z_0 = np.exp(t*1j)
            x_0, y_0 = 0.75 * z_0.real, 0.75 * z_0.imag

            f_z0 = np.dot(f_M, np.array([[x_0], [y_0]]))
            f_x0, f_y0 = f_z0[0][0], f_z0[1][0]

            f_v0 = self.get_vec(
                c2, [f_x0, f_y0], stroke_color=A_GREEN, stroke_opacity=self.vec_opacity)

            f_v0.move_to(c2.c2p(1, 1), aligned_edge=[-f_x0, -f_y0, 0])

            img_vecs2.add(f_v0)

        output_dot.non_time_updaters = []

        eq_g = Tex("dg = g'(z) \cdot dz", tex_to_color_map={
            "g": A_GREEN, "z": A_PINK, "'": A_GREEN})
        eq_g.add_background_rectangle()
        eq_g.scale(1.5)
        eq_g.shift(2.75 * DOWN)

        g_dot_text = Tex("g(z)", tex_to_color_map={
            r"z": A_PINK, "g": A_GREEN})
        g_dot_text.add_background_rectangle()
        g_dot_text.move_to(
            output_dot_text.get_center() + c2.c2p(1, 1) - c2.c2p(*f_z) + 0.4 * DOWN
        )

        dg_label = Tex("dg", tex_to_color_map={"g": A_GREEN})
        dg_label.add_background_rectangle()
        dg_label.move_to(
            df_label.get_center() + c2.c2p(1, 1) - c2.c2p(*f_z) + 0.3 * UP
        )

        self.play(
            Uncreate(img_vecs_cp),
            ApplyMethod(output_dot.move_to, c2.c2p(1, 1)),
            Transform(output_dot_text, g_dot_text),
            Transform(df_label, dg_label),
            Transform(eq, eq_g)
        )
        self.wait(0.5)

        self.play(
            TransformFromCopy(vecs_cp, img_vecs2), run_time=5
        )
        self.wait()

        self.play(
            Indicate(vecs_cp[0], scale_factor=2),
            Indicate(img_vecs2[0], scale_factor=2),
            run_time=3
        )
        self.wait()

        self.play(
            Indicate(vecs_cp[4], scale_factor=2),
            Indicate(img_vecs2[4], scale_factor=2),
            run_time=3
        )
        self.wait()

        self.embed()

    def get_vec(self, plane, coors, **kwargs):
        x, y = coors[0], coors[1]
        z = plane.c2p(x, y)
        return Arrow(plane.c2p(0, 0), z, buff=0, **kwargs)

    def f_deriv(self, z, dz=1e-6+1e-6*1j):
        return (self.func(z+dz)-self.func(z))/dz

    def func(self, z):
        return (1*z + np.sin(z)) * 0.3 - 1
        r = abs(z)
        t = PI/2 if z.real == 0 else np.arctan(z.imag/z.real)
        new_t = 3*t**2 + t + 2
        new_r = 3 * np.sin(r + 6)**2 * np.cos(3 * r + 2)
        return new_r * (np.cos(new_t) + np.sin(new_t) * 1j)


class ComplexMul(Scene):
    def construct(self):
        plane = ComplexPlane(faded_line_ratio=2, background_line_style={
                             "stroke_opacity": 0.65})
        plane.axes.set_opacity(0.65)
        plane.add_coordinate_labels()

        v_0 = 0.7 * np.array([3, 1, 0])
        v0 = 0.7 * (3 + 1j)
        theta1 = np.arctan2(1, 3)

        w_0 = 0.7 * np.array([-2, 2, 0])
        w0 = 0.7 * (-2 + 2j)
        theta2 = np.arctan2(2, -2)

        v = Line(ORIGIN, v_0, color=A_GREEN)
        v_dot = Dot(v_0, color=A_GREEN)
        angle1 = Arc(0, theta1, color=A_YELLOW)

        v_label = Tex("z", color=A_GREEN)
        v_label.add_background_rectangle()
        v_label.move_to(v, v_0)
        v_label.shift([0.45, 0.15, 0])

        w = Line(ORIGIN, w_0, color=A_VIOLET)
        w_dot = Dot(w_0, color=A_VIOLET)
        angle2 = Arc(0, theta2, radius=0.75, color=A_YELLOW)

        w_label = Tex("w", color=A_VIOLET)
        w_label.add_background_rectangle()
        w_label.move_to(w, w_0)
        w_label.shift([-0.5, 0.5, 0])

        r1_label = Tex("r_1", color=A_GREEN)
        r1_label.add_background_rectangle()
        r1_label.move_to(v, UP)
        r1_label.shift([0.3, 0.3, 0])

        r2_label = Tex("r_2", color=A_VIOLET)
        r2_label.add_background_rectangle()
        r2_label.move_to(w, UP)

        eq1 = Tex(r"z = r_1 e^{i \theta_1}", tex_to_color_map={
                  "z": A_GREEN, "r_1": A_GREEN, r"\theta_1": A_YELLOW})
        eq1.add_background_rectangle()
        eq1.scale(1.5)
        eq1.move_to([-FRAME_WIDTH/4, -4/3, 0])

        eq2 = Tex(r"w = r_2 e^{i \theta_2}", tex_to_color_map={
                  "w": A_VIOLET, "r_2": A_VIOLET, r"\theta_2": A_YELLOW})
        eq2.add_background_rectangle()
        eq2.scale(1.5)
        eq2.move_to([-FRAME_WIDTH/4, -8/3, 0])

        eq3 = Tex(
            r"z \cdot w = r_1 r_2 e^{i (\theta_1 + \theta_2)}",
            tex_to_color_map={
                "z": A_GREEN,
                "r_1": A_GREEN,
                "w": A_VIOLET,
                "r_2": A_VIOLET,
                r"\theta_1": A_YELLOW,
                r"\theta_2": A_YELLOW
            })
        eq3.add_background_rectangle()
        eq3.scale(1.5)
        eq3.move_to([FRAME_WIDTH/4, -2, 0])

        t1_label = Tex(r"\theta_1", color=A_YELLOW)
        t1_label.add_background_rectangle()
        t1_label.move_to(angle1)
        t1_label.shift(0.5 * RIGHT)

        t2_label = Tex(r"\theta_2", color=A_YELLOW)
        t2_label.add_background_rectangle()
        t2_label.shift(1.25 * UP)

        v0 = 2.1 + 0.7 * 1j
        w0 = -1.4 + 1.4 * 1j
        vw0 = v0 * w0

        vw = Line(ORIGIN, [-3.92, 1.96, 0], color=A_AQUA)
        vw_dot = Dot([-3.92, 1.96, 0], color=A_AQUA)

        vw_label = Tex("z \cdot w", tex_to_color_map={
                       "z": A_GREEN, "w": A_VIOLET})
        vw_label.add_background_rectangle()
        vw_label.move_to(vw, [-3.92, 1.96, 0])
        vw_label.shift(0.3 * np.array([-3.92, 1.96, 0]))

        dtheta = Arc(theta2, theta1, color=A_RED, radius=0.75)

        self.play(Write(plane))
        self.play(
            Write(v), Write(v_label), Write(v_dot),
            Write(w), Write(w_label), Write(w_dot)
        )
        self.wait()

        self.play(
            Write(eq1), Write(r1_label),
            Write(angle1), Write(t1_label)
        )
        self.wait()

        self.play(
            Write(eq2), Write(r2_label),
            Write(angle2), Write(t2_label)
        )
        self.wait()

        self.play(
            Write(eq3)
        )
        self.wait()

        self.play(
            TransformFromCopy(angle1, dtheta)
        )
        self.play(
            Write(vw), Write(vw_dot), Write(vw_label)
        )
        self.wait()


class Holomorphic(Scene):
    CONFIG = {
        "plane_opacity": 0.65,
        "x": 0.7,
        "y": 2,
        "vec_opacity": 0.75
    }

    def construct(self):
        complex_kwargs = {
            "background_line_style": {
                "stroke_opacity": self.plane_opacity
            }
        }
        c1 = ComplexPlane(x_range=(-3, 3), y_range=(0, 3), **complex_kwargs)
        c1.add_coordinate_labels()
        c1.coordinate_labels.set_opacity(self.plane_opacity)
        c1.axes.set_opacity(self.plane_opacity)
        c1.shift(FRAME_WIDTH/4 * LEFT + 0.5 * DOWN)

        c2 = ComplexPlane(x_range=(-3, 3), y_range=(0, 3), **complex_kwargs)
        c2.add_coordinate_labels()
        c2.coordinate_labels.set_opacity(self.plane_opacity)
        c2.axes.set_opacity(self.plane_opacity)
        c2.shift(FRAME_WIDTH/4 * RIGHT + 0.5 * DOWN)

        input_dot = Dot(c1.c2p(self.x, self.y), color=PURPLE)
        input_dot.set_color(A_PINK)

        input_dot_text = Tex("z", color=A_PINK)
        input_dot_text.add_background_rectangle()
        input_dot_text.next_to(input_dot, DOWN)
        input_dot_text.shift(0.5 * DOWN)

        f_z = self.func(self.x + self.y * 1j)
        f_z = np.array([f_z.real, f_z.imag, 0])

        output_dot = Dot(c2.c2p(*f_z), color=A_GREEN)
        output_dot_text = Tex("f(z)", tex_to_color_map={
                              r"z": A_PINK, "f": A_GREEN})
        output_dot_text.add_background_rectangle()
        output_dot_text.next_to(output_dot, DOWN)

        z = [self.x, self.y]
        z_deriv = self.f_deriv(self.x + self.y*1j)

        f_z = self.func(self.x + self.y*1j)
        f_z = [f_z.real, f_z.imag]

        img_vecs = VGroup()
        vecs = VGroup()

        for t in np.linspace(0, 2*PI, 15)[:-1]:
            z_0 = np.exp(t*1j)
            x_0, y_0 = 0.75 * z_0.real, 0.75 * z_0.imag

            f_z0 = 0.5 * z_0 * z_deriv
            f_x0, f_y0 = f_z0.real, f_z0.imag

            v_0 = self.get_vec(
                c1, [x_0, y_0], stroke_color=A_PINK, stroke_opacity=self.vec_opacity)
            f_v0 = self.get_vec(
                c2, [f_x0, f_y0], stroke_color=A_GREEN, stroke_opacity=self.vec_opacity)

            v_0.move_to(c1.c2p(*z), aligned_edge=[-x_0, -y_0, 0])
            f_v0.move_to(c2.c2p(*f_z), aligned_edge=[-f_x0, -f_y0, 0])

            vecs.add(v_0)
            img_vecs.add(f_v0)

        grp = VGroup(
            c1, c2, input_dot, vecs, output_dot, img_vecs, input_dot_text,
            output_dot_text,
        )
        grp.shift(DOWN)

        eq = Tex("f(z) = e^z", tex_to_color_map={
                 "f": A_GREEN, "z": A_PINK, "e": YELLOW_Z})
        eq.scale(1.5)
        eq.shift(UP)

        text1 = TexText("Complex Differentiable", color=A_GREY)
        text1.scale(1.5)
        text1.move_to(2.5 * UP + 3 * LEFT)

        text2 = TexText("Holomorphic", color=A_GREY)
        text2.scale(1.5)
        text2.move_to(2.5 * UP + 4.5 * RIGHT)

        d = Line(ORIGIN, RIGHT, color=RED, stroke_width=6)
        d.add_tip()
        d.add_tip(at_start=True)
        d.move_to(2.5 * UP + 1.55 * RIGHT)

        self.play(
            Write(text1)
        )
        self.play(
            Write(d), Write(text2)
        )
        self.wait()

        self.play(
            Write(eq)
        )
        self.play(
            Write(c1), Write(c2), Write(input_dot), Write(input_dot_text),
            Write(output_dot), Write(output_dot_text), Write(vecs)
        )
        self.play(
            TransformFromCopy(vecs, img_vecs),
            ApplyMethod(output_dot_text.shift, 0.8 * DOWN),
            run_time=5
        )
        self.wait()

        self.embed()

    def get_vec(self, plane, coors, **kwargs):
        x, y = coors[0], coors[1]
        z = plane.c2p(x, y)
        return Arrow(plane.c2p(0, 0), z, buff=0, **kwargs)

    def f_deriv(self, z, dz=1e-6+1e-6*1j):
        return (self.func(z+dz)-self.func(z))/dz

    def func(self, z):
        return np.exp(z)


class IntroTransformVis(Scene):
    def construct(self):
        n = ComplexPlane()
        n.add_coordinate_labels()

        self.play(Write(n))
        self.wait()

        self.play(Uncreate(n.coordinate_labels))

        n.prepare_for_nonlinear_transform()

        self.play(ApplyMethod(
            n.apply_complex_function,
            self.func),
            run_time=7
        )
        self.wait()

        self.embed()

    def func(self, z):
        return (1*z + np.sin(z)) * 0.3


class TransformationVisual(Scene):
    def construct(self):
        n, _n = ComplexPlane(), ComplexPlane()
        n.add_coordinate_labels()

        _n.apply_complex_function(self.func1)
        _n.add_coordinate_labels()
        _n.coordinate_labels[:10].shift(0.1 * np.array([-np.sqrt(3), 1, 0]))

        eq = Tex(
            r"f(z) = (1 + \sqrt{3} i) z",
            tex_to_color_map={"f": A_GREEN, "z": A_PINK,
                              "1": YELLOW_Z, r"\sqrt{3}": YELLOW_Z}
        )

        eq.add_background_rectangle(buff=0.25)
        eq.scale(1.5)
        eq.shift(3 * UP)

        d = Dot(RIGHT, color=RED)

        d_lbl = Tex("0 + i", color=A_RED)
        d_lbl.add_background_rectangle(buff=0.15)
        d_lbl.next_to(d, DOWN)

        d2 = Dot([1, np.sqrt(3), 0], color=RED)

        d_lbl2 = Tex(r"1 + \sqrt{3}i", color=A_RED)
        d_lbl2.add_background_rectangle(buff=0.15)
        d_lbl2.next_to(d2, DOWN)

        self.play(Write(n), Write(eq))
        self.play(Write(d), Write(d_lbl))
        self.wait()

        self.play(Uncreate(n.coordinate_labels))
        self.bring_to_back(n)
        self.play(
            ApplyMethod(n.apply_complex_function, self.func1,
                        foreground_mobjects=[eq]),
            Transform(d, d2),
            Transform(d_lbl, d_lbl2),
            run_time=7
        )
        self.bring_to_back(n)
        self.play(Write(_n.coordinate_labels))
        self.bring_to_back(n, _n.coordinate_labels)
        self.wait()

        eq2 = Tex(r"f(z) = (2e^{\frac{\pi}{3}i}) z",
                  tex_to_color_map={"f": A_GREEN, "z": A_PINK,
                                    "2": YELLOW_Z, r"\frac{\pi}{3}": YELLOW_Z}
                  )
        eq2.scale(1.5)
        eq2.shift(3 * UP)
        eq2.add_background_rectangle()

        self.play(Transform(eq, eq2))
        self.wait()

        n2 = ComplexPlane()

        eq3 = Tex(
            r"f(z) = z^2",
            tex_to_color_map={"f": A_GREEN, "z": A_PINK}
        )
        eq3.scale(1.5)
        eq3.shift(3 * UP)
        eq3.add_background_rectangle()

        self.bring_to_back(n)
        self.play(
            Uncreate(_n.coordinate_labels),
            Uncreate(d), Uncreate(d_lbl),
            Transform(eq, eq3),
            Transform(n, n2)
        )
        self.bring_to_back(n)

        def g(z): return z**2

        n.prepare_for_nonlinear_transform()

        d1 = Dot([1, 0, 0], color=RED)
        d1_c = d1.copy()

        d1_lbl = Tex("1", color=RED)
        d1_lbl.add_background_rectangle(buff=0.15)
        d1_lbl.next_to(d1, DOWN)
        d1_lbl_c = d1_lbl.copy()

        d2 = Dot([0, 1, 0], color=RED)
        d2_c = d2.copy()

        d2_lbl = Tex("i", color=RED)
        d2_lbl.add_background_rectangle(buff=0.15)
        d2_lbl.next_to(d2, DOWN)
        d2_lbl_c = d2_lbl.copy()

        d3 = Dot([2, 0, 0], color=RED)
        d3_c = d3.copy()

        d3_lbl = Tex("2", color=RED)
        d3_lbl.add_background_rectangle(buff=0.15)
        d3_lbl.next_to(d3, DOWN)
        d3_lbl_c = d3_lbl.copy()

        d1_n = Dot([1, 0, 0], color=RED)
        d1_n_lbl = Tex("1", color=RED)
        d1_n_lbl.add_background_rectangle(buff=0.15)
        d1_n_lbl.next_to(d1_n, DOWN)

        d2_n = Dot([-1, 0, 0], color=RED)
        d2_n_lbl = Tex("-1", color=RED)
        d2_n_lbl.add_background_rectangle(buff=0.15)
        d2_n_lbl.next_to(d2_n, DOWN)

        d3_n = Dot([4, 0, 0], color=RED)
        d3_n_lbl = Tex("4", color=RED)
        d3_n_lbl.add_background_rectangle(buff=0.15)
        d3_n_lbl.next_to(d3_n, DOWN)

        self.play(
            Write(d1), Write(d1_lbl),
            Write(d2), Write(d2_lbl),
            Write(d3), Write(d3_lbl)
        )
        self.wait()
        self.bring_to_back(n)

        self.play(
            ApplyMethod(n.apply_complex_function, g),
            Transform(d1, d1_n), Transform(d1_lbl, d1_n_lbl),
            Transform(d2, d2_n), Transform(d2_lbl, d2_n_lbl),
            Transform(d3, d3_n), Transform(d3_lbl, d3_n_lbl),
            run_time=7
        )
        self.bring_to_back(n)

        n_ = ComplexPlane()

        self.play(
            Transform(n, n_),
            Transform(d1, d1_c), Transform(d1_lbl, d1_lbl_c),
            Transform(d2, d2_c), Transform(d2_lbl, d2_lbl_c),
            Transform(d3, d3_c), Transform(d3_lbl, d3_lbl_c),
            run_time=3
        )
        self.bring_to_back(n)
        self.wait(2)

        self.play(
            ApplyMethod(n.apply_complex_function, g),
            Transform(d1, d1_n), Transform(d1_lbl, d1_n_lbl),
            Transform(d2, d2_n), Transform(d2_lbl, d2_n_lbl),
            Transform(d3, d3_n), Transform(d3_lbl, d3_n_lbl),
            run_time=5
        )
        self.bring_to_back(n)
        self.wait()

        self.play(
            Transform(n, n_),
            Uncreate(d1), Uncreate(d1_lbl),
            Uncreate(d2), Uncreate(d2_lbl),
            Uncreate(d3), Uncreate(d3_lbl),
            run_time=2
        )
        self.wait(0.5)

        r = Rectangle(height=3, width=4, fill_color=BLACK,
                      fill_opacity=1, stroke_color=A_ORANGE)
        r.move_to([4, 2, 0])

        eq4 = Tex(r"f'(z) = 2z", tex_to_color_map={
                  r"f'": A_GREEN, "z": A_PINK})
        eq4.move_to([-5.5, 2.5, 0])

        br2 = Rectangle(height=2, width=12, fill_opacity=0.75, color=BLACK)
        br2.move_to([-5, 3, 0])

        br = Rectangle(height=2, width=3, fill_opacity=0.75, color=BLACK)
        br.move_to([-5.5, 3, 0])

        z_rect = Rectangle(height=0.2, width=0.2, color=A_ORANGE)
        z_rect.move_to([-1, 2, 0])

        f_rect = Rectangle(height=0.2, width=0.2, color=A_ORANGE)
        f_rect.move_to([-3, -4, 0])

        obj = VMobject()
        for i in eq:
            if i is not eq.background_rectangle:
                obj.add(i)

        eq5 = Tex(
            r"f(-1+2i) = -3-4i",
            tex_to_color_map={
                "1": YELLOW_Z, "2": YELLOW_Z,
                "3": YELLOW_Z, "4": YELLOW_Z,
                "f": A_GREEN}
        )
        eq5.move_to([-1.5, 3.5, 0])

        eq6 = Tex(
            r"f'(-1+2i) = -2+4i",
            tex_to_color_map={
                "1": YELLOW_Z, "2": YELLOW_Z,
                "4": YELLOW_Z, "f'": A_GREEN
            }
        )
        eq6.move_to([-1.5, 2.5, 0])

        z_lbl = Tex("-1+2i", color=A_ORANGE)
        z_lbl.add_background_rectangle(buff=0.15)
        z_lbl.next_to(z_rect, LEFT + DOWN)

        z_lbl2 = Tex("-3-4i", color=A_ORANGE)
        z_lbl2.add_background_rectangle(buff=0.15)
        z_lbl2.next_to(f_rect, LEFT + UP)

        z_rect_points = z_rect.get_vertices()
        f_rect_points = f_rect.get_vertices()
        r_points = deepcopy(r.get_vertices())

        dash_1 = DashedLine(z_rect_points[0], r_points[1])
        dash_2 = DashedLine(z_rect_points[3], r_points[2])

        dash_1f = DashedLine(f_rect_points[0], r_points[1])
        dash_2f = DashedLine(f_rect_points[3], r_points[2])

        self.play(
            Write(br),
            ApplyMethod(obj.scale, 1/1.5),
            Uncreate(eq.background_rectangle)
        )
        self.bring_to_front(eq)

        self.play(
            ApplyMethod(eq.move_to, 5.5 * LEFT + 3.5 * UP),
            Write(eq4)
        )

        self.play(
            Write(r),
            Write(z_rect),
            Write(dash_1), Write(dash_2)
        )

        self.play(Write(z_lbl))
        self.bring_to_front(br)
        self.bring_to_front(eq, eq4)
        self.wait()

        self.play(Transform(br, br2))
        self.play(
            Write(eq5), Write(eq6),
        )
        self.wait()

        self.play(
            ApplyMethod(n.apply_complex_function, g),
            Transform(z_rect, f_rect),
            Transform(z_lbl, z_lbl2),
            Transform(dash_1, dash_1f), Transform(dash_2, dash_2f),
            run_time=10
        )
        self.wait()

        eq7 = Tex(
            r"f(1+i) = 2i",
            tex_to_color_map={
                "1": YELLOW_Z, "2": YELLOW_Z,
                "f": A_GREEN}
        )
        eq7.move_to([-1.5, 3.5, 0])

        eq8 = Tex(
            r"f'(1+i) = 2+2i",
            tex_to_color_map={
                "1": YELLOW_Z, "2": YELLOW_Z,
                "f'": A_GREEN
            }
        )
        eq8.move_to([-1.5, 2.5, 0])

        z_rect2 = Rectangle(height=0.2, width=0.2, color=A_ORANGE)
        z_rect2.move_to([1, 1, 0])
        z_rect_points2 = z_rect2.get_vertices()

        f_rect2 = Rectangle(height=0.2, width=0.2, color=A_ORANGE)
        f_rect2.move_to([0, 2, 0])
        f_rect_points2 = f_rect2.get_vertices()

        dash1_2 = DashedLine(z_rect_points2[0], r_points[1])
        dash2_2 = DashedLine(z_rect_points2[3], r_points[2])

        dash1f_2 = DashedLine(f_rect_points2[0], r_points[1])
        dash2f_2 = DashedLine(f_rect_points2[3], r_points[2])

        z2_lbl = Tex("1+i", color=A_ORANGE)
        z2_lbl.add_background_rectangle(buff=0.15)
        z2_lbl.next_to(z_rect2, LEFT + DOWN)

        z2_lbl2 = Tex("2i", color=A_ORANGE)
        z2_lbl2.add_background_rectangle(buff=0.15)
        z2_lbl2.next_to(f_rect2, LEFT + DOWN)

        self.play(
            Transform(n, n_),
            Transform(dash_1, dash1_2),
            Transform(dash_2, dash2_2),
            Transform(z_rect, z_rect2),
            Transform(eq5, eq7),
            Transform(eq6, eq8),
            Transform(z_lbl, z2_lbl),
            run_time=2
        )
        self.wait()

        self.play(
            ApplyMethod(n.apply_complex_function, g),
            Transform(z_rect, f_rect2),
            Transform(z_lbl, z2_lbl2),
            Transform(dash_1, dash1f_2), Transform(dash_2, dash2f_2),
            run_time=10
        )

        self.embed()

    def func1(self, z):
        return (1+np.sqrt(3)*1j)*z
