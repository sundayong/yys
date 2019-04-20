import time
import win32gui, win32ui, win32con, win32api
from ctypes import *
import cv2
import numpy as np
import random
import os
import gc

hwnd_title = dict()

def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click_it(pos,hd):
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

def moveCurPos(x, y):  # 移动鼠标
    windll.user32.SetCursorPos(x, y)


def getCurPos():  # 获得鼠标位置信息，这个再实际代码没用上，调试用得上
    return win32gui.GetCursorPos()



def window_capture(filename,hd):
    hwnd = hd  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    #print(w, h)#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()



def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

def get():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t is not "":
            if t == '阴阳师-网易游戏':
                return h


def main():
    #hd = get()
    hd = 2164316
    #filename = "blackground.jpg"  # 储存的文件名
    filename = "nextground.jpg"
    i = 0
    k = 0
    while True:
        time.sleep(1)  # 设置隔2秒运行一次
        # 截图
        window_capture(filename, hd=hd)  # 对整个屏幕截图，并保存截图为filename
        # 原图
        srcImg = cv2.imread(filename)  # 读取filename的截图文件，这里应该是可以对截图函数进行修改，不用产生中间的文件，截图直接与ndarray形式存在
        begin = cv2.imread('begin.png')  # 读取点击开始战斗的 标准图像
        end1 = cv2.imread('end1-1.png')  # 结束之后点击屏幕任意位置，开宝箱
        end2 = cv2.imread('end777.png')  # 开完宝箱后，点击任意结束本轮
        end2_2 = cv2.imread('end2-2.png')
        end3_3 = cv2.imread('end3-3.png')
        end_agin = cv2.imread('endagin.png')
        end_danren = cv2.imread('end_danren.png')
        end_shibai = cv2.imread('endshibai.png')
        end_last = cv2.imread('endlast.png')
        # 用了一个最简答的图像相见的方式来完成以下动作，具体图示往下翻
        begin_meanValue = np.mean(srcImg[450:494, 799:904, :] - begin)  # 检测截图是否包含开始战斗
        end1_meanValue = np.mean(srcImg[119:184, 380:480, :] - end1)  # 检测战斗是否结束
        end2_meanValue = np.mean(srcImg[563:575, 585:624, :] - end2)  # 检测最后的界面
        end2_2_meanValue = np.mean(srcImg[543:586, 862:1006, :] - end2_2)
        end3_3_meanValue = np.mean(srcImg[385:416, 747:783, :] - end3_3)
        end_danren_meanValue = np.mean(srcImg[161:220, 390:459, :] - end_danren)
        end_agin_meanValue = np.mean(srcImg[398:426, 615:742, :] - end_agin)
        end_shibai_meanValue = np.mean(srcImg[109:161, 389:454, :] - end_shibai)
        end_last_meanValue = np.mean(srcImg[249:270, 116:146, :] - end_last)
        # print(begin)


        if end3_3_meanValue < 50:
            k = 0
            move_x = random.randint(1135, 1163)
            move_y = random.randint(575, 604)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y), hd=hd)

        if end_shibai_meanValue < 50:
            move_x = random.randint(490, 551)
            move_y = random.randint(491, 658)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y), hd=hd)

        if end2_2_meanValue < 50:
            k = 0
            move_x = random.randint(1240, 1395)
            move_y = random.randint(728, 778)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y), hd=hd)
        if end_agin_meanValue < 50:
            move_x = random.randint(620, 730)
            move_y = random.randint(400, 420)
            click_it((move_x, move_y), hd=hd)
        if begin_meanValue < 50:  # 界面运行到由战斗开始就点击战斗开始
            k = 0
            move_x = random.randint(1185, 1289)  # 设计随机点击坐标点，防止被检测，虽然不知道有没效果，初衷设置如此
            move_y = random.randint(640, 683)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y),hd=hd)

        if end_last_meanValue < 50:
            move_x = random.randint(587, 613)
            move_y = random.randint(432, 460)
            click_it((move_x, move_y), hd=hd)


        if end1_meanValue < 80 or end_danren_meanValue < 80:  # 检测开宝箱和结束
            k = 1
            move_x = random.randint(490, 551)
            move_y = random.randint(491, 658)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y), hd=hd)
            time.sleep(1)
            move_x = random.randint(490, 551)
            move_y = random.randint(491, 658)
            click_it((move_x, move_y), hd=hd)
            '''while True:
                k += 1
                window_capture(filename_next)
                srcImg_next = cv2.imread(filename_next)
                end2_meanValue_next = np.mean(srcImg_next[402:593, 469:691, :] - end2)
                if end2_meanValue_next < 50:
                    i += 1
                    print("挑战次数: %d   %s" % (i, time.ctime(time.time())))
                    time.sleep(1)
                    move_x = random.randint(465, 500)
                    move_y = random.randint(491, 658)
                    #moveCurPos(move_x, move_y)
                    #clickLeftCur()
                    click_it((move_x, move_y))
                    time.sleep(1)
                    move_x = random.randint(465, 500)
                    move_y = random.randint(491, 658)
                    #moveCurPos(move_x, move_y)
                    #clickLeftCur()
                    click_it((move_x, move_y))
                    break'''



        if end2_meanValue < 80:
            if k == 1:
                i += 1
                print("挑战次数: %d   %s" % (i, time.ctime(time.time())))
                k = 0
            move_x = random.randint(490, 550)
            move_y = random.randint(491, 658)
            #moveCurPos(move_x, move_y)
            #clickLeftCur()
            click_it((move_x, move_y), hd=hd)
            #move_x = random.randint(465, 550)
            #move_y = random.randint(491, 658)
            # moveCurPos(move_x, move_y)
            # clickLeftCur()
            #click_it((move_x, move_y))




if __name__=="__main__":
    main()






