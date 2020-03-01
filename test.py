from manimlib.imports import *


class EMWave(VGroup):
    def __init__(
        self,
        E_COLOR=YELLOW, M_COLOR=BLUE,
        frequency=1,
        alpha=1,
        num_vects=30,
        start=-FRAME_WIDTH/2,
        end=FRAME_WIDTH/2,
        **kwargs
    ):
        VGroup.__init__(self, **kwargs)
        self.alpha = alpha
        self.frequency = frequency
        self.start = start
        self.end = end
        self.tracker = ValueTracker(0)
        e_wave = VGroup(
            *[self.get_vect(E_COLOR, t, direction=UP) for t in np.linspace(self.start, self.end, num=num_vects)]
        )
        m_wave = VGroup(
            *[self.get_vect(M_COLOR, t, direction=IN) for t in np.linspace(self.start, self.end, num=num_vects)]
        )
        self.add(e_wave)
        self.add(m_wave)

    def get_t(self, value):
        return value - self.start

    def get_vect(self, color, t, direction=IN):
        x = self.get_t(t)
        length = self.alpha * np.sin(x)
        vect = Vector(direction=direction * length, color=color).shift(t * RIGHT)
        vect.add_updater(lambda obj: obj.become(
            self.get_vect_updater(self.tracker.get_value(), color, t, direction=direction)))
        return vect

    def get_vect_updater(self, t, color, phi, direction=IN):
        x = self.get_t(t)
        length = self.alpha * np.sin(self.frequency * x + self.frequency * phi)
        return Vector(length * direction, color=color).shift(phi * RIGHT)


class EMTest(ThreeDScene):
    def construct(self):
        vect = Vector(OUT, color=YELLOW)
        self.move_camera(0.4 * np.pi / 2, -PI/2)
        self.add(vect)
        wave = EMWave()
        #self.add(wave)
        #self.play(wave.tracker.increment_value, 4 *
                  #PI, run_time=4, rate_func=linear)


"""
class EMScene(Scene):
    CONFIG = {
        "frequency": 1,
        "num_vects": 30,
        "alpha": 1,
        "run_time": 8,
        "osc_freq": 1
    }

    def construct(self):
        self.tracker = ValueTracker(0)
        wave = VGroup(
            *[self.get_vect(YELLOW, t) for t in np.linspace(-2*PI, 2*PI, num=self.num_vects)]
        )
        self.play(Write(wave))
        self.play(
            self.tracker.increment_value,
            self.osc_freq * self.run_time * PI,
            run_time=self.run_time,
            rate_func=linear
        )
        self.wait()

    def get_vect(self, color, t):
        length = self.alpha * np.sin(t)
        vect = Vector(direction=np.array(
            [0, length, 0]), color=color).shift(t * RIGHT)
        vect.add_updater(lambda x: x.become(
            self.get_vect_updater(self.tracker.get_value(), color, t)))
        return vect

    def get_vect_updater(self, t, color, phi):
        length = self.alpha * np.sin(self.frequency * t + self.frequency * phi)
        return Vector([0, length, 0], color=color).shift(phi * RIGHT)
"""
