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


class Database(Scene):
    def construct(self):
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
        color_map = {
            "select".upper(): ORANGE,
            "from".upper(): ORANGE,
            "where".upper(): ORANGE,
            "insert into".upper(): ORANGE,
            "create table".upper(): ORANGE
        }

        s1 = TextMobject("CREATE TABLE `Codes` (", tex_to_color_map={**color_map, **{"`Codes`": RED}})
        s1.move_to(3 * LEFT + 1.5 * UP)

        s2 = TextMobject("`Room Number` INTEGER,", tex_to_color_map={**color_map, **{"`Room Number`": RED}})
        s3 = TextMobject("`Code` TEXT(4)", tex_to_color_map={**color_map, **{"`Code`": RED, "TEXT": BLUE}})
        s4 = TextMobject(");", tex_to_color_map={**color_map})

        s2.next_to(s1.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)
        s3.next_to(s2.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)
        s4.next_to(s3.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)

        l1 = Line(2 * UP + 1 * RIGHT, 2 * DOWN + 1 * RIGHT)
        l2 = Line(2 * UP + 1 * RIGHT, 2 * UP + 5 * RIGHT)
        l3 = Line(1 * UP + 1 * RIGHT, 1 * UP + 5 * RIGHT)
        l4 = Line(1 * RIGHT, 5 * RIGHT)
        l5 = Line(1 * DOWN + 1 * RIGHT, 1 * DOWN + 5 * RIGHT)
        l6 = Line(2 * DOWN + 1 * RIGHT, 2 * DOWN + 5 * RIGHT)

        l7 = Line(2 * UP + 3 * RIGHT, 2 * DOWN + 3 * RIGHT)
        l8 = Line(2 * UP + 5 * RIGHT, 2 * DOWN + 5 * RIGHT)

        t1 = TextMobject("Room Number")
        t2 = TextMobject("Code")
        t3 = TextMobject("703")
        t4 = TextMobject("192")
        t5 = TextMobject("214")
        t6 = TextMobject("1XFF")
        t7 = TextMobject("2OD1")
        t8 = TextMobject("1OAB")

        t1.move_to(1.5 * UP + 2 * RIGHT)
        t1.scale(0.5)
        t2.move_to(1.5 * UP + 4 * RIGHT)
        t2.scale(0.5)

        t3.move_to(0.5 * UP + 2 * RIGHT)
        t4.move_to(0.5 * DOWN + 2 * RIGHT)
        t5.move_to(1.5 * DOWN + 2 * RIGHT)

        t6.move_to(0.5 * UP + 4 * RIGHT)
        t7.move_to(0.5 * DOWN + 4 * RIGHT)
        t8.move_to(1.5 * DOWN + 4 * RIGHT)

        head = TextMobject("Table: Codes", color=RED)
        head.move_to(3 * UP + 3 * RIGHT)
        head.scale(1.25)

        self.play(Write(s1), Write(s2), Write(s3), Write(s4))

        self.play(Write(l1))
        self.play(Write(l2), Write(l3), Write(l4), Write(l5), Write(l6))
        self.play(Write(l7), Write(l8))

        self.play(Write(head))

        self.play(Write(t1), Write(t2))

        self.wait(2)

        i1 = TextMobject("INSERT INTO `Codes`", tex_to_color_map={**color_map, **{"`Codes`": RED}})
        i1.move_to(3 * LEFT + 1.5 * UP)

        i2 = TextMobject("values(", tex_to_color_map={**color_map, **{"values": BLUE}})
        i3 = TextMobject("703, `1XFF`", tex_to_color_map={**color_map, **{"703": RED, "`1XFF`": RED}})
        i4 = TextMobject(");", tex_to_color_map={**color_map})

        i2.next_to(i1.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)
        i3.next_to(i2.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)
        i4.next_to(i3.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)

        i5 = TextMobject("192, `2OD1`", tex_to_color_map={**color_map, **{"192": RED, "`2OD1`": RED}})
        i5.next_to(i2.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)

        i6 = TextMobject("214, `1OAB`", tex_to_color_map={**color_map, **{"214": RED, "`1OAB`": RED}})
        i6.next_to(i2.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)

        self.play(Transform(s1, i1), Transform(s2, i2), Transform(s3, i3), Transform(s4, i4))
        self.play(Write(t3), Write(t6))
        self.play(Transform(s3, i5), Write(t4), Write(t7))
        self.play(Transform(s3, i6), Write(t5), Write(t8))


