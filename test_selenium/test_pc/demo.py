# Time: 2020/9/29 18:00
# Author: jiangzhw
# FileName: demo.py
import win32gui
import win32con

HWND = win32gui.GetForegroundWindow()
print(HWND)
win32gui.SetWindowPos(HWND, None, 0, 0, 720, 600, win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)
