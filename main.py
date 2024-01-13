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

# x,y,점프할위치,줄잡았을떄y,점프불리언,성공여부,2층y
# globals.map_scope = [115,155] # 개미굴 1-1
# globals.map_scope = [105,140] # 개미굴 1-2
# globals.map_scope = [205,250] # 개미굴 2-2
# globals.map_scope = [320,380] # 개미굴 3-2
# globals.map_scope = [105,285] # 와보땅 1
# globals.map_scope = [185,220,216,175,True,False,136] # 와보땅 2
map = gml.findMap("와보땅 2~3")
# 내케릭 픽셀
globals.my_pixel = [(238, 119, 0)] # 혁지션
# globals.my_pixel = [(34, 102, 68)] # 장달프

# globals.monsters.append((239, 238, 239)) #좀비버섯
# globals.monsters.append((170, 175, 137)) # 뿔버섯
globals.monsters.append((198, 146, 148)) # 와보
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

        if(globals.minimap_my_pos[1] > 185) :
            gsl.offHardKey()
            gsl.playBeep()
            exit()
        # 타이머
        # if(gsl.compareTime(timer,14000)) :
        #     gsl.hardKey(globals.insert)
        #     time.sleep(1)
        #     gsl.offHardKey()
        # 좌표에따른 방향 설정
        if not map["catch"] :
            if map["x"] > globals.minimap_my_pos[0]:
                globals.direction = "right"
                map["jump"] = True

            if map["y"] < globals.minimap_my_pos[0]:
                globals.direction = "left"
        else :
            if map["x_2"] > globals.minimap_my_pos[0]:
                globals.direction = "right"
                map["jump"] = True

            if map["y_2"] < globals.minimap_my_pos[0]:
                globals.direction = "left"

        if globals.direction == "left" and globals.minimap_my_pos[0] < map["alt_y"]  and map["jump"]:
            map["jump"] = False

            if map["catch"] : # 올라가기성공했을때
                gsl.hardKey(globals.down,True)
                time.sleep(0.5)
                gsl.hardKey(globals.alt)
                gsl.hardKey(globals.down, False)
                gsl.hardKey(globals.right, False)
                gsl.hardKey(globals.left, False)
                time.sleep(1)
                gml.getMyPosition()
                if globals.minimap_my_pos[1] > map["catch_y"]:
                    map["catch"] = False

            else : #올라가기 실패했을떄
                gsl.hardKey(globals.alt)
                gsl.hardKey(globals.up,True)
                time.sleep(0.5)
                gsl.hardKey(globals.up,False)
                gml.getMyPosition()
                if  globals.minimap_my_pos[1] < map["catch_y"] :
                    map["catch"] = True
                    gsl.hardKey(globals.up, True)
                    gsl.hardKey(globals.right, False)
                    gsl.hardKey(globals.left, False)
                    a = time.time()
                    while True:
                        gml.getMyPosition()
                        time.sleep(0.1)
                        if(globals.minimap_my_pos[1] < (map["end_y"] + 2)) :
                            break

                        if gsl.compareTime(a,4) :
                            break
                    gsl.hardKey(globals.up, False)


        if globals.minimap_my_pos[1] < 130 :
            gsl.offHardKey()
            gsl.playBeep()
            exit()
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


        # 조건 체크후 공격
        if(globals.monster_pos) :
            if(globals.monster_pos[0] < globals.my_pos[0]) :
                gsl.hardKey(globals.right, False)
                gsl.hardKey(globals.left)
            elif globals.monster_pos[0] > globals.my_pos[0] :
                gsl.hardKey(globals.left, False)
                gsl.hardKey(globals.right)

            gsl.hardKey(globals.ctrl)


        # 방향에 따른 이동및 사거리 체크
        if globals.direction == "left":
            gsl.hardKey(globals.right, False)
            gsl.hardKey(globals.left, True)
        elif globals.direction == "right":
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, True)



    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
