input_dot.move_to(c1.c2p(-1.2, 1.3))
input_dot.move_to(c1.c2p(-1, 1.3))
input_dot.move_to(c1.c2p(1, 1.3))
c1.coordinate_labels.set_opacity(0.65)
c2.coordinate_labels.set_opacity(0.65)
c2.coordinate_labels.set_opacity(0.75)
c2.coordinate_labels.set_opacity(0.75)
c1.coordinate_labels.set_opacity(0.75)
x, y
x
y
x, y = 1, 1.3
z = c1.c2p(x, y)
Vector([1, 1]).move_to(z, DOWN)
v1 =Vector([1, 1]).move_to(z, DOWN)
add(v1)
v1.move_to(z)
v1.move_to(z, LEFT)
v1.move_to(z, UP)
v1.move_to(z, RIGHT)
v1.move_to(z)
v1.move_to(z, aligned_edge=LEFT)
v1.move_to(z, aligned_edge=[1, 1, 0])
v1.move_to(z, aligned_edge=[-1, -1, 0])
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = np.c2p(x, y)
    return Vector(z, **kwargs)
v1 = get_vec(c1, [1, 1])
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = plane.c2p(x, y)
    return Vector(z, **kwargs)
v1 = get_vec(c1, [1, 1])
add(v1)
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = plane.c2p(x, y)
    return Arrow(z, plane.c2p(0, 0) **kwargs)
v1 = get_vec(c1, [1, 1])
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = plane.c2p(x, y)
    return Arrow(z, plane.c2p(0, 0), **kwargs)
remove(self.mobjects[-1])
remove(self.mobjects[-1])
v1 = get_vec(c1, [1, 1])
add(v1)
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = plane.c2p(x, y)
    return Arrow(plane.c2p(0, 0), z, **kwargs)
remove(self.mobjects[-1])
v1 = get_vec(c1, [1, 1])
add(v1)
def get_vec(plane, coors, **kwargs):
    x, y = coors[0], coors[1]
    z = plane.c2p(x, y)
    return Arrow(plane.c2p(0, 0), z, buff=0, **kwargs)
remove(v1)
v1 = get_vec(c1, [1, 1])
add(v1)
remove(v1)
PURPLE
x, y
z
for t in np.linspace(0, 2*PI, 10):
    pass
vecs = VGroup()
for t in np.linspace(0, 2*PI, 10):
    z_0 = np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
for t in np.linspace(0, 2*PI, 10):
    z_0 = np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    vecs.add(v_0)
