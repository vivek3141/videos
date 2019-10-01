from manimlib.imports import *


class ECircle(Scene):
    def construct(self):
        plane = ComplexPlane(

        )
        plane.add(plane.get_coordinate_labels())
        plane.scale(2,about_point=ORIGIN)

        curve = ParametricFunction(
            function=lambda t: 2*np.array([np.cos(t), np.sin(t), 0]),
            t_min=0,
            t_max=2*PI,
            color=YELLOW
        )

        rtex = TexMobject(r"r(t) = e^{it}")
        rtex.scale(1.5)

        rb = BackgroundRectangle(rtex, fill_opacity=1, stroke_opacity=1)
        rtitle = VGroup(rb, rtex)

        rtitle.shift(3 * UP)

        r0 = Vector([2, 0], color=RED)

        r0tex = TexMobject(r"r(0) = 1+0i")
        r0tex.scale(1.5)

        r0b = BackgroundRectangle(r0tex, fill_opacity=1, stroke_opacity=1)
        r0title = VGroup(r0b, r0tex)

        r0title.shift(3 * RIGHT)

        self.play(Write(plane))
        self.wait()

        self.play(Write(rtitle))
        self.wait()

        self.play(Write(r0))
        self.wait()

