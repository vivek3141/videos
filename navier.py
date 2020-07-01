from manimlib.imports import *

color_map = {
    r"{u}": BLUE,
    r"\rho": YELLOW,
    r"{p}": RED,
    r"\mu": GOLD,
    r"{g}": GOLD
}


class NumberedList(BulletedList):
    CONFIG = {
        "dot_scale_factor": 1,
        "num_color": BLUE,
    }

    def __init__(self, *items, **kwargs):
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)
        for num, part in enumerate(self):
            dot = TexMobject(f"{num+1})", color=self.dot_color,
                             tex_to_color_map={f"{num+1}": self.num_color}).scale(
                self.dot_scale_factor)
            dot.next_to(part[0], LEFT, MED_SMALL_BUFF)
            part.add_to_back(dot)
        self.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=self.buff
        )


class Intro(Scene):
    def construct(self):
        v = VGroup(
            *[Vector([0, 1, 0], color=PURPLE).shift([x, y, 0])
              for x in np.arange(-9, 8, 0.75)
              for y in np.arange(-4, 4, 1.5)])
        self.play(Write(v))
        self.wait()


class Equations(Scene):
    def construct(self):
        eq1 = TexMobject(r"\nabla \cdot {u} = 0", tex_to_color_map=color_map)
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(
            r"\rho {{d {u} } \over {d {t} }} = -\nabla {p} + \mu \nabla^2 {u} + \textbf{F}", tex_to_color_map=color_map)
        eq2.scale(1.5)
        eq2.shift(1 * DOWN)

        title = Text("Navier-Stokes Equations", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait()


class MilleniumPrize(Scene):
    def construct(self):
        title = Text(
            "Millenium Prize Problems", color=PURPLE)
        title.scale(1.25)
        title.shift(3 * UP)

        l = NumberedList(
            *"""Yang–Mills and Mass Gap
Riemann Hypothesis
P vs NP Problem
Existence and smoothness of the Navier-Stokes equation
Hodge Conjecture
Poincare Conjecture
Birch and Swinnerton-Dyer Conjecture""".split("\n")
        )
        l.scale(0.75)
        l.shift(0.5 * DOWN)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        self.play(l.fade_all_but, 3)
        self.wait()


class ApplicationsOne(Scene):
    def construct(self):
        rect1 = ScreenRectangle(height=3.5)
        rect2 = ScreenRectangle(height=3.5)
        rect3 = ScreenRectangle(height=3.5)

        rect1.shift(2 * UP + 3.5 * LEFT)
        rect2.shift(2 * UP + 3.5 * RIGHT)
        rect3.shift(2 * DOWN)

        self.play(Write(rect1))
        self.wait()

        self.play(Write(rect2))
        self.wait()

        self.play(Write(rect3))
        self.wait()


class Assumptions(Scene):
    def construct(self):
        title = Text(
            "Assumptions for this video", color=PURPLE)
        title.scale(1.25)
        title.shift(3 * UP)

        l = BulletedList("Newtonian", "Incompressible",
                         "Isothermal", dot_color=BLUE, buff=0.75*LARGE_BUFF)
        l.scale(1.5)
        l.shift(0.25*DOWN)

        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        self.play(l.fade_all_but, 0)
        self.wait()

        self.play(l.fade_all_but, 1)
        self.wait()

        self.play(l.fade_all_but, 2)
        self.wait()


class Newtonian(Scene):
    def construct(self):
        title = Text("Newtonian Fluid", color=GOLD)
        title.scale(1.5)
        title.shift(3.25 * UP)

        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        f1 = FunctionGraph(self.f1, x_min=0, x_max=6, color=TEAL)
        f2 = FunctionGraph(self.f2, x_min=1/25, x_max=6, color=RED)

        xlbl = Text("Shear Rate")
        xlbl.shift(3 * DOWN)

        grpp = VGroup(axes, f1, f2)
        grpp.center()

        f2.shift(2.75 * LEFT)

        grp = VGroup(axes, f1)

        ylbl = Text("Viscosity")
        ylbl.rotate(PI/2)
        ylbl.shift(3.5 * LEFT + 0 * UP)

        grp1 = VGroup(grp, xlbl, ylbl)
        grp1.shift(0.25 * DOWN)

        lbl1 = Text("Newtonian", color=TEAL)
        lbl1.scale(0.75)
        lbl1.move_to(f1, RIGHT)
        lbl1.shift(3 * LEFT + 0.5 * UP)

        lbl2 = Text("Non-Newtonian", color=RED)
        lbl2.scale(0.75)
        lbl2.shift(1.5 * DOWN + 1 * LEFT)

        self.play(FadeInFromDown(title))
        self.play(Write(axes), FadeInFromDown(xlbl), FadeInFromDown(ylbl))
        self.play(Write(f1), FadeInFromDown(lbl1))
        self.wait()

        self.play(grp1.shift, 2.75 * LEFT)

        rect = ScreenRectangle(height=5, aspect_ratio=1)
        rect.shift(3.75 * RIGHT + 0.15 * DOWN)

        self.play(Write(rect))
        self.bring_to_back(f2)
        self.play(Write(f2), FadeInFromDown(lbl2))
        self.wait()

    @staticmethod
    def f1(x):
        return 3

    @staticmethod
    def f2(x):
        return x ** (-0.5)


class Incompressible(Scene):
    def construct(self):
        title = Text("Incompressible", color=PURPLE)
        title.scale(1.5)
        title.shift(3.25 * UP)

        self.play(FadeInFromDown(title))

        s_width = 8

        obj = VGroup(
            *[*[
                Line([i, 2, 0], [i, -2, 0], stroke_width=s_width)
                for i in [2, -2]
            ],
                Line([-2, -2, 0], [2, -2, 0], stroke_width=s_width)
            ]
        )

        t = ValueTracker(1)

        obj2 = VGroup(
            *[
                Line([-2, 1, 0], [2, 1, 0], stroke_width=s_width),
                Line([0, 1, 0], [0, 2, 0], stroke_width=s_width),
                Rectangle(height=0.25, width=0.75, fill_opacity=1,
                          color=YELLOW, stroke_width=s_width).shift([0, 2, 0])
            ]
        )

        t2 = ValueTracker(1)
        water = Polygon(
            [-2, t.get_value(), 0],
            [2, t.get_value(), 0],
            [2, -2, 0],
            [-2, -2, 0],
            color=BLUE_E, fill_opacity=1)

        def update_vgroup(grp):
            grp.move_to(water, UP)
            grp.shift(1.125 * UP)

        obj2.add_updater(update_vgroup)

        def update_func_water(water):
            water2 = Polygon(
                [-2, t.get_value(), 0],
                [2, t.get_value(), 0],
                [2, -2, 0],
                [-2, -2, 0],
                color=BLUE_E, fill_opacity=1)
            water.become(water2)

        water.add_updater(update_func_water)

        self.play(Write(water), Write(obj), Write(obj2))
        self.play(t.increment_value, -1, rate_func=there_and_back)
        self.wait()

        self.play(t.increment_value, -1, rate_func=there_and_back)
        self.wait()


class Isothermal(Scene):
    def construct(self):
        title = Text("Incompressible", color=ORANGE)
        title.scale(1.5)
        title.shift(3.25 * UP)

        rect = ScreenRectangle(height=5).shift(0.15 * DOWN)

        self.play(FadeInFromDown(title))
        self.play(Write(rect))
        self.wait()


class Divergence(Scene):
    def construct(self):
        eq1 = TexMobject(r"\nabla", r"\cdot",
                         r"{u}", r"=", r"0", tex_to_color_map=color_map)
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(
            r"\rho {{d {u} } \over {d {t} }} = -\nabla {p} + \mu \nabla^2 {u} + \textbf{F}", tex_to_color_map=color_map)
        eq2.scale(1.5)
        eq2.shift(1 * DOWN)

        title = Text("Navier-Stokes Equations", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        self.add(title, eq1, eq2)
        self.wait()

        self.play(Uncreate(title), Uncreate(eq2), ApplyMethod(eq1.center))
        self.play(eq1.scale, 1.5)

        self.play(*[ApplyMethod(eq1[i].move_to, [(i-2) * 2, 0, 0])
                    for i in range(5)])
        self.wait()

        b1 = Brace(eq1[:2])
        t1 = b1.get_text("Divergence")
        b2 = Brace(eq1[2], direction=UP)
        t2 = b2.get_text("Velocity Vector Field")

        self.play(Write(VGroup(b1, t1)))
        self.play(Write(VGroup(b2, t2)))
        self.wait()


class VectorFieldDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.set_opacity(0.5)
        plane.add(plane.get_axis_labels())

        field1 = VectorField(
            lambda t: 1.5*np.array([np.cos(t[0]), np.sin(t[1]), 0])
        )

        title = Text("Vector Field")
        title.scale(2)
        title.to_edge(UP)
        title.add_background_rectangle()

        self.play(ShowCreation(plane))
        self.play(ShowCreation(field1))
        self.play(Write(title))
        self.wait()


class DivergenceDemo(Scene):
    def construct(self):
        field = VectorField(
            lambda t: t/3
        )

        title = TexMobject(r"\text{div} \vec{\text{F}} > 0", tex_to_color_map={
                           r"\text{div}": YELLOW})
        title.scale(2)
        title.to_edge(UP)
        title.add_background_rectangle()

        self.play(Write(field))
        self.wait()

        self.play(Write(title))
        self.wait()

        field2 = VectorField(
            lambda t: -t/3
        )

        title2 = TexMobject(r"\text{div} \vec{\text{F}} < 0", tex_to_color_map={
            r"\text{div}": YELLOW})
        title2.scale(2)
        title2.to_edge(UP)
        title2.add_background_rectangle()

        self.play(Transform(field, field2), Transform(title, title2))
        self.wait()


class DivergenceEq(Scene):
    def construct(self):
        eq = TexMobject(
            r"""
        \text{div} \vec{\text{F}} = \nabla \cdot \vec{\text{F}} = 
        \begin{bmatrix}
        \frac{\partial}{\partial x} \\
        \frac{\partial}{\partial y} \\
        \frac{\partial}{\partial z} \\
        \end{bmatrix} \cdot \vec{\text{F}}
        """, tex_to_color_map={
                r"\text{div}": YELLOW, r"\nabla": RED}
        )
        eq.scale(2)

        self.play(Write(eq))
        self.wait()


class SecondEq(Scene):
    def construct(self):
        eq1 = TexMobject(r"\nabla", r"\cdot",
                         r"{u}", r"=", r"0", tex_to_color_map=color_map)
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(
            r"\rho {{d {u} } \over {d {t} }} = ", r"-\nabla {p}", r" + ", r"\mu \nabla^2 {u}", r" + ", r"\textbf{F}", tex_to_color_map=color_map)
        eq2.scale(1.5)
        eq2.shift(1 * DOWN)

        title = Text("Navier-Stokes Equations",
                     color=GREEN, font='Berlin Sans FB')
        title.scale(1.5)
        title.shift(3 * UP)

        self.add(title, eq1, eq2)
        self.wait()

        eq3 = TexMobject(r"\text{m}", r"{a}", r"=", r"\Sigma F", tex_to_color_map={
                         r"F": YELLOW, r"{a}": GREEN, })
        eq3.scale(1.5)
        eq3.shift(1.5 * UP + 2.07 * LEFT)

        self.play(Uncreate(title), Uncreate(eq1))
        self.play(ApplyMethod(eq2.shift, 0.5 * DOWN), Write(eq3))
        self.wait()

        eq2cp = TexMobject(
            r"\rho {{d {u} } \over {d {t} }}", r" = ", r"-\nabla {p} + \mu \nabla^2 {u} + ", r"\textbf{F}", tex_to_color_map=color_map)
        eq2cp.scale(1.5)
        eq2cp.shift(1.5 * UP)

        eq2cp2 = TexMobject(
            r"\rho {{d {u} } \over {d {t} }}", r" = ", r"-\nabla {p} + \mu \nabla^2 {u} + ", r"\rho {g}", tex_to_color_map=color_map)
        eq2cp2.scale(1.5)
        eq2cp2.shift(1.5 * UP)

        self.play(Transform(eq3[0], eq2cp[0]))
        self.wait()

        self.play(Transform(eq3[1], eq2cp[1:4]))
        self.wait()

        legend = Rectangle(height=2, width=5, color=RED)
        eqq = TexMobject(r"{{d {u} } \over {d {t} }} = ", r"{{\partial {u} } \over {\partial {t} }}",
                         r" + {u} \cdot \nabla {u}", tex_to_color_map=color_map)

        grp = VGroup(legend, eqq)
        grp.shift(3 * RIGHT + 1.5 * UP)

        self.play(Write(grp))
        self.wait()

        self.play(FadeOut(grp))
        self.wait()

        br_config = {
            "buff": 0.1875,
            "fill_opacity": 0,
            "stroke_opacity": 1,
            "stroke_width": 4,
            "color": TEAL
        }
        r1 = BackgroundRectangle(eq2[4:6], **br_config)

        t1 = Text("Pressure", color=TEAL)
        t1.move_to(r1, aligned_edge=DOWN)
        t1.shift(0.7 * DOWN)

        self.play(Write(r1))
        self.play(FadeInFromDown(t1))
        self.play(ApplyMethod(eq3[3:].shift, 2.5 * RIGHT),
                  TransformFromCopy(eq2[4:7], eq2cp[5:8]))
        self.wait()

        r2 = BackgroundRectangle(eq2[7:10], **br_config)

        t2 = Text("Friction", color=TEAL)
        t2.move_to(r2, aligned_edge=DOWN)
        t2.shift(0.7 * DOWN)

        self.play(Transform(r1, r2), Transform(t1, t2))
        self.play(ApplyMethod(eq3[3:].shift, 2.75 * RIGHT),
                  TransformFromCopy(eq2[7:11], eq2cp[8:12]))
        self.wait()

        r3 = BackgroundRectangle(eq2[11:], **br_config)

        t3 = Text("External", color=TEAL)
        t3.move_to(r3, aligned_edge=DOWN)
        t3.shift(0.7 * DOWN)

        self.play(Transform(r1, r3), Transform(t1, t3))
        self.play(Transform(eq3[3:], eq2cp[12:]))
        self.wait()

        self.play(Uncreate(r1), Uncreate(t1))
        self.wait()

        self.play(Transform(eq3[3:], eq2cp2[12:]))
        self.wait()


class Smooth(MovingCameraScene):
    CONFIG = {
        "x1": -0.4,
        "x2": -4,
        "down": 0
    }

    def construct(self):
        plane = NumberPlane()
        plane.set_opacity(0.25)
        f = FunctionGraph(lambda x: self.f_s(x) - self.down,
                          color=GOLD, stroke_opacity=0.8)
        self.add(plane)

        title = Text("Smooth Solution")
        title.scale(2)
        title.to_edge(UP)
        title.add_background_rectangle()

        self.play(Write(f), FadeInFromDown(title))
        self.wait()
        p1 = Dot(fill_opacity=1, color=YELLOW)
        p1.shift([self.x1, self.f_s(self.x1) - self.down, 0])

        t = ValueTracker(self.x2)

        p2 = Dot(fill_opacity=1, color=YELLOW)
        p2.shift([t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        p2.add_updater(lambda x: x.become(
            Dot(fill_opacity=1, color=YELLOW).shift(
                [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        ))

        line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                    [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        line.scale(100)

        def line_update(l):
            line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                        [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
            line.scale(100)
            l.become(line)

        line.add_updater(line_update)

        self.play(Write(line), Write(p1), Write(p2))
        self.wait()

        self.play(t.increment_value, (self.x1-self.x2) - 0.1,
                  run_time=3, rate_func=linear)
        self.wait()

    def f_s(self, x, scale=17):
        return -0.3 * x**2 + 1.5
