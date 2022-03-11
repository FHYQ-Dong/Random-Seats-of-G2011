from prefix import *
from os import _exit

global lines_number,columns_number,seats,seats_change_mode,students_name
lines_number,columns_number=0,0
seats,seats_change_mode,students_name=[],[],[]

# 按小大排序
def chkmin(x:tuple,y:tuple):
    return (min(x[0],y[0]),min(x[1],y[1])),(max(x[0],y[0]),max(x[1],y[1]))

# 欢迎界面（没什么用）
def greet():

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.InitUI()

        def InitUI(self):
            self.setGeometry(300,300,400,200)
            self.setWindowTitle("欢迎")
            self.setWindowIcon(QIcon("icon.ico"))

            self.Image=QImage("icon.ico")
            self.ImageView=Label(self,(67,25),True,(70,63))
            self.ImageView.setPixmap(QPixmap.fromImage(self.Image).scaled(70,63))


            self.Title=Label(self,(150,30),True,(150,50),"随 机 座 位",\
                QFont("Microsoft YaHei",20),"color:rgb(85,141,232)")
            self.LoadingText=Label(self,(175,90),True,(70,20),"加载中...",QFont('',12))
            
            self.LoadingBar=QProgressBar(self)
            self.LoadingBar.resize(300,20)
            self.LoadingBar.move(60,115)
            self.pv=0

            self.show()

            # 时钟控件用于进度条
            self.timer=QBasicTimer()
            self.timer.start(100,self)
            seed(time())

        def timerEvent(self,e):
            if self.pv>=100:
                self.LoadingBar.setValue(100)
                self.timer.stop()
                self.LoadingText.setVisible(False)
                self.EnterButton=Button(self,(170,150),QCoreApplication.instance().quit,\
                    False,(60,30),"进 入",True)
                self.EnterButton.setFont(QFont("",12))
            else:
                self.pv+=int(random()*10)
                self.LoadingBar.setValue(self.pv)

        def closeEvent(self,e):
            _exit(0)

    greet_app=QApplication(argv)
    greetWindow=Window()
    return greet_app.exec_()

# 导入、新建
def import_create_last():
    
    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.mode=NONE
            self.InitUI()

        def InitUI(self):
            self.setWindowTitle("导入/新建")
            self.setWindowIcon(QIcon("icon.ico"))
            self.setGeometry(300,300,150,150)

            self.ImportButton=Button(self,(40,25),self.changemode,"import",(70,30),"导 入",True,QFont("",14))
            self.NewButton=Button(self,(40,60),self.changemode,"new",(70,30),"新 建",True,QFont("",14))
            self.LastButton=Button(self,(40,95),self.changemode,"last",(70,30),"最 近",True,QFont("",14))

            self.show()

        def changemode(self,arg:str):
            self.mode=arg
            if self.mode=="last":
                if not isfile(FileDir+"last_rsd.rsd"):
                    QMessageBox.warning(self,"错误","找不到最近一次的资料",\
                        buttons=QMessageBox.Ok)
                    return
            QCoreApplication.instance().quit()
        
        def closeEvent(self,e):
            _exit(0)

    import_create_last_app=QApplication(argv)
    importCreateLastWindow=Window()
    import_create_last_app.exec_()
    return importCreateLastWindow.mode

