from manimlib.imports import *
import time


E_COLOR = BLUE
M_COLOR = YELLOW


class Intro(Scene):
    def construct(self):
        pass


class Equations(Scene):
    def construct(self):
        title = TextMobject("Maxwell's Equations", color=BLUE)
        title.scale(1.25)
        title.shift(3.5 * UP)

        l = Line(6 * LEFT, 6 * RIGHT, stroke_width=0.5 *
                 DEFAULT_STROKE_WIDTH).shift(3 * UP)

        self.play(Write(title), Write(l))
        self.wait()

        l2 = Line(4 * DOWN, 3 * UP, stroke_widt=0.5 * DEFAULT_STROKE_WIDTH)
        c_color = GOLD

        color_map = {
            r"\phi": ORANGE,
            r"\nabla": RED,
            r"\textbf{B}": M_COLOR,
            r"\textbf{E}": E_COLOR,
            r"\cdot": GREEN,
            r"\cross": GREEN,
            r"\textbf{J}": PURPLE,
            r"\textbf{I}": PURPLE,
            r"\mu_0": c_color,
            r"\epsilon_0": c_color,
            r"\frac{1}{c^2}": MAROON
        }
        eq1 = TexMobject(
            r"\nabla \cdot \textbf{E} = \frac{\rho}{\epsilon_0}", tex_to_color_map=color_map)
        eq2 = TexMobject(
            r"\nabla \cdot \textbf{B} = 0", tex_to_color_map=color_map)
        eq3 = TexMobject(
            r"\nabla \cross \textbf{E} = - {{\partial \textbf{B}} \over {\partial t}}", tex_to_color_map=color_map)
        eq4 = TexMobject(
            r"\nabla \cross \textbf{B} = \mu_0 \textbf{J} + \frac{1}{c^2} {{\partial \textbf{E} } \over {\partial t}}", tex_to_color_map=color_map)

        i1 = TexMobject(
            r"\oint \textbf{E} \cdot d \vec{S} = \frac{Q}{\epsilon_0}", tex_to_color_map=color_map)
        i2 = TexMobject(
            r"\oint \textbf{B} \cdot d \vec{S} = 0", tex_to_color_map=color_map)
        i3 = TexMobject(
            r"\oint \textbf{E} \cdot d \vec{l} = -{{d \phi_{\textbf{B}}} \over {dt}}", tex_to_color_map=color_map)
        i4 = TexMobject(
            r"\oint \textbf{B} \cdot d \vec{l} = \mu_0 \textbf{I} + \frac{1}{c^2} {{d \phi_{\textbf{E}}} \over {dt}}", tex_to_color_map=color_map)

        eq1.shift(2 * UP)
        eq2.shift(0.5 * UP)
        eq3.shift(1 * DOWN)
        eq4.shift(2.5 * DOWN)

        i1.shift(2 * UP)
        i2.shift(0.5 * UP)
        i3.shift(1 * DOWN)
        i4.shift(2.5 * DOWN)

        diff = VGroup(eq1, eq2, eq3, eq4)
        integ = VGroup(i1, i2, i3, i4)

        diff.shift(3.5 * LEFT)
        integ.shift(3.5 * RIGHT)

        self.play(Write(l2))
        self.play(FadeInFromDown(diff), FadeInFromDown(integ))
        self.wait()


class EMScene(Scene):
    CONFIG = {
        "frequency": 1,
        "num_vects": 40,
        "alpha": 1.5,
        "osc_freq": 1
    }

    def construct(self):
        wave = VGroup(
            *[self.get_vect(E_COLOR, t) for t in np.linspace(0, 4*PI, num=self.num_vects)]
        ).center()

        self.play(Write(wave))
        self.wait()

    def get_vect(self, color, t):
        length = self.alpha * np.sin(self.frequency * t)
        return Vector(direction=np.array([0, length, 0]), color=color).shift(t * RIGHT)


class TestWave(ThreeDScene):
    def construct(self):
        wave = EMWave()
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.add(wave)
        self.wait(10)


class Charge(Circle):
    CONFIG = {
        "radius": 0.2,
        "stroke_width": 3,
        "color": RED,
        "fill_color": RED,
        "fill_opacity": 0.5,
        "sign": "+"
    }

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        plus = TexMobject(self.sign)
        plus.scale(0.7)
        plus.move_to(self)
        self.add(plus)


class ACWave(ThreeDScene):
    def construct(self):
        self.pos = VGroup()
        self.neg = VGroup()
        self.update = False
        shift = 6 * LEFT

        for i in range(1, 4):
            charge = Charge()
            charge.shift(i * UP + 0.5 * RIGHT)
            self.pos.add(charge)

            charge = Charge(sign="-", color=BLUE, fill_color=BLUE)
            charge.shift(i * DOWN + 0.5 * RIGHT)
            self.neg.add(charge)

        gen = VGroup()
        rect = Rectangle(height=1, width=1, color=GREEN)
        rect2 = Rectangle(height=0.35, width=0.75, color=RED)
        gen.add(rect)
        gen.add(rect2)
        gen.add(TextMobject("120V").scale(0.5))
        gen.add(Line(0.5 * UP, 3 * UP))
        gen.add(Line(0.5 * DOWN, 3 * DOWN))

        gen.shift(shift)
        self.neg.shift(shift)
        self.pos.shift(shift)

        self.neg2 = self.neg.copy()
        self.neg2.shift(4 * UP)

        self.pos2 = self.pos.copy()
        self.pos2.shift(4 * DOWN)

        self.neg3 = self.neg.copy()
        self.pos3 = self.pos.copy()

        self.play(Write(gen))
        self.play(Write(self.pos), Write(self.neg))

        wave = EMWave(frequency=1/3)
        self.add(wave)

        self.move_camera(0.4 * np.pi / 2, -PI/2)

        for i in range(3):
            self._update()

    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if self.update:
            pass

    def _update(self):
        self.play(Transform(self.pos, self.neg2),
                  Transform(self.neg, self.pos2))
        self.wait(0.5)
        self.play(Transform(self.pos, self.pos3),
                  Transform(self.neg, self.neg3))
        self.wait(0.5)
