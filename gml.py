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

def checkHP() :
    gsl.pixelSearch([500,1050,510,1060])
def getDist() :
    if globals.direction == "left" :
        globals.dist = (globals.my_pos[0] - 500, globals.my_pos[1] - 100, globals.my_pos[0] + 30, globals.my_pos[1] + 200)
    else :
        globals.dist = (globals.my_pos[0],globals.my_pos[1]-100,globals.my_pos[0]+500,globals.my_pos[1]+200)

def myPos() :
    try :
        p = gsl.pixelSearch([350,400,1650,800],globals.my_pixel)
        if(p) :
            globals.my_pos = (p[0],p[1])
    except Exception as e :
        print("myPos")

def update() :
    while True:
        getMyPosition()
        myPos()
        getDist()
        checkMonsterPix()
        # 좌표에따른 방향 설정
        if globals.map_scope[0] > globals.minimap_my_pos[0]:
            globals.direction = "right"

        if globals.map_scope[1] < globals.minimap_my_pos[0]:
            globals.direction = "left"

def render() :
    try :
        pm.overlay_init()
        color = pm.get_color("#0400ff")
        color2 = pm.get_color("#ff0000")
        while pm.overlay_loop():
            pm.begin_drawing()
            pm.draw_rectangle_lines(globals.dist[0],globals.dist[1],globals.dist[2] - globals.dist[0],globals.dist[3] - globals.dist[1], color, 3.0)
            if globals.monster_pos :
                pm.draw_rectangle(globals.monster_pos[0],globals.monster_pos[1],50,50,color2)
            pm.end_drawing()
    except Exception as e:
        print("hwnd")
        print(e)
        print(globals.dist)
        globals.thread_flag = True
        gsl.playBeep()
        globals.threadRender = True



def findMonsters(target_image_paths):
    # 메인 이미지와 타겟 이미지 로드
    try :
        main_image = np.array(gsl.screenshot())

        lists = []
        for target_image_path in target_image_paths :

            target_image = cv2.imread(target_image_path)
            # 타겟 이미지의 높이와 너비
            target_height, target_width = target_image.shape[:2]

            # 템플릿 매칭 수행
            result = cv2.matchTemplate(main_image, target_image, cv2.TM_CCOEFF_NORMED)

            # 일정 유사도 이상의 위치 찾기
            threshold = 0.8

            obj = {
                "target_height": target_height,
                "target_width": target_width,
                "loc": np.where(result >= threshold)
            }
            lists.append(obj)

        # 타겟 이미지가 등장한 횟수 계산
        monsters = []
        for obj in lists :
            for pt in zip(*obj["loc"][::-1]):

                flag = False
                for monster in monsters :
                    if abs(pt[0] - monster[0]) < 4 :
                        flag = True
                        break
                if(flag) :
                    continue
                monsters.append((pt[0],pt[1],obj["target_width"],obj["target_height"]))


        globals.monsters = monsters
    except Exception as e :
        print("find")

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