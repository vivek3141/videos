from PIL import Image
import numpy as np
import matplotlib.cm as cm
import math

ASPECT_RATIO = 1.0 / 1.0
FRAME_HEIGHT = 8.0
FRAME_WIDTH = FRAME_HEIGHT * ASPECT_RATIO

XRES = 1000
YRES = 1000

x_min = -FRAME_WIDTH/2
x_max = FRAME_WIDTH/2
y_min = -FRAME_HEIGHT/2
y_max = FRAME_HEIGHT/2

x_values = np.linspace(x_min, x_max, XRES+1)
y_values = np.linspace(y_min, y_max, YRES+1)

#print(x_values)
#print(y_values)

pixels = []

for i in range(len(y_values) - 1)[::-1]:
    pixels.append([])
    for j in range(len(x_values) - 1):
        x1, x2 = x_values[j:j + 2]
        y1, y2 = y_values[i:i + 2]
        x, y = (x1 + x2)/2, (y1 + y2)/2

        if x > 0:
            y = -y

        # if -2 < x < 2 and -2 < y < 2:
        #     pixel = [0, 0, 0]
        # else:
        #     pixel = [255, 255, 255]

        z = (x+y*1j)

        if z.real != 0:
            theta = 2*(math.atan(z.imag/z.real) + np.pi/2)
        else:
            theta = np.pi
        
        pixel = [x * 255 for x in cm.viridis(theta/(2*np.pi))]
        
        pixels[-1].append(pixel)



array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save("img/z_squared.png")
new_image.show()
