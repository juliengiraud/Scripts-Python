from PIL import Image
from numpy import asarray
import sys
f = sys.argv[1]
image = Image.open(f)
data = asarray(image).copy()

height = data.shape[0]
width = data.shape[1]

for y in range(height):
    for x in range(width):
        R = data[y][x][0]
        G = data[y][x][1]
        B = data[y][x][2]
        if R > 200 and G > 200 and B > 200:
            data[y][x][0] = 255
            data[y][x][1] = 0
            data[y][x][2] = 0
        elif R > 100 and G < 50 and B < 50:
            data[y][x][0] = 255
            data[y][x][1] = 255
            data[y][x][2] = 255
        elif R < 50 and G > 100 and B < 100:
            data[y][x][0] = 0
            data[y][x][1] = 0
            data[y][x][2] = 255

image2 = Image.fromarray(data)
image2.save(f)
