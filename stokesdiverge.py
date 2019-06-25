from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pass


class ThreeDVectorField(ThreeDScene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):

        axes_config = {"x_min": -5,
                       "x_max": 5,
                       "y_min": -5,
                       "y_max": 5,
                       "z_axis_config": {},
                       "z_min": -5,
                       "z_max": 5,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = ThreeDAxes(**axes_config)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP + z * OUT, lambda x, y, z: np.array([np.cos(x), z, y]), prop=0)
              for x in np.arange(-3, 4, 1)
              for y in np.arange(-3, 4, 1)
              for z in np.arange(-3, 4, 1)
              ]
        )

        field = VGroup(axes, f)

        self.play(Write(field))
        self.wait()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.begin_ambient_camera_rotation()
        self.wait(10)

    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y, z = point[:]
        func = f(x, y, z)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2 + func[2] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0])
        func = func / 1.5
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
        return v
