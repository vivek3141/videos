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
        h1 = TextMobject("4 Characters")
        h12 = TextMobject("4 Characters:")
        t1 = TexMobject("256^4")
        t2 = TexMobject("4294967296")
        t3 = TextMobject("136 Years")
        h12.scale(1.25)
        h1.scale(1.5)
        t1.scale(1.5)
        t2.scale(1.5)
        t3.scale(1.5)
        b.scale(2)
        self.play(Write(b))
        self.play(ApplyMethod(b.shift, 3 * UP))
        self.play(Write(h1))
        self.play(Transform(h1, t1))
        self.play(Transform(h1, t2))
        self.play(Transform(h1, t3))
        self.wait(1)
        self.play(ApplyMethod(h1.shift, 1 * UP))
        h12.next_to(h1, 2 * LEFT)
        self.play(Write(h12))

        h11 = TextMobject("6 Characters")
        h13 = TextMobject("6 Characters:")
        t1 = TexMobject("256^6")
        t2 = TexMobject("28147498" + "0" * 7)
        t3 = TextMobject("900000 Years")
        h13.scale(1.25)
        h11.move_to(1 * DOWN)
        h11.scale(1.5)
        t1.scale(1.5)
        t2.scale(1.5)
        t3.scale(1.5)
        t1.move_to(1 * DOWN)
        t2.move_to(1 * DOWN)
        t3.move_to(1 * DOWN)
        self.play(Write(h11))
        self.play(Transform(h11, t1))
        self.play(Transform(h11, t2))
        self.play(Transform(h11, t3))
        h13.next_to(h11, 2 * LEFT)
        self.play(Write(h13))


class SQLInjection(Scene):
    def construct(self):
        pass
