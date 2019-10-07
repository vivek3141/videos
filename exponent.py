from manimlib.imports import *


class ECircle(Scene):
    def construct(self):
        plane = ComplexPlane(

        )
        plane.add(plane.get_coordinate_labels())
        plane.scale(2, about_point=ORIGIN)

        curve = ParametricFunction(
            function=self.r,
            t_min=0,
            t_max=0.01,
            color=YELLOW
        )

        rtex = TexMobject(r"r(t) = e^{it}")
        rtex.scale(1.5)

        rb = BackgroundRectangle(rtex, fill_opacity=1, stroke_opacity=1)
        rtitle = VGroup(rb, rtex)

        rtitle.shift(3 * UP)

        r0 = Vector(self.r(0), color=RED)
        v0 = Vector(self.v(0), color=GREEN).shift(self.r(0))

        r0tex = TexMobject(r"r(0) = 1+0i")
        r0tex.scale(1.5)

        r0b = BackgroundRectangle(r0tex, fill_opacity=1, stroke_opacity=1)
        r0title = VGroup(r0b, r0tex)

        r0title.shift(3 * RIGHT)

        self.play(Write(plane))
        self.wait()

        self.play(Write(rtitle))
        self.wait()

        self.play(Write(r0), Write(curve), Write(v0))
        self.wait()

        self.play(
            UpdateFromAlphaFunc(r0, self.update_position),
            UpdateFromAlphaFunc(curve, self.update_curve),
            UpdateFromAlphaFunc(v0, self.update_velocity),
            rate_func=linear,
            run_time=2
        )
        self.wait()

    def r(self, t, a=2):
        return a*np.array([
            np.cos(t),
            np.sin(t),
            0
        ])

    def v(self, t, a=2):
        return a*np.array([
            -np.sin(t),
            np.cos(t),
            0
        ])

    def update_position(self, c, dt):
        a = interpolate(0, 2*PI, dt)
        c1 = Vector(self.r(a), color=RED)
        c.become(c1)

    def update_curve(self, c, dt):
        a = interpolate(0.01, 2*PI, dt)
        curve2 = ParametricFunction(
            function=self.r,
            t_min=0,
            t_max=a,
            color=YELLOW
        )
        c.become(curve2)

    def update_velocity(self, c, dt):
        a = interpolate(0, 2*PI, dt)
        c1 = Vector(self.v(a), color=GREEN).shift(self.r(a))
        c.become(c1)
