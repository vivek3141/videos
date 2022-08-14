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


def c_to_str(c, conv=int, compare=lambda c: c.imag < 0):
    '''
    Complex Number to String
    (1+1j) -> "1 + i"
    (1) -> "1"
    (1-1j) -> "1 - i"
    '''
    if c.imag == 0:
        return f"{conv(c.real)}"
    else:
        return f"{conv(c.real)} {'-' if compare(c) else '+'} {conv(abs(c.imag))}i"


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
        self.uniforms["num_steps"] = float(self.num_steps)
        self.uniforms["max_arg"] = float(self.max_arg)
        self.uniforms["offset"] = self.offset
        self.uniforms["color_style"] = float(self.color_style)

    def init_data(self):
        super().init_data()
        self.data["points"] = np.array([UL, DL, UR, DR])

    def set_opacity(self, opacity):
        super().set_opacity(opacity)
        self.uniforms["opacity"] = float(opacity)


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
                      "f": A_GREEN, "z": A_PINK, r"\epsilon": A_LAVENDER}
    }

    def construct(self):
        # This is some bad code by me, but hey it works. This is something I think manim can do better.
        # If you're wondering why I don't transform each ComplexPlane into one another,
        # it's because the coordinate labels make it weird-looking.

        c1 = ComplexPlane()
        c1.add_coordinate_labels()
        c1.remove(c1.coordinate_labels)

        c2 = ComplexPlane()
        c2.scale(3)
        c2.add_coordinate_labels()
        c2.remove(c2.coordinate_labels)

        c3 = ComplexPlane()
        c3.scale(3)
        c3.shift(2.25 * LEFT)
        c3.add_coordinate_labels()

        self.play(Write(c1), Write(c1.coordinate_labels))
        self.wait()

        self.play(Uncreate(c1.coordinate_labels), Transform(c1, c2))
        self.play(Write(c2.coordinate_labels))

        c2.add(c2.coordinate_labels)
        self.remove(c1)
        self.add(c2)

        rect = Polygon(
            [0.77, FRAME_HEIGHT/2, 0],
            [FRAME_WIDTH/2, FRAME_HEIGHT/2, 0],
            [FRAME_WIDTH/2, -FRAME_HEIGHT/2, 0],
            [0.77, -FRAME_HEIGHT/2, 0],
            fill_opacity=1,
            stroke_width=0,
            fill_color=BLACK
        )

        c = ComplexPlane(x_range=(-2, 1), y_range=(-2, 2))
        c.scale(3)
        c.shift(3.75 * LEFT)
        c.add_coordinate_labels()

        self.play(Transform(c2, c3))
        self.play(FadeIn(rect))

        m = MandelbrotSet(c, opacity=0.75, color_style=1)

        l = Line(10 * UP, 10 * DOWN).shift(c.n2p(1))

        self.play(Write(l))
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

        self.play(Transform(eq1[:-1], eq2[:-6]), Uncreate(eq1[-1]))
        self.play(Write(eq2[-6:]))

        self.remove(eq1)
        self.add(eq2)
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

        d = [self.get_dot_grp(z, c) for z in vals[:6]]

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

        mandel1 = self.get_mandel_lines(-0.25 + 0.25j, c)
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

        d = self.get_dot_grp(-0.75, c, conv=lambda s: f"{s:.2f}", color=A_RED)
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
            d_ = self.get_dot_grp(
                -0.75 + v.get_value()*1j, c,
                conv=lambda s: f"{s:.2f}", color=A_RED)
            d.become(d_)

        def m_updater(m):
            m_ = self.get_mandel_lines(-0.75 + v.get_value()*1j, c)
            m.become(m_)
            self.bring_to_front(d)

        m1 = self.get_mandel_lines(-0.75, c)
        m1.add_updater(m_updater)
        d.add_updater(dot_updater)

        self.play(Write(m1))
        self.play(v.increment_value, 1, run_time=7.5)
        self.wait()

        h1 = Tex(r"\epsilon", color=A_LAVENDER)
        h1.scale(1.5)
        h1.move_to(2.34 * RIGHT + 1.75 * UP)

        h_eq = Tex(r"f(z) = z^2 + (-0.75 + \epsilon i)",
                   tex_to_color_map=self.color_map)
        h_text = Text("# of steps till\n\nreaches a magnitude of 2")
        h2 = VGroup(h_text, h_eq)
        h2.scale(0.5)
        h2.move_to(5.52 * RIGHT + 1.75 * UP)

        l1 = Line(2.25 * UP, 5 * DOWN).shift(3.93 * RIGHT)
        l2 = Line(0.75 * RIGHT, 7 * RIGHT).shift(1.25 * UP)

        self.play(Write(l1), Write(l2))
        self.play(Write(h1), Write(h2))

        num_steps = ["3", "33", "315", "3143",
                     "31417", "314160", "3141593", "31415928"]
        # str(1/10**i) produces 1eX
        epsilon = ["1.0", *[f"0.{'0'*i}1" for i in range(9)]]

        tab = VGroup()
        for i in range(8):
            t1 = Tex(epsilon[i]).move_to(h1).scale(
                0.75).shift(0.65 * (i+1) * DOWN)
            t2 = Tex(num_steps[i]).move_to(h2).scale(
                0.75).shift(0.65 * (i+1) * DOWN)
            tab.add(t1, t2)
        tab.shift(0.2 * DOWN)

        for i in range(2):
            t_temp = Tex(epsilon[i], color=A_YELLOW).move_to(d[1][-5:-1])
            self.add(t_temp)

            self.play(Transform(
                t_temp,
                tab[2*i]
            ))
            self.play(TransformFromCopy(m1[0], tab[2*i+1]))
            self.play(v.set_value, 1/10**(i+1))

        t_temp = Tex(epsilon[2], color=A_YELLOW).move_to(d[1][-5:-1])
        self.add(t_temp)

        self.play(Transform(
            t_temp,
            tab[2*2])
        )
        self.play(TransformFromCopy(m1[0], tab[2*2+1]))

        for i in range(3, 8):
            self.play(FadeIn(tab[2*i], DOWN), FadeIn(tab[2*i+1], DOWN))

        self.wait()
        self.embed()

    def get_dot_grp(self, z, c, conv=int,
                    c_str_func=c_to_str, color=A_ORANGE,
                    tex_to_color_map=None, radius=0.1):
        if tex_to_color_map is None:
            tex_to_color_map = self.color_map

        d_ = Dot(c.n2p(z), color=color, radius=radius)
        return VGroup(
            d_,
            Tex(c_str_func(z, conv), tex_to_color_map=tex_to_color_map
                ).next_to(d_, DOWN).add_background_rectangle(buff=0.075),
        )

    def get_mandel_lines(self, point, c, steps=15, max_arg=10000):
        curr, prev = point, 0
        grp = VGroup()

        for i in range(steps):
            grp.add_to_back(
                Line(c.n2p(curr), c.n2p(prev), stroke_opacity=0.5))
            grp.add(Dot(c.n2p(prev), color=A_ORANGE))
            if abs(curr) < max_arg:  # Avoid overflow
                curr, prev = (lambda z: z**2 + point)(curr), curr
            else:
                break

        return grp


