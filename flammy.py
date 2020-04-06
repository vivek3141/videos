from manimlib.imports import *

import math
from random import *


class LawLarge(Scene):
    def construct(self):
        rect = Rectangle(width=1, height=0, color=GOLD_B, fill_opacity=1)
        rect.to_edge(DOWN)

        tracker = ValueTracker(0)
        rect.add_updater(lambda x: x.become(
            self.get_rect(tracker.get_value())))

        self.play(Write(rect))

        for _ in range(6):
            self.play(tracker.increment_value, 1, rate_func=linear)
            self.wait()

    def get_rect(self, value):
        return Rectangle(width=1, height=value, color=GOLD_B, fill_opacity=1).to_edge(DOWN)


class Prob(Scene):

    def construct(self):

        throws = int(input('How many throws?: '))

        rectstarthead = Rectangle(
            fill_color=GOLD_B, fill_opacity=1, height=0, width=1, color=GOLD_B)
        rectstarthead.to_edge(DOWN)
        rectstarthead.shift(2*LEFT)
        self.play(ShowCreation(rectstarthead))

        rectstarttails = Rectangle(
            fill_color=BLUE_B, fill_opacity=1, height=0, width=1, color=BLUE_B)
        rectstarttails.to_edge(DOWN)
        rectstarttails.shift(2*RIGHT)
        self.play(ShowCreation(rectstarttails))

        t = 1
        heads = 0
        tails = 0
        HeightAdjust = 2/throws

        CounterHeadsTxt = TextMobject("Heads:")
        CounterTailsTxt = TextMobject("Tails:")

        CounterHeadsTxt.to_edge(UP)
        CounterTailsTxt.to_edge(UP)
        CounterHeadsTxt.shift(2*LEFT)
        CounterTailsTxt.shift(2*RIGHT)

        self.play(Write(CounterHeadsTxt))
        self.play(Write(CounterTailsTxt))

        #CounterHeads = TextMobject(heads)
        #CounterTails = TextMobject(heads)

        #CounterHeads.next_to(CounterHeadsTxt, RIGHT)
        #CounterTails.next_to(CounterTailsTxt, RIGHT)
        # self.play(Write(CounterHeads))
        # self.play(Write(CounterTails))
        CounterHeads = TextMobject("0")
        CounterHeads.next_to(CounterHeadsTxt, RIGHT)
        CounterTails = TextMobject("0")
        CounterTails.next_to(CounterTailsTxt, RIGHT)
        
        while t < throws+1:

            ht = randint(0, 1)

            if ht == 0:

                heads = heads + 1

                
                CounterHeadsNew = TextMobject(heads)

                recttailsbefore = Rectangle(fill_color=GOLD_B, fill_opacity=1, height=(
                    heads-1)*HeightAdjust, width=1, color=GOLD_B)
                recttailsnew = Rectangle(fill_color=GOLD_B, fill_opacity=1, height=(
                    heads)*HeightAdjust, width=1, color=GOLD_B)

                recttailsbefore.to_edge(DOWN)
                recttailsnew.to_edge(DOWN)
                recttailsnew.shift(2*LEFT)
                recttailsbefore.shift(2*LEFT)
                
                CounterHeadsNew.next_to(CounterHeadsTxt, RIGHT)

                # self.play(Uncreate(CounterHeadsOld))
                self.play(Transform(recttailsbefore, recttailsnew),
                          Transform(CounterHeads, CounterHeadsNew))

            elif ht == 1:

                tails = tails + 1

                
                CounterTailsNew = TextMobject(tails)

                rectheadbefore = Rectangle(fill_color=BLUE_B, fill_opacity=1, height=(
                    tails-1)*HeightAdjust, width=1, color=BLUE_B)
                rectheadnew = Rectangle(
                    fill_color=BLUE_B, fill_opacity=1, height=tails*HeightAdjust, width=1, color=BLUE_B)

                rectheadbefore.to_edge(DOWN)
                rectheadnew.to_edge(DOWN)
                rectheadnew.shift(2*RIGHT)
                rectheadbefore.shift(2*RIGHT)
                
                CounterTailsNew.next_to(CounterTailsTxt, RIGHT)

                # self.play(Uncreate(CounterTailsOld))
                self.play(Transform(rectheadbefore, rectheadnew),
                          Transform(CounterTails, CounterTailsNew))

            t = t + 1
