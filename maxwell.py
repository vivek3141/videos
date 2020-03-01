from manimlib.imports import *
import time


E_COLOR = BLUE
M_COLOR = YELLOW


class ThreeDArrow(Line):
    CONFIG = {
        "tip_length": 0.25,
        "tip_width_to_length_ratio": 1,
        "max_tip_length_to_length_ratio": 0.35,
        "max_stem_width_to_tip_width_ratio": 0.3,
        "buff": MED_SMALL_BUFF,
        "propagate_style_to_family": False,
        "preserve_tip_size_when_scaling": True,
        "normal_vector": OUT,
        "use_rectangular_stem": True,
        "rectangular_stem_width": 0.05,
    }

    def __init__(self, *args, **kwargs):
        points = list(map(self.pointify, args))
        if len(args) == 1:
            args = (points[0] + UP + LEFT, points[0])
        Line.__init__(self, *args, **kwargs)
        self.add_tip()

    def add_tip(self, add_at_end=True):
        tip = VMobject(
            close_new_points=True,
            mark_paths_closed=True,
            fill_color=self.color,
            fill_opacity=1,
            stroke_color=self.color,
            stroke_width=0,
        )
        tip.add_at_end = add_at_end
        self.set_tip_points(tip, add_at_end, preserve_normal=False)
        self.add(tip)
        if not hasattr(self, 'tip'):
            self.tip = VGroup()
            self.tip.match_style(tip)
        self.tip.add(tip)
        return tip

    def set_tip_points(
        self, tip,
        add_at_end=True,
        tip_length=None,
        preserve_normal=True,
    ):
        if tip_length is None:
            tip_length = self.tip_length
        if preserve_normal:
            normal_vector = self.get_normal_vector()
        else:
            normal_vector = self.normal_vector
        line_length = get_norm(self.points[-1] - self.points[0])
        tip_length = min(
            tip_length, self.max_tip_length_to_length_ratio * line_length
        )

        indices = (-2, -1) if add_at_end else (1, 0)
        pre_end_point, end_point = [
            self.get_anchors()[index]
            for index in indices
        ]
        vect = end_point - pre_end_point
        perp_vect = np.cross(vect, normal_vector)
        for v in vect, perp_vect:
            if get_norm(v) == 0:
                v[0] = 1
            v *= tip_length / get_norm(v)
        ratio = self.tip_width_to_length_ratio
        tip.set_points_as_corners([
            end_point,
            end_point - vect + perp_vect * ratio / 2,
            end_point - vect - perp_vect * ratio / 2,
        ])

        return self

    def get_normal_vector(self):
        p0, p1, p2 = self.tip[0].get_anchors()[:3]
        result = np.cross(p2 - p1, p1 - p0)
        norm = get_norm(result)
        if norm == 0:
            return self.normal_vector
        else:
            return result / norm

    def reset_normal_vector(self):
        self.normal_vector = self.get_normal_vector()
        return self

    def get_end(self):
        if hasattr(self, "tip"):
            return self.tip[0].get_anchors()[0]
        else:
            return Line.get_end(self)

    def get_tip(self):
        return self.tip

    def put_start_and_end_on(self, *args, **kwargs):
        Line.put_start_and_end_on(self, *args, **kwargs)
        self.set_tip_points(self.tip[0], preserve_normal=False)
        self.set_rectangular_stem_points()
        return self

    def scale(self, scale_factor, **kwargs):
        Line.scale(self, scale_factor, **kwargs)
        if self.preserve_tip_size_when_scaling:
            for t in self.tip:
                self.set_tip_points(t, add_at_end=t.add_at_end)
        if self.use_rectangular_stem:
            self.set_rectangular_stem_points()
        return self

    def copy(self):
        return self.deepcopy()


class ThreeDVector(ThreeDArrow):
    CONFIG = {
        "color": YELLOW,
        "buff": 0,
    }

    def __init__(self, direction, **kwargs):
        if len(direction) == 2:
            direction = np.append(np.array(direction), 0)
        ThreeDArrow.__init__(self, ORIGIN, direction, **kwargs)


class EMWave(VGroup):
    def __init__(
        self,
        E_COLOR=YELLOW, M_COLOR=BLUE,
        frequency=1,
        alpha=1,
        num_vects=30,
        start=-FRAME_WIDTH/2,
        end=FRAME_WIDTH/2,
        **kwargs
    ):
        VGroup.__init__(self, **kwargs)
        self.alpha = alpha
        self.frequency = frequency
        self.start = start
        self.end = end
        self.tracker = ValueTracker(0)
        e_wave = VGroup(
            *[self.get_vect(E_COLOR, t, direction=UP) for t in np.linspace(self.start, self.end, num=num_vects)]
        )
        m_wave = VGroup(
            *[self.get_vect(M_COLOR, t, direction=IN) for t in np.linspace(self.start, self.end, num=num_vects)]
        )
        self.add(e_wave)
        self.add(m_wave)

    def get_x(self, value):
        return value - self.start

    def get_vect(self, color, t, direction=IN):
        length = self.alpha * np.sin(self.get_x(t))
        vect = ThreeDVector(direction=direction * length,
                            color=color).shift(t * RIGHT)
        vect.add_updater(lambda obj: obj.become(
            self.get_vect_updater(self.tracker.get_value(), color, t, direction=direction)))
        return vect

    def get_vect_updater(self, t, color, phi, direction=IN):
        length = self.alpha * np.sin(self.frequency * (self.get_x(t) + phi))
        return ThreeDVector(length * direction, color=color).shift(phi * RIGHT)


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


class EMTest(ThreeDScene):
    def construct(self):
        wave = EMWave()
        self.add(wave)
        self.move_camera(0.4 * np.pi / 2, -PI/2)
        self.play(wave.tracker.increment_value, 4 *
                  PI, run_time=4, rate_func=linear)


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
