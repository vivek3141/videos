from manimlib.imports import *


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
