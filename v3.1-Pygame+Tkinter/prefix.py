from time import sleep
from pygame.locals import *
from tkinter import Tk
from tkinter.messagebox import showerror,showinfo,askyesno
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Button,Label,Entry,Frame
from os import system
from os.path import isdir,isfile
from time import time
from random import seed,shuffle,random
import pygame
from sys import argv
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog

# 初始化
pygame.init()
pygame.font.init()
# 帧速率
FPS=300
LOW_FPS=100
fps_clock=pygame.time.Clock()
# 颜色
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
GREEN     = (  0,128,  0)
BLUE      = (  0,  0,255)
GRAY      = (128,128,128)
DARK_GRAY = ( 48, 48, 48)
LIME      = (  0,255,  0)
PURPLE    = (128,  0,128)
TEAL      = (  0,128,128)
YELLOW    = (255,255,  0)
# 字体
FONT = pygame.font.SysFont('SimHei', 40)
LITTLE_FONT = pygame.font.SysFont('SimHei', 30)
VERY_LITTLE_FONT = pygame.font.SysFont('SimHei', 20)
EXTREME_LITTLE_FONT = pygame.font.SysFont('SimHei', 15)

def AskOpenFileName(file_mode:str): # file_mode例子："A(*.a)\0"
    App=QApplication(argv)
    Widget=QWidget()
    FileName=QFileDialog.getOpenFileName(parent=Widget,\
        caption="选择文件",directory=".\\",filter=file_mode)
    return FileName[0]

AskOpenFileName("A(*.a)\0B(*.b)\0\0")
# https://blog.csdn.net/ytz201201/article/details/83904119