from PIL import Image
import numpy as np

ASPECT_RATIO = 16.0 / 9.0
FRAME_HEIGHT = 1.75
FRAME_WIDTH = FRAME_HEIGHT * ASPECT_RATIO

XRES = 160
YRES = 90

RED = (252, 98, 85)
YELLOW = (255, 255, 0)
GREEN = (131, 193, 103)
BLUE = (88, 196, 221)
PURPLE = (154, 114, 172)
colors = [RED, YELLOW, GREEN, BLUE, PURPLE]

x_min = -FRAME_WIDTH/2
x_max = FRAME_WIDTH/2
y_min = -FRAME_HEIGHT/2
y_max = FRAME_HEIGHT/2

x_values = np.linspace(x_min, x_max, XRES+1)
y_values = np.linspace(y_min, y_max, YRES+1)

pixels = []

for i in range(len(y_values) - 1)[::-1]:
    pixels.append([])
    for j in range(len(x_values) - 1):
        x1, x2 = x_values[j:j + 2]
        y1, y2 = y_values[i:i + 2]

        x, y = (x1 + x2)/2, (y1 + y2)/2
        c = x + y*1j
        
        z, done = 0, False
        for _ in range(1000):
            if np.sqrt(z.imag**2 + z.real**2) > 2:
                done = True
                break
            z = z**2 + c
        pixel =i (255, 255, 255) if not done else (0, 0, 0)
        pixels[-1].append(pixel)


array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save("img/mandelbrot.png")
new_image.show()
