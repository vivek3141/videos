from manimlib.imports import *
from scipy.special import expi


class PrimeMethods:
    def count_prime(self, x):
        counter = 0

        for i in range(2, int(x)):
            if self.isPrime(i):
                counter += 1

        return counter

    def isPrime(self, x):
        for i in range(2, int(x/2) + 1):
            if x % i == 0:
                return False
        return True

    def pnt(self, x):
        return self.count_prime(x)/(x/math.log(x))

    def pnt_li(self, x):
        return self.count_prime(x)/self.li(x)

    def li(self, x):
        return expi(math.log(x))


class PartScene(Scene):
    CONFIG = {
        "num": 1,
        "text": "filler text",
        "subt": None
    }

    def construct(self):
        grp = VGroup()

        title = TextMobject(f"Part {str(self.num)}", color=PURPLE)
        title.scale(1.5)
        title.shift(1.5 * UP)
        grp.add(title)

        text = TextMobject(self.text)
        text.scale(2)
        grp.add(text)

        if self.subt:
            subt = TextMobject(self.subt)
            subt.shift(1.5 * DOWN)
            grp.add(subt)

        self.play(Write(grp))
        self.wait()


class IntroQuote(Scene):
    def construct(self):
        quote = TextMobject(
            "It is evident that the primes are randomly distributed but,")
        quote2 = TextMobject(
            "unfortunately, we don't know what 'random' means.")
        author = TextMobject("-R. C. Vaughan", color=YELLOW)
        author.shift(1 * DOWN + 1 * RIGHT)
        quote.shift(2 * UP)
        quote2.shift(UP)
        self.play(Write(quote), Write(quote2))
        self.play(Write(author))
        self.wait()


class Intro(Scene):
    def construct(self):
        title = TextMobject("Continue the Following Sequence:", color=BLUE)
        title.scale(1.5)
        title.shift(2 * UP)

        seq = TexMobject("2, 3, 5, 7, 11, 13, 17, 19, ...")
        seq.scale(1.5)

        self.play(Write(title))
        self.play(Write(seq))
        self.wait()


class PartOneTitle(PartScene):
    CONFIG = {
        "num": 1,
        "text": "Euclid’s Theorem",
        "subt": "How many primes are there?"
    }


class EuclidTheorem(Scene):
    def construct(self):


class PrimeFuncGraph(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 500,
        "y_min": 0,
        "x_max": 3000,
        "x_min": 0,
        "y_tick_frequency": 100,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$\pi(x)$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.count_prime,
            color=PINK,
        )

        self.play(Write(f1))
        self.wait()


class PNTGraph(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 2,
        "y_min": 0,
        "x_max": 1000,
        "x_min": 0.001,
        "y_tick_frequency": 1,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": r"$\frac{\pi(x)}{x/ \ln (x)}$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.pnt,
            color=RED,
        )

        self.play(Write(f1))
        self.wait()


class PNTGraph2(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 2,
        "y_min": 0,
        "x_max": 1000,
        "x_min": 0.001,
        "y_tick_frequency": 1,
        "x_tick_frequency": 100,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.pnt,
            color=RED,
        )
        f2 = self.get_graph(
            self.pnt_li,
            color=YELLOW,
        )

        lbl1 = TexMobject(
            r"\frac{\pi(x)}{x / \ln (x)}").shift(2 * UP).scale(0.75)
        lbl2 = TexMobject(r"\frac{\pi(x)}{Li(x)}").shift(1 * DOWN).scale(0.75)

        l1 = VGroup()
        self.freq = 0.33*self.x_tick_frequency
        for i in range(1, int(self.x_max/self.freq), 2):
            l1.add(
                self.get_graph(
                    lambda x: 1,
                    x_min=i * self.freq,
                    x_max=(i+1) * self.freq,
                    color=WHITE,
                    stroke_width=0.5 * DEFAULT_STROKE_WIDTH
                )
            )

        self.play(
            Write(f1),
            Write(f2),
            Write(lbl1),
            Write(lbl2),
            Write(l1)
        )
        self.wait()
