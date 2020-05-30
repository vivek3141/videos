from manimlib.imports import *


class Equations(Scene):
    def construct(self):
        color_map = {
            r"\nabla": RED,
            r"{u}": YELLOW,
            r"\rho": GOLD,
            r"{p}": TEAL,
            r"{g}": TEAL,
            r"\mu": GOLD
        }

        eq1 = TexMobject(r"\nabla \cdot {u} = 0", tex_to_color_map=color_map)
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(
            r"\rho {{\partial {u} } \over {\partial {t} }} = -\nabla {p} + \mu \nabla^2 {u} + {g}", tex_to_color_map=color_map)
        eq2.scale(1.5)
        eq2.shift(1 * DOWN)

        title = TextMobject("Navier-Stokes Equations", color=GREEN)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait()


class Assumptions(Scene):
    def construct(self):
        title = TextMobject(
            "Assumptions for Navier-Stokes equations", color=PURPLE)
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
        title = TextMobject("Newtonian Fluid", color=GOLD)
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

        xlbl = TextMobject("Shear Rate")
        xlbl.shift(3 * DOWN)

        grp = VGroup(axes, f1, f2)
        grp.center()

        ylbl = TextMobject("Viscosity")
        ylbl.rotate(PI/2)
        ylbl.shift(3.5 * LEFT + 0 * UP)

        grp1 = VGroup(grp, xlbl, ylbl)
        grp1.shift(0.25 * DOWN)

        lbl1 = TextMobject("Newtonian", color=TEAL)
        lbl1.scale(0.75)
        lbl1.move_to(f1, RIGHT)
        lbl1.shift(3 * LEFT + 0.5 * UP)

        lbl2 = TextMobject("Non-Newtonian", color=RED)
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
        title = TextMobject("Incompressible", color=PURPLE)
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
        title = TextMobject("Incompressible", color=ORANGE)
        title.scale(1.5)
        title.shift(3.25 * UP)

        rect = ScreenRectangle(height=5).shift(0.15 * DOWN)

        self.play(FadeInFromDown(title))
        self.play(Write(rect))
        self.wait()


class Divergence(Scene):
    def construct(self):
        color_map = {
            r"\nabla": RED,
            r"{u}": YELLOW,
            r"\rho": GOLD,
            r"{p}": TEAL,
            r"{g}": TEAL,
            r"\mu": GOLD
        }

        eq1 = TexMobject(r"\nabla", r"\cdot",
                         r"{u}", r"=", r"0", tex_to_color_map=color_map)
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        eq2 = TexMobject(
            r"\rho {{\partial {u} } \over {\partial {t} }} = -\nabla {p} + \mu \nabla^2 {u} + {g}", tex_to_color_map=color_map)
        eq2.scale(1.5)
        eq2.shift(1 * DOWN)

        title = TextMobject("Navier-Stokes Equations", color=GREEN)
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


class VectorFieldDemo(MovingCameraScene):
    def construct(self):
        plane = NumberPlane()
        plane.set_opacity(0.5)
        plane.add(plane.get_axis_labels())

        field1 = VectorField(
            lambda t: 1.5*np.array([np.cos(t[0]), np.sin(t[1]), 0])
        )

        title = TextMobject("Vector Field")
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
        