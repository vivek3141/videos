from manim import *
import gym


class Intro(Scene):
    def construct(self):
        pass


class QTitle(Scene):
    def construct(self):
        title = TextMobject("Q-Learning", color=BLUE)
        title.scale(2)

        self.play(Write(title))
        self.wait()


class QTable(Scene):
    def construct(self):
        table = Rectangle(height=3.5, width=3.5)

        b1 = Brace(table, LEFT)
        text = b1.get_text("State")

        b2 = Brace(table, UP)
        text2 = b2.get_text("Action")

        title = TextMobject("Q-Table", color=RED)
        title.scale(2)
        title.shift(2.5 * DOWN)

        self.play(Write(table))
        self.play(Write(b1), Write(b2), Write(text), Write(text2))

        self.wait()

        self.play(Write(title))


class MDP(Scene):
    def construct(self):
        mdp = TextMobject("Markov Descision Process", color=RED)
        mdp.scale(1.5)

        #im = ImageMobject("./files/pacman.jpg")
        #im.shift(3 * RIGHT)

        b1 = TextMobject("State")
        b1.scale(1.5)
        b1.shift(2 * LEFT + 1.5 * UP)

        b2 = TextMobject("Action")
        b2.scale(1.5)
        b2.shift(2 * LEFT + 0.5 * DOWN)

        b3 = TextMobject("Reward")
        b3.scale(1.5)
        b3.shift(2 * LEFT + 2.5 * DOWN)

        self.play(Write(mdp))
        self.wait()

        self.play(ApplyMethod(mdp.shift, 2.5 * UP))
        self.wait()

        self.play(Write(b1))
        self.wait()

        self.play(Write(b2))
        self.wait()

        self.play(Write(b3))
        self.wait()


class QLearning(Scene):
    def construct(self):
        flow = BulletedList(
            "Initialize Q Table",
            "Choose an action a",
            "Perform an action",
            "Measure Reward",
            "Update Q",
            "GOTO 1"
        )

        self.play(Write(flow))
        self.wait()

        for i in range(0, 6):
            self.play(ApplyMethod(flow.fade_all_but, i))
            self.wait()


class Initialize(Scene):
    def construct(self):
        table1 = VGroup(
            Rectangle(height=3, width=3),
            Line(0.5 * RIGHT + 1.5 * UP, 0.5 * RIGHT + 1.5 * DOWN),
            Line(0.5 * LEFT + 1.5 * UP, 0.5 * LEFT + 1.5 * DOWN),
            Line(1.5 * LEFT + 0.5 * UP, 1.5 * RIGHT + 0.5 * UP),
            Line(1.5 * LEFT + 0.5 * DOWN, 1.5 * RIGHT + 0.5 * DOWN),
            *[
                TextMobject("0").shift(z * UP + i * RIGHT) for i in range(-1, 2)
                for z in range(-1, 2)
            ]
        )

        table1.shift(2.5 * LEFT)

        title1 = TextMobject("Option 1", color=YELLOW)
        title1.scale(1.5)
        title1.shift(2.5 * UP + 2.5 * LEFT)

        title2 = TextMobject("Option 2", color=RED)
        title2.scale(1.5)
        title2.shift(2.5 * UP + 2.5 * RIGHT)

        colc = VGroup(
            TextMobject("from collections import Counter", tex_to_color_map={
                "from": PURPLE,
                "import": PURPLE
            }).shift(0.5 * UP),
            TextMobject("qtable = Counter()", tex_to_color_map={
                "Counter": BLUE,
                "=": PURPLE
            }).shift(0.5 * DOWN)
        )
        colc.scale(0.75)
        colc.shift(2.5 * RIGHT)

        self.play(
            Write(table1),
            Write(title1)
        )
        self.wait()

        self.play(
            Write(title2),
            Write(colc)
        )

        self.wait()


class QUpdate(Scene):
    def construct(self):
        equation = TexMobject(
            r"\text{New}Q(s,a)", r" = ", r"Q(s,a)", r" + ", r"\alpha", r"[R(s,a)", r" + \gamma", r"\text{max}Q'(s',a')-Q(s,a)]")

        li = equation.break_up_tex_strings([
            r"\text{New}Q(s,a)",
            r"Q(s,a)",
            r"\alpha[R(s,a)",
            r"\gamma\text{max}Q'(s',a')-Q(s,a)"
        ])
        texts = ["Learning Rate", "Reward", "Discount Rate",
                 "Maximum expected future reward"]

        def get_brace(obj, text, scale=0.5):
            brace = Brace(obj)
            t = brace.get_text(text)
            t.scale(scale)
            return [brace, t]

        braces = VGroup(
            *get_brace(equation[0], "New Q Value"),
            *get_brace(equation[2], "Current Q Value"),
            *[
                get_brace(i, n) for n, i in zip(texts, equation[4:])
            ]
        )

        self.play(Write(equation))
        self.wait()

        self.play(Write(braces))
        self.wait()