# 选择座位行列数
def choose_seats_numbers():

    global already_get_lines_columns_number
    already_get_lines_columns_number=False

    # 窗口
    class Window(QWidget):
    
        def __init__(self):
            super().__init__()
            self.InitUI()

        # 初始化窗口界面
        def InitUI(self):                

            # 窗口设置        
            self.setGeometry(300,300,180,100)
            self.setWindowTitle("选择行列数")
            self.setWindowIcon(QIcon("icon.ico"))

            self.LinesLabel=Label(self,(10,10),True,(40,20),"行数：")
            self.LinesEdit=LineEdit(self,(50,10),(100,20),str(lines_number))

            self.ColumnsLabel=Label(self,(10,40),True,(40,20),"列数：")
            self.ColumnsEdit=LineEdit(self,(50,40),(100,20),str(columns_number))

            self.ConfirmButton=Button(self,(60,70),self.confirm_button_func,False,\
                (60,25),"确 定")

            self.show()

        def confirm_button_func(self):
            global lines_number,columns_number,already_get_lines_columns_number
            if self.LinesEdit.text().isdigit() and self.ColumnsEdit.text().isdigit()\
                and not int(self.LinesEdit.text())==0 and not int(self.ColumnsEdit.text())==0:
                lines_number=int(self.LinesEdit.text())
                columns_number=int(self.ColumnsEdit.text())
                already_get_lines_columns_number=True
                QCoreApplication.instance().quit()
                return
            else:
                QMessageBox.warning(self,"错误","行和列数必须是正整数",\
                    buttons=QMessageBox.Ok)
                return

        def closeEvent(self,e):
            _exit(0)

    choose_seats_numbers_surface_app=QApplication(argv)
    chooseSeatsNumbersWindow=Window()
    return choose_seats_numbers_surface_app.exec_()

# 选择“空”座位
def choose_blank_seats(mode="new"):
    global seats,seats_change_mode,lines_number,columns_number

    if mode=="new":
        seats_buf=[[False for j in range(lines_number)]
                for i in range(columns_number)]
    else:
        seats_buf=[[(False if not seats[i][j]=="$BLANK$" else True)
                 for j in range(lines_number)] for i in range(columns_number)]

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.InitUI()

        def InitUI(self):
            global seats,seats_change_mode,lines_number,columns_number
            self.setGeometry(200,200,100+45*columns_number,200+45*(lines_number-1))
            self.setWindowTitle("选择空座位")
            self.setWindowIcon(QIcon("icon.ico"))
            # 座位和讲台
            self.SeatButtons=[[Button(self,(50+45*i,50+45*j),self.seats_clicked_func,\
                (i,j),(40,40),"空" if seats_buf[i][j] else " ",True,QFont("",16))\
                     for j in range(lines_number)] for i in range(columns_number)]
            self.Stage=Label(self,(45*columns_number-85,50+45*lines_number),True,\
                (85,40),"讲 台",QFont("",16),"border-width:1px;border-style:solid;border-color:rgb(0,0,0)")
            self.Stage.setAlignment(Qt.AlignCenter)

            self.ConfirmButton=Button(self,(7.5+45*columns_number/2,100+45*lines_number),\
                self.confirm_button_func,False,(85,40),"确 定",True,QFont("",16))

            self.show()

        def seats_clicked_func(self,pos:tuple):
            seats_buf[pos[0]][pos[1]]=not seats_buf[pos[0]][pos[1]]
            self.SeatButtons[pos[0]][pos[1]].setText("空" if seats_buf[pos[0]][pos[1]] else " ")

        def confirm_button_func(self):
            for x in range(columns_number):
                for y in range(lines_number):
                    if seats_buf[x][y]:
                        seats[x][y]="$BLANK$"
                        seats_change_mode[x][y]=(-1,-1)
            QCoreApplication.instance().quit()
            return

        def closeEvent(self,e):
            _exit(0)

        
    choose_blank_seats_app=QApplication(argv)
    chooseBlankSeatsWindow=Window()
    return choose_blank_seats_app.exec_()

