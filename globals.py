import time
# 설정
gameTitle = "MapleStory Worlds-Mapleland"
ddl = None
hwnd = None
windowMode = False
window_x = 0
window_y = 0
windowPlusX = 1
windowPlusY = 31
main = False
mainKey = 0x05

# 회원정보
user = None
characters = None
character = None
skills = None
movings = None

# 메랜
mp_pixcel = [(0, 170, 255),(0, 159, 238)]
minimap = []
minimap_my = [(255, 255, 136)]
my_pos = (1000,560)
threadRender = False
threadUpdate = False
my_pixel = []
map_scope = []
hp = None



monsters = []
monster_pos = None
minimap_my_pos = None
direction = "left"
dist = None #총 공격사거리
init_dist = [] # 공격사거리 설정값

thread_flag = False

# 하드웨어 키값
esc,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12 = 100,101,102,103,104,105,106,107,108,109,110,111,112
q,w,e,r,t,y,u,i,o,p = 301,302,303,304,305,306,307,308,309,310
n1,n2,n3,n4,n5,n6,n7,n8,n9,n0 = 201,202,203,204,205,206,207,208,209,210
a,s,d,f,g,h,j,k,l = 401,402,403,404,405,406,407,408,409
z,x,c,v,b,n,m = 501,502,503,504,505,506,507
up,left,down,right = 709,710,711,712
shift,ctrl,alt,space,enter = 500,600,602,603,313
insert,home,pageup,delete,end,pagedown = 703,704,705,706,707,708

skills = [
    {
        "key" : home,
        "cooldown" : 200,
        "time" : time.time()
    },

    {
        "key" : pageup,
        "cooldown" : 600,
        "time" : time.time()
    }
]

