from manimlib.imports import *
from scipy.special import expi
from scipy.integrate import quad
from mpmath import *
from mpmath.libmp.libintmath import moebius


class PrimeMethods:
    def count_prime(self, x):
        counter = 0

        for i in range(2, int(x) + 1):
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


class Series(Scene):
    def construct(self):
        title = TextMobject("Series", color=RED)
        title.scale(2)
        title.shift(3 * UP)

        eq1 = TexMobject(
            r"\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + ... ").scale(1.5)

        self.play(Write(title))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        eq2 = TexMobject(
            r"\sum_{n=1}^{\infty} \frac{1}{n^p}", r" = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + ... ",
            tex_to_color_map={r"^p}": YELLOW}
        )
        eq2.scale(1.5)

        self.play(Transform(eq1, eq2))
        self.wait()

        conv = TexMobject(
            r"\text{Coverges for } p > 1",
            tex_to_color_map={r"p": YELLOW}
        )
        conv.shift(2 * DOWN)

        conv2 = TexMobject(
            r"\text{Coverges for } s > 1",
            tex_to_color_map={r"} s": YELLOW}
        )
        conv2.shift(2 * DOWN)

        self.play(Write(conv))
        self.wait()

        zeta = TexMobject(r"\zeta (s) =")
        zeta.scale(1.5)
        zeta.shift(1 * LEFT)

        eq3 = TexMobject(
            r"\sum_{n=1}^{\infty} \frac{1}{n^s}",
            tex_to_color_map={r"^s}": YELLOW}
        )
        eq3.scale(1.5)
        eq3.shift(1.5 * RIGHT)

        self.play(
            Uncreate(eq1[2:]),
            ApplyMethod(eq1[:2].shift, -eq1[:2].get_center() + 1.5 * RIGHT)
        )
        self.play(Transform(eq1[:2], eq3), FadeInFromDown(
            zeta), Transform(conv, conv2))
        self.wait()


class EulerProductFormula(Scene):
    def construct(self):
        eq1 = TexMobject(
            r"\zeta(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \frac{1}{5^s}... ")
        eq1.scale(1.5)

        eq2 = TexMobject(
            r"\frac{1}{2^s} \zeta(s) = \frac{1}{2^s} + \frac{1}{4^s} + \frac{1}{6^s} + \frac{1}{8^s} + \frac{1}{10^s}... ")
        eq2.scale(1.5)

        eq3 = TexMobject(
            r"(1 - \frac{1}{2^s}) \zeta(s) = 1 + \frac{1}{3^s} + \frac{1}{5^s} + \frac{1}{7^s} + \frac{1}{9^s}... ")
        eq3.scale(1.5)

        eq4 = TexMobject(
            r"\frac{1}{3^s} (1 - \frac{1}{2^s}) \zeta(s) = \frac{1}{3^s} + \frac{1}{9^s} + \frac{1}{15^s} + \frac{1}{21^s} + \frac{1}{27^s}... ")
        eq4.scale(1.25)

        eq5 = TexMobject(
            r"(1 - \frac{1}{3^s}) (1 - \frac{1}{2^s}) \zeta(s) =1+ \frac{1}{5^s} + \frac{1}{7^s} + \frac{1}{11^s} + \frac{1}{13^s}... ")
        eq5.scale(1.20)

        eq6 = TexMobject(
            r"...(1 - \frac{1}{11^s})(1 - \frac{1}{7^s})(1 - \frac{1}{5^s})(1 - \frac{1}{3^s}) (1 - \frac{1}{2^s}) \zeta(s) =1")
        eq6.scale(1.15)

        eq7 = TexMobject(
            r"\sum_{n \in \mathbb{N}} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1-p^{-s}}")
        eq7.scale(1.5)

        box = Rectangle(height=3, width=10, color=YELLOW)

        text = TextMobject("Euler Product Formula", color=GREEN)
        text.shift(3 * UP)
        text.scale(1.5)

        self.play(Write(eq1))
        self.wait()

        self.play(Transform(eq1, eq2))
        self.wait()

        self.play(Transform(eq1, eq3))
        self.wait()

        self.play(Transform(eq1, eq4))
        self.wait()

        self.play(Transform(eq1, eq5))
        self.wait()

        self.play(Transform(eq1, eq6))
        self.wait()

        self.play(Transform(eq1, eq7))
        self.wait()

        self.play(Write(box), Write(text))
        self.wait()


