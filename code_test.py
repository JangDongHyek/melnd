import cv2
import numpy as np
import time
import gsl
import globals
import init
import gml

init.Init()
gml.getMinimap()
gml.getMyPosition()
print(globals.minimap_my_pos)