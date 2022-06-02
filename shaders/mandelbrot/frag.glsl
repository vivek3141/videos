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

#define RES=2;

uniform float max_arg;
uniform int num_steps;

uniform int color_style;

in vec3 xyz_coords;
out vec4 frag_color;

#INSERT finalize_color.glsl

float interpolate(float start, float end, float alpha) {
    return (1.0 - alpha) * start + alpha * end;
}

float mandelbrot(in vec2 c) {
    const float B = 256.0;

    float n = 0.0;
    vec2 z = vec2(0.0);
    for(int i = 0; i < num_steps; i++) {
        z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c; // z = z² + c
        if(dot(z, z) > (B * B))
            break;
        n += 1.0;
    }

    float sn = n - log2(log2(dot(z, z))) + 4.0;  // optimized smooth iteration count

    return sn;
}

vec3 colorize(int steps) {
    vec3 mapping[15] = vec3[](
        vec3(0.0980,0.0275,0.1020),
        vec3(0.0353,0.0039,0.1843),
        vec3(0.0157,0.0157,0.2863),
        vec3(0.0000,0.0275,0.3922),
        vec3(0.0471,0.1725,0.5412),
        vec3(0.0941,0.3216,0.6941),
        vec3(0.2235,0.4902,0.8196),
        vec3(0.5255,0.7098,0.8980),
        vec3(0.8275,0.9255,0.9725),
        vec3(0.9451,0.9137,0.7490),
        vec3(0.9725,0.7882,0.3725),
        vec3(1.0000,0.6667,0.0000),
        vec3(0.8000,0.5020,0.0000),
        vec3(0.6000,0.3412,0.0000),
        vec3(0.4157,0.2039,0.0118)
    );
    return mapping[steps%16];
}

void main() {
    vec2 c = vec2(xyz_coords.x, xyz_coords.y);
    vec3 color;

    if(color_style == 0) {
        bool done = false;
        int steps = num_steps;
        vec2 curr = vec2(0, 0);

        while(steps >= 0 && !done) {
            curr = product(curr, curr) + c;
            steps--;

            if(arg(curr) > max_arg) {
                done = true;
            }
        }
        if(done) {
            float ratio = float(steps) / float(num_steps);
            color = vec3(0.5, 0.7, interpolate(0.3, 0.8, ratio));
        } else {
            color = vec3(0, 0, 0);
        }

    } else {
        float l = mandelbrot(c);
        color = 0.5 + 0.5 * cos(3.0 + l * 0.15 + vec3(0.0, 0.6, 1.0));
    }

    frag_color = finalize_color(vec4(color, opacity), xyz_coords, vec3(0.0, 0.0, 1.0), light_source_position, gloss, shadow);
}
