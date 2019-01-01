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


class ProgramStructure(Scene):
    def construct(self):
        html = SVGMobject("files/html.svg", color=ORANGE)
        py = SVGMobject("files/python.svg", color=YELLOW)
        js = SVGMobject("files/js.svg", color=YELLOW)
        db = SVGMobject("files/database.svg")
        html.move_to(3.5 * LEFT + 1 * UP)
        js.move_to(3.5 * LEFT + 1 * DOWN)
        html.scale(0.75)
        js.scale(0.75)
        py.scale(0.75)
        db.scale(0.75)
        db.move_to(3.5 * RIGHT)
        a1 = Arrow(ORIGIN, 2 * RIGHT, color=BLUE)
        a1.next_to(html, 1 * DOWN + 1 * RIGHT)
        a2 = Arrow(ORIGIN, 2 * RIGHT, color=BLUE)
        a2.next_to(py, 1 * RIGHT)
        self.play(Write(html), Write(js))
        self.play(Write(a1))
        self.play(Write(py))
        self.play(Write(a2))
        self.play(Write(db))


class SQLInjection(Scene):
    def construct(self):
        color_map = {
            "select": ORANGE,
            "from": ORANGE,
            "where": ORANGE,
            "insert into": ORANGE,
            "create table": ORANGE
        }
        l1 = Line(2 * UP, 2 * DOWN)
        l2 = Line(2 * UP, 2 * UP + 4 * RIGHT)
        l3 = Line(1 * UP, 1 * UP + 4 * RIGHT)
        l4 = Line(ORIGIN, ORIGIN + 4 * RIGHT)
        l5 = Line(1 * DOWN, 1 * DOWN + 4 * RIGHT)
        l6 = Line(2 * DOWN, 2 * DOWN + 4 * RIGHT)

        l7 = Line(2 * UP + 2 * RIGHT, 2 * DOWN + 2 * RIGHT)
        l8 = Line(2 * UP + 4 * RIGHT, 2 * DOWN + 4 * RIGHT)

        t1 = TextMobject("Room Number")
        t2 = TextMobject("Code")
        t3 = TextMobject("703")
        t4 = TextMobject("192")
        t5 = TextMobject("214")
        t6 = TextMobject("1XFF")
        t7 = TextMobject("2OD1")
        t8 = TextMobject("1OAB")

        t1.move_to(1.5 * UP + 1 * RIGHT)
        t1.scale(0.5)
        t2.move_to(1.5 * UP + 3 * RIGHT)
        t2.scale(0.5)

        t3.move_to(0.5 * UP + 1 * RIGHT)
        t4.move_to(0.5 * DOWN + 1 * RIGHT)
        t5.move_to(1.5 * DOWN + 1 * RIGHT)

        t6.move_to(0.5 * UP + 3 * RIGHT)
        t7.move_to(0.5 * DOWN + 3 * RIGHT)
        t8.move_to(1.5 * DOWN + 3 * RIGHT)

        head = TextMobject("Table: Codes", color=RED)
        head.move_to(3 * UP + 2 * RIGHT)
        head.scale(1.25)

        db = SVGMobject("files/database.svg")
        db_text = TextMobject("Database")

        db_text.scale(1.5)
        db.scale(0.75)

        db.move_to(3.5 * LEFT + 1 * DOWN)
        db_text.move_to(3.5 * LEFT + 1 * UP)

        self.play(Write(l1))
        self.play(Write(l2), Write(l3), Write(l4), Write(l5), Write(l6))
        self.play(Write(l7), Write(l8))

        self.play(Write(t1), Write(t2))
        self.play(Write(t3), Write(t4), Write(t5))
        self.play(Write(t6), Write(t7), Write(t8))

        self.play(Write(head))

        self.play(Write(db), Write(db_text))
        self.wait(2)


class CreateTable(Scene):
    def construct(self):
        pass
