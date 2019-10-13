from p5 import *
import random

canvas_x = 1280
canvas_y = 600
my_eric_angle = 0

def setup():
    # Sets the screen to be 720 pixels wide and 400 pixels high
    size(canvas_x, canvas_y)


def draw():
    background(0)
    starting_x, starting_y = int(canvas_x/2), int(canvas_y/2)
    length, weight = 40, 4

    for angle in [-PI/2, 0, PI/2, PI]:
        reset_transforms()
        translate(starting_x, starting_y)
        rotate(angle)

        x, y = 0, 0
        max_x, max_y = x + int(0.2 * canvas_x), y + int(0.4 * canvas_y)

        stroke_weight(5)
        stroke(255)
        no_fill()
        rect((x, y), max_x-x, max_y-y)

        while y < max_y:
            while int(x+(length/2)) < max_x:
                x_wobble = random.choice(range(-3, 4))
                y_wobble = random.choice(range(-4, 5))
                length_variation = int(random.uniform(-1, 1) * length / 3)
                weight_variation = int(random.uniform(-1, 1) * (weight-1))
                assert length > length_variation
                assert weight > weight_variation

                end_x = min(x + x_wobble + length + length_variation, canvas_x)
                end_y = min(y + y_wobble, canvas_y)
                draw_stroke((x, y), (end_x, end_y), weight + weight_variation)
                x = end_x

            x = 0
            y += int(1.5 * weight)
    no_loop()


def draw_stroke(start, end, weight):
    current_color = 145 + random.uniform(-1, 1)*100
    stroke(0, current_color, 0, 255*0.5)
    stroke_weight(weight)
    line(start, end)


if __name__ == '__main__':
    run()
