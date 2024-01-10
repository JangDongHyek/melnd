import time

import gml
import init
import lib
import win32api
import globals
import gsl
import threading
init.Init()

dirTime = time.time()
left = True
flag = False
thread = False
p_mp = None
mp_pixcel = [(0, 170, 255),(0, 159, 238)]


# main_image = "res/log/1.bmp"

# threadFind = threading.Thread(target=gml.getMyPosition)
# threadPaint = threading.Thread(target=gml.hwndRactangle)

# threadPaint.start()
left_x = 110
right_x = 240
direction = "left"
monsters = [(255, 255, 222),(255, 239, 173)]

gml.getMinimap()
# gml.myPos()
# left
# gsl.screenshot("1",[globals.my_pos[0]-400,globals.my_pos[1]-150,globals.my_pos[0]+30,globals.my_pos[1]+100])
# gsl.screenshot("2",[globals.my_pos[0]+50,globals.my_pos[1]-150,globals.my_pos[0]+400,globals.my_pos[1]+100])
# exit()
while True :
    if win32api.GetKeyState(globals.mainKey):
        if not flag :
            gml.getMinimap()
            flag = True
            thread = True

        gml.getMyPosition()

        # 방향에 따른 이동및 사거리 체크
        if direction == "left" :
            gsl.hardKey(globals.z, False)
            gsl.hardKey(globals.right, False)
            time.sleep(0.1)
            gsl.hardKey(globals.left,True)
            time.sleep(0.1)
            gsl.hardKey(globals.z, True)
            gml.myPos()
            dist = (globals.my_pos[0]-400,globals.my_pos[1]-150,globals.my_pos[0]+30,globals.my_pos[1]+100)
        else :
            gsl.hardKey(globals.z, False)
            gsl.hardKey(globals.left, False)
            time.sleep(0.1)
            gsl.hardKey(globals.right, True)
            time.sleep(0.1)
            gsl.hardKey(globals.z, True)
            gml.myPos()
            dist = (globals.my_pos[0]+50,globals.my_pos[1]-150,globals.my_pos[0]+400,globals.my_pos[1]+100)


        # 조건 체크후 공격
        if(gml.checkMp() and gml.checkMonsterPix(dist,monsters)) :
            gsl.hardKey(globals.shift)
            time.sleep(0.5)

        # 좌표에따른 방향 설정
        if left_x > globals.minimap_my_pos[0] :
            direction = "right"

        if right_x < globals.minimap_my_pos[0] :
            direction = "left"

    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
