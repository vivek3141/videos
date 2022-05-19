#version 330

uniform vec3 light_source_position;
uniform float gloss;
uniform float shadow;
uniform float focal_distance;

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

in vec3 xyz;
out vec4 fragColor;

void main()
{
    bool done = false;
    int steps = num_steps;

    vec2 fragCoord = vec2(xyz.x, xyz.y); 
    
    vec2 curr = vec2(0, 0);
    vec2 uv = fragCoord;
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
        fragColor = vec4(ratio, ratio, 1.0, 1.0);
    } else {
        fragColor = vec4(0, 0, 0, 1.0);
    }
}





// uniform vec2 parameter;
// uniform float opacity;
// uniform float n_steps;
// uniform float mandelbrot;

// uniform vec3 color0;
// uniform vec3 color1;
// uniform vec3 color2;
// uniform vec3 color3;
// uniform vec3 color4;
// uniform vec3 color5;
// uniform vec3 color6;
// uniform vec3 color7;
// uniform vec3 color8;

// uniform vec2 frame_shape;

// in vec3 xyz_coords;

// out vec4 frag_color;

// #INSERT finalize_color.glsl
// #INSERT complex_functions.glsl

// const int MAX_DEGREE = 5;

// void main() {
//     frag_color = vec4(1.0, 1.0, 0.0, 1.0);

//     return;

//     vec3 color_map[9] = vec3[9](
//         color0, color1, color2, color3,
//         color4, color5, color6, color7, color8
//     );
//     vec3 color;

//     vec2 z;
//     vec2 c;

//     if(bool(mandelbrot)){
//         c = xyz_coords.xy;
//         z = vec2(0.0, 0.0);
//     }else{
//         c = parameter;
//         z = xyz_coords.xy;
//     }

//     float outer_bound = 2.0;
//     bool stable = true;
//     for(int n = 0; n < int(n_steps); n++){
//         z = complex_mult(z, z) + c;
//         if(length(z) > outer_bound){
//             float float_n = float(n);
//             float_n += log(outer_bound) / log(length(z));
//             float_n += 0.5 * length(c);
//             color = float_to_color(sqrt(float_n), 1.5, 8.0, color_map);
//             stable = false;
//             break;
//         }
//     }
//     if(stable){
//         color = vec3(0.0, 0.0, 0.0);
//     }

//     frag_color = finalize_color(
//         vec4(color, opacity),
//         xyz_coords,
//         vec3(0.0, 0.0, 1.0),
//         light_source_position,
//         gloss,
//         shadow
//     );
//  }
