import cv2
import numpy as np
import time
import gsl
import globals
import init
import gml
import win32gui

init.Init()
map = gml.findMap("1호선 4구역")
globals.init_dist = map["init_dist"]
globals.monsters = map["monsters"]
floors = map["floors"]
globals.minimap = map["minimap"]


gml.getMyPosition()
print(globals.minimap_my_pos)