class ExpIntro(MandelbrotIntro):
    CONFIG = {
        "color_map": {**{str(i): A_YELLOW for i in range(10)},
                      "i": A_YELLOW, ".": A_YELLOW, "-": None,
                      "f": A_GREEN, "z": A_PINK, r"\epsilon": A_LAVENDER}
    }

    def construct(self):
        c = ComplexPlane(x_range=(-3, 2), y_range=(-1, 1))
        c.scale(4)
        c.add_coordinate_labels()

        m = MandelbrotSet(c, opacity=0.75, color_style=1)
        d1 = self.get_dot_grp(0.25, c, conv=lambda s: f"{s:.2f}", color=A_RED)

        self.play(Write(c), FadeIn(m))
        self.play(Write(d1), FocusOn(d1[0]))
        self.wait()

        d2 = self.get_dot_grp(
            0.6, c, c_str_func=lambda c, _: r"0.25 + \epsilon",
            tex_to_color_map={"0.25": A_YELLOW, "+": A_YELLOW, r"\epsilon": A_LAVENDER})

        self.play(TransformFromCopy(d1, d2))
        self.wait()

        eq = Tex("f(z) = z^2 + 0.25", tex_to_color_map=self.color_map)
        eq.scale(1.5)
        eq.shift(3.35 * UP)
        eq.add_background_rectangle(buff=0.1, opacity=0.9)

        axes = Axes(
            x_range=(-1, 1, 0.5), y_range=(0, 1, 0.5), axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 6}, y_axis_config={"stroke_width": 6},
        )
        axes.scale(0.95)
        axes.shift(0.3 * DOWN)
        axes.add_coordinate_labels(font_size=36, num_decimal_places=1)

        c1 = axes.get_graph(
            lambda x: x**2 + 0.25,
            x_range=(-np.sqrt(0.75), np.sqrt(0.75)),
            color=A_RED, stroke_width=6
        )

        self.play(Write(eq))
        self.wait()

        l1 = DashedLine(
            axes.c2p(-1, 0.25), axes.c2p(1, 0.25), dash_length=0.1,
            positive_space_ratio=0.4, color=A_YELLOW, opacity=0.5)

        lbl1 = Tex("0.25", color=A_YELLOW)
        lbl1.move_to(l1, LEFT)
        lbl1.shift(0.4 * UP)

        cp = lbl1.copy()
        cp.scale(1.5)
        cp.move_to(eq[8:12])

        self.play(FadeOut(m), Uncreate(d1), Uncreate(d2), Uncreate(c))
        self.play(Write(axes))
        self.play(TransformFromCopy(eq, c1))
        self.play(Write(l1))
        self.play(TransformFromCopy(cp, lbl1))
        self.wait()

        eq.remove(eq.background_rectangle)

        br1 = Polygon(
            axes.c2p(0.55, 1.0), axes.c2p(0.55, 1.5),
            axes.c2p(1.5, 1.5), axes.c2p(1.5, 0.3),
            axes.c2p(1.0, 0.3), axes.c2p(1.0, 1.0),
            stroke_width=0, fill_opacity=1, color=BLACK
        )  # Rectangle to mask off blue lines
        self.add(br1)

        l2 = axes.get_graph(lambda x: x)
        l2_lbl = Tex("y = x")
        l2_lbl.rotate(np.arctan2(5.805, 5.7))  # c2p(1, 1) - c2p(0, 0)
        l2_lbl.move_to(4.2844 * RIGHT + 0.5710 * UP)

        dot = Dot(axes.c2p(0, 0), color=A_BLUE)

        self.play(Write(l2), Write(l2_lbl))
        self.wait()

        self.play(Write(dot))
        self.play(FocusOn(dot))

        num_steps = 40
        max_arg = 10
        path = self.get_bounce_lines(
            axes, num_steps=num_steps, offset=0.25, max_arg=max_arg)
        curr, f = 0, lambda z: z**2 + 0.25

        for i in range(10):
            self.play(
                ShowCreation(path[2*i]),
                ApplyMethod(dot.move_to, axes.c2p(curr, f(curr)))
            )
            self.play(
                ShowCreation(path[2*i+1]),
                ApplyMethod(dot.move_to, axes.c2p(f(curr), f(curr)))
            )
            curr = f(curr)

        for i in range(10, len(path)//2):
            self.play(
                ShowCreation(path[2*i]),
                ApplyMethod(dot.move_to, axes.c2p(curr, f(curr))),
                run_time=1/(num_steps-10)
            )
            self.play(
                ShowCreation(path[2*i+1]),
                ApplyMethod(dot.move_to, axes.c2p(f(curr), f(curr))),
                run_time=1/(num_steps-10)
            )
            curr = f(curr)

        self.wait()

        e = ValueTracker(0)

        def para_updater(c):
            c1 = axes.get_graph(
                lambda x: x**2 + (0.25+e.get_value()),
                # x_range=(-1, 2),
                x_range=(-np.sqrt(0.75-e.get_value()),
                         np.sqrt(0.75-e.get_value())),
                color=A_RED, stroke_width=6
            )
            c.become(c1)
        c1.add_updater(para_updater)

        def path_updater(path):
            path.become(self.get_bounce_lines(
                axes, num_steps=num_steps, offset=0.25+e.get_value(), max_arg=max_arg))
            self.bring_to_front(br1)
        path.add_updater(path_updater)

        def dot_updater(dot):
            curr, f = 0, lambda z: z**2 + 0.25 + e.get_value()
            for _ in range(num_steps):
                if curr > max_arg:
                    break
                curr = f(curr)
            dot.become(Dot(axes.c2p(curr, curr), color=A_BLUE))
        dot.add_updater(dot_updater)

        """
        Okay, the reason this is done is because in update_frame, it iterates through all mobjects,
        but the updater is on the VGroup, not each individual line, so we need to add it as a VGroup,
        so the updater updates it, so we remove it from the scene, removing all the lines, then add
        the VGroup
        """
        self.remove(path)
        self.add(path)

        eq2 = Tex("f(z) = z^2 + 0.25 + \epsilon",
                  tex_to_color_map=self.color_map)
        eq2.scale(1.5)
        eq2.shift(3.35 * UP)

        self.play(TransformMatchingTex(eq, eq2))
        self.wait()

        self.play(e.increment_value, 0.05, run_time=5)
        self.wait()

        self.play(e.set_value, 0.01)
        path.remove_updater(path_updater)
        c1.remove_updater(para_updater)
        self.play(FocusOn(Point(axes.c2p(0.5, 0.5))))
        self.wait()

        eq3 = Tex("f(z) = z^2 + 0.25 + \epsilon - 0.5",
                  tex_to_color_map=self.color_map)
        eq3.scale(1.5)
        eq3.shift(3.35 * UP)

        c2 = axes.get_graph(lambda x: x**2 - 0.25+0.01,
                            color=A_RED, stroke_width=6)
        path2 = self.get_bounce_lines(
            axes, offset=0.25+0.01, num_steps=40, start_coord=(0, -0.5))
        l3 = axes.get_graph(lambda x: x-0.5)

        self.play(Uncreate(l2_lbl))
        self.play(TransformMatchingTex(eq2, eq3))
        self.play(Transform(c1, c2), Transform(path, path2), Transform(l2, l3))
        self.wait()

        eq4 = Tex("f(z) = (z+0.5)^2 + 0.25 + \epsilon - 0.5",
                  tex_to_color_map=self.color_map)
        eq4.scale(1.5)
        eq4.shift(3.35 * UP)

        c3 = axes.get_graph(lambda x: (x+0.5)**2-0.25+0.01,
                            color=A_RED, stroke_width=6)
        path3 = self.get_bounce_lines(
            axes, offset=0.25+0.01, num_steps=100, max_arg=2.0, start_coord=(-0.5, -0.5))
        l4 = axes.get_graph(lambda x: x)

        self.play(TransformMatchingTex(eq3, eq4))
        self.play(Transform(c1, c3), Transform(path, path3), Transform(l2, l4))
        self.wait()

        to_remove = VGroup(
            *[i for i in self.mobjects if isinstance(i, VMobject) and i is not eq4]
        )
        self.play(Uncreate(to_remove))
        self.wait()

        self.embed()

    def get_bounce_lines(self, axes, num_steps=20, offset=0.25, start_coord=(0, 0), max_arg=1.0):
        curr, f = 0, lambda z: z**2 + offset
        x, y = start_coord
        path = VGroup()

        for _ in range(num_steps):
            if curr > max_arg:
                break

            path.add(Line(
                axes.c2p(x + curr, y + curr),
                axes.c2p(x + curr, y + f(curr)),
                color=A_BLUE, stroke_width=6))
            path.add(Line(
                axes.c2p(x + curr, y + f(curr)),
                axes.c2p(x + f(curr), y + f(curr)),
                color=A_BLUE, stroke_width=6))
            curr = f(curr)

        return path


class Exp2(ExpIntro):
    CONFIG = {
        "color_map": {**{str(i): A_YELLOW for i in range(10)},
                      "i": A_YELLOW, ".": A_YELLOW,
                      r"\epsilon": A_LAVENDER,
                      "f": A_GREEN, "z": A_PINK,
                      "{n}": A_YELLOW}
    }

    def construct(self):
        eq1 = Tex("f(z) = (z+0.5)^2 + 0.25 + \epsilon - 0.5",
                  tex_to_color_map=self.color_map)
        eq1.scale(1.5)
        eq1.shift(3.35 * UP)

        self.add(eq1)
        self.wait()

        eq2 = Tex("f(z)", "=", "z^2 + z + \epsilon",
                  tex_to_color_map=self.color_map)
        eq2.scale(1.5)
        eq2.shift(3.35 * UP)

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()

        eq3 = Tex("z_{{n}+1} = z^2 + z + \epsilon",
                  tex_to_color_map=self.color_map)
        eq3.scale(1.5)
        eq3.shift(eq2[4].get_center() - eq3[4].get_center())

        eq4 = Tex("z_{{n}+1} = z_{{n}}^2 + z_{{n}} + \epsilon",
                  tex_to_color_map=self.color_map)
        eq4.scale(1.5)
        eq4.shift(3.35 * UP)

        self.play(FadeOut(eq2[:4], UP), FadeIn(eq3[:4], UP))
        self.remove(eq2)
        self.add(eq3)

        self.play(
            Transform(eq3[:5], eq4[:5]),
            FadeOut(eq3[5:7], UP), FadeIn(eq4[5:8], UP),
            Transform(eq3[7], eq4[8])
        )
        self.play(
            FadeOut(eq3[8], UP), FadeIn(eq4[9:11], UP),
            Transform(eq3[9:], eq4[11:])
        )
        self.remove(eq3)
        self.add(eq4)
        self.wait()

        eq5 = Tex("z_{{n}+1} - z_{{n}} = z_{{n}}^2 + \epsilon",
                  tex_to_color_map=self.color_map)
        eq5.scale(1.5)
        eq5.shift(1.85 * UP)

        self.play(TransformFromCopy(eq4[:4], eq5[:4]))
        self.play(TransformFromCopy(eq4[8], eq5[4]),
                  TransformFromCopy(eq4[9:11], eq5[5:7]))
        self.play(
            TransformFromCopy(eq4[4], eq5[7]), TransformFromCopy(
                eq4[5:8], eq5[8:11]),
            TransformFromCopy(eq4[11:], eq5[11:])
        )
        self.wait()

        self.play(FadeOut(eq4, UP), ApplyMethod(eq5.shift, 1.5 * UP))
        self.wait()

        rect = ScreenRectangle(height=6)
        rect.shift(0.5 * DOWN)

        self.play(Indicate(eq5[-1]))
        self.play(Write(rect))
        self.wait()

        eq6 = Tex(
            r"z^{\prime} = z^2 + \epsilon",
            tex_to_color_map={
                "z": A_PINK, r"\epsilon": A_LAVENDER, "2": A_YELLOW, r"\prime": A_YELLOW}
        )
        eq6.scale(1.5)
        eq6.shift(1.85 * UP)

        # TransformFromCopy creates copies w/out pointers making removing the entire
        # group a pain, so creating copies manually makes it easier.
        cp1 = eq5[:7].copy()
        cp2 = eq5[8:11].copy()

        self.play(Uncreate(rect))
        self.play(Transform(cp1, eq6[:2]))
        self.play(TransformFromCopy(eq5[7], eq6[2]),
                  Transform(cp2, eq6[3:5]))
        self.play(TransformFromCopy(eq5[11:], eq6[5:]))

        self.remove(cp1, cp2, eq6)
        self.add(eq6)

        self.play(FadeOut(eq5, UP), ApplyMethod(eq6.shift, 1.5 * UP))
        self.wait()

        eq7 = Tex(
            r"\int {dz \over z^2 + \epsilon} = \int d{n}",
            tex_to_color_map={"z": A_PINK, r"\epsilon": A_LAVENDER,
                              r"\int": WHITE, "2": A_YELLOW, "{n}": A_GREEN}
        )
        eq7.scale(1.5)
        eq7.move_to(eq6).shift(2 * DOWN)

        eq8 = Tex(
            r"{{1} \over \sqrt{\epsilon} } \tan^{-1} \left(",
            r"{{z} \over \sqrt{\epsilon}} \right) = {n}",
            tex_to_color_map={"{z}": A_PINK, r"\sqrt{\epsilon}": A_LAVENDER,
                              "{n}": A_GREEN, "{1}": A_YELLOW}
        )
        eq8.scale(1.5)
        eq8.move_to(eq7).shift(2.5 * DOWN)

        eq9 = Tex(r"{z} = \sqrt{\epsilon} \tan \left( \sqrt{\epsilon} {n} \right)",
                  tex_to_color_map={"{z}": A_PINK, "{n}": A_GREEN, r"\sqrt{\epsilon}": A_LAVENDER})
        eq9.scale(1.5)
        eq9.move_to(eq8).shift(2 * DOWN)

        self.play(FadeIn(eq7, DOWN))
        self.play(FadeIn(eq8, DOWN))
        self.play(FadeIn(eq9, DOWN))
        self.wait()

        self.play(FadeOut(VGroup(eq6, eq7, eq8), UP),
                  ApplyMethod(eq9.shift, 6.25 * UP))

        axes = Axes(
            x_range=(-2*PI, 2*PI, PI/2), y_range=(-4, 4, 2), axis_config={"include_tip": False},
            x_axis_config={"stroke_width": 6}, y_axis_config={"stroke_width": 6},
        )
        axes.shift(0.5 * DOWN)

        tanc_kwargs = {
            "color": A_RED,
            "strok_width": 6
        }

        # Split since Manim treats as continuous
        tanc = VGroup(*[
            axes.get_graph(lambda x: np.tan(x), **tanc_kwargs,
                           x_range=(max(-2*PI, np.arctan(-4)+i*PI), min(2*PI, np.arctan(4)+i*PI)))
            for i in range(-2, 3)
        ])

        n_lbl = Tex("n", color=A_GREEN)
        n_lbl.move_to(axes, RIGHT).shift(0.5 * UP)

        self.play(Write(axes), Write(tanc),
                  TransformFromCopy(eq9[-2], n_lbl))
        self.wait()

        t = ValueTracker(0)

        d1, d2 = VMobject(), VMobject()

        def dot_updater(dot, coeff=(1, 1), color=A_AQUA):
            dot.become(
                Dot(axes.c2p(coeff[0] * t.get_value(), np.tan(coeff[1] * t.get_value())), color=color))
        d1.add_updater(lambda dot: dot_updater(dot, (1, 1)))
        d2.add_updater(lambda dot: dot_updater(dot, (-1, -1)))

        part_tanc = VMobject()

        def part_tanc_updater(curve):
            curve.become(axes.get_graph(lambda x: np.tan(
                x), x_range=(-t.get_value(), t.get_value()), color=A_AQUA))
        part_tanc.add_updater(part_tanc_updater)

        d3, d4 = VMobject(), VMobject()
        d3.add_updater(lambda dot: dot_updater(dot, (1, 0), color=A_YELLOW))
        d4.add_updater(lambda dot: dot_updater(dot, (-1, 0), color=A_YELLOW))

        line = VMobject()

        def line_updater(l):
            l.become(Line(axes.c2p(-t.get_value(), 0),
                     axes.c2p(t.get_value(), 0), color=A_YELLOW, stroke_width=10))
        line.add_updater(line_updater)

        self.play(FocusOn(Point(axes.c2p(0, 0))))
        self.play(Write(VGroup(d1, d2, d3, d4, part_tanc, line)))
        self.play(t.increment_value, np.arctan(4), run_time=10)

        d1.clear_updaters()
        d2.clear_updaters()
        part_tanc.clear_updaters()

        self.play(t.increment_value, PI/2-np.arctan(4))
        self.wait()

        b = Brace(line)
        lbl = b.get_tex(
            r"{\pi \over \sqrt{\epsilon}}",
            tex_to_color_map={r"\pi": A_YELLOW, r"\sqrt{\epsilon}": A_LAVENDER})
        b.add_background_rectangle()
        lbl.add_background_rectangle()

        self.play(Write(b), Write(lbl))
        self.wait()

        self.embed()


class TitleScene(Scene):
    CONFIG = {
        "color": None,
        "text": None
    }

    def construct(self):
        if self.text is None:
            raise NotImplementedError

        brect = Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH,
                          fill_opacity=1, color=self.color)

        title = TexText(self.text)
        title.scale(1.5)
        title.to_edge(UP)

        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.add(brect)
        self.play(FadeIn(rect, DOWN), Write(title), run_time=2)
        self.wait()


