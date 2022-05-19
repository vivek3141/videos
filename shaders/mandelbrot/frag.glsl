#version 330

uniform vec3 light_source_position;
uniform float gloss;
uniform float shadow;
uniform float focal_distance;

//uniform vec2 parameter;
uniform float opacity;

#define product(a, b) vec2(a.x*b.x-a.y*b.y, a.x*b.y+a.y*b.x)
#define conjugate(a) vec2(a.x,-a.y)
#define divide(a, b) vec2(((a.x*b.x+a.y*b.y)/(b.x*b.x+b.y*b.y)),((a.y*b.x-a.x*b.y)/(b.x*b.x+b.y*b.y)))

float interpolate(float start, float end, float alpha) {
    return (1.0-alpha) * start + alpha * end;
}

float max_arg = 2.0;
const int num_steps = 100;

const float X_MAX = 1.75;
const float ASPECT_RATIO = 800.0/450.0;
const float Y_MAX = X_MAX / ASPECT_RATIO;

in vec3 xyz_coords;
out vec4 frag_color;

#INSERT finalize_color.glsl

void main()
{
    // //printf("%f %f %f\n", xyz_coords.x, xyz_coords.y, xyz_coords.z);
    // vec3 color = vec3(xyz_coords.x/16.0 + 0.5, xyz_coords.y/8.0 + 0.5, 0.0);
    // frag_color = finalize_color(
    //     vec4(color, opacity),
    //     xyz_coords,
    //     vec3(0.0, 0.0, 1.0),
    //     light_source_position,
    //     gloss,
    //     shadow
    // );
    // return;
    bool done = false;
    int steps = num_steps; 
    
    vec2 curr = vec2(0, 0);
    vec2 fragCoord = vec2(xyz_coords.x, xyz_coords.y);
    vec3 color;
    //fragCoord = vec2(interpolate(-X_MAX, X_MAX, uv.x), interpolate(-Y_MAX, Y_MAX, uv.y));
    while (steps >= 0) {
        if (sqrt(curr.x*curr.x + curr.y*curr.y) > max_arg) {
            done = true;
            break;
        }
        curr = product(curr, curr) + fragCoord;
        steps--;
    }
    
    if (done) {
        float ratio = interpolate(0.0, 1.0, float(steps)/float(num_steps));
        color = vec3(ratio, ratio, 1.0);
    } else {
        color = vec3(0, 0, 0);
    }
    frag_color = finalize_color(
        vec4(color, opacity),
        xyz_coords,
        vec3(0.0, 0.0, 1.0),
        light_source_position,
        gloss,
        shadow
    );
    
}


