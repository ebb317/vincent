from p5 import *
from random import choice, uniform

from vincent import draw_stroke


def draw_filled_arc(center_coord, painting_stroke, max_radius,
                    min_radius=1, starting_angle=0, ending_angle=TWO_PI, angle_increment=PI/8):

    # Configuration - TODO may want to extract to a config, or add dependency to length/weight
    x_wobble_range = range(-3, 4)
    y_wobble_range = range(-4, 5)

    radius = max_radius
    while radius >= min_radius:
        length = calculate_length_from_radius(radius, angle_increment)
        x, y = center_coord[0] - int(length / 2), center_coord[1] - radius

        angle = starting_angle
        while angle < ending_angle:
            x_wobble = choice(x_wobble_range)
            y_wobble = choice(y_wobble_range)

            length_variation = int(uniform(-1, 1) * length / 3)
            weight_variation = int(uniform(-1, 1) * (painting_stroke.weight - 1))

            end_x = x + x_wobble + int(cos(angle) * (length + length_variation))
            end_y = y + y_wobble + int(sin(angle) * (length + length_variation))

            draw_stroke((x, y), (end_x, end_y), painting_stroke.weight + weight_variation, painting_stroke.palette)

            # Next x, y are without the wobble/variation to stay on the same line:
            x = x + int(cos(angle) * (length + 2))
            y = y + int(sin(angle) * (length + 2))

            angle += angle_increment
        radius -= int(painting_stroke.weight / 3) + 1


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