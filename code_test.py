import cv2
import numpy as np
import time
import pyMeow as pm
pm.overlay_init()
color = pm.get_color("#0400ff")
color2 = pm.get_color("#ff0000")
while pm.overlay_loop():
    pm.begin_drawing()
    pm.draw_rectangle_lines(globals.dist[0],globals.dist[1],globals.dist[2] - globals.dist[0],globals.dist[3] - globals.dist[1], color, 3.0)
    if globals.monster_pos :
        pm.draw_rectangle(globals.monster_pos[0],globals.monster_pos[1],50,50,color2)
    pm.end_drawing()
