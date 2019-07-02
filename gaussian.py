from manimlib.imports import *


class Cylinder(Sphere):

    def func(self, u, v):
        return np.array([
            np.cos(u),
            np.sin(u),
            v
        ])


class UnwrappedCylinder(Cylinder):
    def func(self, u, v):
        return np.array([
            v - PI,
            -self.radius,
            np.abs(np.cos(u))
        ])


class ParametricDisc(Sphere):
    CONFIG = {
        "u_min": 0,
        "u_max": 1,
        "stroke_width": 0,
        "checkerboard_colors": [BLUE_D],
    }

    def func(self, u, v):
        return np.array([
            u * np.cos(v),
            u * np.sin(v),
            0,
        ])


class Intro(Scene):
    CONFIG = {"default_riemann_start_color": BLUE,
              "default_riemann_end_color": GREEN,
              "area_opacity": 0.8,
              "num_rects": 50, }

    def construct(self):
        f = ParametricFunction(
            function=self.func,
            t_min=-3,
            t_max=3,
            color=BLUE
        )

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        rect = self.get_riemann_sums(self.func)
        rect.scale(1.95)
        rect.shift(2.4 * DOWN)

        func = VGroup(axes, f)
        func.scale(2)
        func.shift(2 * DOWN)

        eq1 = TexMobject(r"f(x) = e^{-x^2}")
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        eq2 = TexMobject(r"\int_{-\infty}^{\infty} e^{-x^2} \ dx = \sqrt{\pi}")
        eq2.scale(1.5)
        eq2.shift(3 * UP)

        self.play(Write(func))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Write(rect), Transform(eq1, eq2))
        self.wait()

    @staticmethod
    def get_riemann_sums(func, dx=0.01, x=(-3, 3), color=RED):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[1]
            rect = Rectangle(height=h, width=dx, color=color,
                             stroke_opacity=0.3, fill_opacity=0.3)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects

    def func(self, t):
        return np.array([t, np.exp(-t**2), 0])


class DefiniteIntegral(Scene):
    def construct(self):
        graph = ParametricFunction(
            function=lambda t: np.array([t, t ** 2, 0]),
            t_min=-1,
            t_max=2,
            color=RED
        )
        axes = Axes(
            x_min=-1,
            x_max=3,
            y_min=0,
            y_max=4
        )

        rects = self.get_riemann_sums(lambda t: np.array([t, t ** 2, 0]))
        func = VGroup(graph, axes, rects)
        func.shift(3.5 * LEFT + 2 * DOWN)

        eq1 = TexMobject(r"\int_1^2 x^2 dx")
        eq1.shift(1.5 * RIGHT + 3 * UP)

        eq2 = TexMobject(r"= \frac{x^3}{3} \Big|_1^2")
        eq2.shift(1.5 * RIGHT + 1 * UP)

        eq3 = TexMobject(r"= \frac{2^3}{3} - \frac{1^3}{3}")
        eq3.shift(1.5 * RIGHT + 1 * DOWN)

        eq4 = TexMobject(r"= \frac{7}{3}")
        eq4.shift(1.5 * RIGHT + 3 * DOWN)

        self.play(Write(eq1), Write(func))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))

        self.wait()

    @staticmethod
    def get_riemann_sums(func, dx=0.01, x=(1, 2), color=GREEN):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[1]
            rect = Rectangle(height=h-dx, width=dx, color=color,
                             stroke_opacity=0.3, fill_opacity=0.3)
            rect.shift(i * RIGHT + (h / 2) * UP)
            rects.add(rect)

        return rects


class Nonelem(Scene):
    def construct(self):
        eq = TexMobject(r"\int e^{-x^2} dx")
        eq.scale(2)

        brace = Brace(eq)
        text2 = brace.get_text("Nonelementary")
        text1 = brace.get_text("???")

        self.play(Write(eq))
        self.play(Write(brace), Write(text1))
        self.play(Transform(text1, text2))
        self.wait()


