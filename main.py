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
globals.my_pixel = [(254, 111, 242)] # 장달프
map = gml.findMap("와일드보어의 땅")
# map = gml.findMap("1호선 4구역")

globals.init_dist = map["init_dist"]
globals.monsters = map["monsters"]
floors = map["floors"]
globals.minimap = map["minimap"]

update = threading.Thread(target=gml.update)
update.start()
time.sleep(1)
render = threading.Thread(target=gml.render)
render.start()

dict = map["map_dict"]
jump = False
floor_dict = "left"
minus = False
floor = floors[0]
next_floors = floors[0]
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


        # 현재위치 계산
        for i,m in enumerate(floors) :
            low_y = m["low_y"] - 1
            high_y = m["high_y"] + 1

            if (low_y <= globals.minimap_my_pos[1] and globals.minimap_my_pos[1] <= high_y and
                m["search_start_x"] <= globals.minimap_my_pos[0] and globals.minimap_my_pos[0] <= m["search_end_x"]) :
                floor = m

                if (i + 1) > (len(floors) -1) :
                    next_floors = floors[0]
                else :
                    next_floors = floors[i+1]

                break

        print(floor["name"])

        # 좌표에따른 방향 설정 및 점프 초기화
        if floor["start_x"] >= globals.minimap_my_pos[0]:
            globals.direction = "right"
        if floor["end_x"] <= globals.minimap_my_pos[0]:
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

        if floor["move_type"] == "teleport" : # 이동타입이 텔포면
            if (dict == globals.direction) and jump and gml.teleportIF(floor_dict,floor) :

                jump = False

                if floor["move_dict"]  == "up" : # 위에방향 텔포면
                    gsl.hardKey(globals.left, False)
                    gsl.hardKey(globals.right, False)

                    gsl.hardKey(globals.up, True)
                    time.sleep(0.2)
                    gsl.hardKey(globals.shift)
                    gsl.hardKey(globals.up, False)
                else : # 아랫방향 텔포면
                    print("미구현")

                if floor["double_y"] :
                    if floor_dict == "left" :
                        floor_dict = "right"
                    else :
                        floor_dict = "left"

        else : # 이동타입이 점프면
            if (dict == globals.direction) and jump and gml.jumpIF(floor["rope_x"]): # 아랫점프
                jump = False
                if floor["move_dict"]  == "up" : # 줄잡고 올라가는
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
                            if (globals.minimap_my_pos[1] <= (next_floors["low_y"] + 2)):
                                break

                            if gsl.compareTime(a, 4):
                                break
                        gsl.hardKey(globals.up, False)

                        if floor["double_y"] :
                            floor["move_dict"] = "down"

                else : # 아랫점프
                    gsl.hardKey(globals.down, True)
                    time.sleep(0.5)
                    gsl.hardKey(globals.alt)
                    gsl.hardKey(globals.down, False)
                    gsl.hardKey(globals.right, False)
                    gsl.hardKey(globals.left, False)
                    time.sleep(1)

                    if floor["double_y"]:
                        floor["move_dict"] = "up"

        # 조건 체크후 힐힐
        if gml.checkHP() :
            gsl.hardKey(globals.pagedown)

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
