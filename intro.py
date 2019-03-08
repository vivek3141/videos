from manim import *


class Intro(Scene):
    def construct(self):
        logo = SVGMobject("files/logo_t.svg")
        self.play(Write(logo))
        self.wait()


class ElectricField(ThreeDScene):
    """def reset(self):
        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line60),
        )
        self.play(
            Transform(line0, line0),
            Transform(line1, line1),
            Transform(line2, line2),
            Transform(line3, line3),
            Transform(line4, line4),
            Transform(line5, line5),
            Transform(line6, line6),
        )"""
    def construct(self):
        OPACITY = 0.1
        line0 = Line(3 * DOWN + 0.5 * LEFT, 2 * DOWN + 0.5 * LEFT, stroke_width=8)
        line1 = Line(2 * DOWN + 0.5 * LEFT, 2 * DOWN + 2 * LEFT, stroke_width=8)
        line3 = Line(2 * UP + 2 * LEFT, 2 * UP + 2 * RIGHT, stroke_width=8)
        line4 = Line(2 * UP + 2 * RIGHT, 2 * DOWN + 2 * RIGHT, stroke_width=8)
        line2 = Line(2 * DOWN + 2 * LEFT, 2 * UP + 2 * LEFT, stroke_width=8)
        line5 = Line(2 * DOWN + 2 * RIGHT, 2 * DOWN + 0.5 * RIGHT, stroke_width=8)
        line6 = Line(2 * DOWN + 0.5 * RIGHT, 3 * DOWN + 0.5 * RIGHT, stroke_width=8)

        line00 = Line(3 * DOWN + 0.5 * LEFT, 2 * DOWN + 0.5 * LEFT, stroke_opacity=OPACITY)
        line10 = Line(2 * DOWN + 0.5 * LEFT, 2 * DOWN + 2 * LEFT, stroke_opacity=OPACITY)
        line30 = Line(2 * UP + 2 * LEFT, 2 * UP + 2 * RIGHT, stroke_opacity=OPACITY)
        line40 = Line(2 * UP + 2 * RIGHT, 2 * DOWN + 2 * RIGHT, stroke_opacity=OPACITY)
        line20 = Line(2 * DOWN + 2 * LEFT, 2 * UP + 2 * LEFT, stroke_opacity=OPACITY)
        line50 = Line(2 * DOWN + 2 * RIGHT, 2 * DOWN + 0.5 * RIGHT, stroke_opacity=OPACITY)
        line60 = Line(2 * DOWN + 0.5 * RIGHT, 3 * DOWN + 0.5 * RIGHT, stroke_opacity=OPACITY)

        arrow = Arrow(ORIGIN, 1 * UP, color=RED)
        arrow.move_to(line2, 1 * LEFT)

        circle = Circle()
        circle.rotate(np.pi / 4, axis=X_AXIS)
        circle.shift(2 * LEFT)

        head = TextMobject("Isolate segment 1", color=BLUE)
        head.scale(1.25)
        head.shift(3 * UP)

        head3 = TextMobject("Do the same for every other segment", color=BLUE)
        head3.scale(1.25)
        head3.shift(3 * UP)

        head2 = TextMobject("Find the direction of magnetic field at A, B, C, D  \\ only using this current", color=GREEN)
        head2.scale(1.25)
        head2.shift(3 * DOWN)

        self.play(Write(line0))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.play(Write(line6))

        self.wait()

        self.play(Write(arrow))
        self.play(Write(circle))

        self.wait()

        self.play(Write(head))

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line60),
        )

        self.wait()
        self.play(Write(head2))

        self.wait()

        self.play(Transform(head, head3))
        self.wait()

        self.play(
            Transform(line0, line0),
            Transform(line1, line1),
            Transform(line2, line2),
            Transform(line4, line4),
            Transform(line5, line5),
            Transform(line6, line6),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line4),
            Transform(line5, line50),
            Transform(line6, line60),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line5),
            Transform(line6, line60),
        )
        self.wait()

        self.play(
            Transform(line0, line00),
            Transform(line1, line10),
            Transform(line2, line20),
            Transform(line3, line30),
            Transform(line4, line40),
            Transform(line5, line50),
            Transform(line6, line6),
        )
        self.wait()
