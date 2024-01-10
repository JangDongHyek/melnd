import globals
import gsl
import cv2
import numpy as np
import win32gui
import win32con
import win32api
import ctypes
import pyMeow as pm

def findAll() :
    while True :
        myPos()
        findMonsters(globals.hunt_monsters)

def myPos() :
    try :
        p = gsl.imageSearch("res/my.png")
        if(p) :
            globals.my_pos = (p[0],p[1])
    except Exception as e :
        print("myPos")

def hwndRactangle() :
    try :
        pm.overlay_init()

        while pm.overlay_loop():
            pm.begin_drawing()
            my_pos = globals.my_pos
            color = pm.get_color("#0400ff")
            for monster in globals.monsters :
                pm.draw_line(my_pos[0],my_pos[1],monster[0],monster[1],color)
                pm.draw_rectangle_lines(monster[0],monster[1],monster[2],monster[3], color, 3.0)

            pm.end_drawing()
    except Exception as e:
        print("hwnd")


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

def checkMonsterPix(dist,monsters) :
    if(gsl.pixelSearch(dist,monsters)) :
        return True
    return False
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