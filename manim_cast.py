from manimlib.imports import *


class ParabolaGraph(GraphScene):
    CONIFG = {
        "x_min": -2,
        "x_max": 6,
        "y_max": 10,
        "y_min": -4
    }

    def construct(self):
        self.setup_axes()
        f = self.get_graph(lambda x: 0.25 * math.pow(x, 2))

        self.play(Write(f))
        self.wait()


class NumberLineTest(Scene):
    def construct(self):
        a = Axes(
            x_min=-3,
            x_max=3,
            y_min=-3,
            y_max=3,
            axis_config={
                "include_tip": False,
            }
        )
        f = ParametricFunction(self.func, t_min=0, t_max=2*PI,
                               color=BLUE)
        self.add(a, f)

    def func(self, t):
        return [2*math.sin(t), math.cos(t), 0]


class ThreeDGraph(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5.5,
            "x_max": 5.5,
            "y_min": -5.5,
            "y_max": 5.5,
            "z_min": -3.5,
            "z_max": 3.5,
        }
        a = ThreeDAxes(**axis_config)
        surface = ParametricSurface(self.sur,u_min=-3, u_max=3, v_min=-3, v_max=3)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.add(a, surface)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.wait(10)
        

    def sur(self, u, v):
        return [u, v, u**2 + v**2]