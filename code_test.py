import cv2
import numpy as np
import time
import gsl
import globals
import init
import gml
import win32gui

init.Init()
win32gui.SetForegroundWindow(globals.hwnd)
x, y, x1, y1 = win32gui.GetClientRect(globals.hwnd)
x, y = win32gui.ClientToScreen(globals.hwnd, (x, y))
print(x,y)
x1, y1 = win32gui.ClientToScreen(globals.hwnd, (x1 - x, y1 - y))
print(x1,y1)