# 设置轮换规则
def set_change_mode(mode="new"):
    global seats,seats_change_mode,lines_number,columns_number

    class Window(QWidget):
        def __init__(self):
            self.preidx=self.pstidx=NONE
            self.preFirstButton,self.pstFirstButton=NONE,NONE
            self.preSecondButton,self.pstSecondButton=NONE,NONE
            self.pre_pos_to_idx,self.pst_pos_to_idx={},{}
                        
            super().__init__()
            self.InitUI()

        def InitUI(self):
            self.setGeometry(300,300,140+70*columns_number,170+35*lines_number)
            self.setWindowTitle("设置轮换规则")
            self.setWindowIcon(QIcon("icon.ico"))

            # seats
            self.PreSeatButtons=[[Button(self,(40+35*i,40+35*j),self.pre_seat_buttons_func,\
                (i,j),(30,30)," ",True,QFont("",12)) for j in range(lines_number)]\
                     for i in range(columns_number)]
            self.PstSeatButtons=[[Button(self,(110+35*(columns_number+i),40+35*j),\
                self.pst_seat_buttons_func,(i,j),(30,30)," ",True,QFont("",12))\
                     for j in range(lines_number)] for i in range(columns_number)]

            if mode=="import":
                for x in range(columns_number):
                    for y in range(lines_number):
                        if seats[x][y]=="$BLANK$":continue
                        prepos,pstpos=seats_change_mode[x][y],(x,y)
                        self.preidx+=1
                        self.pstidx+=1
                        self.pre_pos_to_idx[prepos]=self.preidx
                        self.pst_pos_to_idx[pstpos]=self.pstidx
                        self.PreSeatButtons[prepos[0]][prepos[1]].setText(str(self.preidx))
                        self.PstSeatButtons[pstpos[0]][pstpos[1]].setText(str(self.pstidx))
            
            for i in range(columns_number):
                for j in range(lines_number):
                    if seats[i][j]=="$BLANK$":
                        self.PreSeatButtons[i][j].setVisible(False)
                        self.PstSeatButtons[i][j].setVisible(False)
            
            # stage
            self.PreStage=Label(self,(35*columns_number-65,40+35*lines_number),True,\
                (65,30),"讲 台",QFont("",12),"border-width:1px;border-style:solid;border-color:rgb(0,0,0)")
            self.PreStage.setAlignment(Qt.AlignCenter)
            self.PstStage=Label(self,(5+70*columns_number,40+35*lines_number),True,\
                (65,30),"讲 台",QFont("",12),"border-width:1px;border-style:solid;border-color:rgb(0,0,0)")
            self.PstStage.setAlignment(Qt.AlignCenter)

            # reminder
            self.PreReminder=Label(self,(15,10),True,(50,20),"轮换前",QFont("",10))
            self.PreReminder.setAlignment(Qt.AlignCenter)
            self.PrePressReminder=Label(self,(15,80+35*lines_number),True,(100,20),\
                "请选择第1个座位",QFont("",10))
            self.PstReminder=Label(self,(85+35*columns_number,10),True,(50,20),"轮换后",QFont("",10))
            self.PstReminder.setAlignment(Qt.AlignCenter)
            self.PstPressReminder=Label(self,(85+35*columns_number,80+35*lines_number),\
                True,(100,20),"请选择第1个座位",QFont("",10))

            self.ConfirmButton=Button(self,(27.5+35*columns_number,120+35*lines_number),\
                self.confirm_button_func,False,(85,40),"确 定",True,QFont("",16))
            
            self.show()

        def pre_seat_buttons_func(self,pos:tuple):
            if not self.preFirstButton:
                self.preFirstButton=pos
                self.PrePressReminder.setText("请选择第2个座位")
                self.PreSeatButtons[pos[0]][pos[1]].setText("*")
            else:
                self.preSecondButton=pos
                self.preFirstButton,self.preSecondButton=chkmin(self.preFirstButton,self.preSecondButton)
                for x in range(self.preFirstButton[0],self.preSecondButton[0]+1):
                    for y in range(self.preFirstButton[1],self.preSecondButton[1]+1):
                        if seats[x][y]=="$BLANK$":continue
                        self.preidx+=1
                        self.pre_pos_to_idx[(x,y)]=self.preidx
                        self.PreSeatButtons[x][y].setText(str(self.preidx))
                self.preFirstButton,self.preSecondButton=False,False
                self.PrePressReminder.setText("请选择第1个座位")
            return

        def pst_seat_buttons_func(self,pos:tuple):
            if not self.pstFirstButton:
                self.pstFirstButton=pos
                self.PstPressReminder.setText("请选择第2个座位")
                self.PstSeatButtons[pos[0]][pos[1]].setText("*")
            else:
                self.pstSecondButton=pos
                self.pstFirstButton,self.pstSecondButton=chkmin(self.pstFirstButton,self.pstSecondButton)
                for x in range(self.pstFirstButton[0],self.pstSecondButton[0]+1):
                    for y in range(self.pstFirstButton[1],self.pstSecondButton[1]+1):
                        if seats[x][y]=="$BLANK$":continue
                        self.pstidx+=1
                        self.pst_pos_to_idx[(x,y)]=self.pstidx
                        self.PstSeatButtons[x][y].setText(str(self.pstidx))
                self.pstFirstButton,self.pstSecondButton=False,False
                self.PstPressReminder.setText("请选择第1个座位")
            return

        def confirm_button_func(self):
            self.pre_idx_to_pos={}
            for pos in self.pre_pos_to_idx:self.pre_idx_to_pos[self.pre_pos_to_idx[pos]]=pos
            for pos in self.pst_pos_to_idx:
                try:
                    seats_change_mode[pos[0]][pos[1]]=(self.pre_idx_to_pos[self.pst_pos_to_idx[pos]][0],\
                        self.pre_idx_to_pos[self.pst_pos_to_idx[pos]][1])
                except:
                    QMessageBox.warning(self,"错误","轮换方式设置有误",\
                        buttons=QMessageBox.Ok)
                    return
            
            for i in seats_change_mode:
                if (-1,0) in i:
                    QMessageBox.warning(self,"错误","轮换方式未设置完成",\
                        buttons=QMessageBox.Ok)
                    return

            QApplication.instance().quit()

        def closeEvent(self,e):
            _exit(0)

    set_change_mode_app=QApplication(argv)
    setChangeModeWindow=Window()
    return set_change_mode_app.exec_()

