from manim import *


class Intro(Scene):
    def construct(self):
        text = TextMobject("Why do we use Mean Squared Error?", tex_to_color_map={"Mean Squared Error": YELLOW})
        text.scale(1.5)
        self.play(Write(text))


class CostFunction(Scene):
    def construct(self):
        text = TextMobject("Cost Function", tex_to_color_map={"Cost Function": YELLOW})
        text2 = TextMobject("not", tex_to_color_map={"not": RED})
        eq2 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} |h_\\theta (x^{(i)}) - y^{(i)}| $")
        eq1 = TextMobject("$\\frac{1}{2m} \\sum_{i=1}^{m} (h_\\theta (x^{(i)}) - y^{(i)})^2 $")
        text.scale(2)
        eq1.scale(2.5)
        eq2.scale(2.5)
        text2.scale(2)
        eq2.move_to(3 * DOWN)
        text.move_to(3 * UP)
        self.play(Write(text))
        self.play(Transform(text, eq1))
        self.play(ApplyMethod(text.shift, 3 * UP))
        self.play(Write(text2))
        self.play(Write(eq2))
        self.wait(2)


class ExampleThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "point_charge_loc": 0.5 * RIGHT - 1.5 * UP,
    }

    def construct(self):
        self.set_camera_position(0, -np.pi / 2)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x * RIGHT + y * UP)
                           for x in np.arange(-9, 9, 1)
                           for y in np.arange(-5, 5, 1)
                           ])

        self.play(ShowCreation(field2D))
        self.wait()
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)

    def calc_field2D(self, point):
        x, y = point[:2]
        Rx, Ry = self.point_charge_loc[:2]
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return Vector(efield).shift(point)
