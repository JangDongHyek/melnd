import pyMeow as pm
from random import randint


def main():
    pm.overlay_init()

    while pm.overlay_loop():


        pm.begin_drawing()
        color = pm.get_color("#00ff08")
        pm.draw_rectangle_lines(100,100,200,200,color,3.0)

        pm.end_drawing()


if __name__ == "__main__":
    main()