# x,y,점프할위치,줄잡았을떄y,점프할건지,성공여부,2층y
maps = [
    {
        "name" : "와일드보어의 땅",
        "map_dict" : "left",
        "minimap" : [12,55,360,230],
        "init_dist" : [-450,-100,+450,+200],
        "monsters" : [(198, 146, 148),(137, 122, 88)],#와보,스텀프
        "floors" : [

            {
                "name": "1",
                "search_start_x": 95,
                "search_end_x": 295,
                "start_x": 105,
                "end_x": 285,
                "low_y": 199,
                "high_y": 207,
                "move_dict": "up",
                "double_y": False,
                "move_type": "jump",
                "rope_x": 270,
                "rope_y": 196,
                "teleport_xL": None,
                "teleport_yL": None,
                "teleport_xR": None,
                "teleport_yR": None
            },

            {
                "name": "2",
                "search_start_x": 185,
                "search_end_x": 230,
                "start_x": 185,
                "end_x": 220,
                "low_y": 181,
                "high_y": 181,
                "move_dict": "up",
                "double_y": True,
                "move_type": "jump",
                "rope_x": 203,
                "rope_y": 178,
                "teleport_xL": None,
                "teleport_yL": None,
                "teleport_xR": None,
                "teleport_yR": None
            },

            {
                "name": "3",
                "search_start_x": 165,
                "search_end_x": 237,
                "start_x": 175,
                "end_x": 227,
                "low_y": 136,
                "high_y": 136,
                "move_dict": "down",
                "double_y": False,
                "move_type": "jump",
                "rope_x": 190,
                "rope_y": 136,
                "teleport_xL": None,
                "teleport_yL": None,
                "teleport_xR": None,
                "teleport_yR": None
            },

        ]
    },
{
        "name" : "1호선 4구역",
        "map_dict": "right",
        "minimap" : [12,55,432,218],
        "init_dist" : [-250,-70,+250,+250],
        "monsters" : [(206, 222, 239)],#레이스
        "floors" : [
            {
                "name" : "1-1",
                "search_start_x" : 90,
                "search_end_x" : 175,
                "start_x" : 101,
                "end_x" : 158,
                "low_y" : 153,
                "high_y" : 153,
                "move_dict" : "up",
                "double_y" : False,
                "move_type" : "teleport",
                "rope_x" : None,
                "rope_y" : None,
                "teleport_xL" : 131,
                "teleport_yL" : 153,
                "teleport_xR" : 131,
                "teleport_yR" : 153
            },

            {
                "name" : "1-2",
                "search_start_x" : 194,
                "search_end_x" : 320,
                "start_x" : 210,
                "end_x" : 310,
                "low_y" : 153,
                "high_y" : 153,
                "move_dict" : "up",
                "double_y" : False,
                "move_type" : "teleport",
                "rope_x" : None,
                "rope_y" : None,
                "teleport_xL" : 300,
                "teleport_yL" : 153,
                "teleport_xR" : 300,
                "teleport_yR" : 153
            },

            {
                "name" : "2-1",
                "search_start_x": 90,
                "search_end_x": 170,
                "start_x" : 115,
                "end_x" : 147,
                "low_y" : 138,
                "high_y" : 138,
                "move_dict" : "up",
                "double_y": False,
                "move_type" : "teleport",
                "rope_x" : None,
                "rope_y" : None,
                "teleport_xL" : 134,
                "teleport_yL" : 138,
                "teleport_xR" : 134,
                "teleport_yR" : 138
            },

            {
                "name": "2-2",
                "search_start_x": 186,
                "search_end_x": 260,
                "start_x": 209,
                "end_x": 221,
                "low_y": 138,
                "high_y": 138,
                "move_dict": "down",
                "double_y": False,
                "move_type": "jump",
                "rope_x": None,
                "rope_y": None,
                "teleport_xL": 219,
                "teleport_yL": 138,
                "teleport_xR": 219,
                "teleport_yR": 138
            },

{
                "name": "2-3",
                "search_start_x": 257,
                "search_end_x": 342,
                "start_x": 274,
                "end_x": 324,
                "low_y": 138,
                "high_y": 138,
                "move_dict": "up",
                "double_y": False,
                "move_type": "teleport",
                "rope_x": None,
                "rope_y": None,
                "teleport_xL": 314,
                "teleport_yL": 138,
                "teleport_xR": 314,
                "teleport_yR": 138
            },


            {
                "name" : "3-1",
                "search_start_x": 115,
                "search_end_x": 203,
                "start_x" : 135,
                "end_x" : 180,
                "low_y" : 123,
                "high_y" : 123,
                "move_dict" : "up",
                "double_y" : True,
                "move_type" : "teleport",
                "rope_x" : None,
                "rope_y" : None,
                "teleport_xL" : 125,
                "teleport_yL" : 123,
                "teleport_xR" : 175,
                "teleport_yR" : 123,
            },

            {
                "name": "3-2",
                "search_start_x": 212,
                "search_end_x": 304,
                "start_x": 220,
                "end_x": 227,
                "low_y": 127,
                "high_y": 127,
                "move_dict": "up",
                "double_y": True,
                "move_type": "teleport",
                "rope_x": None,
                "rope_y": None,
                "teleport_xL": 225,
                "teleport_yL": 127,
                "teleport_xR": 225,
                "teleport_yR": 127,
            },

            {
                "name": "3-3",
                "search_start_x": 300,
                "search_end_x": 356,
                "start_x": 312,
                "end_x": 342,
                "low_y": 127,
                "high_y": 127,
                "move_dict": "up",
                "double_y": True,
                "move_type": "teleport",
                "rope_x": None,
                "rope_y": None,
                "teleport_xL": 314,
                "teleport_yL": 127,
                "teleport_xR": 314,
                "teleport_yR": 127,
            },

            {
                "name" : "4-1",
                "search_start_x": 90,
                "search_end_x": 132,
                "start_x" : 86,
                "end_x" : 130,
                "low_y" : 108,
                "high_y" : 108,
                "move_dict" : "down",
                "double_y": False,
                "move_type" : "jump",
                "rope_x" : 125,
                "rope_y" : 108,
                "teleport_xL" : None,
                "teleport_yL" : None,
                "teleport_xR" : None,
                "teleport_yR" : None
            },

            {
                "name" : "4-2",
                "search_start_x": 167,
                "search_end_x": 272,
                "start_x" : 189,
                "end_x" : 220,
                "low_y" : 108,
                "high_y" : 108,
                "move_dict" : "down",
                "double_y": False,
                "move_type" : "jump",
                "rope_x" : 213,
                "rope_y" : 108,
                "teleport_xL" : None,
                "teleport_yL" : None,
                "teleport_xR" : None,
                "teleport_yR" : None
            },

            {
                "name": "4-3",
                "search_start_x": 220,
                "search_end_x": 310,
                "start_x": 230,
                "end_x": 298,
                "low_y": 108,
                "high_y": 108,
                "move_dict": "down",
                "double_y": False,
                "move_type": "jump",
                "rope_x": 233,
                "rope_y": 108,
                "teleport_xL": None,
                "teleport_yL": None,
                "teleport_xR": None,
                "teleport_yR": None
            },
        ]
    }
]