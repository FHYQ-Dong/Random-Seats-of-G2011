from os import system
from os.path import isdir,isfile
from time import time
from random import seed,shuffle,random
from sys import argv
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox,QLabel,\
    QPushButton,QLineEdit,QProgressBar
from PyQt5.QtGui import QIcon,QFont,QImage,QPixmap
from PyQt5.QtCore import QBasicTimer,QCoreApplication,Qt

NONE=0
FileDir=".\\files\\" if len(argv)==1 else "..\\files\\"

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

# 弹出选择文件页面
def select_file(file_mode:str) -> str : # file_mode例子："A文件(*.a);;B文件(*.b)"
    App=QApplication(argv)
    Widget=QWidget()
    FileName=QFileDialog.getOpenFileName(parent=Widget,\
        caption="选择文件",directory=".\\",filter=file_mode)
    return FileName[0]

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

# 组件
class Label(QLabel):
    def  __init__(self,parent:QWidget,pos:tuple,show:bool=True,\
        size:tuple=False,text:str=False,font:QFont=False,style:str=False):
        super().__init__(parent)
        if text:self.setText(str(text))
        else:self.setText("Label")
        if size:self.resize(size[0],size[1])
        else:self.resize(self.sizeHint())
        if font:self.setFont(font)
        if style:self.setStyleSheet(style)
        self.move(pos[0],pos[1])
        self.show()
        self.setVisible(bool(show))

class Button(QPushButton):
    def  __init__(self,parent:QWidget,pos:tuple,func=False,arg:tuple=False,\
        size:tuple=False,text:str=False,show:bool=True,font:QFont=False):
        super().__init__(parent)
        if text:self.setText(str(text))
        else:self.setText("Button")
        if size:self.resize(size[0],size[1])
        else:self.resize(self.sizeHint())
        if func:
            if arg:self.clicked.connect(lambda:func(arg))
            else:self.clicked.connect(func)
        self.move(int(pos[0]),int(pos[1]))
        if font:self.setFont(font)
        self.show()
        self.setVisible(bool(show))

class LineEdit(QLineEdit):
    def  __init__(self,parent:QWidget,pos:tuple,size:tuple=False,defaultText:str=False,\
        show:bool=True):
        super().__init__(parent)
        if defaultText:self.setText(str(defaultText))
        if size:self.resize(size[0],size[1])
        else:self.resize(self.sizeHint())
        self.move(pos[0],pos[1])
        self.show()
        self.setVisible(bool(show))