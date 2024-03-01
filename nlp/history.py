from manimlib import *


"""
Scenes In Order:

EmailModel
MNISTClassification
NextWordPrediction
DiceProbability
NGramModel
Inference
"""

A_AQUA = "#8dd3c7"
A_YELLOW = "#ffffb3"
A_LAVENDER = "#bebada"
A_RED = "#fb8072"
A_BLUE = "#80b1d3"
A_ORANGE = "#fdb462"
A_GREEN = "#b3de69"
A_PINK = "#fccde5"
A_GREY = "#d9d9d9"
A_VIOLET = "#bc80bd"
A_UNKA = "#ccebc5"
A_UNKB = "#ffed6f"


class RNNCell(VMobject):
    def __init_(self, fill_color=A_RED, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sq = Square()


class MNISTImage(VMobject):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for x, xpos in enumerate(np.arange(-3, 3, 6 / 28)):
            for y, ypos in enumerate(np.arange(-3, 3, 6 / 28)):
                self.add(
                    Rectangle(
                        height=6 / 28,
                        width=6 / 28,
                        stroke_width=1,
                        stroke_opacity=0.25,
                        fill_opacity=data[abs(y - 27) * 28 + x],
                    ).shift([xpos, ypos, 0])
                )

    def set_opacity(self, opacity):
        for rect in self:
            rect.set_fill(opacity=opacity * rect.get_fill_opacity())
            rect.set_stroke(opacity=opacity * rect.get_stroke_opacity())


class Dice(VMobject):
    def __init__(
        self,
        number,
        square_width=2.0,
        dot_radius=0.15,
        dot_color=A_UNKA,
        square_color=A_GREY,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.square = RoundedRectangle(
            height=square_width,
            width=square_width,
            corner_radius=0.375,
            color=square_color,
        )
        self.dots = VGroup()

        dot_kwargs = {"radius": dot_radius, "color": dot_color}
        if number == 1:
            self.dots.add(Dot(**dot_kwargs))
        elif number == 2:
            self.dots.add(
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * RIGHT),
            )
        elif number == 3:
            self.dots.add(
                Dot(**dot_kwargs),
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * RIGHT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * LEFT),
            )
        elif number == 4:
            self.dots.add(
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * RIGHT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * RIGHT),
            )
        elif number == 5:
            self.dots.add(
                Dot(**dot_kwargs),
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * RIGHT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * RIGHT),
            )
        elif number == 6:
            self.dots.add(
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * UP + 0.5 * RIGHT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * DOWN + 0.5 * RIGHT),
                Dot(**dot_kwargs).shift(0.5 * LEFT),
                Dot(**dot_kwargs).shift(0.5 * RIGHT),
            )

        self.add(self.square, self.dots)


