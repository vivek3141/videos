from manim import *
import gym
import numpy as np


class QLearning(Scene):
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
        table = VGroup(*[
            Line(3 * UP + i * RIGHT, 3 * DOWN + i * RIGHT) for i in range(-2, 3)
        ])

        self.play(Write(table))

    def continual_update(self, dt):
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
                self.q[s, action] = learning_rate * (reward + gamma * np.max(self.q[state]))

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
                state, reward, done, info = self.env.step(np.argmax(self.q[state]))
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
