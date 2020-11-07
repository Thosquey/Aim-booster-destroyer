import keyboard
import pyautogui
import win32api, win32con
import time

MIN_X = 680
MIN_Y = 350
MAX_X = 1250
MAX_Y = 750

def click(xPos, yPos):
    win32api.SetCursorPos((xPos, yPos))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

click(1000, 750)

while not keyboard.is_pressed('esc'):
    frame = pyautogui.screenshot(region=(MIN_X, MIN_Y, MAX_X, MAX_Y))
    
    for h in range(MIN_X, MAX_X, 5):
        for v in range(MIN_Y, MAX_Y, 5):
            if frame.getpixel((h - MIN_X, v - MIN_Y)) == (255, 219, 195):
                click(h, v)
