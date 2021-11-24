from manimlib import *
import itertools


class Cylinder(Sphere):
    def func(self, u, v):
        return np.array([
            np.cos(v),
            np.sin(v),
            np.cos(u)
        ])


class UnwrappedCylinder(Cylinder):
    def func(self, u, v):
        return np.array([
            v - PI,
            -self.radius,
            np.cos(u)
        ])


class Scene(Scene):
    def interact(self):
        self.quit_interaction = False
        self.lock_static_mobject_data()
        try:
            while True:
                self.update_frame()
        except KeyboardInterrupt:
            self.unlock_mobject_data()


class LatticeTorus(Scene):
    def construct(self):
        f_plane_kwargs = {
            "x_range": (-4, 4),
            "y_range": (-3, 3)
        }

        points = VGroup()
        plane2 = NumberPlane(**f_plane_kwargs)
        for x, y in itertools.product(*[np.arange(args[0], args[1]+1, args[2]) for args in plane2.get_all_ranges()]):
            points.add(Dot([x, y, 0]))

        self.add(plane2, points)
        self.embed()

    def cyln(self, u, v):
        return np.array([
            np.cos(u),
            np.sin(u),
            v
        ])
