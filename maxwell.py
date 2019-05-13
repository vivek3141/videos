from manim import *


E_COLOR = BLUE
M_COLOR = YELLOW


class Intro(Scene):
    def construct(self):
        pass


class OscillatingVector(ContinualAnimation):
    CONFIG = {
        "tail": ORIGIN,
        "frequency": 1,
        "A_vect": [1, 0, 0],
        "phi_vect": [0, 0, 0],
        "vector_to_be_added_to": None,
    }

    def setup(self):
        self.vector = self.mobject

    def update_mobject(self, dt):
        f = self.frequency
        t = self.internal_time
        angle = 2*np.pi*f*t
        vect = np.array([
            A*np.exp(complex(0, angle + phi))
            for A, phi in zip(self.A_vect, self.phi_vect)
        ]).real
        self.update_tail()
        self.vector.put_start_and_end_on(self.tail, self.tail+vect)

    def update_tail(self):
        if self.vector_to_be_added_to is not None:
            self.tail = self.vector_to_be_added_to.get_end()


class OscillatingVectorComponents(ContinualAnimationGroup):
    CONFIG = {
        "tip_to_tail": False,
    }

    def __init__(self, oscillating_vector, **kwargs):
        digest_config(self, kwargs)
        vx = Vector(UP, color=GREEN).fade()
        vy = Vector(UP, color=RED).fade()
        kwargs = {
            "frequency": oscillating_vector.frequency,
            "tail": oscillating_vector.tail,
        }
        ovx = OscillatingVector(
            vx,
            A_x=oscillating_vector.A_x,
            phi_x=oscillating_vector.phi_x,
            A_y=0,
            phi_y=0,
            **kwargs
        )
        ovy = OscillatingVector(
            vy,
            A_x=0,
            phi_x=0,
            A_y=oscillating_vector.A_y,
            phi_y=oscillating_vector.phi_y,
            **kwargs
        )
        components = [ovx, ovy]
        self.vectors = VGroup(ovx.vector, ovy.vector)
        if self.tip_to_tail:
            ovy.vector_to_be_added_to = ovx.vector
        else:
            self.lines = VGroup()
            for ov1, ov2 in (ovx, ovy), (ovy, ovx):
                ov_line = ov1.copy()
                ov_line.mobject = ov_line.vector = DashedLine(
                    UP, DOWN, color=ov1.vector.get_color()
                )
                ov_line.vector_to_be_added_to = ov2.vector
                components.append(ov_line)
                self.lines.add(ov_line.line)

        ContinualAnimationGroup.__init__(self, *components, **kwargs)


class EMWave(ContinualAnimationGroup):
    CONFIG = {
        "wave_number": 1,
        "frequency": 0.25,
        "n_vectors": 40,
        "propogation_direction": RIGHT,
        "start_point": FRAME_X_RADIUS*LEFT + DOWN + OUT,
        "length": FRAME_WIDTH,
        "amplitude": 1,
        "rotation": 0,
        "A_vect": [0, 0, 1],
        "phi_vect": [0, 0, 0],
        "requires_start_up": False,
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        if not all(self.propogation_direction == RIGHT):
            self.matrix_transform = np.dot(
                z_to_vector(self.propogation_direction),
                np.linalg.inv(z_to_vector(RIGHT)),
            )
        else:
            self.matrix_transform = None

        vector_oscillations = []
        self.E_vects = VGroup()
        self.M_vects = VGroup()

        self.A_vect = np.array(self.A_vect)/get_norm(self.A_vect)
        self.A_vect *= self.amplitude

        for alpha in np.linspace(0, 1, self.n_vectors):
            tail = interpolate(ORIGIN, self.length*RIGHT, alpha)
            phase = -alpha*self.length*self.wave_number
            kwargs = {
                "phi_vect": np.array(self.phi_vect) + phase,
                "frequency": self.frequency,
                "tail": np.array(tail),
            }
            E_ov = OscillatingVector(
                Vector(
                    OUT, color=E_COLOR,
                    normal_vector=UP,
                ),
                A_vect=self.A_vect,
                **kwargs
            )
            M_ov = OscillatingVector(
                Vector(
                    UP, color=M_COLOR,
                    normal_vector=OUT,
                ),
                A_vect=rotate_vector(self.A_vect, np.pi/2, RIGHT),
                **kwargs
            )
            vector_oscillations += [E_ov, M_ov]
            self.E_vects.add(E_ov.vector)
            self.M_vects.add(M_ov.vector)
        ContinualAnimationGroup.__init__(self, *vector_oscillations)

    def update_mobject(self, dt):
        if self.requires_start_up:
            n_wave_lengths = self.length / (2*np.pi*self.wave_number)
            prop_time = n_wave_lengths/self.frequency
            middle_alpha = interpolate(
                0.4, 1.4,
                self.external_time / prop_time
            )
            new_smooth = squish_rate_func(smooth, 0.4, 0.6)

            ovs = self.continual_animations
            for ov, alpha in zip(ovs, np.linspace(0, 1, len(ovs))):
                epsilon = 0.0001
                new_amplitude = np.clip(
                    new_smooth(middle_alpha - alpha), epsilon, 1
                )
                norm = get_norm(ov.A_vect)
                if norm != 0:
                    ov.A_vect = new_amplitude * np.array(ov.A_vect) / norm

        ContinualAnimationGroup.update_mobject(self, dt)
        self.mobject.rotate(self.rotation, RIGHT)
        if self.matrix_transform:
            self.mobject.apply_matrix(self.matrix_transform)
        self.mobject.shift(self.start_point)

