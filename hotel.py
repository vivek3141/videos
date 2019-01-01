from manim import *


class Intro(Scene):
    def construct(self):
        hotel = SVGMobject(file_name="files/hotel.svg")
        plane = SVGMobject(file_name="files/black-plane.svg")
        hotel.move_to(3 * RIGHT)
        plane.move_to(3 * LEFT)
        self.play(Write(plane))
        self.play(Write(hotel), ApplyMethod(plane.shift, 3.5 * RIGHT))


class Wifi(Scene):
    def construct(self):
        wifi = SVGMobject(file_name="files/wifi.svg")
        self.play(Write(wifi))


class Reconnaissance(Scene):
    def construct(self):
        r = TextMobject("Reconnaissance", color=BLUE)
        r.scale(3)
        self.play(Write(r))
        self.wait(2)
        self.play(ApplyMethod(r.shift, 1 * UP))
        t = TextMobject("Act of information gathering")
        t.shift(1 * DOWN)
        t.scale(1.5)
        self.play(Write(t))


class Defining(Scene):
    def construct(self):
        d = TextMobject("Defining The Problem", color=RED)
        d.scale(2)
        self.play(Write(d))


class BruteForce(Scene):
    def construct(self):
        b = TextMobject("Brute Force", color=YELLOW)
        b.scale(2)
        self.play(Write(b))
        self.play(ApplyMethod(b.shift, 2*UP))
        h1 = TextMobject("")
