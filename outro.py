from manimlib import *


def split_into(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i+n]


class Outro(Scene):
    def construct(self):
        line = Line(12 * UP, 12 * DOWN)
        
        btxt = TexText("Brought to you by", color=RED)
        btxt.scale(1.25)
        btxt.shift(FRAME_WIDTH/4 * LEFT + 0.5 * RIGHT + 3.25 * UP)

        plogo = SVGMobject("./img/Patreon_logomark.svg")
        plogo.scale(0.3)
        plogo.shift(3.25 * UP + 6.25 * LEFT)
        plogo[-2].set_color("#f86754")
        plogo[-1].set_color(BLUE_E)

        t = ImageMobject("img/twitter.png")
        t.scale(0.35)
        t.shift(3 * DOWN + 1.5 * RIGHT)

        i = ImageMobject("img/instagram.png")
        i.scale(0.35)
        i.next_to(t, RIGHT)

        t_text = TexText("@vcubingx")
        t_text.next_to(i, RIGHT)

        self.play(Write(line))
        self.play(Write(btxt), Write(plogo), FadeIn(t), FadeIn(i), Write(t_text))

        old_patreons = None
        list_of_patreons = open("patreon.txt").read().split("\n")

        for i in split_into(list_of_patreons, 15):
            patreons = VGroup()

            for name, pos in zip(i, np.linspace(FRAME_HEIGHT/2, -FRAME_HEIGHT/2, num=18)):
                patreons.add(
                    TexText(name, tex_to_color_map={} if name != "3blue1brown" else {"blue": BLUE, "brown": "#CD853F"}).move_to([0, pos, 0]).scale(0.75)
                )

            patreons.center()
            patreons.shift(FRAME_WIDTH/4 * LEFT + 0.5 * DOWN)

            if not old_patreons:
                self.play(Write(patreons))
                old_patreons = patreons
            else:
                self.play(Transform(old_patreons, patreons))
            
            self.wait(5)

        self.embed()
