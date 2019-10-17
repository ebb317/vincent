from p5 import *

from vincent import draw_filled_arc, draw_directional_lines
from vincent import PaintingStroke
from color_palette import *

canvas_x = 1440
canvas_y = 900
bg_color = (73, 115, 173)


def setup():
    size(canvas_x, canvas_y)


def draw():
    background(*bg_color)

    # Starry Night ---
    # Sky
    draw_directional_lines((0,   0),
                           PaintingStroke(50, 6, cp_light_blues + cp_dark_blues * 6 + cp_light_greens),
                           1440, 400, alpha=0.7, gap_y=0.6)
    draw_directional_lines((0, 400),
                           PaintingStroke(50, 6, cp_light_blues * 4 + cp_dark_blues), 1440, 350, alpha=0.8, gap_y=0.7)

    draw_directional_lines((-100, 300), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 850, 200,
                           angle=-PI/24, gap_y=0.8, alpha=0.8)
    draw_filled_arc((700, 400), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 200,
                    starting_angle=0, ending_angle=3*PI/4, alpha=0.8)
    draw_filled_arc((750, 450), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 100,
                    starting_angle=3*PI/4, ending_angle=PI, alpha=0.8)
    draw_filled_arc((750, 550), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 150,
                    starting_angle=5*PI/4, ending_angle=2*PI, alpha=0.8)
    draw_filled_arc((700, 580), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 100,
                    starting_angle=PI/2, ending_angle=3*PI/2, alpha=0.8)
    draw_directional_lines((700, 600), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 400, 100,
                           angle=-PI/6, gap_y=0.8, alpha=0.8)
    draw_filled_arc((1050, 500), PaintingStroke(30, 6, cp_whites + cp_light_blues * 2), 100,
                    starting_angle=-PI/4, ending_angle=PI, alpha=0.8)

    draw_filled_arc((1300, 200), PaintingStroke(40, 8, cp_light_blues + cp_dark_blues * 3), 300, alpha=0.3)
    draw_filled_arc((700, -200), PaintingStroke(40, 8, cp_light_blues + cp_dark_blues * 3), 300, alpha=0.3)

    # Stars
    draw_filled_arc((500, 600), PaintingStroke(30, 5, cp_whites), 100, gap_x=2, gap_y=0.5, alpha=0.8)
    draw_filled_arc((500, 600), PaintingStroke(30, 4, cp_whites+cp_yellows), 60, alpha=0.9)
    draw_filled_arc((500, 600), PaintingStroke(10, 6, cp_yellows), 15, alpha=0.9)

    draw_filled_arc((560, 415), PaintingStroke(40, 4, cp_whites), 50)
    draw_filled_arc((560, 415), PaintingStroke(40, 4, cp_yellows+cp_light_greens), 30)
    draw_filled_arc((560, 415), PaintingStroke(40, 8, cp_yellows), 20, alpha=1)

    draw_filled_arc((150, 50), PaintingStroke(40, 4, cp_whites), 60)
    draw_filled_arc((150, 50), PaintingStroke(40, 4, cp_yellows), 60)
    draw_filled_arc((150, 50), PaintingStroke(40, 8, cp_yellows), 20, alpha=0.8)

    draw_filled_arc((500, 60), PaintingStroke(40, 4, cp_light_blues), 50)
    draw_filled_arc((500, 60), PaintingStroke(40, 4, cp_light_greens), 50)
    draw_filled_arc((500, 60), PaintingStroke(40, 8, cp_yellows), 20, alpha=0.9)

    draw_filled_arc((600, 80), PaintingStroke(40, 4, cp_yellows), 20)
    draw_filled_arc((600, 80), PaintingStroke(40, 8, cp_yellows), 10, alpha=0.9)

    draw_filled_arc((900, 100), PaintingStroke(40, 4, cp_light_blues), 70)
    draw_filled_arc((900, 100), PaintingStroke(40, 4, cp_light_greens), 70)
    draw_filled_arc((900, 100), PaintingStroke(40, 8, cp_yellows), 30, alpha=0.9)

    draw_filled_arc((1000, 250), PaintingStroke(40, 4, cp_light_greens), 70)
    draw_filled_arc((1000, 250), PaintingStroke(40, 4, cp_light_blues), 70, alpha=0.7)
    draw_filled_arc((1000, 250), PaintingStroke(40, 8, cp_yellows), 30, alpha=0.9)

    draw_filled_arc((350, 50), PaintingStroke(40, 4, cp_light_blues), 25)
    draw_filled_arc((350, 50), PaintingStroke(40, 8, cp_yellows), 10, alpha=1)

    draw_filled_arc((50, 500), PaintingStroke(40, 4, cp_light_greens+cp_whites), 25, gap_y=0.5)
    draw_filled_arc((50, 500), PaintingStroke(40, 8, cp_yellows), 10, alpha=1, gap_y=0.5)

    draw_filled_arc((180, 550), PaintingStroke(40, 4, cp_yellows), 50)
    draw_filled_arc((180, 550), PaintingStroke(40, 8, cp_light_greens), 10, alpha=1)

    draw_filled_arc((360, 200), PaintingStroke(40, 4, cp_yellows), 50)
    draw_filled_arc((360, 200), PaintingStroke(40, 8, cp_yellows), 25, alpha=0.9)

    # Moon
    draw_filled_arc((1300, 200), PaintingStroke(40, 4, cp_yellows), 120)
    draw_filled_arc((1300, 200), PaintingStroke(40, 8, cp_yellows), 90, alpha=0.9)

    # Hills
    draw_directional_lines((0, 690), PaintingStroke(80, 5, cp_light_greens), 720, 120, gap_y=0.8, alpha=0.8)
    draw_directional_lines((620, 690), PaintingStroke(50, 5, cp_light_greens), 900, 120,
                           angle=-PI/16, gap_y=0.8, alpha=0.8)

    # Foreground
    draw_directional_lines((0, 800), PaintingStroke(60, 8, cp_dark_blues + cp_blacks), 1440, 250, gap_y=0.3)
    draw_directional_lines((620, 800), PaintingStroke(50, 8, cp_dark_blues + cp_blacks), 900, 180,
                           angle=-PI/16, gap_y=0.3)
    draw_directional_lines((900, 850), PaintingStroke(50, 8, cp_dark_blues + cp_blacks), 900, 180,
                           angle=-PI/16, gap_y=0.3)

    draw_directional_lines((200, 900), PaintingStroke(60, 8, cp_blacks), 500, 120, angle=-PI/2, gap_y=0.6, alpha=0.8)
    draw_directional_lines((280, 400), PaintingStroke(60, 8, cp_blacks), 350,  35, angle=-PI / 2, gap_y=0.6, alpha=0.8)

    draw_directional_lines((320, 900), PaintingStroke(60, 8, cp_blacks), 200, 60, angle=-PI/2, gap_y=0.6, alpha=0.8)
    draw_directional_lines((380, 900), PaintingStroke(60, 8, cp_blacks), 100, 60, angle=-PI / 2, gap_y=0.6, alpha=0.8)

    no_loop()


if __name__ == '__main__':
    run()

