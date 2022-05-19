#version 330

uniform vec3 light_source_position;
uniform float gloss;
uniform float shadow;
uniform float focal_distance;
uniform float opacity;

#define product(a, b) vec2(a.x*b.x-a.y*b.y, a.x*b.y+a.y*b.x)
#define conjugate(a) vec2(a.x,-a.y)
#define divide(a, b) vec2(((a.x*b.x+a.y*b.y)/(b.x*b.x+b.y*b.y)),((a.y*b.x-a.x*b.y)/(b.x*b.x+b.y*b.y)))
#define arg(a) sqrt(a.x*a.x+a.y*a.y)

uniform float max_arg;
uniform int num_steps;

in vec3 xyz_coords;
out vec4 frag_color;

#INSERT finalize_color.glsl

void main() {
    bool done = false;
    int steps = num_steps;

    vec2 curr = vec2(0, 0);
    vec2 c = vec2(xyz_coords.x, xyz_coords.y);

    while(steps >= 0 && !done) {        
        curr = product(curr, curr) + c;
        steps--;

        if(arg(curr) > max_arg) {
            done = true;
        }
    }

    vec3 color;
    if(done) {
        float ratio = float(steps) / float(num_steps);
        color = vec3(ratio, ratio, 1.0);
    } else {
        color = vec3(0, 0, 0);
    }
    frag_color = finalize_color(vec4(color, opacity), xyz_coords, vec3(0.0, 0.0, 1.0), light_source_position, gloss, shadow);
}