class Gaussian(Scene):
    def construct(self):
        func = TexMobject(r"f(x,y) = e^{-(x^2+y^2)}", tex_to_color_map={})
        func.shift(3 * UP)
        func.scale(1.5)

        eq1 = TexMobject(
            r"I = \int_{-\infty}^{\infty} e^{-x^2} dx", tex_to_color_map={"I": YELLOW})
        eq1.shift(ORIGIN)
        eq1.scale(2)

        eq2 = TexMobject(r"\iint_{\Bbb R ^ 2} e^{-(x^2 + y^2)} \ dy dx")
        eq2.shift(ORIGIN)
        eq2.scale(2)

        eq3 = TexMobject(
            r"\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-(x^2 + y^2)}  \ dy dx")
        eq3.shift(ORIGIN)
        eq3.scale(2)

        eq4 = TexMobject(
            r"\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-x^2} \bullet e^{-y^2}  \ dy dx")
        eq4.shift(ORIGIN)
        eq4.scale(2)

        circ = Circle(color=RED, radius=1.2)
        circ.shift(0.5 * LEFT)

        eq5 = TexMobject(
            r"\int_{-\infty}^{\infty}e^{-x^2}\int_{-\infty}^{\infty} e^{-y^2}  \ dy dx")
        eq5.shift(ORIGIN)
        eq5.scale(2)

        eq6 = TexMobject(
            r"\int_{-\infty}^{\infty}e^{-x^2} \ dx", r"\int_{-\infty}^{\infty} e^{-y^2}  \ dy")
        eq6.shift(ORIGIN)
        eq6.scale(2)

        eq7 = TexMobject(
            r"\iint_{\Bbb R^2} e^{-(x^2 + y^2)} \ dy dx = I^2", tex_to_color_map={"I": YELLOW})
        eq7.shift(ORIGIN)
        eq7.scale(2)

        eq8 = TexMobject(
            r"I = \sqrt{\iint_{\Bbb R^2} e^{-(x^2 + y^2)} \ dy dx}", tex_to_color_map={"I": YELLOW})
        eq8.shift(ORIGIN)
        eq8.scale(2)

        br1 = Brace(eq6[0])
        t1 = br1.get_text("I").scale(2)
        t1.set_color(YELLOW)
        b1 = VGroup(br1, t1)

        br2 = Brace(eq6[1])
        t2 = br2.get_text("I").scale(2)
        t2.set_color(YELLOW)
        b2 = VGroup(br2, t2)

        self.play(Write(func))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(ApplyMethod(eq1.scale, 0.5))
        self.play(ApplyMethod(eq1.shift, 4 * LEFT + 3 * UP),
                  ApplyMethod(func.shift, 2 * RIGHT))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Transform(eq2, eq3))
        self.wait()

        self.play(Transform(eq2, eq4))
        self.wait()

        self.play(Write(circ))
        self.wait()

        self.play(Uncreate(circ))
        self.play(Transform(eq2, eq5))
        self.wait()

        self.play(Transform(eq2, eq6))
        self.wait()

        self.play(Write(b1), Write(b2))
        self.wait()

        self.play(Uncreate(b1), Uncreate(b2), Transform(eq2, eq7))
        self.wait()

        self.play(Transform(eq2, eq8))
        self.wait()


class ThreeFunc(ThreeDScene):
    def construct(self):
        s = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        )

        axes = ThreeDAxes(
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        conf = {"fill_color": ORANGE,
                "fill_opacity": 1.0,
                "checkerboard_colors": [ORANGE, RED],
                "stroke_color": RED,
                "stroke_width": 0.5, }

        surface = VGroup(axes, s)
        surface.scale(2)

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(15)

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])


class GaussianVisualOld(ThreeDScene):
    def construct(self):
        s = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        )

        axes = ThreeDAxes(
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        conf = {"fill_color": ORANGE,
                "fill_opacity": 1.0,
                "checkerboard_colors": [ORANGE, RED],
                "stroke_color": RED,
                "stroke_width": 0.5, }

        const = self.func(0, 1)[-1]
        cyln = ParametricSurface(
            self.cyln,
            u_min=0,
            u_max=2*PI,
            v_min=0,
            v_max=const,
            **conf
        ).scale(2)

        surface = VGroup(axes, s)
        surface.scale(2)

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        rect = VGroup(Rectangle(stroke_color=RED,
                                fill_color=RED_A, fill_opacity=1))

        for i in np.arange(0, 1, 0.1):
            rec = Rectangle(stroke_color=RED, fill_color=RED_A,
                            fill_opacity=1).shift(i * OUT)
            #rec.rotate(np.pi / 2, axis=X_AXIS)
            rect.add(rec)

        #rect = Rectangle(color=RED, fill_color=RED, fill_opacity=1)

        b1 = Brace(rect, UP)
        t1 = b1.get_tex(r"2\pi r")

        b2 = Brace(rect, LEFT)
        t2 = b2.get_tex(r"e^{-r^2}")

        rec = VGroup(rect, b1, t1, b2, t2)
        rec.rotate(np.pi / 2, axis=X_AXIS)

        self.play(Write(surface))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(5)

        s.set_style(fill_opacity=0.25,
                    stroke_opacity=0.25)
        self.play(Write(cyln))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(5)
        self.move_camera(np.pi / 2, -np.pi / 2)

        self.play(ReplacementTransform(cyln, rect), Uncreate(surface))

        self.play(Write(rec))
        self.wait()

        self.move_camera(np.pi / 2, -np.pi / 2 + 0.5)

        self.wait()

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])

    def cyln(self, u, v):
        return np.array([
            np.cos(u),
            np.sin(u),
            v
        ])


