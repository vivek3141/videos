from manimlib import *


class Scene(Scene):
    def interact(self):
        # If there is a window, enter a loop
        # which updates the frame while under
        # the hood calling the pyglet event loop
        log.info("Tips: You are now in the interactive mode. Now you can use the keyboard"
                 " and the mouse to interact with the scene. Just press `q` if you want to quit.")
        try:
            self.quit_interaction = False
            self.lock_static_mobject_data()
            while not (self.window.is_closing or self.quit_interaction):
                self.update_frame(1 / self.camera.frame_rate)
            if self.window.is_closing:
                self.window.destroy()
            if self.quit_interaction:
                self.unlock_mobject_data()
        except KeyboardInterrupt:
            self.unlock_mobject_data()

class MandelbrotTest(Scene):
    def construct(self):
        self.embed()


ROOT_COLORS_BRIGHT = [RED, GREEN, BLUE, YELLOW, MAROON_B]
ROOT_COLORS_DEEP = ["#440154", "#3b528b", "#21908c", "#5dc963", "#29abca"]
CUBIC_COLORS = [RED_E, TEAL_E, BLUE_E]


MANDELBROT_COLORS = [
    "#00065c",
    "#061e7e",
    "#0c37a0",
    "#205abc",
    "#4287d3",
    "#D9EDE4",
    "#F0F9E4",
    "#BA9F6A",
    "#573706",
]

class MandelbrotFractal(Mobject):
    CONFIG = {
        "shader_folder": "mandelbrot_fractal",
        "shader_dtype": [
            ('point', np.float32, (3,)),
        ],
        "scale_factor": 1.0,
        "offset": ORIGIN,
        "colors": MANDELBROT_COLORS,
        "n_colors": 9,
        "parameter": complex(0, 0),
        "n_steps": 300,
        "mandelbrot": True,
    }

    def __init__(self, plane, **kwargs):
        super().__init__(
            scale_factor=plane.get_x_unit_size(),
            offset=plane.n2p(0),
            **kwargs,
        )
        self.replace(plane, stretch=True)

    def init_uniforms(self):
        Mobject.init_uniforms(self)
        self.uniforms["mandelbrot"] = float(self.mandelbrot)
        self.set_parameter(self.parameter)
        self.set_opacity(self.opacity)
        self.set_scale(self.scale_factor)
        self.set_colors(self.colors)
        self.set_offset(self.offset)
        self.set_n_steps(self.n_steps)

    def init_data(self):
        self.data = {
            "points": np.array([UL, DL, UR, DR]),
        }

    def set_parameter(self, c):
        self.uniforms["parameter"] = np.array([c.real, c.imag])
        return self

    def set_opacity(self, opacity):
        self.uniforms["opacity"] = opacity
        return self

    def set_scale(self, scale_factor):
        self.uniforms["scale_factor"] = scale_factor
        return self

    def set_colors(self, colors):
        for n in range(len(colors)):
            self.uniforms[f"color{n}"] = color_to_rgb(colors[n])
        return self

    def set_offset(self, offset):
        self.uniforms["offset"] = np.array(offset)
        return self

    def set_n_steps(self, n_steps):
        self.uniforms["n_steps"] = float(n_steps)
        return self
