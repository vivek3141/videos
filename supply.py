from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        w = SVGMobject("./img/covid20.svg")
        self.add(w)
        self.wait()
        
class DemandTitle(Scene):
    def construct(self):
        part = TextMobject("Part 1")
        part.scale(1.5)
        part.shift(2 * UP)

        title = TextMobject("Demand", color=RED)
        title.scale(1.5)

        self.play(Write(part))
        self.play(Write(title))
        self.wait()
    
class Demand(Scene):
    def construct(self):
        l = 5.5
        pad = 1.5
        f1 = TextMobject("Demand:", color=RED)
        f1.shift(l * LEFT + (pad + 0.75) * UP)
        f1.scale(1.25)

        f2 = TextMobject("Fact 2:")
        f2.shift(l * LEFT + (pad - 0.75) * DOWN)
        f2.scale(1.25)

        fact1 = TextMobject(
            r"The amount of some good or service \\ \
                consumers are willing to buy at \\ \
                a specific price", alignment=r"")

        fact1.shift(pad * UP + 1 * RIGHT)
        fact1.scale(1.25)

        self.play(FadeInFromDown(f1))
        self.play(Write(fact1))
        self.wait()


class Supply(Scene):
    def construct(self):
        l = 5.5
        pad = 1.5
        f1 = TextMobject("Supply:", color=BLUE)
        f1.shift(l * LEFT + (pad + 0.75) * UP)
        f1.scale(1.25)

        fact1 = TextMobject(
            r"The amount of some good or service \\ \
                manufacturers are willing to supply at \\ \
                a specific price", alignment=r"")

        fact1.shift(pad * UP + 1 * RIGHT)
        fact1.scale(1.25)

        self.play(FadeInFromDown(f1))
        self.play(Write(fact1))
        self.wait()


class DemandGraph(Scene):
    def construct(self):
        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        line = FunctionGraph(self.func,
                             x_min=0, x_max=6, color=RED)

        grp = VGroup(axes, line)
        grp.center()

        xlbl = TextMobject("Quantity")
        xlbl.shift(3 * DOWN)

        ylbl = TextMobject(r"Price (\$)")
        ylbl.rotate(PI/2)
        ylbl.shift(4 * LEFT + 0.5 * UP)

        self.play(Write(axes))
        self.play(Write(line))
        self.play(FadeInFromDown(xlbl), FadeInFromDown(ylbl))
        self.wait()

    @staticmethod
    def func(x):
        return -0.5 * x + 4

class SupplyGraph(Scene):
    def construct(self):
        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        line = FunctionGraph(self.func,
                             x_min=0, x_max=6, color=BLUE)

        grp = VGroup(axes, line)
        grp.center()

        xlbl = TextMobject("Quantity")
        xlbl.shift(3 * DOWN)

        ylbl = TextMobject(r"Price (\$)")
        ylbl.rotate(PI/2)
        ylbl.shift(4 * LEFT + 0.5 * UP)

        self.play(Write(axes))
        self.play(Write(line))
        self.play(FadeInFromDown(xlbl), FadeInFromDown(ylbl))
        self.wait()

    @staticmethod
    def func(x):
        return 0.425 * x + 0.785

class SupplyAndDemand(Scene):
    def construct(self):
        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=5,
            axis_config={
                "include_tip": False
            }
        )

        supply = FunctionGraph(self.supply,
                             x_min=0, x_max=6, color=BLUE)
        
        demand = FunctionGraph(self.demand, x_min=0, x_max=6, color=RED)

        point = Dot(point=[3.475, 2.262, 0], color=YELLOW)

        grp = VGroup(axes, supply, demand, point)
        grp.center()

        xlbl = TextMobject("Quantity")
        xlbl.shift(3 * DOWN)

        ylbl = TextMobject(r"Price (\$)")
        ylbl.rotate(PI/2)
        ylbl.shift(4 * LEFT + 0.5 * UP)

        self.play(Write(axes))
        self.play(Write(demand))
        self.play(Write(supply))
        self.play(FadeInFromDown(xlbl), FadeInFromDown(ylbl))
        self.wait()

        self.play(Write(point))
        self.wait()

        

    @staticmethod
    def demand(x):
        return -0.5 * x + 4
    
    @staticmethod
    def supply(x):
        return 0.425 * x + 0.785