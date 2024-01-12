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


# globals.map_scope = [115,155] # 개미굴 1-1
# globals.map_scope = [105,140] # 개미굴 1-2
# globals.map_scope = [205,250] # 개미굴 2-2
# globals.map_scope = [320,380] # 개미굴 3-2

globals.map_scope = [80,310] # 와보땅 1

# 내케릭 픽셀
globals.my_pixel = [(34, 102, 68)]

# globals.monsters.append((239, 238, 239)) #좀비버섯
# globals.monsters.append((170, 175, 137)) # 뿔버섯
globals.monsters.append((154, 137, 121)) # 와보
globals.monsters.append((137, 122, 88)) # 스텀프
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

        gml.getMyPosition()
        globals.hp = gml.checkHP()

        # 타이머
        # if(gsl.compareTime(timer,14000)) :
        #     gsl.hardKey(globals.insert)
        #     time.sleep(1)
        #     gsl.offHardKey()
        # 좌표에따른 방향 설정
        if globals.map_scope[0] > globals.minimap_my_pos[0]:
            globals.direction = "right"

        if globals.map_scope[1] < globals.minimap_my_pos[0]:
            globals.direction = "left"

        # if globals.hp :
        #     gsl.hardKey(globals.pagedown)
        #     time.sleep(0.6)

        # 스킬사용
        for skill in globals.skills :
            if gsl.compareTime(skill["time"],skill["cooldown"]) :
                time.sleep(0.7)
                gsl.hardKey(skill["key"])
                time.sleep(0.7)
                skill["time"] = time.time()



        # 방향에 따른 이동및 사거리 체크
        if globals.direction == "left" :
            gsl.hardKey(globals.right, False)
            gsl.hardKey(globals.left,True)
        elif globals.direction == "right" :
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, True)
        elif globals.direction == "up" :
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, False)

        # 조건 체크후 공격
        if(globals.monster_pos) :
            if(globals.monster_pos[0] < globals.my_pos[0]) :
                gsl.hardKey(globals.right, False)
                gsl.hardKey(globals.left)
            elif globals.monster_pos[0] > globals.my_pos[0] :
                gsl.hardKey(globals.left, False)
                gsl.hardKey(globals.right)

            gsl.hardKey(globals.ctrl)


    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