class GaussianScene(SpecialThreeDScene):
    CONFIG = {
        "cap_config": {
            "stroke_width": 1,
            "stroke_color": WHITE,
            "fill_color": BLUE_D,
            "fill_opacity": 1,
        }
    }

    def get_cylinder(self, **kwargs):
        config = merge_dicts_recursively(self.sphere_config, kwargs)
        return Cylinder(**config)

    def get_cylinder_caps(self):
        R = self.sphere_config["radius"]
        caps = VGroup(*[
            Circle(
                radius=R,
                **self.cap_config,
            ).shift(R * vect)
            for vect in [IN, OUT]
        ])
        caps.set_shade_in_3d(True)
        return caps

    def get_unwrapped_cylinder(self):
        return UnwrappedCylinder(**self.sphere_config)

    def get_xy_plane(self):
        pass

    def get_ghost_surface(self, surface):
        result = surface.copy()
        result.set_fill(BLUE_E, opacity=0.5)
        result.set_stroke(WHITE, width=0.5, opacity=0.5)
        return result

    def project_point(self, point):
        radius = self.sphere_config["radius"]
        result = np.array(point)
        result[:2] = normalize(result[:2]) * radius
        return result

    def project_mobject(self, mobject):
        return mobject.apply_function(self.project_point)


class GaussianVisual(GaussianScene):
    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])

    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=-3,
            u_max=3,
            v_min=-3,
            v_max=3
        )

        axes = self.get_axes()

        #surface = VGroup(axes, s)
        surface.scale(2)

        conf = {"fill_color": ORANGE,
                "fill_opacity": 1.0,
                "checkerboard_colors": [ORANGE, RED],
                "stroke_color": RED,
                "stroke_width": 0.5, }

        const = self.func(0.75, 0)[-1]
        cylinder = Cylinder(
            u_min=0,
            u_max=2*PI,
            v_min=0,
            v_max=const,
            radius=0.75,
            **conf
        ).scale(2)

        radius = cylinder.get_width() / 2

        self.add(axes, surface)
        self.wait()
        self.begin_ambient_camera_rotation()
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )
        # self.wait(2)
        surface.set_fill(opacity=0.75)
        self.play(
            Write(cylinder),
            run_time=3
        )

        self.wait(3)

        unwrapped_cylinder = UnwrappedCylinder(radius=0.75, **conf)
        unwrapped_cylinder.set_fill(opacity=0.75)
        self.play(Uncreate(surface), Uncreate(axes))
        self.play(
            ReplacementTransform(cylinder, unwrapped_cylinder),
            run_time=3
        )
        self.stop_ambient_camera_rotation()
        self.move_camera(
            phi=90 * DEGREES,
            theta=-90 * DEGREES,
        )
        self.play(ApplyMethod(cylinder.scale, 2.5))

        # Show dimensions
        stroke_width = 5
        radius = 1.785
        r = 1.35
        top_line = Line(
            PI * radius * LEFT + r * OUT,
            PI * radius * RIGHT + r * OUT,
            color=YELLOW,
            stroke_width=stroke_width,
        )
        side_line = Line(
            PI * radius * LEFT + r * OUT,
            PI * radius * LEFT + 0.45 * IN,
            color=GREEN,
            stroke_width=stroke_width,
        )
        lines = VGroup(top_line, side_line)
        lines.shift(radius * DOWN)
        two_pi_R = TexMobject(r"2\pi r")
        two_R = TexMobject(r"e^{-r^2}")
        texs = VGroup(two_pi_R, two_R)
        for tex in texs:
            tex.scale(1.5)
            tex.rotate(90 * DEGREES, RIGHT)
        two_pi_R.next_to(top_line, OUT)
        two_R.next_to(side_line, RIGHT)

        self.play(
            ShowCreation(top_line),
            FadeInFrom(two_pi_R, IN)
        )
        self.wait()
        self.play(
            ShowCreation(side_line),
            FadeInFrom(two_R, RIGHT)
        )
        self.wait()


class Volume(Scene):
    def construct(self):
        head = TextMobject("Total Volume:")
        head.scale(1.5)
        head.shift(2 * UP)

        eq1 = TexMobject(r"\int_{0}^{\infty}2\pi r e^{-r^2} dr", tex_to_color_map={"e":RED, r"{0}^{\infty}":GREEN,"r":YELLOW})
        eq1.scale(2)

        rect = Rectangle(height=3, width=3, color=RED)
        rect.shift(5 * RIGHT + 2 * UP)

        text1 = TexMobject(r"u=r^2")
        text1.shift(5 * RIGHT + 2.5 * UP)

        text2 = TexMobject(r"du = 2r \ dr")
        text2.shift(5 * RIGHT + 1.5 * UP)

        sub = VGroup(rect, text1, text2)
        
        self.play(Write(eq1), Write(head))
        self.wait()

        self.play(Uncreate(head), Write(sub))
        self.wait()