# 选择姓名文件
def get_name_file():
    global students_name,seats

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.name_file_name=""
            self.InitUI()

        def InitUI(self):
            self.setGeometry(300,300,220,210)
            self.setWindowTitle("选择姓名文件")
            self.setWindowIcon(QIcon("icon.ico"))

            self.RecentStudentNameButton=Button(self,(40,30),self.recent_func,False,(140,35),"当前学生姓名",\
                True,QFont("",12))
            self.SelectStudentNameButton=Button(self,(40,70),self.select_func,False,(140,35),"选择姓名文件",\
                True,QFont("",12))
            self.LastStudentNameButton=Button(self,(40,110),self.last_func,False,(140,35),"使用上次配置",\
                True,QFont("",12))
            self.ConfirmButton=Button(self,(67.5,155),self.confirm_button_func,False,(85,40),"确 定",True,\
                QFont("",16))

            self.show()

        def closeEvent(self,e):
            _exit(0)

        def recent_func(self):
            QMessageBox.information(self,"查看",",".join(students_name) if not students_name==[] else "空",\
                QMessageBox.Ok)
            return

        def select_func(self):
            global students_name
            self.name_file_name=QFileDialog.getOpenFileName(parent=self,\
                caption="选择文件",directory=".\\",filter="All Files(*.*)")[0]
            if self.name_file_name=="":
                return
            else:
                try:
                    with open (self.name_file_name,mode="r",encoding="utf-8") as f:
                        students_name=f.readlines()
                        for i in range(len(students_name)):
                            students_name[i]=students_name[i].replace("\n","")

                except Exception as e:
                    QMessageBox.warning(self,"错误","无法打开文件\n"+str(e),QMessageBox.Ok)
            return 

        def last_func(self):
            global students_name
            if isfile(FileDir+"last_name_file"):
                with open(FileDir+"last_name_file",mode="r",encoding="utf-8") as f:
                    students_name=eval(f.readline())
                    QMessageBox.information(self,"提示","成功",QMessageBox.Ok)
            else:
                QMessageBox.warning(self,"错误","不存在上次配置",QMessageBox.Ok)
            return
        
        def get_students_name_check(self) -> bool:
            global students_name,seats
            # 更正 students_name
            name_tmp=[]
            for each_name in students_name:
                name_tmp.append(each_name.replace("\n",""))
            students_name=name_tmp
            while "\n" in students_name:
                students_name.remove("\n")
            while "" in students_name:
                students_name.remove("")
            # 检查是否合法
            seats_cnt=0
            for i in seats:
                for j in i:
                    if not j=="$BLANK$":
                        seats_cnt+=1
            return seats_cnt==len(students_name)

        def confirm_button_func(self):
            if self.get_students_name_check():
                if not isdir(FileDir):
                    system("mkdir "+FileDir)
                    with open (FileDir+"last_name_file",mode="w",encoding="utf-8") as f:
                        f.write(str(students_name))
                QApplication.instance().quit()
            else:
                QMessageBox.warning(self,"错误","座位数必须与学生人数相等",QMessageBox.Ok)
                return

    get_name_file_app=QApplication(argv)
    getNameFileWindow=Window()
    return get_name_file_app.exec_()

