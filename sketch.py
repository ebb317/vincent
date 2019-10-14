from p5 import *

from curves import draw_filled_arc
from straights import draw_directional_lines
from color_palette import cp_whites, cp_yellows, cp_light_blues
from painting_stroke import PaintingStroke

canvas_x = 1440
canvas_y = 900
bg_color = (32, 50, 126)


def setup():
    size(canvas_x, canvas_y)


def draw():
    background(*bg_color)

    # Starry Night ---
    # Sky

    # Middleground
    draw_directional_lines((0, 590), PaintingStroke(50, 3, cp_whites+cp_yellows), 720, 120)
    draw_directional_lines((0, 590), PaintingStroke(50, 3, cp_whites+cp_yellows), 720, 120)
    draw_directional_lines((620, 590), PaintingStroke(50, 3, cp_whites+cp_yellows), 900, 120, -PI/16)
    draw_directional_lines((620, 590), PaintingStroke(50, 3, cp_whites+cp_yellows), 900, 120, -PI/16)
    #draw_directional_lines((500, 500), PaintingStroke(30, 4, cp_whites), 600, 300, PI/7)

    # Stars
    draw_filled_arc((480, 510), PaintingStroke(30, 4, cp_whites), 60)
    draw_filled_arc((480, 510), PaintingStroke(30, 4, cp_whites*2+cp_yellows), 60)
    draw_filled_arc((480, 510), PaintingStroke(10, 6, cp_yellows), 15)

    # Moon
    draw_filled_arc((1300, 200), PaintingStroke(40, 4, cp_yellows), 120)
    draw_filled_arc((1300, 200), PaintingStroke(40, 8, cp_yellows), 90)
    no_loop()

    # Foreground


if __name__ == '__main__':
    run()

