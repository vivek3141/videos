from manimlib.imports import *


class ECircle(Scene):
    def construct(self):
        plane = NumberPlane(
            x_line_frequency=2,
            y_line_frequency=2
        )
        plane.add(plane.get_axis_labels())

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

        self.play(Write(plane))
        self.wait()

        self.play(Write(rtitle))
        self.wait()

        self.play(Write(r0))
        self.wait()
        # self.play(Write(curve))

        self.wait()
