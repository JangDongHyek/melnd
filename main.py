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
threadPaint = threading.Thread(target=gml.hwndRactangle)

# threadPaint.start()
# 개미굴 1-2
left_x = 105
right_x = 135




# gml.getMinimap()
# gml.myPos()
# left
# gsl.screenshot("1",[globals.my_pos[0]-400,globals.my_pos[1]-150,globals.my_pos[0]+30,globals.my_pos[1]+100])
# gsl.screenshot("2",[globals.my_pos[0]+50,globals.my_pos[1]-150,globals.my_pos[0]+400,globals.my_pos[1]+100])
# exit()

skills = [
    {
        "key" : globals.home,
        "cooldown" : 132,
        "time" : time.time()
    },

    {
        "key" : globals.pageup,
        "cooldown" : 600,
        "time" : time.time()
    }
]
timer = time.time()
threadPaint.start()
while True :
    if win32api.GetKeyState(globals.mainKey):
        if not flag :
            gml.getMinimap()
            flag = True
            thread = True

        gml.getMyPosition()

        if(gsl.compareTime(timer,14000)) :
            gsl.hardKey(globals.insert)
            time.sleep(1)
            gsl.offHardKey()


        # 스킬사용
        for skill in skills :
            if gsl.compareTime(skill["time"],skill["cooldown"]) :
                gsl.hardKey(skill["key"])
                time.sleep(0.5)
                skill["time"] = time.time()

            # 좌표에따른 방향 설정
        if left_x > globals.minimap_my_pos[0]:
            globals.direction = "right"

        if right_x < globals.minimap_my_pos[0]:
            globals.direction = "left"

        # 방향에 따른 이동및 사거리 체크
        if globals.direction == "left" :
            gsl.hardKey(globals.right, False)
            gsl.hardKey(globals.left,True)
            # gml.myPos()
            # dist = (globals.my_pos[0]-400,globals.my_pos[1]-150,globals.my_pos[0]+30,globals.my_pos[1]+100)
        else :
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, True)

        # 업데이트
        # monster = gml.checkMonsterPix(globals.dist, monsters)



        # 조건 체크후 공격
        if(globals.monster_pos) :
            gsl.hardKey(globals.shift)
            time.sleep(1.1)


    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
