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
height = 1000
# start_fig = [(500, 333), (200, 800), (800, 800)]
start_fig = [(600, 200), (400, 200), (600, 800), (400, 800), (200, 500), (800, 500)]
background_color = c.colors_dict['black']

# choose the starting point and the number of points to be drawn
start_pt = (300, 500)
start_pt_color = c.colors_dict['white']
total_pt = 50000

# instantiation of the new image and setting it up
image = img.new(mode="RGB", size=(width, height), color=background_color)
for i in start_fig:
    image.putpixel(i, start_pt_color)

image.putpixel(start_pt, start_pt_color)
last_pt = start_pt

while total_pt != 0:
    # randomly choose a point and a color
    pick = start_fig[(r.randrange(0, 1001) % len(start_fig))]
    color = c.colors_list[(r.randrange(0, 1001)) % len(c.colors_list)]

    # get the medium point with the random chosen one
    last_pt = get_mid_point(pick, last_pt)

    image.putpixel(last_pt, color)

    total_pt -= 1

image.show()