class PartThreeTitle(PartScene):
    CONFIG = {
        "num": 3,
        "text": r"$$\pi(x)\text{ and the PNT}$$",
        "subt": r"$$\lim_{x \rightarrow \infty} \frac{\pi(x)}{x/\ln(x)}=1$$"
    }


class PrimeFunc(Scene, PrimeMethods):
    def construct(self):
        title = TextMobject("Prime Counting Function", color=YELLOW)
        title.scale(1.5)

        self.play(Write(title))
        self.wait()

        self.play(title.shift, 3 * UP)
        self.wait()

        n = 2.5

        eq1 = TexMobject(r"\pi(5)")
        eq1.scale(1.5)

        eq2 = TexMobject(r"\pi(10)")
        eq2.scale(1.5)
        eq2.shift(-0.5 * UP + n * LEFT)
        eq1.move_to(eq2, LEFT).shift(1.5 * UP)

        eq3 = TexMobject(r"\pi(20)")
        eq3.scale(1.5)
        eq3.shift(2 * DOWN + n * LEFT)

        arr = VGroup(*[Arrow(1 * LEFT, 1 * RIGHT, color=RED).shift(i * UP + 0 * LEFT)
                       for i in np.arange(-2, 2, 1.5)[::-1]])

        ans = VGroup(*[TexMobject([3, 4, 8][int((i + 2)/1.5)]).shift(i * UP + 2 * RIGHT).scale(1.5)
                       for i in np.arange(-2, 2, 1.5)[::-1]])

        self.play(FadeInFromDown(eq1), FadeInFromDown(
            eq2), FadeInFromDown(eq3))

        self.play(Write(arr), FadeInFromDown(ans))
        self.wait()


class PNTEq(Scene):
    def construct(self):
        eq = TexMobject(
            r"\lim_{x \rightarrow \infty} \frac{\pi(x)}{x/\ln(x)} = 1")
        eq.scale(2)

        title = TextMobject("Prime Number Theorem", color=RED)
        title.shift(2.5 * UP)
        title.scale(1.5)

        self.play(Write(title), Write(eq))
        self.wait()


class PrimeFuncGraph(GraphScene, PrimeMethods):
    CONFIG = {
        "y_max": 100,
        "y_min": 0,
        "x_max": 500,
        "x_min": 0,
        "y_tick_frequency": 10,
        "x_tick_frequency": 20,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "g_color": RED,
        "g_width": DEFAULT_STROKE_WIDTH*1,
    }

    def construct(self):
        self.setup_axes()
        f1 = self.get_graph(
            self.count_prime,
            color=PINK,
        )
        l1 = self.get_graph_label(f1, label=r'\pi(x)')
        l1.scale(0.75)

        f2 = self.get_graph(lambda x: x/math.log(x),
                            color=YELLOW, x_min=0.0001)
        l2 = self.get_graph_label(f2, label=r'\frac{x}{\ln(x)}')
        l2.scale(0.75)

        f3 = self.get_graph(lambda x: self.li(x), color=GREEN, x_min=3)
        l3 = self.get_graph_label(f3, label=r'\text{Li}(x)')
        l3.scale(0.75)
        l3.shift(3 * LEFT)

        self.play(Write(f1), Write(l1))
        self.wait()

        self.play(Write(f2), Write(l2))
        self.wait()

        self.play(Write(f3), Write(l3))
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
            r"\frac{\pi(x)}{x / \ln (x)}", color=RED).shift(2 * UP).scale(0.75)
        lbl2 = TexMobject(r"\frac{\pi(x)}{\text{Li}(x)}", color=YELLOW).shift(
            1 * DOWN).scale(0.75)

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
            Write(lbl1),
            Write(l1)
        )
        self.wait()

        self.play(
            Write(f2),
            Write(lbl2)
        )
        self.wait()


