import globals
import gsl
import cv2
import numpy as np
import win32gui
import win32con
import win32api
import ctypes
import pyMeow as pm
import lib

def findMap(name) :
    for map in globals.maps :
        if name == map["name"] :
            return map

def checkHP() :
    return gsl.pixelSearch([500,1050,510,1060],(190, 190, 190))
def getDist() :
    # if globals.direction == "left" :
    #     globals.dist = (globals.my_pos[0] - 500, globals.my_pos[1] - 100, globals.my_pos[0] + 30, globals.my_pos[1] + 200)
    # else :
    #     globals.dist = (globals.my_pos[0],globals.my_pos[1]-100,globals.my_pos[0]+500,globals.my_pos[1]+200)

    globals.dist = (globals.my_pos[0] - 450, globals.my_pos[1] - 100, globals.my_pos[0] + 450, globals.my_pos[1] + 200)

def myPos() :
    try :
        p = gsl.pixelSearch([350,400,1650,800],globals.my_pixel)
        if(p) :
            globals.my_pos = (p[0],p[1])
    except Exception as e :
        print("myPos")

def update() :
    while True:

        myPos()
        getDist()
        checkMonsterPix()


def render() :
    try :
        pm.overlay_init()
        color = pm.get_color("#0400ff")
        color2 = pm.get_color("#ff0000")
        main = True
        while pm.overlay_loop() and main:
            pm.begin_drawing()
            pm.draw_rectangle_lines(globals.dist[0],globals.dist[1],globals.dist[2] - globals.dist[0],globals.dist[3] - globals.dist[1], color, 3.0)
            if globals.monster_pos :
                pm.draw_rectangle(globals.monster_pos[0],globals.monster_pos[1],50,50,color2)
            pm.end_drawing()
    except Exception as e:
        print("hwnd")
        print(e)
        print(globals.dist)
        print(globals.my_pos)
        globals.thread_flag = True
        gsl.playBeep()
        globals.threadRender = True
        main = False


def checkMonsterPix() :
    p = gsl.pixelSearch(globals.dist,globals.monsters)
    if(p) :
        globals.monster_pos = p
    else :
        globals.monster_pos = None
def checkMp():
    p = gsl.imageSearch("res/mp.png")
    if (p):
        mp = [p[0] + 60, p[1] + 35, p[0] + 70, p[1] + 45]

        if (gsl.pixelSearch(mp, globals.mp_pixcel)):
            return True
    return False

def getMinimap() :
    x = gsl.imageSearch("res/world.png")
    y = gsl.imageSearch("res/minimap_y.png")

    globals.minimap = [12,55,x[0] + 66,y[1]]
    # globals.obj_minimap = {
    #     "start_x" : 12,
    #     "end_x" : x[0] + 66,
    #     "start_y" : 55,
    #     "end_y" : y[1]
    # }


def getMyPosition() :
    p = gsl.pixelSearch(globals.minimap,globals.minimap_my)
    if(p) :
        globals.minimap_my_pos = p

    return None