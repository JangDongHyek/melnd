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



# 내케릭 픽셀
globals.my_pixel = [(34, 102, 68)] # 장달프
map = gml.findMap("와일드보어의 땅")
globals.monsters = map["monsters"]
floors = map["floors"]
globals.minimap = map["minimap"]

print(globals.minimap)

update = threading.Thread(target=gml.update)
update.start()
time.sleep(1)
render = threading.Thread(target=gml.render)
render.start()

my_floors = [0,1,2]
dict = "left"
jump = False
minus = False
while True :
    if globals.threadRender :
        globals.threadRender = False
        render = threading.Thread(target=gml.render)
        render.start()

    if globals.threadUpdate :
        globals.threadUpdate = False
        update = threading.Thread(target=gml.update)
        update.start()

    if win32api.GetKeyState(globals.mainKey):
        if not flag :
            flag = True
            thread = True

        gml.getMyPosition()


        # 현재위치 층수계산
        floor = floors[0]
        next_floor = 0
        add_floor = 0
        for i,m in enumerate(floors) :
            low_y = m["low_y"] - 2
            high_y = m["high_y"] + 2
            if low_y <= globals.minimap_my_pos[1] and globals.minimap_my_pos[1] <= high_y :
                floor = m
                add_floor = 1
                if i >= my_floors[-1] :
                    minus = True
                if i <= my_floors[0] :
                    minus = False

                if minus :
                    add_floor = -1
                next_floor = i + add_floor
                break


        # 좌표에따른 방향 설정 및 점프 초기화
        if floor["start_x"] > globals.minimap_my_pos[0]:
            globals.direction = "right"
        if floor["end_x"] < globals.minimap_my_pos[0]:
            globals.direction = "left"

        if dict != globals.direction :
            jump = True


        # 방향에 따른 이동및 사거리 체크
        if globals.direction == "left":
            gsl.hardKey(globals.right, False)
            gsl.hardKey(globals.left, True)
        elif globals.direction == "right":
            gsl.hardKey(globals.left, False)
            gsl.hardKey(globals.right, True)

        if (dict == globals.direction) and (next_floor in my_floors) and jump and gml.jumpIF(floor["rope_x"]):
            jump = False
            if add_floor < 0 : # 내려가는
                gsl.hardKey(globals.down, True)
                time.sleep(0.5)
                gsl.hardKey(globals.alt)
                gsl.hardKey(globals.down, False)
                gsl.hardKey(globals.right, False)
                gsl.hardKey(globals.left, False)
                time.sleep(1)
            else : # 올라가는
                gsl.hardKey(globals.alt)
                gsl.hardKey(globals.up, True)
                time.sleep(0.5)
                gsl.hardKey(globals.up, False)
                gml.getMyPosition()
                if globals.minimap_my_pos[1] <= floor["rope_y"]:
                    gsl.hardKey(globals.up, True)
                    gsl.hardKey(globals.right, False)
                    gsl.hardKey(globals.left, False)
                    a = time.time()
                    while True:
                        gml.getMyPosition()
                        time.sleep(0.1)
                        if (globals.minimap_my_pos[1] <= (floors[next_floor]["low_y"] +2 )):
                            break

                        if gsl.compareTime(a, 4):
                            break
                    gsl.hardKey(globals.up, False)

        # 조건 체크후 힐힐
        # if gml.ceckHP() :
        #     gsl.hardKey(globals.pagedown)

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





    else :
        if(flag) :
            gsl.offHardKey()
            flag = False
