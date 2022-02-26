from time import sleep
from pygame.locals import MOUSEBUTTONUP,QUIT
from os import system
from os.path import isdir,isfile
from time import time
from random import seed,shuffle,random
import pygame
from sys import argv
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox,QLabel,QPushButton,QLineEdit
from PyQt5.QtGui import QIcon


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
IMG=pygame.image.load("icon.ico")

# 弹出选择文件页面
def select_file(file_mode:str) -> str : # file_mode例子："A文件(*.a);;B文件(*.b)"
    App=QApplication(argv)
    Widget=QWidget()
    FileName=QFileDialog.getOpenFileName(parent=Widget,\
        caption="选择文件",directory=".\\",filter=file_mode)
    return FileName[0]

# 弹出另存文件界面
def ask_saveas_file_name(file_mode:str,extension:str) -> str : # file_mode例子："A文件(*.a);;B文件(*.b)"
    App=QApplication(argv)
    Widget=QWidget()
    FileName=QFileDialog.getSaveFileName(parent=Widget,\
        caption="导出文件",directory=".\\",filter=file_mode)
    return FileName[0]+extension

# 弹出选择是否
def ask_yes_no(event) -> bool :
    App=QApplication(argv)
    Widget=QWidget()
    reply=QMessageBox.question(Widget,"提示",str(event),\
        buttons=QMessageBox.Yes|QMessageBox.No,defaultButton=QMessageBox.No)
    return reply==QMessageBox.Yes

# 弹出提示
def show_info(event,title:str="提示") -> None :
    App=QApplication(argv)
    Widget=QWidget()
    window=QMessageBox.information(Widget,title,str(event),\
        buttons=QMessageBox.Ok)
    return

# 弹出错误
def show_error(event) -> None :
    App=QApplication(argv)
    Widget=QWidget()
    window=QMessageBox.warning(Widget,"错误",str(event),\
        buttons=QMessageBox.Ok)
    return