class LiEq(Scene):
    def construct(self):
        eq1 = TexMobject(r"\int", r"_2^x", r"\frac{dx}{\ln(x)}", tex_to_color_map={
                         r"_2^x": YELLOW})
        eq1.scale(1.5)

        liEq = TexMobject(r"\text{Li}(x) =")
        liEq.scale(1.5)
        liEq.shift(3 * LEFT)

        title = TextMobject("Logarithmic Integral Function", color=ORANGE)
        title.scale(1.5)
        title.shift(2 * UP)

        self.play(Write(VGroup(eq1[0], eq1[2])))
        self.wait()

        self.play(FadeInFromDown(liEq), FadeInFromDown(eq1[1]), Write(title))
        self.wait()


class Riemann(Scene):
    def construct(self):
        r = ImageMobject("./files/riemann.jpg", height=4)
        r.shift(1 * UP)

        subt = TextMobject("Bernhard Riemann")
        subt.scale(1.25)
        subt.shift(2 * DOWN)

        f = ["Analysis", "Number Theory", "Differential Geometry"]
        fields = VGroup()

        for i in range(0, 3):
            b = Circle(radius=0.1, fill_opacity=1, color=ORANGE)
            b.shift(i * UP + 1 * RIGHT)

            t = TextMobject(f[i]).move_to(b, LEFT)
            t.shift(0.5 * RIGHT)

            fields.add(b, t)

        self.play(FadeInFromDown(r), Write(subt))
        self.wait()

        self.play(ApplyMethod(r.shift, 2 * LEFT),
                  ApplyMethod(subt.shift, 2 * LEFT))
        self.play(FadeInFromDown(fields))
        self.wait()


class ReferenceVideo(Scene):
    def construct(self):
        title = TextMobject("Riemann Zeta Function by 3b1b")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(
            FadeInFromDown(title),
            Write(rect)
        )
        self.wait()


class RiemannZeta(Scene):
    def construct(self):
        p = ComplexPlane()
        plane = VGroup(p, p.get_coordinate_labels())
        plane.scale(1.5)

        self.play(Write(plane))
        self.wait()

        r1 = Rectangle(width=8, height=20, fill_opacity=0.5,
                       color=RED).shift(5.5 * RIGHT)
        t1 = TexMobject(r"\zeta(s) \text{ converges}")
        t1.scale(1.25)
        t1.shift(1.5 * 3 * RIGHT + 1 * UP)

        b1 = BackgroundRectangle(t1)

        self.play(Write(r1))
        self.play(Write(b1), Write(t1))
        self.wait()


class ComplexExponent(Scene):
    def construct(self):
        eq1 = TexMobject(r"\zeta(a + bi) = 1 + ",
                         r"\left ( \frac{1}{2} \right )^{a + bi} + ...", tex_to_color_map={r"a + bi": ORANGE})
        eq1.scale(1.5)

        self.play(Write(eq1))
        self.wait()

        b1 = BackgroundRectangle(
            eq1[3:5],
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_opacity=1,
            fill_opacity=0,
            buff=0.2,
            color=YELLOW
        )

        self.play(Write(b1))
        self.wait()

        self.play(FadeOut(eq1[0:3]), FadeOut(eq1[5:]), ApplyMethod(
            eq1[3:5].center), ApplyMethod(b1.center))
        self.wait()

        eq2 = TexMobject(r"\left ( \frac{1}{2} \right )^{a} + \left ( \frac{1}{2} \right )^{bi}",
                         tex_to_color_map={r"{a}": ORANGE, r"{bi}": ORANGE})
        eq2.scale(1.5)

        self.play(Uncreate(b1), Transform(eq1[3:5], eq2))
        self.wait()

        b2 = BackgroundRectangle(
            eq2[2:],
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_opacity=1,
            fill_opacity=0,
            buff=0.2,
            color=BLUE
        )

        self.play(Write(b2))
        self.wait()


