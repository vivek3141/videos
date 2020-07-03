from manimlib.imports import *


class IntroQuote(Scene):
    def construct(self):
        quote = TextMobject("""
        I have to pay a certain sum, which I have collected in my pocket.
        I take the bills and coins out of my pocket and give them to the 
        creditor in the order I find them until I have reached the total 
        sum. This is the Riemann integral. But I can proceed differently. 
        After I have taken all the money out of my pocket I order the bills 
        and coins according to identical values and then I pay the 
        several heaps one after the other to the creditor. This is my integral.""")
        quote.scale(0.75)
        author = TextMobject("- Henri Lebesgue", color=YELLOW)
        author.shift(2 * DOWN + 3 * RIGHT)
        self.play(Write(quote))
        self.play(Write(author))
        self.wait(5)