add(vecs)
vecs.set_color(PURPLE)
vecs.move_to(z)
remove(vecs)
vecs = VGroup()
for t in np.linspace(0, 2*PI, 10):
    z_0 = np.exp(t*0.75j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
add(vecs)
remove(vecs)
for t in np.linspace(0, 2*PI, 20):
    z_0 = 0.75*np.exp(t*j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
for t in np.linspace(0, 2*PI, 20):
    z_0 = 0.75*np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
vecs.set_color(PURPLE)
add(vecs)
vecs = VGroup()
remove(self.mobjects[-1])
for t in np.linspace(0, 2*PI, 20):
    z_0 = 0.75*np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
add(vecs)
vecs.set_color(PURPLE)
vecs.set_color(PURPLE)
remove(vecs)
vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
add(vecs)
vecs.set_color(PURPLE)
self.bring_to_front(input_dot_label)
input_dot_text
self.bring_to_front(input_dot_text)
vecs.set_opacity(0.5)
vecs.set_opacity(0.75)
z_vals = []
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)
    z_vals.append(z_0)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    #vecs.add(v_0)
z_vals
dz = 0.00001 + 0.0001*1j
func
z
x, y
z
x, y
z_0 = x+y*1j
z_0
(f(z_0+dz)-f(z_0))/dz
(self.func(z_0+dz)-self.func(z_0))/dz
z_vals
img_vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)*f_deriv
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    #vecs.add(v_0)
f_deriv = (self.func(z_0+dz)-self.func(z_0))/dz
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)*f_deriv
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
self.func(z)
z_0
z
f_zself.func(x+y*1j)
f_z=self.func(x+y*1j)
f_z
f_z = [f_z.real, f_z.imag]
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)*f_deriv
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
add(img_vecs)
remove(img_vecs)
img_vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.1*np.exp(t*1j)*f_deriv
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
add(img_vecs)
img_vecs.set_color(GREEN)
img_vecs.set_opacity(0.7)
img_vecs.set_opacity(0.75)
self.bring_to_front(output_dot_text)
input_label
input_text
input_text.add_background_rectangle()
input_text.background_rectangle
self.bring_to_front(input_text.background_rectangle)
self.remove(input_text.background_rectangle)
input_dot_text.add_background_rectangle()
output_dot_text.add_background_rectangle()
remove(img_vecs)
play(TransformFromCopy(vecs, img_vecs), run_time=10)
touch()
remove(img_vecs)
play(TransformFromCopy(vecs, img_vecs), run_time=10)
remove(img_vecs)
play(TransformFromCopy(vecs[0], img_vecs[0]), run_time=10)
remove(img_vecs[0])
f_deriv
f_deriv.angle
np.atan2(f_deriv.imag, f_deriv.real)
np.arctan2(f_deriv.imag, f_deriv.real)
np.arctan2(f_deriv.imag, f_deriv.real) * 360/(2*PI)
dz
func = self.func
def f_deriv(z):
    return (func(z+dz)-func(z))/dz
f_deriv(x+y*1j)
def f_deriv(z, func=func):
    return (func(z+dz)-func(z))/dz
f_deriv(x+y*1j)
def f_deriv(z, dz=dz, func=func):
    return (func(z+dz)-func(z))/dz
f_deriv(x+y*1j)
f_deriv(1+1*1j)
f_deriv(2+2.3*1j)
f_deriv(1.5+2.3*1j)
test =f_deriv(1.5+2.3*1j)
test.real
test.imag
np.arctan2(test.imag, test.real)
input_dot.move_to(c1.c2p(1.5, 2.3))
input_dot.move_to(c1.c2p(1.5, 2))
test =f_deriv(1.5+2*1j)
np.arctan2(test.imag, test.real)
remove(vecs)
vecs = VGroup()
for
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)*f_deriv
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
vecs = VGroup()
x, y = 1.5, 2
z = c1.c2p(1.5, 2)
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
add(vecs)
remove(vecs)
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.75*np.exp(t*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c1, [x_0, y_0], color=PURPLE)
    v_0.move_to(z, aligned_edge=[-x_0, -y_0, 0])
    vecs.add(v_0)
add(vecs)
vecs.set_opacity(0.75)
vecs.set_color(PURPLE)
self.bring_to_front(input_dot_text)
img_vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.1*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
f_z=self.func(x+y*1j)
img_vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.1*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
f_z
f_z = [f_z.real, f_z.imag]
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.1*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
addd(img_vecs)
add(img_vecs)
remove(img_vecs)
img_vecs = VGroup()
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.25*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
add(img_vecs)
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.3*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
img_vecs = VGroup()
remove(self.mobjects[-1])
for t in np.linspace(0, 2*PI, 15):
    z_0 = 0.3*np.exp(t*1j)*f_deriv(x+y*1j)
    x_0, y_0 = z_0.real, z_0.imag
    v_0 = get_vec(c2, [x_0, y_0], color=PURPLE)
    v_0.move_to(c2.c2p(*f_z), aligned_edge=[-x_0, -y_0, 0])
    img_vecs.add(v_0)
add(img_vecs)
img_vecs.set_opacity(0.75)
img_vecs.set_color(GREEN)
input_ve
self.bring_to_front(output_dot_text)
remove(img_vecs)
play(TransformFromCopy(vecs, img_vecs), run_time=10)
self.bring_to_front(output_dot_text)
%hist