class CExpPlane(Scene):
    def construct(self):
        p = ComplexPlane()
        plane = VGroup(p, p.get_coordinate_labels())
        plane.scale(1.5, about_point=p.get_center())

        c = Circle(radius=0.15, fill_opacity=1, color=YELLOW)
        c.shift(1.5 * RIGHT)

        t1 = TexMobject(r"\left ( \frac{1}{2} \right )^{0i}")
        t1.scale(1.25)
        t1.shift(2.75 * UP)
        b1 = BackgroundRectangle(t1, color=BLACK, fill_opacity=1, buff=0.1)

        self.play(Write(plane))
        self.play(Write(c), Write(b1), Write(t1))
        self.wait()

        self.play(UpdateFromAlphaFunc(c, self.update), UpdateFromAlphaFunc(t1, self.update2),
                  rate_func=linear, run_time=3)

        self.wait()

        circ = Circle(radius=1.5, color=RED)
        self.bring_to_back(circ)

        self.play(Write(circ))
        self.wait()

    def update(self, point, dt):
        p = interpolate(0, 9.0647, dt)
        new_p = 0.5 ** (p * 1j)
        c = Circle(radius=0.15, fill_opacity=1, color=YELLOW)
        c.shift(1.5 * RIGHT)
        c.center()
        c.shift(new_p.real * 1.5 * RIGHT + new_p.imag * 1.5 * UP)
        point.become(c)

    def update2(self, text, dt):
        p = interpolate(0, 9.0647, dt)
        t1 = TexMobject(
            r"\left ( \frac{1}{2} \right )^{ "+str(round(float(p), 2))+r"i}")
        t1.scale(1.25)
        t1.shift(2.75 * UP)
        text.become(t1)


class RealZetaGraph(Scene):
    def construct(self):
        N = 125
        axes = Axes(
            x_min=-12,
            x_max=1,
            y_max=3,
            y_min=-3
        )

        axes.center()
        labels = axes.get_x_axis().get_number_mobjects(
            *[-2 * x for x in range(1, 6)])
        brects = VGroup()

        for i in labels:
            b = BackgroundRectangle(i, fill_opacity=1, color=BLACK, buff=0.1)
            brects.add(b)

        graph = FunctionGraph(
            lambda x: 3 * N * float(zeta(complex(x, 0)).real),
            x_min=-12, x_max=0
        )
        graph.shift(5.5 * RIGHT)

        l1 = TexMobject(r"\zeta(s)").shift(3.5 * UP + 5.5 * RIGHT)
        l2 = TexMobject(r"x").shift(6.75 * RIGHT)

        self.play(Write(axes), Write(graph),  Write(
            brects), Write(labels), Write(l1), Write(l2))
        self.wait()

    def riemann_zeta(self, x):
        return (2 ** x) * (PI**(x-1)) * math.sin(PI*x/2) * gamma(1 - x) * zeta(1 - x)


class RiemannZeros(Scene):
    def construct(self):
        func = TexMobject(
            r"\zeta (s)=2^{s}\pi ^{s-1} \ ", r"\sin \left({\frac {\pi s}{2}}\right)\ ", r" \Gamma (1-s)\ ", r" \zeta (1-s)")
        func.scale(1.5)

        b1 = BackgroundRectangle(
            func[2],
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_opacity=1,
            fill_opacity=0,
            buff=0.2,
            color=YELLOW
        )

        self.play(Write(func))
        self.wait()

        self.play(Write(b1))
        self.wait()

        self.play(Uncreate(b1))
        self.wait()

        b2 = BackgroundRectangle(
            func[1],
            stroke_width=DEFAULT_STROKE_WIDTH,
            stroke_opacity=1,
            fill_opacity=0,
            buff=0.2,
            color=RED
        )

        t1 = TexMobject(r"\zeta(s) = 0 \text{ when Re} (s) = -2n", tex_to_color_map={
                        r"\zeta(s) = 0": GREEN, r"Re} (s) = -2n": RED})
        t1.shift(2 * DOWN)

        self.play(Write(b2))
        self.play(Write(t1))
        self.wait()

# Unused Scene


