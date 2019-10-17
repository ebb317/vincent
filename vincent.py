from p5 import *
from random import choice, uniform


class PaintingStroke:
    def __init__(self, length, weight, palette):
        self.length = length
        self.weight = weight
        self.palette = palette


def draw_stroke(start_coord, end_coord, weight, palette, alpha=0.5):
    if start_coord != end_coord:
        stroke_color = choice(palette)
        stroke(stroke_color[0], stroke_color[1], stroke_color[2], 255 * alpha)
        stroke_weight(weight)
        line(start_coord, end_coord)


def draw_directional_lines(starting_coord, painting_stroke, width, height,
                           angle=0, gap_x=0, gap_y=1, alpha=0.5):

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

            draw_stroke((x, y), (end_x, end_y), painting_stroke.weight + weight_variation,
                        painting_stroke.palette, alpha)
            x = end_x + gap_x

        x = 0
        y += max(int(gap_y * painting_stroke.weight), 1)

    reset_transforms()


def draw_filled_arc(center_coord, painting_stroke, max_radius,
                    gap_x=2, gap_y=1, alpha=0.5,
                    min_radius=1, starting_angle=0, ending_angle=TWO_PI, angle_increment=PI/8):

    # Configuration - TODO may want to extract to a config, or add dependency to length/weight
    x_wobble_range = range(-3, 4)
    y_wobble_range = range(-4, 5)

    translate(center_coord[0], center_coord[1])
    rotate(starting_angle)

    radius = max_radius
    while radius >= min_radius:
        length = calculate_length_from_radius(radius, angle_increment) - gap_x
        x, y = - int(length / 2), - radius

        angle = 0
        while angle < (ending_angle - starting_angle):
            x_wobble = choice(x_wobble_range)
            y_wobble = choice(y_wobble_range)

            length_variation = int(uniform(-1, 1) * length / 3)
            weight_variation = int(uniform(-1, 1) * (painting_stroke.weight - 1))

            end_x = x + x_wobble + int(cos(angle) * (length + length_variation))
            end_y = y + y_wobble + int(sin(angle) * (length + length_variation))

            draw_stroke((x, y), (end_x, end_y), painting_stroke.weight + weight_variation,
                        painting_stroke.palette, alpha)

            # Next x, y are without the wobble/variation to stay on the same line:
            x = x + int(cos(angle) * (length + gap_x))
            y = y + int(sin(angle) * (length + gap_x))

            angle += angle_increment
        radius -= max(int(gap_y * painting_stroke.weight), 1)

    reset_transforms()


def calculate_length_from_radius(radius, angle_increment):
    """ Calculates the (rough) length of the stroke required to draw a circle
    given a desired radius and the angle increment for each segment
    The initial stroke is half-way across the x-axis and expected to start at angle 0, thus the 1/2 initial value
    We only consider the x-axis progress from 0 to PI/2
     - 0 being the angle of the first stroke
     - PI/2 being when the x-axis progress stops.

    :param radius: length of the desired radius (int)
    :param angle_increment: angle currently considered in radians (float)
    :return: length of the stroke (int)
    """
    cumulative_sum = 1/2
    cumulative_angle = angle_increment
    while cumulative_angle <= PI / 2:
        cumulative_sum += cos(cumulative_angle)
        cumulative_angle += angle_increment

    return int(radius / cumulative_sum)

