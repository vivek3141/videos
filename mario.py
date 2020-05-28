from manimlib.imports import *
from scipy.optimize import curve_fit


def yx2features(ran=[0, 5], number=100):

    def func(): return ((max(ran) - min(ran) + 1) * np.random.random(number)) + min(ran)
    x1 = np.array(func)
    x2 = np.array(list(map(lambda z: int(z), func())))
    y = np.array([1 if x1[i] > x2[i] else 0 for i in range(number)])
    data = [[x1[i], x2[i]] for i in range(number)]

    return data, y


class LinReg(Scene):
    def construct(self):
        xdata = np.linspace(0.25, 5.75, 15)
        ydata = [self.func(i) + 2 * (np.random.random() - 0.5) for i in xdata]

        def f(x, a, b):
            return a * x + b

        theta, _ = curve_fit(f, xdata, ydata)

        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        points = VGroup(
            *[Dot(
                [xdata[i], ydata[i], 0],
                color=BLUE,
                radius=0.75 * DEFAULT_DOT_RADIUS
            ) for i in range(15)]
        )

        line = FunctionGraph(lambda x: f(x, *theta),
                             x_min=0, x_max=6, color=RED)
        dlines = VGroup(
            DashedLine(2.9 * RIGHT, f(2.9, *theta) * UP + 2.9 * RIGHT),
            DashedLine(f(2.9, *theta) * UP, f(2.9, *theta) * UP + 2.9 * RIGHT)
        )

        grp1 = VGroup(axes, points, line)
        grp = VGroup(grp1, dlines)
        grp.center()

        self.play(Write(axes))
        self.play(Write(points), Write(line))
        self.wait()

        xlbl = TextMobject("Plot Size (ft\(^2\))")
        xlbl.shift(3 * DOWN)

        ylbl = TextMobject(r"Market Price (\$)")
        ylbl.rotate(PI/2)
        ylbl.shift(4 * LEFT + 0.5 * UP)

        self.play(grp1.shift, 0.5 * UP)
        dlines.shift(0.5 * UP)
        self.play(FadeInFromDown(xlbl), FadeInFromDown(ylbl))

        lbl = TexMobject(
            f"\\hat{{ \\text{{price}}}} = {round(theta[0], 2)} + {round(theta[1], 2)} \\ \\text{{size}}", color=RED)
        lbl.shift(5 * RIGHT + 2 * UP)
        lbl.scale(0.75)

        ypoint = Dot([0, 0.32, 0], color=YELLOW, radius=0.08)

        self.play(points.set_opacity, 0.5)
        self.play(Write(lbl), Write(dlines), Write(ypoint))
        self.wait()

    @staticmethod
    def func(x):
        return 0.425 * x + 0.785


class LogReg(Scene):
    def construct(self):
        n = 100
        points = []
        colors = []
        c1 = "#99EDCC"
        c2 = "#B85C8C"

        for _ in range(n):
            point = np.random.random(2) * 5.5 + 0.25
            points.append(point)
            colors.append(1 if point[0] > point[1] else 0)

        pointg = VGroup(
            *[Dot([points[i][0], points[i][1], 0], color=c1 if colors[i] else c2) for i in range(len(colors))]
        )
        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=6,
            axis_config={
                "include_tip": False
            }
        )
        line = FunctionGraph(lambda x: x, x_min=0, x_max=6)
        grp = VGroup(axes, pointg, line)
        grp.center()

        self.play(Write(axes))
        self.play(Write(pointg))
        self.wait()

        self.play(ApplyMethod(pointg.set_opacity, 0.5), Write(line))
        self.wait()

        self.play(grp.shift, 3 * LEFT)
        eq1 = TexMobject(r"\hat{y} = ", r"\sigma ( ", r"b_0 + b_1 x ", r")",
                         tex_to_color_map={r"x": GREEN, "y": GOLD, r"\sigma": YELLOW})
        eq1.scale(1.5)
        eq1.shift(3.5 * RIGHT)

        self.play(Write(VGroup(eq1[:3], eq1[5:7])))
        self.wait()

        self.play(FadeInFromDown(VGroup(eq1[3:5], eq1[7])))
        self.wait()

        eq2 = TexMobject(
            r"\sigma ( x ) = \frac{1}{1 + e^{-x}}", tex_to_color_map={r"\sigma": YELLOW})
        eq2.scale(1.5)
        eq2.shift(2.75 * UP)

        self.play(Uncreate(grp))
        self.play(TransformFromCopy(eq1[3], eq2[0]))
        self.play(Write(eq2[1:]))
        self.play(Uncreate(VGroup(eq1)))
        self.wait()

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=0,
            y_max=2,
            axis_config={
                "include_tip": False
            }
        )
        eq = FunctionGraph(lambda x: 2/(1+np.exp(-2*x)),
                           x_min=-3, x_max=3, color=GOLD)
        grp2 = VGroup(axes, eq)
        grp2.scale(2)
        grp2.center()
        grp2.shift(DOWN)

        lbls = VGroup(
            TexMobject("0.5").shift(DOWN),
            TexMobject("1.0").shift(UP)).shift(0.75 * LEFT + 0.2 * UP)

        self.play(Write(grp2))
        self.wait()

        self.play(Write(lbls))
        self.wait()
