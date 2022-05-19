from manimlib import *


class MandelbrotFractal(Mobject):
    CONFIG = {
        "shader_folder": "shaders/mandelbrot",
        "fractal_scale_factor": 2.5,
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
        self.uniforms["scale_factor"] = self.fractal_scale_factor
        self.uniforms["opacity"] = self.opacity
        self.uniforms["num_steps"] = self.num_steps
        self.uniforms["max_arg"] = self.max_arg

    def init_data(self):
        self.data = {
            "points": np.array([UL, DL, UR, DR]),
        }


class MandelbrotTest(Scene):
    def construct(self):
        c = ComplexPlane()
        t = MandelbrotFractal(c)
        self.add(t)
        self.embed()