class Select(Scene):
    def construct(self):
        color_map = {
            "select".upper(): ORANGE,
            "from".upper(): ORANGE,
            "where".upper(): ORANGE,
            "insert into".upper(): ORANGE,
            "create table".upper(): ORANGE
        }

        s1 = TextMobject("SELECT * FROM Codes;", tex_to_color_map={**color_map, **{"Codes": RED}})
        s1.move_to(3 * LEFT)

        l1 = Line(2 * UP + 1 * RIGHT, 2 * DOWN + 1 * RIGHT)
        l2 = Line(2 * UP + 1 * RIGHT, 2 * UP + 5 * RIGHT)
        l3 = Line(1 * UP + 1 * RIGHT, 1 * UP + 5 * RIGHT)
        l4 = Line(1 * RIGHT, 5 * RIGHT)
        l5 = Line(1 * DOWN + 1 * RIGHT, 1 * DOWN + 5 * RIGHT)
        l6 = Line(2 * DOWN + 1 * RIGHT, 2 * DOWN + 5 * RIGHT)

        l7 = Line(2 * UP + 3 * RIGHT, 2 * DOWN + 3 * RIGHT)
        l8 = Line(2 * UP + 5 * RIGHT, 2 * DOWN + 5 * RIGHT)

        t1 = TextMobject("Room Number")
        t2 = TextMobject("Code")
        t3 = TextMobject("703")
        t4 = TextMobject("192")
        t5 = TextMobject("214")
        t6 = TextMobject("1XFF")
        t7 = TextMobject("2OD1")
        t8 = TextMobject("1OAB")

        t1.move_to(1.5 * UP + 2 * RIGHT)
        t1.scale(0.5)
        t2.move_to(1.5 * UP + 4 * RIGHT)
        t2.scale(0.5)

        t3.move_to(0.5 * UP + 2 * RIGHT)
        t4.move_to(0.5 * DOWN + 2 * RIGHT)
        t5.move_to(1.5 * DOWN + 2 * RIGHT)

        t6.move_to(0.5 * UP + 4 * RIGHT)
        t7.move_to(0.5 * DOWN + 4 * RIGHT)
        t8.move_to(1.5 * DOWN + 4 * RIGHT)

        head = TextMobject("Table: Codes", color=RED)
        head.move_to(3 * UP + 3 * RIGHT)
        head.scale(1.25)

        s = TextMobject("SELECT * FROM Codes", tex_to_color_map={**color_map, **{"Codes": RED}})
        s.move_to(3 * LEFT + 1 * UP)
        s2 = TextMobject("WHERE Code=`1XFF`;", tex_to_color_map={**color_map, **{"`1XFF`": RED}})
        s2.next_to(s1.get_corner(DOWN + LEFT), 1 * DOWN + RIGHT)

        ll1 = Line(2 * UP + 1 * RIGHT, 1 * RIGHT)
        ll2 = Line(2 * UP + 1 * RIGHT, 2 * UP + 5 * RIGHT)
        ll3 = Line(1 * RIGHT, 5 * RIGHT)
        ll4 = Line(1 * UP + 1 * RIGHT, 1 * UP + 5 * RIGHT)

        ll7 = Line(2 * UP + 3 * RIGHT, 3 * RIGHT)
        ll8 = Line(2 * UP + 5 * RIGHT, 5 * RIGHT)

        self.play(Write(s1))

        self.play(Write(l1))
        self.play(Write(l2), Write(l3), Write(l4), Write(l5), Write(l6))
        self.play(Write(l7), Write(l8))

        self.play(Write(head), Write(t1), Write(t2), Write(t3), Write(t6), Write(t4), Write(t7), Write(t5), Write(t8))

        self.play(Transform(s1, s), Write(s2))
        self.play(Transform(l1, ll1), Transform(l2, ll2),
                  Transform(l3, ll3), Transform(l4, ll4),
                  Transform(l5, ll2), Transform(l6, ll3),
                  Transform(l7, ll7), Transform(l8, ll8),
                  Transform(t7, t6), Transform(t8, t6),
                  Transform(t5, t3), Transform(t4, t3)
                  )

        self.wait(2)


