from manimlib import *


"""
Scenes In Order:

EmailModel
MNISTClassification
NextWordPrediction
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

        self.add(dice_grp)

        self.embed()