class Document(VMobject):
    def __init__(self, rect_color=GREY_D, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rect = Rectangle(
            height=2.5, width=2, fill_color=rect_color, fill_opacity=1
        )
        self.lines = VGroup(
            *[
                Line(0.75 * LEFT, 0.75 * RIGHT).shift(0.25 * (i - 3) * UP)
                for i in range(7)
            ]
        )
        self.lines[-1].set_width(1)
        self.lines[-1].shift(0.25 * LEFT)

        self.add(self.rect, self.lines)


class MNISTGroup(VGroup):
    def set_opacity(self, opacity):
        for img in self:
            img.set_opacity(opacity)


class EmailModel(Scene):
    def construct(self):
        prompt = Text("Write an email to my mom.")
        prompt.scale(1.25)
        prompt.shift(3 * UP)

        # Found the offset by averaging the bounding boxes
        model_sq = RoundedRectangle(width=12.5)
        model_sq.set_fill(GREY_D, 1)
        model_sq.shift(0.6576390599999999 * UP)

        question = Text("?")
        question.move_to(model_sq)
        question.scale(2.5)

        arr1 = Arrow(
            prompt,
            model_sq,
            stroke_color=RED_A,
            max_width_to_Length_ratio=float("inf"),
            stroke_width=10,
        )

        response = Text(
            "Hi Mom,\nHope you're doing well.\n"
            "Just wanted to see how you're feeling today."
            "\nLove, Vivek"
        )
        response.shift(2.5 * DOWN)

        arr2 = Arrow(
            model_sq,
            response,
            stroke_color=RED_A,
            max_width_to_Length_ratio=float("inf"),
            stroke_width=10,
        )

        VGroup(prompt, model_sq, question, arr1, response, arr2).center()

        self.play(Write(prompt))
        self.play(
            Write(arr1),
            Write(model_sq),
            Write(question),
            Write(arr2),
        )
        self.play(Write(response))
        self.wait()

        self.embed()


class MNISTClassification(Scene):
    def construct(self):
        np.random.seed(0)
        mnist = np.load("mnist_data.npy")

        cols = 8
        rows = 5
        mnist_images = MNISTGroup()
        for i in range(rows):
            for j in range(cols):
                mnist_images.add(
                    MNISTImage(mnist[i * cols + j].flatten())
                    .shift(
                        [
                            -FRAME_WIDTH / 2 + FRAME_WIDTH / (cols + 1) * (j + 1),
                            -FRAME_HEIGHT / 2 + FRAME_HEIGHT / (rows + 1) * (i + 1),
                            0,
                        ]
                    )
                    .scale(0.2)
                )

        accuracy = 0.9
        actual = 0
        labels = VGroup()
        for i in range(len(mnist_images)):
            if np.random.rand() < accuracy:
                labels.add(Checkmark().scale(1.5).move_to(mnist_images[i]))
                actual += 1
            else:
                labels.add(Exmark().scale(1.5).move_to(mnist_images[i]))

        accuracy_text = Tex(
            r"\text{Accuracy: }", f"{round(100 * actual/len(mnist_images), 1)}", r"\%"
        )
        accuracy_text.scale(1.5)
        accuracy_text.shift(3.25 * UP)

        self.play(Write(mnist_images))
        self.wait()

        self.play(ApplyMethod(mnist_images.set_opacity, 0.25))
        self.play(Write(labels))
        self.wait()

        self.play(ApplyMethod(VGroup(mnist_images, labels).shift, 0.4 * DOWN))
        self.play(Write(accuracy_text))
        self.wait()

        self.embed()


class NextWordPrediction(Scene):
    def construct(self):
        probs = [
            ("the", 0.1524),
            ("blue", 0.0859),
            ("falling", 0.0729),
            ("a", 0.0508),
            ("full", 0.034),
            ("dark", 0.0299),
            ("not", 0.028),
            ("clear", 0.0237),
            ("black", 0.0189),
        ][::-1]

        rect = RoundedRectangle(
            height=2.5,
            width=2.5,
            fill_color=GREY_D,
            fill_opacity=1,
        )
        rect.shift(0.5 * LEFT)
        p_theta = Tex(r"\mathbb{P}_{\theta}")
        p_theta.scale(2)
        p_theta.move_to(rect)

        self.play(Write(rect), Write(p_theta))
        self.wait()

        prompt = Text("The sky is")
        prompt.scale(1.5)
        prompt.shift(5 * LEFT)

        arr = Arrow(
            prompt,
            rect,
            stroke_color=A_PINK,
            max_width_to_Length_ratio=float("inf"),
            stroke_width=10,
        )

        brace = Brace(prompt)
        brace_tex = brace.get_tex(
            r"k = 3", tex_to_color_map={r"k": A_YELLOW, "3": A_UNKA}
        )
        brace.add(brace_tex)

        self.play(Write(prompt), Write(arr))
        self.play(Write(brace))
        self.wait()

        prob_bars = VGroup()
        prob_arrows = VGroup()
        for i, (word, prob) in enumerate(probs):
            bar = Rectangle(
                height=0.5,
                width=prob * 10,
                fill_color=A_LAVENDER,
                fill_opacity=1,
            )
            bar.move_to(FRAME_HEIGHT / (len(probs) + 1) * i * UP, LEFT)

            word_text = Text(word)
            word_text.move_to(bar.get_bounding_box_point(LEFT) + 1 * LEFT)

            prob_text = Text(f"{prob:.4f}")
            prob_text.move_to(bar.get_bounding_box_point(RIGHT) + 1 * RIGHT)

            prob_bars.add(bar, word_text, prob_text)

        prob_bars.center()
        prob_bars.shift(4.5 * RIGHT)

        min_left_point = min(
            [
                prob_bars[3 * i + 1].get_bounding_box_point(LEFT)[0]
                for i in range(len(probs))
            ]
        )

        prob_arrows = VGroup()
        for i in range(len(probs)):
            left_point = prob_bars[3 * i + 1].get_bounding_box_point(LEFT)
            left_point[0] = min_left_point - 0.25

            prob_arrows.add(
                Arrow(
                    rect.get_bounding_box_point(RIGHT),
                    left_point,
                    stroke_color=A_PINK,
                    max_width_to_Length_ratio=float("inf"),
                    stroke_width=5,
                    buff=0,
                )
            )

        self.play(Write(prob_arrows))
        self.play(Write(prob_bars))
        self.wait()

        anims = [
            ApplyMethod(prob_arrows[i].set_opacity, 0.25)
            for i in range(len(probs))
            if i != len(probs) - 2
        ]
        for i in range(len(probs)):
            if i == len(probs) - 2:
                continue

            for j in range(3):
                anims.append(ApplyMethod(prob_bars[3 * i + j].set_opacity, 0.25))

        self.play(*anims)
        self.wait()

        lm_text = Text("Language\nModel", color=A_UNKA)
        c1 = lm_text[:-5].get_center()
        c2 = lm_text[-5:].get_center()
        lm_text[-5:].move_to([c1[0], c2[1], 0])

        lm_text.move_to(rect)
        lm_text.shift(2 * UP)

        self.play(Write(lm_text))

        self.embed()


class DiceProbability(Scene):
    def construct(self):
        dice_grp = VGroup()
        for i in range(1, 7):
            d = Dice(
                i,
                square_width=2.0,
                dot_radius=0.15,
                dot_color=A_UNKA,
                square_color=A_GREY,
            )
            d.shift(FRAME_WIDTH / 7 * i * RIGHT)
            d.scale(0.75)
            dice_grp.add(d)
        dice_grp.center()

        two_three = dice_grp[1:3].deepcopy()
        two_three.center()
        two_three.shift(1.5 * UP)

        hline = Line(6.25 * LEFT, 6.25 * RIGHT)

        self.play(Write(dice_grp))
        self.wait()

        self.play(ApplyMethod(dice_grp.shift, 1.5 * DOWN), Write(hline))
        self.play(TransformFromCopy(dice_grp[1:3], two_three))
        self.wait()

        self.embed()


class NGramModel(Scene):
    def construct(self):
        eq = Tex(
            r"\mathbb{P}[" r"\text{blue} \ | \ \text{the sky is}]",
            r"= {C(\text{the }\text{sky is}\text{ }\text{blue}) \over C(\text{the }\text{sky is})}",
            tex_to_color_map={
                r"\text{blue}": A_BLUE,
                r"\text{the sky is}": A_UNKA,
                r"\text{sky is}": A_UNKA,
                r"\text{the }": A_UNKA,
                r"C": A_UNKB,
                r"\mathbb{P}": A_ORANGE,
            },
        )
        eq.scale(1.5)

        self.play(Write(eq[:6]))
        self.wait(0.5)

        self.play(Write(eq[6:]))
        self.wait()

        self.play(Transform(eq, eq.copy().scale(1 / 1.5).shift(3 * UP)))

        d_grp = VGroup()
        for i in range(2):
            for j in range(4):
                d_grp.add(Document().shift(i * 3 * UP + j * 3 * RIGHT))
        d_grp.center()
        d_grp.shift(0.75 * DOWN)

        d = Document()

        anims = [TransformFromCopy(d, d_grp[i]) for i in range(len(d_grp) - 1)] + [
            Transform(d, d_grp[-1], replace_mobject_with_target_in_scene=True)
        ]
        self.play(Write(d))
        self.play(*anims)
        self.wait()

        blue_prob = 0.3
        other_words = ["red", "green", "yellow", "orange"]
        other_word_color_map = {
            "red": A_RED,
            "green": A_GREEN,
            "yellow": A_YELLOW,
            "orange": A_ORANGE,
        }

        np.random.seed(15)
        texts_is, texts_was, texts_two = VGroup(), VGroup(), VGroup()
        is_anims, was_anims, two_anims = [], [], []

        for i in range(len(d_grp)):
            if np.random.rand() < blue_prob:
                text_is = TexText(
                    "the sky is blue",
                    tex_to_color_map={"blue": A_BLUE, "the sky is": A_UNKA},
                )
                text_was = TexText(
                    "the sky was blue",
                    tex_to_color_map={"blue": A_BLUE, "sky was": A_UNKA, "the": A_UNKA},
                )
                text_two = TexText(
                    "sky is blue",
                    tex_to_color_map={"blue": A_BLUE, "sky is": A_UNKA},
                )
            else:
                other_word = np.random.choice(other_words)
                text_is = TexText(
                    f"the sky is {other_word}",
                    tex_to_color_map={
                        other_word: other_word_color_map[other_word],
                        "the sky is": A_UNKA,
                    },
                )
                text_was = TexText(
                    f"the sky was {other_word}",
                    tex_to_color_map={
                        other_word: other_word_color_map[other_word],
                        "sky was": A_UNKA,
                        "the": A_UNKA,
                    },
                )
                text_two = TexText(
                    f"sky is {other_word}",
                    tex_to_color_map={
                        other_word: other_word_color_map[other_word],
                        "sky is": A_UNKA,
                    },
                )

            curr_line = d_grp[i].lines[np.random.randint(7)]

            text_is.move_to(curr_line)
            text_is.scale(0.45)

            text_was.move_to(curr_line)
            text_was.scale(0.45)

            text_two.move_to(curr_line)
            text_two.scale(0.45)

            texts_is.add(text_is)
            texts_was.add(text_was)
            texts_two.add(text_two)

            is_anims.append(
                Transform(curr_line, text_is, replace_mobject_with_target_in_scene=True)
            )
            was_anims.append(
                TransformMatchingShapes(
                    text_is, text_was, replace_mobject_with_target_in_scene=True
                )
            )
            two_anims += [
                Uncreate(text_was[0]),
                TransformMatchingShapes(
                    text_was[1:], text_two, replace_mobject_with_target_in_scene=True
                ),
            ]

        self.play(*is_anims)
        self.wait()

        self.play(*was_anims)
        self.wait()

        b = Brace(eq[-1], RIGHT)
        b_tex = b.get_tex(r"k = 3", tex_to_color_map={r"k": A_YELLOW, "3": A_UNKA})
        b_tex.add_background_rectangle(buff=0.1)

        self.play(Write(b), Write(b_tex))
        self.wait()

        self.play(Uncreate(b), Uncreate(b_tex))

        eq2 = Tex(
            r"\mathbb{P}[" r"\text{blue} \ | \ \text{the sky is}]",
            r"= {C(\text{sky is}\text{ }\text{blue}) \over C(\text{sky is})}",
            tex_to_color_map={
                r"\text{blue}": A_BLUE,
                r"\text{the sky is}": A_UNKA,
                r"\text{sky is}": A_UNKA,
                r"C": A_UNKB,
                r"\mathbb{P}": A_ORANGE,
            },
        )
        eq2.shift(3 * UP)

        self.play(
            Transform(eq[:9], eq2[:9]),
            FadeOut(eq[9]),
            Transform(eq[10:15], eq2[9:14]),
            Uncreate(eq[15]),
            Transform(eq[16:], eq2[14:]),
        )
        self.remove(eq)
        self.add(eq2)

        self.play(*two_anims)
        self.wait()

        eq3 = Tex(
            r"\mathbb{P}[" r"\text{blue} \ | \ \text{the sky is}]",
            r"\approx {C(\text{sky is}\text{ }\text{blue}) \over C(\text{sky is})}",
            tex_to_color_map={
                r"\text{blue}": A_BLUE,
                r"\text{the sky is}": A_UNKA,
                r"\text{sky is}": A_UNKA,
                r"C": A_UNKB,
                r"\mathbb{P}": A_ORANGE,
            },
        )
        eq3.shift(3 * UP)

        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()

        self.play(
            FadeOut(
                VGroup(
                    *[i for i in self.mobjects if isinstance(i, VMobject) and i != eq3]
                ),
                DOWN,
            )
        )

        eq4 = Tex(
            r"\mathbb{P}[" r"w_i \ | \ w_{i-3}w_{i-2}w_{i-1}]",
            r"\approx {C(w_{i-2}w_{i-1}w_i) \over C(w_{i-2}w_{i-1})}",
            tex_to_color_map={
                r"w_i": A_BLUE,
                r"w_{i-3}": A_UNKA,
                r"w_{i-2}": A_UNKA,
                r"w_{i-1}": A_UNKA,
                r"C": A_UNKB,
                r"\mathbb{P}": A_ORANGE,
            },
        )
        eq4.scale(1.25)

        self.play(
            TransformFromCopy(eq3[:2], eq4[:2]),
            TransformFromCopy(eq3[3], eq4[3]),
            TransformFromCopy(eq3[5:9], eq4[7:11]),
            TransformFromCopy(eq3[11:14], eq4[14:17]),
            TransformFromCopy(eq3[15:], eq4[19:]),
        )
        self.play(
            TransformFromCopy(eq3[2], eq4[2]), TransformFromCopy(eq3[10], eq4[13])
        )
        self.play(TransformFromCopy(eq3[4][:3], eq4[4]))
        self.play(
            TransformFromCopy(eq3[4][3:6], eq4[5]),
            TransformFromCopy(eq3[9][:3], eq4[11]),
            TransformFromCopy(eq3[14][:3], eq4[17]),
        )
        self.play(
            TransformFromCopy(eq3[4][6:], eq4[6]),
            TransformFromCopy(eq3[9][3:], eq4[12]),
            TransformFromCopy(eq3[14][3:], eq4[18]),
        )
        self.remove(eq3)
        self.add(eq4)

        title = Text("N-Gram Language Model", color=A_VIOLET)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(FadeOut(eq3, UP), Write(title))
        self.wait()

        b = Brace(eq4)
        b_tex = b.get_tex(r"\text{Trigram Model}")

        self.play(Write(b), Write(b_tex))
        self.wait()

        self.play(Uncreate(b), Uncreate(b_tex))

        eq5 = Tex(
            r"\mathbb{P}[" r"w_i \ | \ w_{i-3}w_{i-2}w_{i-1}]",
            r"\approx {C(w_{i-2}w_{i-1}w_i) + 1 \over C(w_{i-2}w_{i-1}) + |V|}",
            tex_to_color_map={
                r"w_i": A_BLUE,
                r"w_{i-3}": A_UNKA,
                r"w_{i-2}": A_UNKA,
                r"w_{i-1}": A_UNKA,
                r"C": A_UNKB,
                r"\mathbb{P}": A_ORANGE,
                r"V": MAROON_A,
                r"1": A_UNKA,
            },
        )
        eq5.scale(1.25)

        self.play(
            ApplyMethod(eq4[:14].move_to, eq5[:14]),
            ApplyMethod(eq4[14][0].move_to, eq5[14][0]),
            Transform(eq4[14][1:], eq5[16]),
            ApplyMethod(eq4[15:].move_to, VGroup(eq5[17:21], eq5[21][0])),
        )
        self.play(
            Write(eq5[15]), Write(eq5[14][1:]), Write(eq5[21][1:]), Write(eq5[22:])
        )
        self.wait()

        self.embed()


class Inference(Scene):
    def construct(self):
        words1 = [
            " a",
            " the",
            " not",
            " to",
            " ,",
            " that",
            " in",
        ]
        probs1 = (
            0.08705387523141485,
            0.07940873709043825,
            0.05225144958160702,
            0.027861431060304042,
            0.024988107409824458,
            0.023519410891033286,
            0.017348392643645783,
        )
        # words1, probs1 = words1[::-1], probs1[::-1]

        text = Text("The most beautiful proof in math is")
        text.scale(1.25)
        text.shift(3 * UP)

        self.play(Write(text))

        prob_bars_small, prob_bars_large = VGroup(), VGroup()
        words, probs = VGroup(), VGroup()

        for i, (word, prob) in enumerate(zip(words1, probs1)):
            bar_small = Rectangle(
                height=0.5,
                width=0,
                fill_color=A_LAVENDER,
                fill_opacity=1,
            )

            bar_large = Rectangle(
                height=0.5,
                width=prob * 10,
                fill_color=A_LAVENDER,
                fill_opacity=1,
            )

            bar_small.move_to(FRAME_HEIGHT / 10 * i * DOWN, LEFT)
            bar_large.move_to(FRAME_HEIGHT / 10 * i * DOWN, LEFT)

            word_text = Text(word)
            word_text.move_to(bar_large.get_bounding_box_point(LEFT) + 1 * LEFT)

            prob_text = Text(f"{prob:.4f}")
            prob_text.move_to(bar_large.get_bounding_box_point(RIGHT) + 1 * RIGHT)

            prob_bars_small.add(bar_small)
            prob_bars_large.add(bar_large)
            words.add(word_text)
            probs.add(prob_text)

        prob_bars_grp = VGroup(prob_bars_large, words, probs)
        prob_bars_grp.center()
        prob_bars_grp.shift(0.5 * DOWN)

        anims = []
        for i in range(len(prob_bars_small)):
            prob_bars_small[i].move_to(prob_bars_large[i], LEFT)
            anims.append(
                ApplyMethod(prob_bars_small[i].become, prob_bars_large[i].copy())
            )

        # prob_bars = VGroup()
        # widths = []

        # for i, (word, prob) in enumerate(zip(words1, probs1)):
        #     bar = Rectangle(
        #         height=0.5,
        #         width=prob * 10,
        #         fill_color=A_LAVENDER,
        #         fill_opacity=1,
        #     )
        #     widths.append(prob * 10)

        #     bar.move_to(FRAME_HEIGHT / (10) * i * UP, LEFT)

        #     word_text = Text(word)
        #     word_text.move_to(bar.get_bounding_box_point(LEFT) + 1 * LEFT)

        #     prob_text = Text(f"{prob:.4f}")
        #     prob_text.move_to(bar.get_bounding_box_point(RIGHT) + 1 * RIGHT)

        #     prob_bars.add(bar, word_text, prob_text)

        # prob_bars.center()
        # prob_bars.shift(0.5 * DOWN)

        # anims = [
        #     ApplyMethod(
        #         prob_bars[3 * i].become,
        #         Rectangle(
        #             height=0.5, width=widths[i], fill_color=A_LAVENDER, fill_opacity=1
        #         ).move_to(prob_bars[3 * i]),
        #     )
        #     for i in range(len(words1))
        # ]

        # self.add(prob_bars)

        self.embed()