# 开始排列前确认
def start_confirm():

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.InitUI()

        def InitUI(self):
            self.setGeometry(300,300,150,150)
            self.setWindowTitle("开始？")
            self.setWindowIcon(QIcon("icon.ico"))

            self.ConfirmButton=Button(self,(30,45),QApplication.instance().quit,\
                False,(90,60),"开始",True,QFont("",20))

            self.show()

        def closeEvent(self,e):
            _exit(0)

    start_confirm_app=QApplication(argv)
    startConfirmWindow=Window()
    return start_confirm_app.exec_()

# 随机排列
def random_arrange(visual=False) -> bool:
    global lines_number,columns_number,seats,students_name,seats_change_mode

    if not visual:
        seed(time())
        shuffle(students_name)
        random_cnt=0
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if not seats[i][j]=="$BLANK$":
                    seats[i][j]=students_name[random_cnt]
                    random_cnt+=1
                else:
                    continue

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.arrange_over=visual
            self.all_seats_cnt=0
            self.x,self.y=0,0
            self.change_pre,self.change_pst=(-1,-1),(-1,-1)
            
            self.InitUI()

        def InitUI(self):
            self.setGeometry(300,300,100+75*columns_number,200+45*lines_number)
            self.setWindowTitle("随机排列")
            self.setWindowIcon(QIcon("icon.ico"))
            
            self.SeatButtons=[[Button(self,(50+75*i,50+45*j),self.seat_buttons_func,(i,j),(70,40),\
                seats[i][j],True if visual else False,QFont("",14))\
                     for j in range(lines_number)] for i in range(columns_number)]
            for i in range(columns_number):
                for j in range(lines_number):
                    if seats[i][j]=="$BLANK$":self.SeatButtons[i][j].setVisible(False)
                    else:self.all_seats_cnt+=1

            self.Stage=Label(self,(-25+75*(columns_number-2),50+45*lines_number),True,\
                (145,40),"讲 台",QFont("",14),"border-width:1px;border-style:solid;border-color:rgb(0,0,0)")
            self.Stage.setAlignment(Qt.AlignCenter)

            # 功能性按钮
            self.SaveRsdButton=Button(self,(25+45*columns_number,45*lines_number+127.5),self.save_rsd_button_func,\
                False,(80,35),"导出(.rsd)")
            self.SaveTxtButton=Button(self,(5+30*columns_number,45*lines_number+127.5),self.save_txt_button_func,\
                False,(80,35),"导出(.txt)")
            self.ChangeSeatsButton=Button(self,(-15+15*columns_number,45*lines_number+127.5),self.change_seats_button_func,\
                False,(80,35),"轮换")
            self.ConfirmButton=Button(self,(45+60*columns_number,45*lines_number+127.5),QApplication.instance().quit,\
                False,(80,35),"确定")

            if not visual:
                self.timer=QBasicTimer()
                self.seats_cnt=0
                self.timer.start(300,self)

            self.show()

        def seat_buttons_func(self,pos):
            global lines_number,columns_number,seats
            if not self.arrange_over:return
            if self.change_pre==(-1,-1):
                self.change_pre=pos
                return
            else:
                self.change_pst=pos
                tmp1=seats[self.change_pre[0]][self.change_pre[1]]
                tmp2=seats[self.change_pst[0]][self.change_pst[1]]
                seats[self.change_pre[0]][self.change_pre[1]]=tmp2
                seats[self.change_pst[0]][self.change_pst[1]]=tmp1
                self.SeatButtons[self.change_pre[0]][self.change_pre[1]].setText(tmp2)
                self.SeatButtons[self.change_pst[0]][self.change_pst[1]].setText(tmp1)
                self.change_pre,self.change_pst=(-1,-1),(-1,-1)

        def save_rsd_button_func(self):
            global lines_number,columns_number,seats,seats_change_mode
            saveas_file_name=QFileDialog.getSaveFileName(parent=self,caption="导出文件",\
                directory=".\\",filter="数据文件(.rsd)")[0]+".rsd"
            if saveas_file_name==".rsd":
                return
            with open (saveas_file_name,mode="w",encoding="utf-8") as f:
                f.write(str(columns_number)+"\n"+str(lines_number)+"\n"+str(seats)+"\n"+\
                    str(seats_change_mode)+"\n"+str(students_name))
            QMessageBox.information(self,"提示","导出成功",buttons=QMessageBox.Ok)
            return

        def save_txt_button_func(self):
            global lines_number,columns_number,seats
            saveas_file_name=QFileDialog.getSaveFileName(parent=self,caption="导出文件",\
                directory=".\\",filter="文本文件(.txt)")[0]+".txt"
            if saveas_file_name==".txt":
                return
            with open (saveas_file_name,mode="w",encoding="utf-8") as f:
                space="\u3000"
                for y in range(lines_number):
                    f.write("%d/%d>" %(lines_number-y,lines_number))
                    for x in range(columns_number):
                        f.write(space)
                        if seats[x][y]=="$BLANK$":
                            f.write(space*4)
                        else:
                            f.write(seats[x][y]+space*(4-seats[x][y].__len__()))
                        if not x==columns_number-1:
                            f.write("|")
                    f.write("\n")
                f.write("0/%d>" %(lines_number)+(lines_number-3)*(space*5+"|")+
                    space*3+"讲"+space+"|"+space+"台"+space*3+"|")
            QMessageBox.information(self,"提示","导出成功",buttons=QMessageBox.Ok)
            return

        def change_seats_button_func(self):
            global seats
            new_seats=[["" for j in range(lines_number)] for i in range(columns_number)]
            for x in range(columns_number):
                for y in range(lines_number):
                    new_seats[x][y]=seats[seats_change_mode[x][y][0]][\
                        seats_change_mode[x][y][1]] if not seats_change_mode[x][y]==(-1,-1) else "$BLANK$"
                    
            seats=new_seats
            for x in range(columns_number):
                for y in range(lines_number):
                    self.SeatButtons[x][y].setText(seats[x][y])

            if not isdir(FileDir):
                system("mkdir "+FileDir)
            with open (FileDir+"last_rsd.rsd",mode="w",encoding="utf-8") as f:
                f.write(str(columns_number)+"\n"+str(lines_number)+"\n"+str(seats)+"\n"+\
                    str(seats_change_mode)+"\n"+str(students_name))
            self.change_pre,self.change_pst=(-1,-1),(-1,-1)

        def closeEvent(self,e):
            _exit(0)
        
        def timerEvent(self,e):
            if not self.seats_cnt==self.all_seats_cnt:
                if not seats[self.x][self.y]=="$BLANK$":
                    self.seats_cnt+=1
                    self.SeatButtons[self.x][self.y].setVisible(True)
                if self.y==len(seats[self.x])-1:
                    self.y=0
                    self.x+=1
                else:
                    self.y+=1
            else:
                self.timer.stop()
                self.arrange_over=True
                self.x,self.y=0,0
                
                if not isdir(FileDir):
                    system("mkdir "+FileDir)
                with open (FileDir+"last_rsd.rsd",mode="w",encoding="utf-8") as f:
                    f.write(str(columns_number)+"\n"+str(lines_number)+"\n"+str(seats)+"\n"+\
                        str(seats_change_mode)+"\n"+str(students_name))

        
    random_arrange_app=QApplication(argv)
    randomArrangeWindow=Window()
    return random_arrange_app.exec_()

