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

    stroke_weight(5)
    stroke(150)
    rect((starting_x, starting_y),  2, 2)

    length, weight = 40, 4
    while length > 1:
        radius = length * (1 + cos(PI/8) + cos(PI/4) + cos(3*PI/8))

        x, y = starting_x - int(length/2), starting_y - radius
        angle = 0

        while angle < TWO_PI:
            x_wobble = random.choice(range(-3, 4))
            y_wobble = random.choice(range(-4, 5))
            length_variation = int(random.uniform(-1, 1) * length / 3)
            weight_variation = int(random.uniform(-1, 1) * (weight-1))
            assert length > length_variation
            assert weight > weight_variation

            end_x = x + x_wobble + int(cos(angle)*(length + length_variation))
            end_y = y + y_wobble + int(sin(angle)*(length + length_variation))
            draw_stroke((x, y), (end_x, end_y), weight + weight_variation)

            # Next x, y are without the wobble/variation to stay on the same line:
            x = x + int(cos(angle) * length)
            y = y + int(sin(angle) * length)
            angle += PI/8
        length -= int(weight/4)
    #no_loop()


def draw_stroke(start, end, weight):
    current_color = 145 + random.uniform(-1, 1)*100
    stroke(0, current_color, 0, 255*0.5)
    stroke_weight(weight)
    line(start, end)


if __name__ == '__main__':
    run()
