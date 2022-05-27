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


def c_to_str(c):
    '''
    Complex Number to String
    (1+1j) -> "1 + i"
    (1) -> "1"
    (1-1j) -> "1 - i"
    '''
    if c.imag == 0:
        return f"{int(c.real)}"
    else:
        return f"{int(c.real)} {'-' if c.imag < 0 else '+'} {abs(int(c.imag))}i"


class MandelbrotSet(Mobject):
    CONFIG = {
        "shader_folder": "shaders/mandelbrot",
        "num_steps": 100,
        "max_arg": 2.0,
        "color_style": 0
    }

    def __init__(self, plane, **kwargs):
        super().__init__(
            scale_factor=plane.get_x_unit_size(),
            offset=plane.n2p(0),
            **kwargs,
        )
        self.replace(plane, stretch=True)

    def init_uniforms(self):
        super().init_uniforms()
        self.uniforms["scale_factor"] = self.scale_factor
        self.uniforms["opacity"] = self.opacity
        self.uniforms["num_steps"] = self.num_steps
        self.uniforms["max_arg"] = self.max_arg
        self.uniforms["opacity"] = self.opacity
        self.uniforms["offset"] = self.offset
        self.uniforms["color_style"] = self.color_style

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


class Intro(Scene):
    def construct(self):
        c = ComplexPlane(x_range=(-3, 2), y_range=(-1, 1))
        c.scale(4)

        m = MandelbrotSet(c, opacity=0.75)
        v = ValueTracker(1)

        def m_updater(m, v=v, c=c):
            m_ = MandelbrotSet(c, opacity=0.75, num_steps=v.get_value())
            m.become(m_)
        m.add_updater(m_updater)

        self.add(c, m)
        self.wait(1)
        self.play(v.increment_value, 100, run_time=5)
        self.wait()

        self.embed()


class MandelbrotIntro(Scene):
    CONFIG = {
        "color_map": {**{str(i): A_YELLOW for i in range(10)}, "i": A_YELLOW}
    }

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
        eq2.scale(1.25)
        eq1.scale(1.25)

        # 3.93 = (FRAME_WIDTH/2 - 0.75)/2 + 0.75
        eq1.move_to(3 * UP + 3.93 * RIGHT)
        eq2.move_to(3 * UP + 3.93 * RIGHT)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

        self.play(eq2.shift, 0.35 * LEFT)

        vals = []
        curr = 0
        for _ in range(10):
            vals.append(curr)
            curr = (lambda z: z**2 + (-1 + 1j))(curr)

        steps = VGroup()
        for i in range(4):
            eq = Tex("f(", c_to_str(vals[i]), ")", "=", c_to_str(vals[i+1]),
                     tex_to_color_map={**self.color_map, "f": A_GREEN})
            eq.scale(1.25)
            eq.move_to(eq2, LEFT)
            eq.shift((i+1) * 1.25*DOWN)
            steps.add(eq)

        self.play(Write(steps[0]))
        self.wait()

        for i in range(3):
            self.play(
                TransformFromCopy(steps[i][-5:], steps[i+1][2:7]),
                Write(steps[i+1][:2]), Write(steps[i+1][7])
            )
            self.play(Write(steps[i+1][8:]))
            self.wait()

        dots = Tex(r"\vdots").scale(1.25)
        dots.move_to(steps[-1])
        dots.shift(1.25 * DOWN)

        self.play(Write(dots))
        self.wait()

        self.embed()