# 导入后进行修改或进一步操作
def config_operate():
    global seats_change_mode,seats,columns_number,lines_number

    def getWindow():
        class Window(QWidget):
            def __init__(self):
                super().__init__()
                self.InitUI()

            def InitUI(self):
                self.setGeometry(300,300,200,150)
                self.setWindowTitle("修改/操作")
                self.setWindowIcon(QIcon("icon.ico"))

                self.ConfigButton=Button(self,(40,20),self.button_func,"config",(120,30),\
                    "修改/查看配置",True,QFont("",12))
                self.VisualizeButton=Button(self,(40,57),self.button_func,"visualise",(120,30),\
                    "显示座位表",True,QFont("",12))
                self.RandomArrangeButton=Button(self,(40,94),self.button_func,"randomarrange",\
                    (120,30),"随机排座位",True,QFont("",12))

                self.show()  

            def button_func(self,mode):
                self.mode=mode
                QApplication.instance().quit()

            def closeEvent(self,e):
                _exit(0)

        config_operate_app=QApplication(argv)
        configOperateWindow=Window()
        config_operate_app.exec_()
        return configOperateWindow.mode
    
    mode=getWindow()

    if mode=="config":
        original_lines_number=lines_number
        original_columns_number=columns_number
        choose_seats_numbers()
        if lines_number==original_lines_number and columns_number==original_columns_number:
            original_seats=[[seats[i][j] for j in range(lines_number)]\
                for i in range(columns_number)]
            choose_blank_seats(mode="import")
            if original_seats==seats:set_change_mode(mode="import")
            else:set_change_mode(mode="new")
        else:
            choose_blank_seats(mode="new")
            set_change_mode(mode="new")
        get_name_file()
        
    elif mode=="visualise":
        random_arrange(visual=True)

    elif mode=="randomarrange":
        start_confirm()
        random_arrange(visual=False)

    config_operate()
    return