class RiemannZerosGraph(ThreeDScene):
    def construct(self):
        f1 = ParametricSurface(
            lambda u, v: [u, v, float(zeta(complex(u, v)).real)],
            u_min=-5,
            u_max=5,
            v_min=-5,
            v_max=5
        )
        f2 = ParametricSurface(
            lambda u, v: [u, v, float(zeta(complex(u, v)).imag)],
            u_min=-5,
            u_max=5,
            v_min=-5,
            v_max=5,
            checkerboard_colors=[RED, ORANGE]
        )
        axes = ThreeDAxes()

        plane = ParametricSurface(
            lambda u, v: [u, v, 0],
            u_min=-5,
            u_max=5,
            v_min=-5,
            v_max=5,
            checkerboard_colors=[YELLOW, YELLOW]
        )

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(axes), Write(f1), Write(f2))
        self.begin_ambient_camera_rotation(rate=0.06)
        self.wait(5)

        f2.set_fill(opacity=0.5)
        f1.set_fill(opacity=0.5)

        self.play(Write(plane))
        self.wait(2)


class RiemannVisual(GraphScene):
    CONFIG = {
        "y_max": 6,
        "y_min": -6,
        "x_max": 30,
        "x_min": 0,
        "y_tick_frequency": 3,
        "x_tick_frequency": 5,
        "axes_color": BLUE,
        "x_axis_label": r"$\text{Im}(s)$",
        "y_axis_label": "$\zeta(s)$",
        "graph_origin": 4.5 * LEFT,
        "x_labeled_nums": [i*5 for i in range(7)],
        "y_labeled_nums": [(i*3 - 6) for i in range(5)]
    }

    def construct(self):
        self.setup_axes()

        f1 = self.get_graph(
            lambda x: float(zeta(complex(0.01, x)).real),
            color=GREEN
        )
        f2 = self.get_graph(
            lambda x: float(zeta(complex(0.01, x)).imag),
            color=YELLOW
        )

        text = TexMobject(r"\text{Re}(s) = 0.01")
        text.scale(1.25)
        text.shift(3 * UP)

        line1 = Line(1 * LEFT, 0 * RIGHT,
                     color=GREEN).shift(0.5 * UP + 1.5 * LEFT)
        line2 = Line(1 * LEFT, 0 * RIGHT,
                     color=YELLOW).shift(0.5 * DOWN + 1.5 * LEFT)

        t1 = TexMobject(r"\text{Re}(\zeta(s))").shift(
            0.5 * UP + 0.5 * RIGHT).scale(1.5)
        t2 = TexMobject(r"\text{Im}(\zeta(s))").shift(
            0.5 * DOWN + 0.5 * RIGHT).scale(1.5)

        rect = Rectangle(height=3, width=6)

        legend = VGroup(line1, line2, t1, t2, rect).scale(0.5)
        legend.shift(2.5 * UP + 5 * RIGHT)

        z = [14.13472514173500016454,
             21.02203963877200010302,
             25.01085758014599846888]
        zeros = [x/5 * 1.5 - 4.5 for x in z]
        c = VGroup()
        for i in zeros:
            c.add(
                Circle(radius=0.2, color=RED, stroke_width=1.5 *
                       DEFAULT_STROKE_WIDTH).shift(i * RIGHT)
            )

        self.play(Write(f1), Write(f2), Write(text), Write(legend), Write(c))
        self.wait()

        self.play(UpdateFromAlphaFunc(f1, self.real_update),
                  UpdateFromAlphaFunc(f2, self.imag_update),
                  UpdateFromAlphaFunc(text, self.text_update),
                  rate_func=linear, run_time=4)
        self.wait()

    def real_update(self, func, dt):
        r = interpolate(0.01, 0.99, dt)
        f1 = self.get_graph(
            lambda x: float(zeta(complex(r, x)).real),
            color=GREEN
        )
        func.become(f1)

    def imag_update(self, func, dt):
        r = interpolate(0.01, 0.99, dt)
        f2 = self.get_graph(
            lambda x: float(zeta(complex(r, x)).imag),
            color=YELLOW
        )
        func.become(f2)

    def text_update(self, t, dt):
        x = interpolate(0.01, 0.99, dt)
        text = TexMobject(r"\text{Re}(s) = " + str(round(x, 2)))
        text.scale(1.25)
        text.shift(3 * UP)
        t.become(text)


