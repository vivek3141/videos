from manim import *


class LineIntegral(ThreeDScene):
    CONFIG = {
        "u_min": 0,
        "u_max": 1,
        "v_min": 0,
        "v_max": 1,
        "resolution": 6,
        "surface_piece_config": {},
        "fill_color": BLUE_D,
        "fill_opacity": 1.0,
        "checkerboard_colors": [BLUE_D, BLUE_E],
        "stroke_color": LIGHT_GREY,
        "stroke_width": 0.5,
        "should_make_jagged": False,
        "pre_function_handle_to_anchor_scale_factor": 0.00001,
    }
    def construct(self):
        self.set_camera_orientation(0.8 * np.pi / 2, -0.45 * np.pi)
        surface = ParametricSurface(self.func)
        self.play(ShowCreation(ThreeDAxes))
        self.play(ShowCreation(surface))
        self.wait()

        self.begin_ambient_camera_rotation()
        self.wait(6)

    def func(self, u, v):
        return np.array([
            u,
            v,
            u**2 + v**2
        ])
