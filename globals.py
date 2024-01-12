import time
# 설정
gameTitle = "MapleStory Worlds-Mapleland"
ddl = None
hwnd = None
windowMode = False
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
minimap = None
minimap_my = [(255, 255, 136)]
my_pos = ()
threadRender = False
my_pixel = []
map_scope = []



monsters = []
monster_pos = None
minimap_my_pos = None
direction = "left"
dist = None

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
        "cooldown" : 400,
        "time" : time.time()
    },

    {
        "key" : pageup,
        "cooldown" : 600,
        "time" : time.time()
    }
]