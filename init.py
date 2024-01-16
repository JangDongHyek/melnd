import win32gui
import globals
import ctypes
import lib

class Init :
    def __init__(self):
        # hwnd 찾기 및 설정
        globals.hwnd = win32gui.FindWindow(None, globals.gameTitle)

        win32gui.SetForegroundWindow(globals.hwnd)
        x, y, x1, y1 = win32gui.GetClientRect(globals.hwnd)
        x, y = win32gui.ClientToScreen(globals.hwnd, (x, y))
        globals.window_x = x
        globals.window_y = y

        # classDD 설정
        globals.ddl = ctypes.windll.LoadLibrary("./dd/dd202x.8.x64.dll")
        st = globals.ddl.DD_btn(0)  # classdd 초기설정
        if st != 1:
            lib.alert("ClassDD에 문제가 생겼습니다.")
            exit()



if __name__ == "__main__" :
    Init()
    print(globals.hwnd)