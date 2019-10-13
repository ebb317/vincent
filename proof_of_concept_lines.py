from p5 import *
import random

canvas_x = 1280
canvas_y = 600


def setup():
    # Sets the screen to be 720 pixels wide and 400 pixels high
    size(canvas_x, canvas_y)


def draw():
    background(0)
    x, y = 10, 10
    length, weight = 40, 4

    while y < int(0.8 * canvas_y):
        while x < int(0.9 * canvas_x):
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
        x = 10
        y += int(1.5 * weight)
    no_loop()


def draw_stroke(start, end, weight):
    current_color = 145 + random.uniform(-1, 1)*100
    stroke(0, current_color, 0, 255*0.5)
    stroke_weight(weight)
    line(start, end)


if __name__ == '__main__':
    run()