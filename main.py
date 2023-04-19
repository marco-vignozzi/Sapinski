from PIL import Image as img
import random as r
import colors as c


# this function returns a tuple of integer which represent a point located
# in the middle of the distance between a and b
def get_mid_point(a, b):
    new_point = (int((a[0]+b[0])/2), int((a[1]+b[1])/2))
    return new_point


# initialize the figure
width = 1000
height = 900
start_fig = [(500, 50), (50, 850), (950, 850)]
background_color = c.colors_dict['black']

# choose the starting point, the color and the number of points to be drawn
# if the color isn't in the "colors.py" module it'll be used randomized colors on every iteration
start_pt = (560, 380)
start_pt_color = c.colors_dict['white']
color = 'lime'
total_pt = 1000000

# instantiation of the new image and setting it up
image = img.new(mode="RGB", size=(width, height), color=background_color)
for i in start_fig:
    image.putpixel(i, start_pt_color)

image.putpixel(start_pt, start_pt_color)
last_pt = start_pt
if color in c.colors_dict:
    color_used = c.colors_dict[color]
else:
    color = 'random'

while total_pt != 0:
    # randomly choose a point and a color
    pick = start_fig[(r.randrange(0, 1001) % len(start_fig))]
    if color == 'random':
        color_used = c.colors_list[(r.randrange(0, 1001)) % len(c.colors_list)]

    # get the medium point of the distance with the random chosen one
    last_pt = get_mid_point(pick, last_pt)

    image.putpixel(last_pt, color_used)

    total_pt -= 1

image.show()
image.save('./example.png')
