from manimlib.imports import *


def split_into(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i+n]


class Outro(Scene):
    def construct(self):
        line = Line(12 * UP, 12 * DOWN)
        
        btxt = TextMobject("Brought to you by", color=RED)
        btxt.scale(1.25)
        btxt.shift(FRAME_WIDTH/4 * LEFT + 0.5 * RIGHT + 3.25 * UP)

        plogo = SVGMobject("./img/Patreon_logomark.svg")
        plogo.scale(0.3)
        plogo.shift(3.25 * UP + 6.25 * LEFT)
        plogo[-2].set_color("#f86754")
        plogo[-1].set_color(DARK_BLUE)

        self.play(Write(line))
        self.play(Write(btxt), Write(plogo))

        old_patreons = None
        list_of_patreons = open("patreon.txt").read().split("\n")

        for i in split_into(list_of_patreons, 15):
            patreons = VGroup()

            for name, pos in zip(i, np.linspace(-FRAME_HEIGHT/2, FRAME_HEIGHT/2, num=15)):
                patreons.add(
                    TextMobject(name, tex_to_color_map={} if name != "3blue1brown" else {"blue": BLUE, "brown": "#CD853F"}).move_to([0, pos, 0])
                )

            patreons.center()
            patreons.shift(FRAME_WIDTH/4 * LEFT + 0.5 * DOWN)

            if not old_patreons:
                self.play(Write(patreons[::-1]))
            else:
                self.play(Transform(old_patreons, patreons))
                old_patreons = patreons
            
            self.wait()
