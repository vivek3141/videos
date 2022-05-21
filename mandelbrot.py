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


class MandelbrotSet(Mobject):
    CONFIG = {
        "shader_folder": "shaders/mandelbrot",
        "num_steps": 100,
        "max_arg": 2.0,
    }

    def __init__(self, plane, **kwargs):
        super().__init__(
            scale_factor=plane.get_x_unit_size(),
            offset=plane.n2p(0),
            **kwargs,
        )
        self.init_uniforms()
        self.replace(plane, stretch=True)

    def init_uniforms(self):
        super().init_uniforms()
        self.uniforms["scale_factor"] = self.scale_factor
        self.uniforms["opacity"] = self.opacity
        self.uniforms["num_steps"] = self.num_steps
        self.uniforms["max_arg"] = self.max_arg
        self.uniforms["opacity"] = self.opacity
        self.uniforms["offset"] = self.offset

    def init_data(self):
        self.data = {
            "points": np.array([UL, DL, UR, DR]),
        }

    def set_opacity(self, opacity):
        self.uniforms["opacity"] = opacity


class MandelbrotTest(Scene):
    def construct(self):
        c = ComplexPlane()
        t = MandelbrotSet(c)
        self.add(t)
        self.embed()


class MandelbrotIntro(Scene):
    def construct(self):
        c = ComplexPlane(x_range=(-2, 1), y_range=(-2, 2))
        c.scale(3)
        c.shift(3.75 * LEFT)

        m = MandelbrotSet(c, opacity=0.75)

        l = Line(10 * UP, 10 * DOWN).shift(c.n2p(1))

        self.add(c, m, l)
        self.wait()

        eq1 = Tex("f(z) = z^2 + c",
                  tex_to_color_map={"2": A_YELLOW, "f": A_GREEN, "z": A_PINK, "c": A_YELLOW})
        eq2 = Tex("f(z) = z^2 + (1+i)", tex_to_color_map={
                  "f": A_GREEN, "z": A_PINK, "1": A_YELLOW, "i": A_YELLOW, "2": A_YELLOW})
        eq2.scale(1.5)
        eq1.scale(1.5)

        # 3.93 = (FRAME_WIDTH/2 - 0.75)/2 + 0.75
        eq1.move_to(3 * UP + 3.93 * RIGHT)
        eq2.move_to(3 * UP + 3.93 * RIGHT)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

        self.embed()
