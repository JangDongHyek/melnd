import time

import gml
import init
import lib
import win32api
import globals
import gsl
import threading
init.Init()

flag = False
mp_pixcel = [(0, 170, 255),(0, 159, 238)]


# globals.map_scope = [105,155] # 개미굴 1-1
globals.map_scope = [105,140] # 개미굴 1-2
# globals.map_scope = [205,260] # 개미굴 2-2

# 내케릭 픽셀
globals.my_pixel = [(34, 102, 68)]

# globals.monsters.append((239, 238, 239)) #좀비버섯
globals.monsters.append((170, 175, 137)) # 뿔버섯
timer = time.time()
gml.getMinimap()

update = threading.Thread(target=gml.update)
update.start()
time.sleep(1)
render = threading.Thread(target=gml.render)
render.start()
while True :
    if globals.threadRender :
        threadRender = False
        render = threading.Thread(target=gml.render)
        render.start()

    if win32api.GetKeyState(globals.mainKey):
        if not flag :
            gml.getMinimap()
            flag = True
            thread = True


        # 타이머
        # if(gsl.compareTime(timer,14000)) :
        #     gsl.hardKey(globals.insert)
        #     time.sleep(1)
        #     gsl.offHardKey()


        # 스킬사용
        for skill in globals.skills :
            if gsl.compareTime(skill["time"],skill["cooldown"]) :
                gsl.hardKey(skill["key"])
                time.sleep(0.7)
                skill["time"] = time.time()



        # 방향에 따른 이동및 사거리 체크
        if globals.direction == "left" :
            gsl.hardKey(globals.right, False)
            gsl.hardKey(globals.left,True)
        else :
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, True)

        # 조건 체크후 공격
        if(globals.monster_pos) :
            gsl.hardKey(globals.shift)
            time.sleep(1.3)


    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
