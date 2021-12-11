from manimlib import *

class Test(Scene):
    def construct(self):
        i = Tex(r"\int_a^b f(x) dx")
        i.scale(3)
        self.play(Write(i))
        self.wait()
        self.embed()
