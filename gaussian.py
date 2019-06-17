from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        f = ParametricFunction(
            function=self.func
            t_min=-3,
            t_max=3,
            color=BLUE
        )

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )

        func = VGroup(axes, f)
        func.scale(2)
        func.shift(2 * DOWN)

        eq1 = TexMobject(r"f(x) = e^{-x^2}")
        eq1.scale(1.5)
        eq1.shift(3 * UP)

        eq2 = TexMobject(r"\int_{-\infty}^{\infty} e^{-x^2} \ dx = \sqrt{\pi}")
        eq2.scale(1.5)
        eq2.shift(3 * UP)

        self.play(Write(func))
        self.wait()

        self.play(Write(eq1))
        self.wait()

    def get_riemann_rectangles(
        self,
        graph,
        x_min=None,
        x_max=None,
        dx=0.1,
        input_sample_type="left",
        stroke_width=1,
        stroke_color=BLACK,
        fill_opacity=1,
        start_color=None,
        end_color=None,
        show_signed_area=True,
        width_scale_factor=1.001
    ):
        x_min = x_min if x_min is not None else self.x_min
        x_max = x_max if x_max is not None else self.x_max
        if start_color is None:
            start_color = self.default_riemann_start_color
        if end_color is None:
            end_color = self.default_riemann_end_color
        rectangles = VGroup()
        x_range = np.arange(x_min, x_max, dx)
        colors = color_gradient([start_color, end_color], len(x_range))
        for x, color in zip(x_range, colors):
            if input_sample_type == "left":
                sample_input = x
            elif input_sample_type == "right":
                sample_input = x + dx
            elif input_sample_type == "center":
                sample_input = x + 0.5 * dx
            else:
                raise Exception("Invalid input sample type")
            graph_point = self.input_to_graph_point(sample_input, graph)
            points = VGroup(*list(map(VectorizedPoint, [
                self.coords_to_point(x, 0),
                self.coords_to_point(x + width_scale_factor * dx, 0),
                graph_point
            ])))

            rect = Rectangle()
            rect.replace(points, stretch=True)
            if graph_point[1] < self.graph_origin[1] and show_signed_area:
                fill_color = invert_color(color)
            else:
                fill_color = color
            rect.set_fill(fill_color, opacity=fill_opacity)
            rect.set_stroke(stroke_color, width=stroke_width)
            rectangles.add(rect)
        return rectangles

    def func(self, t):
        return np.array([t, np.exp(-t**2), 0])


class GaussianVisual(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=-2,
            u_max=2,
            v_min=-2,
            v_max=2
        ).scale(2)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    def func(self, u, v):
        return np.array([
            u,
            v,
            np.exp(-(u**2 + v**2))
        ])