class Injection(Scene):
    def construct(self):
        color_map = {
            "select".upper(): ORANGE,
            "from".upper(): ORANGE,
            "where".upper(): ORANGE,
            "insert into".upper(): ORANGE,
            "create table".upper(): ORANGE
        }
        s1 = TextMobject("SELECT * FROM Codes WHERE Code=`1XFF`;",
                         tex_to_color_map={**color_map, **{"Codes": RED, '`1XFF`': RED}})
        s2 = TextMobject("SELECT * FROM Codes WHERE Code=`2DDA`;",
                         tex_to_color_map={**color_map, **{"Codes": RED, '`2DDA`': RED}})
        s3 = TextMobject("SELECT * FROM Codes WHERE Code=`WHAT`;",
                         tex_to_color_map={**color_map, **{"Codes": RED, '`WHAT`': RED}})
        s4 = TextMobject("SELECT * FROM Codes WHERE Code=```;",
                         tex_to_color_map={**color_map, **{"Codes": RED, '```': RED}})

        text1 = TextMobject("Test for vulnerability", color=BLUE)
        text1.scale(2)
        text1.move_to(2.5 * UP)

        text2 = TextMobject("This will always return something", color=BLUE)
        text2.scale(1.25)
        text2.move_to(2.5 * UP)

        self.play(Write(s1))
        self.play(Transform(s1, s2))
        self.play(Transform(s1, s3))
        self.play(Write(text1))
        self.play(Transform(s1, s4))

        self.wait(2)

        st1 = TextMobject("SELECT * FROM Codes", tex_to_color_map={**color_map, **{"`Codes`": RED}})
        st1.move_to(3 * LEFT + 0.5 * UP)

        st2 = TextMobject("WHERE 1=1", tex_to_color_map={**color_map})
        st2.move_to(3 * LEFT + 0.5 * DOWN)

        l1 = Line(2 * UP + 1 * RIGHT, 2 * DOWN + 1 * RIGHT)
        l2 = Line(2 * UP + 1 * RIGHT, 2 * UP + 5 * RIGHT)
        l3 = Line(1 * UP + 1 * RIGHT, 1 * UP + 5 * RIGHT)
        l4 = Line(1 * RIGHT, 5 * RIGHT)
        l5 = Line(1 * DOWN + 1 * RIGHT, 1 * DOWN + 5 * RIGHT)
        l6 = Line(2 * DOWN + 1 * RIGHT, 2 * DOWN + 5 * RIGHT)

        l7 = Line(2 * UP + 3 * RIGHT, 2 * DOWN + 3 * RIGHT)
        l8 = Line(2 * UP + 5 * RIGHT, 2 * DOWN + 5 * RIGHT)

        t1 = TextMobject("Room Number")
        t2 = TextMobject("Code")
        t3 = TextMobject("703")
        t4 = TextMobject("192")
        t5 = TextMobject("214")
        t6 = TextMobject("1XFF")
        t7 = TextMobject("2OD1")
        t8 = TextMobject("1OAB")

        t1.move_to(1.5 * UP + 2 * RIGHT)
        t1.scale(0.5)
        t2.move_to(1.5 * UP + 4 * RIGHT)
        t2.scale(0.5)

        t3.move_to(0.5 * UP + 2 * RIGHT)
        t4.move_to(0.5 * DOWN + 2 * RIGHT)
        t5.move_to(1.5 * DOWN + 2 * RIGHT)

        t6.move_to(0.5 * UP + 4 * RIGHT)
        t7.move_to(0.5 * DOWN + 4 * RIGHT)
        t8.move_to(1.5 * DOWN + 4 * RIGHT)

        self.play(Transform(s1, st1), Write(st2))

        self.play(Write(l1), Write(l2), Write(l3), Write(l4),
                  Write(l5), Write(l6), Write(l7), Write(l8), Transform(text1, text2))
        self.play(Write(t1), Write(t2), Write(t3), Write(t4),
                  Write(t5), Write(t6), Write(t7), Write(t8))

        self.wait(2)

        text3 = TextMobject("SQL Injection", color=BLUE)
        text3.scale(1.25)
        text3.move_to(2.5 * UP)

        r2 = TextMobject("WHERE", tex_to_color_map={**color_map})
        r2.move_to(3 * LEFT + 0.5 * DOWN)

        r4 = TextMobject("`Room Number`=`a` OR 1=1 OR `b`", tex_to_color_map={"OR": BLUE})
        r4.move_to(3 * LEFT + 1.5 * DOWN)
        r4.scale(0.75)

        r3 = TextMobject("WHERE Code=101 OR 1=1", tex_to_color_map={**color_map})
        r3.move_to(3 * LEFT + 0.5 * DOWN)

        self.play(Transform(st2, r2), Transform(text1, text3))
        self.play(Write(r4))
        self.wait(2)

        self.play(Transform(st2, r3), Transform(r4, r3))
        self.wait(2)
