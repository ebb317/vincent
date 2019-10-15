from p5 import *
from random import choice, uniform

from vincent import draw_stroke


def draw_directional_lines(starting_coord, painting_stroke, width, height, 
                           angle=0, gap=1, alpha=0.5):

    # Configuration - TODO may want to extract to a config, or add dependency to length/weight
    x_wobble_range = range(-3, 4)
    y_wobble_range = range(-4, 5)

    translate(starting_coord[0], starting_coord[1])
    rotate(angle)

    x, y = 0, 0

    while y < height:
        while (x + (painting_stroke.length/2)) < width:
            x_wobble = choice(x_wobble_range)
            y_wobble = choice(y_wobble_range)

            length_variation = int(uniform(-1, 1) * painting_stroke.length / 3)
            weight_variation = int(uniform(-1, 1) * (painting_stroke.weight - 1))

            end_x = x + x_wobble + painting_stroke.length + length_variation
            end_y = y + y_wobble

            draw_stroke((x, y), (end_x, end_y), painting_stroke.weight + weight_variation, painting_stroke.palette, alpha)
            x = end_x

        x = 0
        y += int(gap * painting_stroke.weight)

    reset_transforms()