class Taxi(Scene):
    MAP = [
        "+---------+",
        "|R: | : :G|",
        "| : : : : |",
        "| : : : : |",
        "| | : | : |",
        "|Y| : |B: |",
        "+---------+",
    ]

    def construct(self):

        env = gym.make("Taxi-v2")

        self.q = np.zeros([env.observation_space.n, env.action_space.n])
        self.env = env
        self.continual = False

        r = TextMobject("R")
        r.shift(3 * LEFT + (3 - (6 / 10)) * UP)
        r.scale(1.5)

        g = TextMobject("G")
        g.shift(3 * RIGHT + (3 - (6 / 10)) * UP)
        g.scale(1.5)

        b = TextMobject("B")
        b.shift(3 * LEFT + (3 - (6 / 10)) * DOWN)
        b.scale(1.5)

        y = TextMobject("Y")
        y.shift(1 * RIGHT + (3 - (6 / 10)) * DOWN)
        y.scale(1.5)

        rows = VGroup(*[
            Line(i * UP - 4 * RIGHT, i * UP + 4 * RIGHT) for i in np.arange(-3, 4, 6 / 5)
        ])
        rows.set_fill(opacity=0.25)

        columns = VGroup(*[
            Line(3 * UP + i * RIGHT, 3 * DOWN + i * RIGHT) for i in range(-4, 6, 2)
        ])
        columns.set_fill(opacity=0.25)

        rr = np.arange(-3, 4, 6 / 5)
        cc = range(-4, 6, 2)

        taxi = Rectangle(color=YELLOW)

        borders = VGroup(
            Line(3 * UP + -4 * RIGHT, 3 * DOWN + -
                 4 * RIGHT, color=RED, stroke_width=8),
            Line(3 * UP + 4 * RIGHT, 3 * DOWN + 4 *
                 RIGHT, color=RED, stroke_width=8),
            Line(3 * UP - 4 * RIGHT, 3 * UP + 4 *
                 RIGHT, color=RED, stroke_width=8),
            Line(-3 * UP - 4 * RIGHT, -3 * UP + 4 *
                 RIGHT, color=RED, stroke_width=8),
            Line(3 * UP + -4 * RIGHT, 3 * DOWN + -
                 4 * RIGHT, color=RED, stroke_width=8),
            Line((3 - (12 / 5)) * DOWN + -2 * RIGHT, 3 *
                 DOWN + -2 * RIGHT, color=RED, stroke_width=8),
            Line((3 - (12 / 5)) * DOWN + 2 * RIGHT, 3 *
                 DOWN + 2 * RIGHT, color=RED, stroke_width=8),
            Line(3 * UP + 0 * RIGHT, (3 - 6 / 5) * UP +
                 0 * RIGHT, color=RED, stroke_width=8)
        )

        self.play(Write(rows))
        self.play(Write(columns))
        self.play(Write(borders))

        self.wait()

        self.play(Write(r), Write(g), Write(y), Write(b))
        self.wait()

    def continual_update(self, dt):
        if self.continual:
            pass

    def train(self, num_episodes=2000, learning_rate=0.618, gamma=1, to_print=True, interval=50, to_render=True):
        if to_print:
            print("Training...\n")

        for i in range(num_episodes):
            done = False
            total_reward = 0

            s = self.env.reset()

            while not done:
                action = np.argmax(self.q[s])
                state, reward, done, info = self.env.step(action)

                # Q[s_t, a_t] = a * (r + gamma * max(Q[s_t+1, a_t])) -> Q Learning formula
                # https://en.wikipedia.org/wiki/Q-learning
                self.q[s, action] = learning_rate * \
                    (reward + gamma * np.max(self.q[state]))

                s = state
                total_reward += reward

                if to_render:
                    self.env.render()

            if i % interval == 0 and to_print:
                print(f"Episode: {i + 1}, Reward{total_reward}")

    def test(self, num_episodes=5, to_print=True, to_render=True):
        if to_print:
            print("Testing...\n")

        for i in range(num_episodes):
            done = False
            total_reward = 0
            state = self.env.reset()

            while not done:
                state, reward, done, info = self.env.step(
                    np.argmax(self.q[state]))
                total_reward += reward

                if to_render:
                    self.env.render()

            if to_print:
                print(f"Episode {i + 1}, Reward {total_reward}")

    @staticmethod
    def decode(i):
        out = []
        out.append(i % 4)
        i = i // 4
        out.append(i % 5)
        i = i // 5
        out.append(i % 5)
        i = i // 5
        out.append(i)
        assert 0 <= i < 5
        return reversed(out)


class DQL(Scene):
    def construct(self):
        title = TextMobject("Deep Q Learning", color=GREEN)
        title.scale(2)

        t2 = TextMobject("Live Streamer AI")
        t2.scale(1.5)
        t2.shift(3 * UP)

        rect = ScreenRectangle(height=5)

        self.play(Write(title))
        self.wait()

        self.play(Uncreate(title))
        self.wait()

        self.play(Write(t2), Write(rect))
        self.wait()


class TwoStuff(Scene):
    def construct(self):
        sc1 = ScreenRectangle(height=3)
        sc1.shift(3 * LEFT)

        sc2 = ScreenRectangle(height=3)
        sc2.shift(3 * RIGHT)

        title = TextMobject("Applying NEAT", color=BLUE)
        title.scale(1.5)
        title.shift(2.5 * UP)

        self.play(Write(sc1), Write(sc2), Write(title))
        self.wait()
