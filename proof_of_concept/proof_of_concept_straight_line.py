from p5 import *
import random

def setup():
    # Sets the screen to be 720 pixels wide and 400 pixels high
    size(720, 400)


def draw():
    background(0)
    for x in range(10, 400, int(20+random.uniform(0, 1)*40)):
        for y in range(10, 200, int(2+random.uniform(0, 1)*2)):
            length = int(40 + random.uniform(-1, 1)*30)
            x_wobble = int(random.uniform(-1, 1)*3)
            y_wobble = int(random.uniform(-1, 1) * 5)
            draw_stroke((x+x_wobble, y), (x+x_wobble+length, y+y_wobble))
    no_loop()


def draw_stroke(start, end):
    current_color = 145 + random.uniform(-1, 1)*100
    stroke(0, current_color, 0, 255*0.5)
    stroke_weight(3+int(random.uniform(-1, 1)*3))
    line(start, end)


if __name__ == '__main__':
    run()