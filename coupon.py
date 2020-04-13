from manimlib.imports import *


def coupon(N):
    return N * sum([1/i for i in range(1, N+1)])


class Intro(Scene):
    def construct(self):
        cards = VGroup()
        m = [5, 2, -2, -5]
        for i in range(1, 5):
            cards.add(
                ImageMobject(
                    f"./img/card{i}.jpg"
                ).shift(m[i-1] * LEFT).scale(1.5)
            )
        cards.add(TexMobject("...").scale(2))
        cards.shift(1 * UP)

        for i in range(0, 4):
            self.play(FadeInFromDown(cards[i]), run_time=0.5)

        self.play(Write(cards[4]))
        l = Line(6.1 * LEFT, 6.1 * RIGHT).shift(0.75 * DOWN)

        b = Brace(l)
        lbl = b.get_tex("N").scale(1.5).shift(0.25 * DOWN).set_color(TEAL)
        brace = VGroup(b, lbl)
        cards.add(brace)

        self.play(Write(brace))
        self.wait()

        self.play(cards.shift, 1 * UP)

        q = TextMobject(r"How many draws to get all \( N \) cards?",
                        tex_to_color_map={r"\( N \)": TEAL})
        q.scale(1.5)
        q.shift(2.5 * DOWN)

        self.play(Write(q))
        self.wait()

        q2 = TextMobject(r"Expected value of number of draws to get all \( N \) cards",
                         tex_to_color_map={r"Expected value": GOLD, r"\( N \)": TEAL})
        q2.scale(1.1)
        q2.shift(2.5 * DOWN)

        self.play(Transform(q, q2))
        self.wait()


class ExpectedValue(Scene):
    def construct(self):
        title = TextMobject("Expected value", color=GOLD)
        title.scale(1.5)
        title.shift(3 * UP)

        title2 = TextMobject("Expected value", "= predicted outcome", tex_to_color_map={
                             "Expected value": GOLD})
        title2.scale(1.5)
        title2.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.wait()

        self.play(Transform(title, title2[0]))
        self.play(FadeInFromDown(title2[1]))
        self.wait()


class Asymptote(Scene):
    CONFIG = {
        "max_n": 77,
        "skip": 4,
        "x_min": -6,
        "x_max": 6,
        "buff": 0.4
    }

    def construct(self):
        rects = VGroup()
        width = (abs(self.x_min) + abs(self.x_max)) / (self.max_n / self.skip)

        for i in range(int(self.max_n/self.skip)):
            height = 0.1 * coupon(i)
            lbl = TexMobject(str(self.skip * i))
            rects.add(
                Rectangle(
                    width=width - self.buff,
                    height=0.1*coupon(i),
                    fill_opacity=1,
                ).shift([i * width + self.x_min, - 4 + height / 2, 0]
                        ).set_color_by_gradient(RED, BLUE)
            )
            rects.add(
                lbl.next_to(rects[-1], DOWN)
            )

        rects.shift(1 * UP)

        self.play(Write(rects))
        self.wait()
