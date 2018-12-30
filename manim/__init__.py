"""
I won't pretend like this is best practice, by in creating animations for a video,
it can be very nice to simply have all of the Mobjects, Animations, Scenes, etc.
of manim available without having to worry about what namespace they come from.

Rather than having a large pile of "from manim.<module> import *" at the top of every such
script, the intent of this file is to make it so that one can just include
"from manim.big_ol_pile_of_manim_imports import *".  The effects of adding more modules
or refactoring the library on current or older scene scripts should be entirely
addressible by changing this file.

Note: One should NOT import from manim.this file for main library code, it is meant only
as a convenience for scripts creating scenes for videos.
"""


from manim.constants import *

from manim.animation.animation import *
from manim.animation.composition import *
from manim.animation.creation import *
from manim.animation.indication import *
from manim.animation.movement import *
from manim.animation.numbers import *
from manim.animation.rotation import *
from manim.animation.specialized import *
from manim.animation.transform import *
from manim.animation.update import *

from manim.camera.camera import *
from manim.camera.mapping_camera import *
from manim.camera.moving_camera import *
from manim.camera.three_d_camera import *

from manim.continual_animation.continual_animation import *
from manim.continual_animation.from_animation import *
from manim.continual_animation.numbers import *
from manim.continual_animation.update import *

from manim.mobject.coordinate_systems import *
from manim.mobject.frame import *
from manim.mobject.functions import *
from manim.mobject.geometry import *
from manim.mobject.matrix import *
from manim.mobject.mobject import *
from manim.mobject.number_line import *
from manim.mobject.numbers import *
from manim.mobject.probability import *
from manim.mobject.shape_matchers import *
from manim.mobject.svg.brace import *
from manim.mobject.svg.drawings import *
from manim.mobject.svg.svg_mobject import *
from manim.mobject.svg.tex_mobject import *
from manim.mobject.three_d_utils import *
from manim.mobject.three_dimensions import *
from manim.mobject.types.image_mobject import *
from manim.mobject.types.point_cloud_mobject import *
from manim.mobject.types.vectorized_mobject import *
from manim.mobject.updater import *
from manim.mobject.value_tracker import *

from manim.scene.graph_scene import *
from manim.scene.moving_camera_scene import *
from manim.scene.reconfigurable_scene import *
from manim.scene.scene import *
from manim.scene.sample_space_scene import *
from manim.scene.graph_scene import *
from manim.scene.scene_from_video import *
from manim.scene.three_d_scene import *
from manim.scene.vector_space_scene import *
from manim.scene.zoomed_scene import *

from manim.utils.bezier import *
from manim.utils.color import *
from manim.utils.config_ops import *
from manim.utils.images import *
from manim.utils.iterables import *
from manim.utils.output_directory_getters import *
from manim.utils.paths import *
from manim.utils.rate_functions import *
from manim.utils.simple_functions import *
from manim.utils.sounds import *
from manim.utils.space_ops import *
from manim.utils.strings import *

# Non manim libraries that are also nice to have without thinking

import inspect
import itertools as it
import numpy as np
import operator as op
import os
import random
import re
import string
import sys
import math

from PIL import Image
from colour import Color
