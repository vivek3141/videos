from manimlib.imports import *
from scipy.special import expi
from scipy.integrate import quad
from mpmath import *
from mpmath.libmp.libintmath import moebius


class PrimeMethods:
    def count_prime(self, x):
        counter = 0

        for i in range(2, int(x+1)):
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

    def _riemann_int(self, t):
        return 1/(t * (t**2 - 1)*math.log(t))

    def j_zeros(self, x, zz):
        x = float(x)
        zz = [mpc(0.5, float(y)) for y in zz]
        summ = sum([ei(z*log(x)) + ei((1-z)*log(x)) for z in zz])
        summ = summ.real

        def f(t): return 1.0/log(t)/t/(t**2-1)
        integral = quad(f, [x, inf])

        return li(x) - summ + integral - log(2)

    def pi_zeros(self, x, zz):
        x = float(x)
        sup_lim = int(log(x)/log(2.0)) + 2
        summatory = mpf(0)
        for n in range(1, sup_lim+1):
            n = mpf(n)
            jn = self.j_zeros(power(x, 1.0/n), zz)
            mu = moebius(n)
            summatory += mu*jn/n
        return summatory

    def single_pi(self, x, num_zeros, zeros_file):
        f = open(zeros_file)
        nzeros = []
        i = 1
        for l in f:
            if i > num_zeros:
                break
            nzeros.append(mpf(l.strip()))
            i += 1
        return self.pi_zeros(x, nzeros)

    def riemann_count(self, x, num_zeros=35):
        return float(self.single_pi(x, num_zeros, "zeros.txt"))


class PartScene(Scene):
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


class Factorization(Scene):
    def construct(self):
        eq1 = TexMobject("30")
        eq1.scale(2.5)

        eq2 = TexMobject("30 =")
        eq2.scale(2.5)
        eq2.shift(2.5 * LEFT)

        eq3 = TexMobject(r"3 \cdot 2 \cdot 5")
        eq3.scale(2.5)
        eq3.shift(1 * RIGHT)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformFromCopy(eq1, eq2))
        self.wait()

        self.play(Transform(eq1, eq3))
        self.wait()


class EuclidTheorem(Scene):
    def construct(self):
        title = TextMobject("Euclid's Theorem", color=BLUE)
        title.scale(1.5)
        title.shift(2 * UP)

        desc = TextMobject("There are an infinite number of primes")
        desc.scale(1.25)

        self.play(
            Write(title),
            Write(desc)
        )
        self.wait()

        self.play(Uncreate(desc), ApplyMethod(title.scale, 2/3))
        self.play(ApplyMethod(title.shift, 1.5 * UP))

        l = Line(6 * LEFT, 6 * RIGHT, stroke_width=0.5 *
                 DEFAULT_STROKE_WIDTH).shift(3 * UP)

        self.play(Write(l))
        self.wait()

        p1 = TexMobject(
            r"\text{Let }P \text{ be the product of every single prime number}", tex_to_color_map={r"P": YELLOW})
        p1.shift(2 * UP)

        p2 = TexMobject(r"\text{Let }Q = P + 1",
                        tex_to_color_map={r"P": YELLOW, r"Q": PURPLE})
        p2.shift(1 * UP)

        b1 = Circle(fill_opacity=1, radius=0.1,
                    color=BLUE).shift(6 * LEFT + 0.5 * DOWN)
        p3 = TexMobject(r"\text{If }Q \text{ is prime, then contradiction}",
                        tex_to_color_map={r"Q": PURPLE})
        p3.move_to(b1, LEFT).shift(0.5 * RIGHT)

        b2 = Circle(fill_opacity=1, radius=0.1,
                    color=BLUE).shift(6 * LEFT + 1.5 * DOWN)
        p4_1 = TexMobject(r"\text{If }Q \text{ isn't prime, then one of its prime factors } p",
                          tex_to_color_map={r"Q": PURPLE, r"} p": RED})
        p4_1.move_to(b2, LEFT).shift(0.5 * RIGHT)

        p4_2 = TexMobject(r"\text{ must divide }P-Q=1 \text{, contradiction}",
                          tex_to_color_map={r"Q": PURPLE, r"P": YELLOW})
        p4_2.move_to(b2, LEFT).shift(0.5 * RIGHT + 1 * DOWN)

        self.play(Write(p1))
        self.wait()

        self.play(Write(p2))
        self.wait()

        self.play(Write(p3), Write(b1))
        self.wait()

        self.play(Write(p4_1), Write(b2), Write(p4_2))


class PartTwoTitle(PartScene):
    CONFIG = {
        "num": 2,
        "text": "The Euler Product Formula",
        "subt": r"$$\sum_{n} \frac{1}{n^s} = \prod_{p} \frac{1}{1-p^{-s}}$$"
    }


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


class PrimePi(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 12,
        "y_min": 0,
        "x_max": 30,
        "x_min": 0,
        "y_tick_frequency": 3,
        "x_tick_frequency": 5,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$\pi(x)$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        func = VGroup()

        x = 0
        while(x <= self.x_max):
            next_x = x
            while(primepi(next_x) == primepi(x)):
                next_x += 1
            f = self.get_graph(lambda x: primepi(
                x), x_min=x, x_max=next_x, color=PINK)
            func.add(f)
            x = next_x

        self.play(Write(func))
        self.wait()


class RiemannExplicit(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 12,
        "y_min": 0,
        "x_max": 30,
        "x_min": 2,
        "y_tick_frequency": 3,
        "x_tick_frequency": 3,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$\pi(x)$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = VGroup()

        x = 0
        while(x <= self.x_max):
            next_x = x
            while(primepi(next_x) == primepi(x) and next_x <= self.x_max):
                next_x += 1
            f = self.get_graph(lambda x: primepi(
                x), x_min=x, x_max=next_x, color=PINK)
            f1.add(f)
            x = next_x

        f2 = self.get_graph(
            self.riemann_count,
            color=YELLOW,
        )

        self.play(Write(f1), Write(f2))
        self.wait()