class RiemannExplicitEq(Scene):
    def construct(self):
        eq = TexMobject(
            r"{\displaystyle \pi(x)=\operatorname {li} (x)-\sum _{\rho }\operatorname {li} (x^{\rho })-\log(2)+\int _{x}^{\infty }{\frac {dt}{t(t^{2}-1)\log(t)}}}")
        eq.scale(1.15)
        self.play(Write(eq))
        self.wait()

# Unused Scene


class RiemannLevelCurves(Scene):
    def construct(self):
        f = []
        p = ComplexPlane()
        plane = VGroup(p, p.get_coordinate_labels())

        for x in np.arange(-5, 5, 0.1):
            for y in np.arange(-20, 20, 0.1):
                if self.pass_real(x, y):
                    f.append([x, y, 0])

        p = Polygon(*f)
        self.play(Write(plane), Write(p))
        self.wait()

    def pass_real(self, x, y):
        if -0.05 < float(zeta(complex(x, y)).imag) < 0.05:
            return True
        return False


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
            lambda x: self.riemann_count(x, num_zeros=0),
            color=YELLOW,
        )

        text = TexMobject(r"\text{Zeros: } 0")
        text.scale(1.25)
        text.shift(3 * UP)

        self.play(Write(f1), Write(f2), Write(text))
        self.wait()

        self.play(UpdateFromAlphaFunc(f2, self.func_update),
                  UpdateFromAlphaFunc(text, self.text_update),
                  run_time=4, rate_func=linear)

    def func_update(self, func, dt):
        x = interpolate(0, 35, dt)
        f2 = self.get_graph(
            lambda y: self.riemann_count(y, num_zeros=x),
            color=YELLOW
        )
        func.become(f2)

    def text_update(self, tex, dt):
        x = interpolate(0, 35, dt)
        text = TexMobject(r"\text{Zeros: } " + str(int(x)))
        text.scale(1.25)
        text.shift(3 * UP)
        tex.become(text)


class YouTubePost(GraphScene):
    CONFIG = {
        "y_max": 6,
        "y_min": -6,
        "x_max": 30,
        "x_min": 0,
        "y_tick_frequency": 3,
        "x_tick_frequency": 5,
        "axes_color": BLUE,
        "x_axis_label": r"$\text{Im}(s)$",
        "y_axis_label": "$\zeta(s)$",
        "graph_origin": 4.5 * LEFT,
        "x_labeled_nums": [i*5 for i in range(7)],
        "y_labeled_nums": [(i*3 - 6) for i in range(5)]
    }

    def construct(self):
        self.setup_axes()

        f1 = self.get_graph(
            lambda x: float(zeta(complex(0.5, x)).real),
            color=GREEN
        )
        f2 = self.get_graph(
            lambda x: float(zeta(complex(0.5, x)).imag),
            color=YELLOW
        )

        text = TexMobject(r"\text{Re}(s) = 0.5")
        text.scale(1.25)
        text.shift(3 * UP)

        line1 = Line(1 * LEFT, 0 * RIGHT,
                     color=GREEN).shift(0.5 * UP + 1.5 * LEFT)
        line2 = Line(1 * LEFT, 0 * RIGHT,
                     color=YELLOW).shift(0.5 * DOWN + 1.5 * LEFT)

        t1 = TexMobject(r"\text{Re}(\zeta(s))").shift(
            0.5 * UP + 0.5 * RIGHT).scale(1.5)
        t2 = TexMobject(r"\text{Im}(\zeta(s))").shift(
            0.5 * DOWN + 0.5 * RIGHT).scale(1.5)

        rect = Rectangle(height=3, width=6)

        legend = VGroup(line1, line2, t1, t2, rect).scale(0.5)
        legend.shift(2.5 * UP + 5 * RIGHT)

        z = [14.13472514173500016454,
             21.02203963877200010302,
             25.01085758014599846888]
        zeros = [x/5 * 1.5 - 4.5 for x in z]
        c = VGroup()
        for i in zeros:
            c.add(
                Circle(radius=0.2, color=RED, stroke_width=1.5 *
                       DEFAULT_STROKE_WIDTH).shift(i * RIGHT)
            )

        self.play(Write(f1), Write(f2), Write(text), Write(legend), Write(c))
        self.wait()

        self.wait()
