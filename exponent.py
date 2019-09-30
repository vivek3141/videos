from manimlib.imports import *


class ECircle(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels())

        curve = ParametricFunction(
            function=lambda t: np.array(2*[np.cos(t), np.sin(t), 0])
            t_min=0,
            t_max=2*PI,
            color=YELLOW
        )

        self.play(Write(plane))
        self.play(Write(curve))
        self.wait()
