from manimlib.imports import *


class Intro(Scene):
    pass


class Horn(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func, 
        )
    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])