# 主函数
def main():
    global seats,seats_change_mode,already_get_lines_columns_number,lines_number,columns_number,students_name

    greet()
    mode=import_create_last()

    if mode=="import":
        successfully_imported=False
        while not successfully_imported:
            try:
                data_file_name=select_file("数据文件(*.rsd)") # ".rsd" 取自 random、seat、data 首字母
                if data_file_name=="": # 点了取消键
                    _exit(0)
                with open (data_file_name,mode="r",encoding="utf-8") as f:
                    flines=f.readlines()
                    columns_number=eval(flines[0])
                    lines_number=eval(flines[1])
                    seats=eval(flines[2])
                    seats_change_mode=eval(flines[3])
                    students_name=eval(flines[4])
                    
                test=seats[columns_number-1][lines_number-1]
                test=seats_change_mode[columns_number-1][lines_number-1]
                successfully_imported=True
                show_info("成功导入")
                config_operate()
            except Exception as e:
                show_error("导入时出现错误：\n"+str(e))

    elif mode=="new":
        choose_seats_numbers()
        if not already_get_lines_columns_number:
            _exit(0)
        seats=[["" for j in range(lines_number)] for i in range(columns_number)]
        seats_change_mode=[[(-1,0) for j in range(lines_number)] for i in range(columns_number)]
         # seats[x][y]: x为行号，y为列号，后门处为[0][0]
        choose_blank_seats()
        set_change_mode()
        get_name_file()
        start_confirm()
        random_arrange()

    elif mode=="last":
        try:
            with open (FileDir+"last_rsd.rsd",mode="r",encoding="utf-8") as f:
                flines=f.readlines()
                columns_number=eval(flines[0])
                lines_number=eval(flines[1])
                seats=eval(flines[2])
                seats_change_mode=eval(flines[3])
                students_name=eval(flines[4])
                test=seats[columns_number-1][lines_number-1]
                test=seats_change_mode[columns_number-1][lines_number-1]
                show_info("成功导入")
                config_operate()
        except Exception as e:
            show_error("导入时出现错误：\n"+str(e))
    return

if __name__=='__main__':
    main()