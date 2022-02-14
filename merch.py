from manimlib import *

h1 = "#ff5757"
h1_d = "#890000"

h2 = '#5ce1e6'
h2_d = "#116c70"

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


class Hoodie2(Scene):
    def construct(self):
        text = Tex(r"\textbf{\text{v}} ^3 \textbf{\text{(}}\textbf{\text{x}}\textbf{\text{)}}}", tex_to_color_map={
            r'\textbf{\text{v}} ^3': h1,
            r'\textbf{\text{x}}': h2
        }, color=BLACK)
        text.scale(4)

        def func(z):
            return (1+np.sqrt(3)*1j)*z

        complex_kwargs = {
            "background_line_style": {
                "stroke_opacity": 0.85,
                "stroke_width": 6
            }
        }
        c = ComplexPlane(**complex_kwargs)
        c.prepare_for_nonlinear_transform()
        c.apply_complex_function(lambda z: (1+np.sqrt(3)*1j)*z)
        self.add(c)

        # text.apply_complex_function(func)
        # text.scale(0.8)
        self.add(text)

        self.embed()


class LogoTransparent(Scene):
    def construct(self):
        text = Tex(r"\textbf{\text{v}} ^3 \textbf{\text{(}}\textbf{\text{x}}\textbf{\text{)}}}", tex_to_color_map={
            r'\textbf{\text{v}} ^3': h1,
            r'\textbf{\text{x}}': h2
        }, color=WHITE)
        text.scale(4)

        def func(z):
            return (1+np.sqrt(3)*1j)*z
        text.apply_complex_function(func)
        text.scale(0.5)
        self.add(text)


class Hoodie3(Scene):
    CONFIG = {
        "plane_opacity": 0.85,
        "x": 0.5,
        "y": 0.5,
        "vec_opacity": 1
    }

    def construct(self):
        complex_kwargs = {
            "background_line_style": {
                "stroke_opacity": self.plane_opacity,
                "stroke_color": BLUE_E,
                "stroke_width": 6
            }
        }
        text = Tex(r"\textbf{\text{v}} ^3 \textbf{\text{(}}\textbf{\text{x}}\textbf{\text{)}}}", tex_to_color_map={
            r'\textbf{\text{v}} ^3': h1,
            r'\textbf{\text{x}}': h2
        }, color=WHITE)
        text.scale(4)

        c2 = ComplexPlane(x_range=(-3, 3), y_range=(-3, 3), **complex_kwargs)
        c2.shift(FRAME_WIDTH/4 * RIGHT)
        c2.prepare_for_nonlinear_transform()
        c2.apply_complex_function(self.func)

        def func(z):
            return (1+np.sqrt(3)*1j)*z
        text.apply_complex_function(func)
        text.scale(0.5)
        self.add(c2)
        self.embed()

    def get_vec(self, plane, coors, **kwargs):
        x, y = coors[0], coors[1]
        z = plane.c2p(x, y)
        return Arrow(plane.c2p(0, 0), z, buff=0, **kwargs)

    def f_deriv(self, z, dz=1e-6+1e-6*1j):
        return (self.func(z+dz)-self.func(z))/dz

    def func(self, z):
        return (1*z + np.sin(z)) * 0.3 - 1


class HText(Scene):
    def construct(self):
        t = Tex(r"f'(z) = 1 + \sqrt{3}i", color=BLACK)
        t.scale(4)
        self.add(t)
