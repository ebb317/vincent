from p5 import *
from random import choice


def draw_stroke(start_coord, end_coord, weight, palette, alpha=0.5):
    if start_coord != end_coord:
        stroke_color = choice(palette)
        stroke(stroke_color[0], stroke_color[1], stroke_color[2], 255 * alpha)
        stroke_weight(weight)
        line(start_coord, end_coord)