class TitleU(TitleScene):
    CONFIG = {
        "text": "Upcoming",
        "color": GREY
    }


class TitleC(TitleScene):
    CONFIG = {
        "text": "What you just saw",
        "color": GREY
    }


class TitleW(TitleScene):
    CONFIG = {
        "text": "Wren",
        "color": BLUE_E
    }


class TitleA(Scene):
    def construct(self):
        brect = Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH,
                          fill_opacity=1, color=GREY)

        title1 = TexText("Dave Boll")
        title1.scale(1.5)
        title1.to_edge(UP)

        title2 = TexText("Aaron Klebanoff")
        title2.scale(1.5)
        title2.to_edge(UP)

        rect = ScreenRectangle(height=6)
        rect.next_to(title1, DOWN)

        self.add(brect)
        self.play(FadeIn(rect, DOWN), Write(title1), run_time=2)
        self.wait()

        self.play(Transform(title1, title2))
        self.wait()


class Thumb(Scene):
    def construct(self):
        c = ComplexPlane()
        c.scale(3)
        c.shift(LEFT)

        m = MandelbrotSet(c, color_style=1)
        a = Arrow(3 * RIGHT, ORIGIN, stroke_width=16, stroke_color=A_RED)

        self.add(m)
        self.wait()

        self.embed()
