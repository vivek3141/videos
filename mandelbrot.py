from manimlib import *


# MANDELBROT_COLORS = [
#     "#00065c",
#     "#061e7e",
#     "#0c37a0",
#     "#205abc",
#     "#4287d3",
#     "#D9EDE4",
#     "#F0F9E4",
#     "#BA9F6A",
#     "#573706",
# ]


class MandelbrotFractal(Mobject):
    CONFIG = {
        "shader_folder": "/Users/vivek/python/videos/shaders/mandelbrot",
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

# class Test(Mobject):
#     CONFIG = {
#         "shader_folder": "/Users/vivek/python/videos/shaders/mandelbrot",
#         "shader_dtype": [
#             ('point', np.float32, (3,)),
#         ],
#         "scale_factor": 1.0,
#         "offset": ORIGIN,
#         "colors": MANDELBROT_COLORS,
#         "n_colors": 9,
#         "parameter": complex(0, 0),
#         "n_steps": 300,
#         "mandelbrot": True,
#     }

#     def __init__(self, plane, **kwargs):
#         super().__init__(
#             scale_factor=plane.get_x_unit_size(),
#             offset=plane.n2p(0),
#             **kwargs,
#         )
#         self.replace(plane, stretch=True)

#     def init_uniforms(self):
#         Mobject.init_uniforms(self)
#         self.uniforms["mandelbrot"] = float(self.mandelbrot)
#         self.set_parameter(self.parameter)
#         self.set_opacity(self.opacity)
#         self.set_scale(self.scale_factor)
#         self.set_colors(self.colors)
#         self.set_offset(self.offset)
#         self.set_n_steps(self.n_steps)

#     def init_data(self):
#         self.data = {
#             "points": np.array([UL, DL, UR, DR]),
#         }

#     def set_parameter(self, c):
#         self.uniforms["parameter"] = np.array([c.real, c.imag])
#         return self

#     def set_opacity(self, opacity):
#         self.uniforms["opacity"] = opacity
#         return self

#     def set_scale(self, scale_factor):
#         self.uniforms["scale_factor"] = scale_factor
#         return self

#     def set_colors(self, colors):
#         for n in range(len(colors)):
#             self.uniforms[f"color{n}"] = color_to_rgb(colors[n])
#         return self

#     def set_offset(self, offset):
#         self.uniforms["offset"] = np.array(offset)
#         return self

#     def set_n_steps(self, n_steps):
#         self.uniforms["n_steps"] = float(n_steps)
#         return self


# class MandelbrotFractal(Mobject):
#     CONFIG = {
#         "shader_folder": "mandelbrot_fractal",
#         "shader_dtype": [
#             ('point', np.float32, (3,)),
#         ],
#         "scale_factor": 1.0,
#         "offset": ORIGIN,
#         "colors": MANDELBROT_COLORS,
#         "n_colors": 9,
#         "parameter": complex(0, 0),
#         "n_steps": 300,
#         "mandelbrot": True,
#     }

#     def __init__(self, plane, **kwargs):
#         super().__init__(
#             scale_factor=plane.get_x_unit_size(),
#             offset=plane.n2p(0),
#             **kwargs,
#         )
#         self.replace(plane, stretch=True)

#     def init_uniforms(self):
#         Mobject.init_uniforms(self)
#         self.uniforms["mandelbrot"] = float(self.mandelbrot)
#         self.set_parameter(self.parameter)
#         self.set_opacity(self.opacity)
#         self.set_scale(self.scale_factor)
#         self.set_colors(self.colors)
#         self.set_offset(self.offset)
#         self.set_n_steps(self.n_steps)

#     def init_data(self):
#         self.data = {
#             "points": np.array([UL, DL, UR, DR]),
#         }

#     def set_parameter(self, c):
#         self.uniforms["parameter"] = np.array([c.real, c.imag])
#         return self

#     def set_opacity(self, opacity):
#         self.uniforms["opacity"] = opacity
#         return self

#     def set_scale(self, scale_factor):
#         self.uniforms["scale_factor"] = scale_factor
#         return self

#     def set_colors(self, colors):
#         for n in range(len(colors)):
#             self.uniforms[f"color{n}"] = color_to_rgb(colors[n])
#         return self

#     def set_offset(self, offset):
#         self.uniforms["offset"] = np.array(offset)
#         return self

#     def set_n_steps(self, n_steps):
#         self.uniforms["n_steps"] = float(n_steps)
#         return self
