from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        axes = Axes(
            x_min=-2,
            x_max=4,
            y_min=-2,
            y_max=4,
            number_line_config={"include_tip": False}
        )

        f = FunctionGraph(
            lambda x: x * np.sin(np.cos(x)) + 2,
            x_min=-2,
            x_max=4
        )
        
        lbl = TexMobject("f(x)", color=YELLOW).move_to(f, RIGHT)
        xlbl = TexMobject("x").shift(4.5 * RIGHT)
        ylbl = TexMobject("y").shift(4.5 * UP)

        grp = VGroup(axes, f, lbl, xlbl, ylbl)
        grp.move_to(2.5 * LEFT)

        self.add(grp)

