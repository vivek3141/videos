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


def c_to_str(c, conv=int):
    '''
    Complex Number to String
    (1+1j) -> "1 + i"
    (1) -> "1"
    (1-1j) -> "1 - i"
    '''
    if c.imag == 0:
        return f"{conv(c.real)}"
    else:
        return f"{conv(c.real)} {'-' if c.imag < 0 else '+'} {conv(abs(c.imag))}i"


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
        "color_map": {**{str(i): A_YELLOW for i in range(10)},
                      "i": A_YELLOW, "-": A_YELLOW, ".": A_YELLOW,
                      "f": A_GREEN, "z": A_PINK}
    }

    def construct(self):
        c = ComplexPlane(x_range=(-2, 1), y_range=(-2, 2))
        c.scale(3)
        c.shift(3.75 * LEFT)
        c.add_coordinate_labels()

        m = MandelbrotSet(c, opacity=0.75, color_style=1)

        l = Line(10 * UP, 10 * DOWN).shift(c.n2p(1))

        self.play(Write(c), Write(l))
        self.play(FadeIn(m))
        self.wait()

        eq1 = Tex("f(z) = z^2 + c",
                  tex_to_color_map={"2": A_YELLOW, "f": A_GREEN, "z": A_PINK, "c": A_YELLOW})
        eq2 = Tex("f(z) = z^2 + ", "(", "-1+i", ")", tex_to_color_map={
                  "f": A_GREEN, "z": A_PINK, "1": A_YELLOW, "i": A_YELLOW, "2": A_YELLOW, "-": A_YELLOW})
        eq2.scale(1.25)
        eq1.scale(1.25)

        # 3.93 = (FRAME_WIDTH/2 - 0.75)/2 + 0.75
        eq1.move_to(3 * UP + 3.93 * RIGHT)
        eq2.move_to(3 * UP + 3.93 * RIGHT)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

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

        def get_dot_grp(z, conv=int, color=A_ORANGE, radius=0.1):
            d_ = Dot(c.n2p(z), color=color, radius=radius)
            return VGroup(
                d_,
                Tex(c_to_str(z, conv), tex_to_color_map=self.color_map
                    ).next_to(d_, DOWN).add_background_rectangle(buff=0.075),
            )
        d = [get_dot_grp(z) for z in vals[:6]]

        self.play(Write(d[0]))
        self.wait()

        self.play(Write(steps[0]))
        self.play(TransformFromCopy(steps[0][-5:], d[1][1]))
        self.play(Transform(d[0][0], d[1][0]), Uncreate(d[0][1]))
        self.wait()

        for i in range(3):
            self.play(
                TransformFromCopy(steps[i][-5:], steps[i+1][2:7]),
                Write(steps[i+1][:2]), Write(steps[i+1][7])
            )
            self.play(Write(steps[i+1][8:]))
            self.play(TransformFromCopy(steps[i+1][-5:], d[i+2][1]))
            if i < 2:
                self.play(Transform(d[0][0], d[i+2][0]), Uncreate(d[i+1][1]))
                self.wait()

        vdots = Tex(r"\vdots").scale(1.25)
        vdots.move_to(steps[-1])
        vdots.shift(1.25 * DOWN)

        self.play(Write(vdots))
        self.wait()

        eq3 = Tex("f(z) = z^2 + ", "(", "-0.25+0.25i", ")", tex_to_color_map={
                  "f": A_GREEN, "z": A_PINK, "0.25": A_YELLOW,
                  "i": A_YELLOW, "2": A_YELLOW, "-": A_YELLOW})
        eq3.move_to(eq2)

        self.play(FadeOut(VGroup(steps, vdots), DOWN))
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()

        def get_mandel_lines(point, steps=15):
            curr, prev = point, 0
            grp = VGroup()

            for i in range(steps):
                grp.add_to_back(
                    Line(c.n2p(curr), c.n2p(prev), stroke_opacity=0.5))
                grp.add(Dot(c.n2p(prev), color=A_ORANGE))
                try:
                    curr, prev = (lambda z: z**2 + point)(curr), curr
                except RuntimeWarning:
                    break

            return grp

        mandel1 = get_mandel_lines(-0.25 + 0.25j)
        steps2 = VGroup()

        curr, prev = -0.25+0.25j, 0
        for i in range(5):
            eq = Tex(
                "f(", c_to_str(prev, conv=lambda x: f"{x:.2f}"), ")",
                "=", c_to_str(curr, conv=lambda x: f"{x:.2f}"),
                tex_to_color_map={**self.color_map, "f": A_GREEN}
            )
            eq.scale(0.85)
            eq.move_to(eq3, LEFT)
            eq.shift((i+1) * 1*DOWN)
            steps2.add(eq)
            curr, prev = (lambda z: z**2 + (-0.25 + 0.25j))(curr), curr

        vdots = Tex(r"\vdots").scale(1.25)
        vdots.move_to(steps2[4]).shift(1.1 * DOWN)

        self.play(TransformFromCopy(eq3, mandel1))
        for i in steps2:
            self.play(FadeIn(i, DOWN))
        self.play(Write(vdots))
        self.wait()

        self.play(Uncreate(mandel1), FadeOut(steps2, UP), FadeOut(vdots, UP))

        d = get_dot_grp(-0.75, conv=lambda s: f"{s:.2f}", color=A_RED)
        eq4 = Tex("f(z) = z^2 + (-0.75)", tex_to_color_map=self.color_map)
        eq4.move_to(eq3, LEFT)

        self.play(Write(d))
        self.play(FocusOn(d))
        self.play(Uncreate(eq3[8:]), Write(eq4[-1]))
        self.play(TransformFromCopy(d[1], eq4[7:12]))

        self.remove(self.mobjects[-1], eq3)
        self.add(eq4)

        self.play(eq4.move_to, 3 * UP + 3.93 * RIGHT)
        self.wait()

        v = ValueTracker(0)

        def dot_updater(d):
            d_ = get_dot_grp(
                -0.75 + v.get_value()*1j,
                conv=lambda s: f"{s:.2f}", color=A_RED)
            d.become(d_)

        def m_updater(m):
            m_ = get_mandel_lines(-0.75 + v.get_value()*1j)
            m.become(m_)
            self.bring_to_front(d)

        m1 = get_mandel_lines(-0.75)
        m1.add_updater(m_updater)
        d.add_updater(dot_updater)

        self.play(TransformFromCopy(eq4, m1))
        self.play(v.increment_value, 1, run_time=7.5, rate_func=linear)
        self.wait()

        self.embed()
