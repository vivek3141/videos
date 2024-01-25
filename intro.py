from manimlib import *


class IntroSmooth(Scene):
    def construct(self):
        h1 = "#ff5757"
        h2 = "#5ce1e6"

        text = Tex(
            r"\textbf{\text{v}} ^3} \textbf{(}\textbf{\text{x}}}\textbf{)}",
            tex_to_color_map={r"\textbf{\text{v}} ^3": h1, r"\textbf{\text{x}}": h2},
            font_size=48 * 4,
        )
        # text[1].make_smooth()
        # text[-1].make_smooth()

        vc = TexText("vcubingx")
        vc.scale(1.5)
        vc.shift(2 * DOWN)

        self.play(Write(text), run_time=2)
        self.play(FadeIn(vc))
        self.wait()

        self.embed()
