from prefix import *
from os import _exit

global lines_number,columns_number,seats,seats_change_mode,students_name,already_get_lines_columns_number
lines_number=columns_number=0
seats=seats_change_mode=students_name=[]
already_get_lines_columns_number=False

global data_file_name,name_file_name
data_file_name=name_file_name=""

# 判断test的位置
def IN(test,MIN,MAX):
    if test[0]>MIN[0] and test[0]<MAX[0] and test[1]>MIN[1] and test[1]<MAX[1]:
        return True
    else:
        return False

# 按小大排序
def chkmin(x:tuple,y:tuple):
    return (min(x[0],y[0]),min(x[1],y[1])),(max(x[0],y[0]),max(x[1],y[1]))

# 弹出提示
def show_info(event,title="提示"):
    tk=Tk()
    tk.wm_attributes('-topmost',1)
    tk.withdraw()
    tk.update() # 隐藏tkinter窗口，只显示提示窗口
    showinfo(title,event)
    tk.destroy()
    return
# 弹出错误
def show_error(event):
    tk=Tk()
    tk.wm_attributes('-topmost',1)
    tk.withdraw()
    tk.update() # 隐藏tkinter窗口，只显示提示窗口
    showerror('错误',event)
    tk.destroy()
    return
# 弹出选择是否
def ask_yes_no(event) -> bool:
    tk=Tk()
    tk.wm_attributes('-topmost',1)
    tk.withdraw()
    tk.update() # 隐藏tkinter窗口，只显示提示窗口
    yes_no=askyesno('提示',event)
    tk.destroy()
    return yes_no
# 弹出文件选择框
def select_file(file_mode): # file_mode 为包含n个元组的列表
    tk=Tk()
    tk.wm_attributes('-topmost',1)
    tk.withdraw()
    tk.update()
    file_name=askopenfilename(title="选择文件",
            filetypes=file_mode,initialdir=".\\")
    tk.destroy()
    return file_name
# 弹出另存文件界面
def ask_saveas_file_name(file_mode): # file_mode 为包含 n 个元组的数组
    tk=Tk()
    tk.wm_attributes('-topmost',1)
    tk.withdraw()
    tk.update()
    file_name=asksaveasfilename(title="导出为%s" %(file_mode[0][0]),
            filetypes=file_mode,initialdir=".\\")+file_mode[0][1]
    tk.destroy()
    return file_name

# 欢迎界面（没什么用）
def greet():
    # 初始化界面
    greet_surface=pygame.display.set_mode((500,200))
    pygame.display.set_caption("欢迎")
    greet_surface.fill(GRAY)
    LOADING_BLOCKS=[pygame.Rect(100+30*i,139,30,12) for i in range(10)]
    LOADING_BLOCKS=[""]+LOADING_BLOCKS

    for id in range(1,11):
        greet_surface.fill(GRAY)
        greet_word=FONT.render("欢迎使用随机座位v3.0",True,YELLOW) # 内容、抗锯齿、颜色
        greet_word_rect=greet_word.get_rect()
        greet_word_rect.center=(250,60)
        greet_surface.blit(greet_word,greet_word_rect)
        greet_word=VERY_LITTLE_FONT.render(f"加载中...{id}0%",True,YELLOW) # 内容、抗锯齿、颜色
        greet_word_rect=greet_word.get_rect()
        greet_word_rect.center=(250,120)
        greet_surface.blit(greet_word,greet_word_rect)
        loading_rect=pygame.Rect(95,135,310,20)
        pygame.draw.rect(greet_surface,YELLOW,loading_rect,3)
        for i in range(1,id):
            pygame.draw.rect(greet_surface,YELLOW,LOADING_BLOCKS[i])
        sleep(random()/2)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                _exit(0)
        pygame.display.update()
        fps_clock.tick(FPS)
    pygame.display.quit()

# 导入、新建
def import_create_last():
    # 初始化界面
    import_or_create_surface=pygame.display.set_mode((200,200))
    pygame.display.set_caption("导入/新建")

    # 布置界面（三个按钮）
    import_button=LITTLE_FONT.render("导入",True,WHITE)
    import_button_rect=import_button.get_rect()
    import_button_rect.center=(100,55)
    create_button=LITTLE_FONT.render("新建",True,WHITE)
    create_button_rect=create_button.get_rect()
    create_button_rect.center=(100,105)
    last_button=LITTLE_FONT.render("最近",True,WHITE)
    last_button_rect=last_button.get_rect()
    last_button_rect.center=(100,155)

    # 维持窗口
    while True:
        import_or_create_surface.fill(GRAY)
        import_or_create_surface.blit(import_button,import_button_rect)
        import_or_create_surface.blit(create_button,create_button_rect)
        import_or_create_surface.blit(last_button,last_button_rect)

        for event in pygame.event.get():
            # 退出
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)
            
            # 鼠标悬停
            if IN(pygame.mouse.get_pos(),import_button_rect.topleft,import_button_rect.bottomright):
                import_button=LITTLE_FONT.render("导入",True,YELLOW)
            else:
                import_button=LITTLE_FONT.render("导入",True,WHITE)
            if IN(pygame.mouse.get_pos(),create_button_rect.topleft,create_button_rect.bottomright):
                create_button=LITTLE_FONT.render("新建",True,YELLOW)
            else:
                create_button=LITTLE_FONT.render("新建",True,WHITE)
            if IN(pygame.mouse.get_pos(),last_button_rect.topleft,last_button_rect.bottomright):
                last_button=LITTLE_FONT.render("最近",True,YELLOW)
            else:
                last_button=LITTLE_FONT.render("最近",True,WHITE)
        
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                if IN(pygame.mouse.get_pos(),import_button_rect.topleft,import_button_rect.bottomright):
                    pygame.display.quit()
                    return "import"
                elif IN(pygame.mouse.get_pos(),create_button_rect.topleft,create_button_rect.bottomright):
                    pygame.display.quit()
                    return "new"
                elif IN(pygame.mouse.get_pos(),last_button_rect.topleft,last_button_rect.bottomright):
                    return "last"
        
        pygame.display.update()
        fps_clock.tick(FPS)

# 选择座位行列数
def choose_seats_numbers():
    global already_get_lines_columns_number
    already_get_lines_columns_number=False

    choose_seats_numbers_surface=Tk()
    choose_seats_numbers_surface.title("设置行列数")
    lines_frame=Frame(choose_seats_numbers_surface)
    # 行
    lines_frame.pack(fill="both")
    lines_label=Label(lines_frame,text="行数：",font=("",12))
    lines_label.pack(fill="both",side="left")
    lines_entry=Entry(lines_frame,font=("",12),)
    lines_entry.insert(0,lines_number)
    lines_entry.pack(fill="both",side="right")
    # 列
    columns_frame=Frame(choose_seats_numbers_surface)
    columns_frame.pack(fill="both")
    columns_label=Label(columns_frame,text="列数：",font=("",12))
    columns_label.pack(fill="both",side="left")
    columns_entry=Entry(columns_frame,font=("",12))
    columns_entry.insert(0,columns_number)
    columns_entry.pack(fill="both",side="right")
    # 确定按钮
    def get_seats_number():
        global lines_number,columns_number,already_get_lines_columns_number
        lines_number=lines_entry.get()
        columns_number=columns_entry.get()
        if lines_number.isdigit() and columns_number.isdigit() and \
                not int(lines_number)==0 and not int(columns_number)==0:
            lines_number=int(lines_number)
            columns_number=int(columns_number)
            choose_seats_numbers_surface.destroy()
            already_get_lines_columns_number=True
            return
        else:
            show_error("行和列必须是正整数")
            return
    
    confirm_button=Button(choose_seats_numbers_surface,text="确 定",
                        command=get_seats_number,font=("",12))
    confirm_button.pack(fill="both")

    choose_seats_numbers_surface.mainloop()
    return

# 选择“空”座位
def choose_blank_seats(mode="new"):
    global seats,seats_change_mode,lines_number,columns_number

    choose_blank_seats_surface=pygame.display.set_mode((100+45*columns_number,200+45*(lines_number-1)))
    pygame.display.set_caption("选择空座位")

    # 确认按钮
    
    confirm_button_word=LITTLE_FONT.render("确 定",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(50+45*columns_number/2,120+45*lines_number)

    """讲台在屏幕下方，窗户在屏幕右侧"""
    # 讲台
    stage_block=pygame.Rect(45*columns_number-85,50+45*lines_number,85,40)
    stage_word=VERY_LITTLE_FONT.render("讲 台",True,WHITE)
    stage_word_rect=stage_word.get_rect()
    stage_word_rect.center=(45*columns_number-42.5,70+45*lines_number)
    # 座位
    seats_blocks_rect=[[pygame.Rect(50+45*i,50+45*j,40,40)
             for j in range(lines_number)] for i in range(columns_number)]
    if mode=="new":
        seats_blocks_buf=[[False for j in range(lines_number)]
                for i in range(columns_number)]
    else:
        seats_blocks_buf=[[(False if not seats[i][j]=="$BLANK$" else True)
                 for j in range(lines_number)] for i in range(columns_number)]
    # buf 用来临时存储是否设置成了 blank, False 为不是 blank
    seats_blocks_color=[[DARK_GRAY for j in range(lines_number)]
             for i in range(columns_number)]

    # 综合 buf 与 color 判断 block 的颜色
    def get_block_color(x,y):
        if seats_blocks_buf[x][y]==True:
            return YELLOW
        else:
            return seats_blocks_color[x][y]

    while True:
        choose_blank_seats_surface.fill(GRAY)
        
        # 讲台
        pygame.draw.rect(choose_blank_seats_surface,DARK_GRAY,stage_block)
        choose_blank_seats_surface.blit(stage_word,stage_word_rect)
        # 确认按钮
        choose_blank_seats_surface.blit(confirm_button_word,confirm_button_word_rect)
        # 座位
        for x in range(columns_number):
            for y in range(lines_number):
                pygame.draw.rect(choose_blank_seats_surface,
                get_block_color(x,y),seats_blocks_rect[x][y])
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)

            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
                # 在确认按钮上
            if IN(mouse_pos,confirm_button_word_rect.topleft,confirm_button_word_rect.bottomright):
                confirm_button_word=LITTLE_FONT.render("确 定",True,YELLOW)
            else:
                confirm_button_word=LITTLE_FONT.render("确 定",True,WHITE)

                # 在座位上
                break_flag=False
                for x in range(columns_number):
                    for y in range(lines_number):
                        if IN(mouse_pos,seats_blocks_rect[x][y].topleft,
                                seats_blocks_rect[x][y].bottomright):
                            seats_blocks_color[x][y]=YELLOW
                            break_flag=True
                            break
                        else:
                            seats_blocks_color[x][y]=DARK_GRAY
                    if break_flag:
                        break
            
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                # 点击确认按钮
                if IN(mouse_pos,confirm_button_word_rect.topleft,confirm_button_word_rect.bottomright):
                    for x in range(columns_number):
                        for y in range(lines_number):
                            seats[x][y]="$BLANK$" if seats_blocks_buf[x][y] else ""
                            if seats_blocks_buf[x][y]:
                                seats_change_mode[x][y]=(-1,-1)
                    pygame.display.quit()
                    return
                
                # 点击座位
                elif IN(mouse_pos,seats_blocks_rect[0][0].topleft,
                    seats_blocks_rect[-1][-1].bottomright):
                    break_flag=False
                    for x in range(columns_number):
                        for y in range(lines_number):
                            if IN(mouse_pos,seats_blocks_rect[x][y].topleft,
                                    seats_blocks_rect[x][y].bottomright):
                                seats_blocks_buf[x][y]=not seats_blocks_buf[x][y]
                                # 可以取消点击
                                break_flag=True
                                break
                            else:
                                pass
                        if break_flag:
                            break
        
        pygame.display.update()
        fps_clock.tick(FPS)
    return

# 设置轮换规则
def set_change_mode(mode="new"):
    global seats,seats_change_mode,lines_number,columns_number

    set_change_mode_surface=pygame.display.set_mode((140+70*columns_number,170+35*lines_number))
    pygame.display.set_caption("设置轮换规则")

    change_cnt=0 # 可视化轮换方式
    pre_selected=pre_first_click=pst_first_click=False 
    # 用来判断是否选中了【轮换前】中的某些 blocks

    pre_first_block=pre_second_block=pst_first_block=pst_second_block=(-1,-1)
    # 用来存 pre 和 pst 中选中的对角 block (up)

    pre_seats_selected_buf=[[False for j in range(lines_number)] for i in range(columns_number)]
    # 用来存上一次（这一次？）选 pre 选了哪些 block

    
    seats_change_buf=[[(i,j) for j in range(lines_number)] for i in range(columns_number)]
    # 用来临时存轮换的方式，是 pst 的每个 block 在 pre 中是 (x,y)

    pre_seats_change_visualize_word=[[VERY_LITTLE_FONT.render("",True,WHITE) for j in range(lines_number)] for i in range(columns_number)]
    pre_seats_change_visualize_word_rect=[[pre_seats_change_visualize_word[i][j].get_rect()
            for j in range(lines_number)] for i in range(columns_number)]
    for i in range(columns_number):
        for j in range(lines_number):
            pre_seats_change_visualize_word_rect[i][j].center=(45+35*i,55+35*j)
    
    pst_seats_change_visualize_word=[[VERY_LITTLE_FONT.render("",True,WHITE) for j in range(lines_number)] for i in range(columns_number)]
    pst_seats_change_visualize_word_rect=[[pst_seats_change_visualize_word[i][j].get_rect()
            for j in range(lines_number)] for i in range(columns_number)]
    for i in range(columns_number):
        for j in range(lines_number):
            pst_seats_change_visualize_word_rect[i][j].center=(
                115+35*(columns_number+i),55+35*j)
    # 用来和 change_cnt 一起可视化轮换方式
    if mode=="import":
        for x in range(columns_number):
            for y in range(lines_number):
                if seats[x][y]=="$BLANK$":
                    continue
                else:
                    seats_change_buf[x][y]=seats_change_mode[x][y]
                    change_cnt+=1
                    pre_seats_change_visualize_word[seats_change_mode[x][y][0]][
                            seats_change_mode[x][y][1]]=VERY_LITTLE_FONT.render(
                                    str(change_cnt),True,WHITE)
                    pst_seats_change_visualize_word[x][y]=VERY_LITTLE_FONT.render(
                            str(change_cnt),True,WHITE)

    # 确定按钮
    confirm_button_word=LITTLE_FONT.render("确 定",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(70+35*columns_number,120+35*lines_number)

    """讲台在屏幕下方，窗户在屏幕右侧"""
    # 轮换前
    pre_reminder_word=VERY_LITTLE_FONT.render("轮换前",True,WHITE)
    pre_reminder_word_rect=pre_reminder_word.get_rect()
    pre_reminder_word_rect.center=(40,20)
    # 讲台
    pre_stage_block=pygame.Rect(35*columns_number-65,40+35*lines_number,65,30)
    pre_stage_word=VERY_LITTLE_FONT.render("讲 台",True,WHITE)
    pre_stage_word_rect=pre_stage_word.get_rect()
    pre_stage_word_rect.center=(35*columns_number-33,55+35*lines_number)
    # 座位
    pre_seats_blocks_rect=[[pygame.Rect(40+35*i,40+35*j,30,30)
             for j in range(lines_number)] for i in range(columns_number)]
    pre_seats_blocks_color=[[DARK_GRAY for j in range(lines_number)]
             for i in range(columns_number)]
    
    # 轮换后
    pst_reminder_word=VERY_LITTLE_FONT.render("轮换后",True,WHITE)
    pst_reminder_word_rect=pst_reminder_word.get_rect()
    pst_reminder_word_rect.center=(110+35*columns_number,20)
    # 讲台
    pst_stage_block=pygame.Rect(5+70*columns_number,40+35*lines_number,65,30)
    pst_stage_word=VERY_LITTLE_FONT.render("讲 台",True,WHITE)
    pst_stage_word_rect=pst_stage_word.get_rect()
    pst_stage_word_rect.center=(37+70*columns_number,55+35*lines_number)
    # 座位
    pst_seats_blocks_rect=[[pygame.Rect(110+35*(columns_number+i),40+35*j,30,30)
             for j in range(lines_number)] for i in range(columns_number)]
    pst_seats_blocks_color=[[DARK_GRAY for j in range(lines_number)]
             for i in range(columns_number)]

    # 获取 pre seats 的颜色
    def get_pre_seats_color(x,y):
        if pre_seats_selected_buf[x][y]:
            return YELLOW
        else:
            return pre_seats_blocks_color[x][y]

    while True:
        set_change_mode_surface.fill(GRAY)
        # 确定按钮
        set_change_mode_surface.blit(confirm_button_word,confirm_button_word_rect)
        # 轮换前
        set_change_mode_surface.blit(pre_reminder_word,pre_reminder_word_rect)
        # 讲台
        pygame.draw.rect(set_change_mode_surface,DARK_GRAY,pre_stage_block)
        set_change_mode_surface.blit(pre_stage_word,pre_stage_word_rect)
        # 座位
        for x in range(columns_number):
            for y in range(lines_number):
                if seats[x][y]=="$BLANK$":
                    continue
                pygame.draw.rect(set_change_mode_surface,get_pre_seats_color(x,y),
                        pre_seats_blocks_rect[x][y])
                set_change_mode_surface.blit(pre_seats_change_visualize_word[x][y],
                    pre_seats_change_visualize_word_rect[x][y])

        # 分割线
        pygame.draw.line(set_change_mode_surface,DARK_GRAY,
            (70+35*columns_number,10),(70+35*columns_number,70+35*lines_number))

        # 轮换后
        set_change_mode_surface.blit(pst_reminder_word,pst_reminder_word_rect)
        # 讲台
        pygame.draw.rect(set_change_mode_surface,DARK_GRAY,pst_stage_block)
        set_change_mode_surface.blit(pst_stage_word,pst_stage_word_rect)
        # 座位
        for x in range(columns_number):
            for y in range(lines_number):
                if seats[x][y]=="$BLANK$":
                    continue
                pygame.draw.rect(set_change_mode_surface,pst_seats_blocks_color[x][y],
                        pst_seats_blocks_rect[x][y])
                set_change_mode_surface.blit(pst_seats_change_visualize_word[x][y],
                    pst_seats_change_visualize_word_rect[x][y])
                
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)
            
            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
            # 在确定按钮上
            if IN(mouse_pos,confirm_button_word_rect.topleft,confirm_button_word_rect.bottomright):
                confirm_button_word=LITTLE_FONT.render("确 定",True,YELLOW)
            else:
                confirm_button_word=LITTLE_FONT.render("确 定",True,WHITE)
                # 在 pre 那边
                if mouse_pos[0]<70+35*columns_number:
                    # 选起点之前
                    if not pre_first_click:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pre_seats_blocks_rect[x][y].topleft,
                                        pre_seats_blocks_rect[x][y].bottomright):
                                    pre_seats_blocks_color[x][y]=YELLOW
                                    break_flag=True
                                    break
                                else:
                                    pre_seats_blocks_color[x][y]=DARK_GRAY
                            if break_flag:
                                break
                    # 选起点之后
                    else:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pre_seats_blocks_rect[x][y].topleft,
                                        pre_seats_blocks_rect[x][y].bottomright):
                                    for i in range(columns_number):
                                        for j in range(lines_number):
                                            if IN((i,j),
                                                    (min(x,pre_first_block[0])-1,min(y,pre_first_block[1])-1),
                                                    (max(x,pre_first_block[0])+1,max(y,pre_first_block[1])+1)
                                                    ):
                                                pre_seats_blocks_color[i][j]=YELLOW
                                            else:
                                                pre_seats_blocks_color[i][j]=DARK_GRAY
                                    break_flag=True
                                    break
                                else:
                                    pass
                            if break_flag:
                                break
                
                # 在 pst 那边
                # 只有选中 pre 后才能选 pst
                elif mouse_pos[0]>70+35*columns_number and pre_selected: 
                    # 选起点之前
                    if not pst_first_click:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pst_seats_blocks_rect[x][y].topleft,
                                        pst_seats_blocks_rect[x][y].bottomright):
                                    pst_seats_blocks_color[x][y]=YELLOW
                                    break_flag=True
                                    break
                                else:
                                    pst_seats_blocks_color[x][y]=DARK_GRAY
                            if break_flag:
                                break
                    # 选起点之后
                    else:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pst_seats_blocks_rect[x][y].topleft,
                                        pst_seats_blocks_rect[x][y].bottomright):
                                    for i in range(columns_number):
                                        for j in range(lines_number):
                                            if IN((i,j),
                                                    (min(x,pst_first_block[0])-1,min(y,pst_first_block[1])-1),
                                                    (max(x,pst_first_block[0])+1,max(y,pst_first_block[1])+1)
                                                    ):
                                                pst_seats_blocks_color[i][j]=YELLOW
                                            else:
                                                pst_seats_blocks_color[i][j]=DARK_GRAY
                                    break_flag=True
                                    break
                                else:
                                    pass
                            if break_flag:
                                break
            
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                # 确定按钮
                if IN(mouse_pos,confirm_button_word_rect.topleft,confirm_button_word_rect.bottomright):
                    for x in range(columns_number):
                        for y in range(lines_number):
                            if seats_change_mode[x][y]==(-1,-1):
                                continue
                            else:
                                seats_change_mode[x][y]=seats_change_buf[x][y]
                    pygame.display.quit()
                    return

                # pre
                elif mouse_pos[0]<70+35*columns_number:
                    # 选起点
                    if not pre_first_click:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pre_seats_blocks_rect[x][y].topleft,
                                        pre_seats_blocks_rect[x][y].bottomright):
                                    pre_first_click=True
                                    pre_first_block=(x,y)
                                    break_flag=True
                                    break
                                else:
                                    pass
                            if break_flag:
                                break
                    # 选终点
                    else:
                        break_flag=False

                        # 检查所选区域是否合法
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pre_seats_blocks_rect[x][y].topleft,
                                    pre_seats_blocks_rect[x][y].bottomright):
                                    pre_first_click=False
                                    pre_second_block=(x,y)
                                    pre_first_block,pre_second_block=chkmin(pre_first_block,pre_second_block)
                                    break_flag=True
                                    break
                            if break_flag:
                                break
                        break_flag=False
                        unaccepted=False
                        for x in range(pre_first_block[0],pre_second_block[0]+1):
                            for y in range(pre_first_block[1],pre_second_block[1]+1):
                                if seats[x][y]=="$BLANK$":
                                    break_flag=unaccepted=True
                                    break
                            if break_flag:
                                break
                        # 不合法
                        if unaccepted:
                            pre_first_block=pre_second_block=(-1,-1)
                            show_error("轮换时不得包含空座位")
                        # 合法
                        else:
                            break_flag=False
                            for x in range(columns_number):
                                for y in range(lines_number):
                                    if IN(mouse_pos,pre_seats_blocks_rect[x][y].topleft,
                                        pre_seats_blocks_rect[x][y].bottomright):
                                        pre_selected=True
                                        break_flag=True
                                        for i in range(pre_first_block[0],pre_second_block[0]+1):
                                            for j in range(pre_first_block[1],pre_second_block[1]+1):
                                                pre_seats_selected_buf[i][j]=True
                                    else:
                                        pass
                                if break_flag:
                                    break
                
                # pst
                elif mouse_pos[0]>70+35*columns_number and pre_selected:
                    # 选起点
                    if not pst_first_click:
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pst_seats_blocks_rect[x][y].topleft,
                                        pst_seats_blocks_rect[x][y].bottomright):
                                    break_flag=True
                                    pst_first_click=True
                                    pst_first_block=(x,y)
                                    break
                                else:
                                    pass
                            if break_flag:
                                break
                    # 选终点
                    else:
                        break_flag=False
                        # 检查选的两个范围是否合法
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,pst_seats_blocks_rect[x][y].topleft,
                                    pst_seats_blocks_rect[x][y].bottomright):
                                    pst_second_block=(x,y)
                                    break_flag=True
                                    break
                            if break_flag:
                                break
                        pst_first_block,pst_second_block=chkmin(pst_first_block,pst_second_block)
                        break_flag=unaccepted=False
                        for x in range(pst_first_block[0],pst_second_block[0]+1):
                            for y in range(pst_first_block[1],pst_second_block[1]+1):
                                if seats[x][y]=="$BLANK$":
                                    break_flag=unaccepted=True
                                    break
                            if break_flag:
                                break
                        # 不合法
                        if unaccepted:
                            pst_first_click=False
                            pst_first_block=(-1,-1)
                            show_error("轮换时不得包含空座位")
                        elif not pre_second_block[0]-pre_first_block[0]==pst_second_block[0]-pst_first_block[0] or not pre_second_block[1]-pre_first_block[1]==pst_second_block[1]-pst_first_block[1]:
                            pst_first_click=False
                            pst_first_block=(-1,-1)
                            show_error("二者选择的范围必须一样")
                        # 合法    
                        else:
                            break_flag=False
                            for x in range(columns_number):
                                for y in range(lines_number):
                                    if IN(mouse_pos,pst_seats_blocks_rect[x][y].topleft,
                                        pst_seats_blocks_rect[x][y].bottomright):
                                        pst_first_click=False
                                        pre_selected=False
                                        break_flag=True
                                        # 存储
                                        dx=pst_first_block[0]-pre_first_block[0]
                                        dy=pst_first_block[1]-pre_first_block[1]
                                        for i in range(pst_first_block[0],pst_second_block[0]+1):
                                            for j in range(pst_first_block[1],pst_second_block[1]+1):
                                                seats_change_buf[i][j]=(i-dx,j-dy)
                                                pst_seats_blocks_color[i][j]=DARK_GRAY
                                                change_cnt+=1
                                                # 用数字进行可视化
                                                pre_seats_change_visualize_word[i-dx][j-dy]=VERY_LITTLE_FONT.render(
                                                    str(change_cnt),True,WHITE)
                                                pre_seats_selected_buf[i-dx][j-dy]=False
                                                pst_seats_change_visualize_word[i][j]=VERY_LITTLE_FONT.render(
                                                    str(change_cnt),True,WHITE)
                                                
                                        break
                                    else:
                                        pass
                                if break_flag:
                                    break

        pygame.display.update()
        fps_clock.tick(FPS)
    return

# 选择姓名文件
def get_name_file():
    global name_file_name,students_name,seats
    get_name_file_surface=pygame.display.set_mode((400,200))
    pygame.display.set_caption("选择姓名文件")
    # 查看当前学生姓名
    recent_students_name=VERY_LITTLE_FONT.render("当前学生姓名",True,WHITE)
    recent_students_name_rect=recent_students_name.get_rect()
    recent_students_name_rect.center=(200,40)
    # 选择文件按钮
    select_button_word=VERY_LITTLE_FONT.render("选择姓名文件",True,WHITE)
    select_button_word_rect=select_button_word.get_rect()
    select_button_word_rect.center=(200,80)
    # 使用上次文件
    last_file_button_word=VERY_LITTLE_FONT.render("使用上次配置",True,WHITE)
    last_file_button_word_rect=last_file_button_word.get_rect()
    last_file_button_word_rect.center=(200,120)
    # 确定按钮
    confirm_button_word=VERY_LITTLE_FONT.render("确定",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(200,160)

    # 获取学生姓名列表并检查合法性
    def get_students_name_check() -> bool:
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
        if not seats_cnt==len(students_name):
            show_error("座位数必须与学生人数相等")
            return False
        show_info("成功")
        return True

    while True:
        get_name_file_surface.fill(GRAY)
        # 四个按钮
        get_name_file_surface.blit(recent_students_name,recent_students_name_rect)
        get_name_file_surface.blit(select_button_word,select_button_word_rect)
        get_name_file_surface.blit(last_file_button_word,last_file_button_word_rect)
        get_name_file_surface.blit(confirm_button_word,confirm_button_word_rect)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)
            
            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
            if IN(mouse_pos,select_button_word_rect.topleft,
                    select_button_word_rect.bottomright):
                    select_button_word=VERY_LITTLE_FONT.render("选择姓名文件",True,YELLOW)
            else:
                select_button_word=VERY_LITTLE_FONT.render("选择姓名文件",True,WHITE)
            if IN(mouse_pos,last_file_button_word_rect.topleft,
                    last_file_button_word_rect.bottomright):
                last_file_button_word=VERY_LITTLE_FONT.render("使用上次配置",True,YELLOW)
            else:
                last_file_button_word=VERY_LITTLE_FONT.render("使用上次配置",True,WHITE)
            if IN(mouse_pos,confirm_button_word_rect.topleft,
                    confirm_button_word_rect.bottomright):
                    confirm_button_word=VERY_LITTLE_FONT.render("确定",True,YELLOW)
            else:
                confirm_button_word=VERY_LITTLE_FONT.render("确定",True,WHITE)
            if IN(mouse_pos,recent_students_name_rect.topleft,
                    recent_students_name_rect.bottomright):
                recent_students_name=VERY_LITTLE_FONT.render("当前学生姓名",True,YELLOW)
            else:
                recent_students_name=VERY_LITTLE_FONT.render("当前学生姓名",True,WHITE)
            
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                # 查看当前学生姓名
                if IN(mouse_pos,recent_students_name_rect.topleft,
                        recent_students_name_rect.bottomright):
                    show_info(students_name if not students_name==[] else "空","查看")
                # 选择姓名文件
                if IN(mouse_pos,select_button_word_rect.topleft,
                    select_button_word_rect.bottomright):
                    name_file_name=select_file([("All","*.*")])
                    if name_file_name=="":
                        continue
                    with open (name_file_name,mode="r",encoding="utf-8") as f:
                        students_name=f.readlines()
                    get_students_name_check()  
                    
                # 使用上次配置
                elif IN(mouse_pos,last_file_button_word_rect.topleft,
                        last_file_button_word_rect.bottomright):
                    if isfile(".\\files\\last_name_file"):
                        with open(".\\files\\last_name_file",mode="r",encoding="utf-8") as f:
                            students_name=eval(f.readline())
                            get_students_name_check()
                    else:
                        show_info("不存在上次配置")
            
                elif IN(mouse_pos,confirm_button_word_rect.topleft,
                        confirm_button_word_rect.bottomright):
                    if not isdir(".\\files\\"):
                        system("mkdir .\\files\\")
                    with open (".\\files\\last_name_file",mode="w",encoding="utf-8") as f:
                        f.write(str(students_name))
                    
                    pygame.display.quit()
                    return

        pygame.display.update()
        fps_clock.tick(FPS)
    return

# 开始排列前确认
def start_confirm():
    start_confirm_surface=pygame.display.set_mode((150,150))
    pygame.display.set_caption("开始？")

    confirm_button_word=LITTLE_FONT.render("开始",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(75,75)

    while True:
        start_confirm_surface.fill(GRAY)
        start_confirm_surface.blit(confirm_button_word,confirm_button_word_rect)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)
            
            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
            if IN(mouse_pos,confirm_button_word_rect.topleft,
                    confirm_button_word_rect.bottomright):
                confirm_button_word=LITTLE_FONT.render("开始",True,YELLOW)
            else:
                confirm_button_word=LITTLE_FONT.render("开始",True,WHITE)
            
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                if IN(mouse_pos,confirm_button_word_rect.topleft,
                    confirm_button_word_rect.bottomright):
                    pygame.display.quit()
                    return
        pygame.display.update()
        fps_clock.tick(FPS)
    return

# 随机排列
def random_arrange(visual=False) -> bool:
    global lines_number,columns_number,seats,students_name,seats_change_mode
    random_arrange_surface=pygame.display.set_mode((100+75*columns_number,200+45*lines_number))
    pygame.display.set_caption("随机排列")

    # 随机排列后端
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
    
    # 此处加入手动调换座位功能
    handly_change_seat_first=(-1,-1)

    # 前端
    seats_word=[[VERY_LITTLE_FONT.render(seats[i][j],True,WHITE)
             for j in range(lines_number)] for i in range(columns_number)]
    seats_word_rect=[[seats_word[i][j].get_rect()
             for j in range(lines_number)] for i in range(columns_number)]
    for i in range(columns_number):
        for j in range(lines_number):
            seats_word_rect[i][j].center=(85+75*i,70+45*j)
    seats_blocks=[[pygame.Rect(50+75*i,50+45*j,70,40)
             for j in range(lines_number)] for i in range(columns_number)]
    stage_word=VERY_LITTLE_FONT.render("讲 台",True,WHITE)
    stage_word_rect=stage_word.get_rect()
    stage_word_rect.center=(47.5+75*(columns_number-2),70+45*lines_number)
    stage_block=pygame.Rect(-25+75*(columns_number-2),50+45*lines_number,145,40)

    # 功能性按钮
    save_rsd_button_word=VERY_LITTLE_FONT.render("导出(.rsd)",True,WHITE)
    save_rsd_button_word_rect=save_rsd_button_word.get_rect()
    save_rsd_button_word_rect.center=(60+45*columns_number,45*lines_number+150)
    save_rsd_query_word=EXTREME_LITTLE_FONT.render("？",True,WHITE)
    save_rsd_query_word_rect=save_rsd_query_word.get_rect()
    save_rsd_query_word_rect.center=(120+45*columns_number,45*lines_number+140)
    save_rsd_query_circle_color=WHITE

    save_txt_button_word=VERY_LITTLE_FONT.render("导出(.txt)",True,WHITE)
    save_txt_button_word_rect=save_txt_button_word.get_rect()
    save_txt_button_word_rect.center=(40+30*columns_number,45*lines_number+150)

    change_seats_button_word=VERY_LITTLE_FONT.render("轮换",True,WHITE)
    change_seats_button_word_rect=change_seats_button_word.get_rect()
    change_seats_button_word_rect.center=(20+15*columns_number,45*lines_number+150)

    confirm_button_word=VERY_LITTLE_FONT.render("确定",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(80+60*columns_number,45*lines_number+150)

    visual=visual
    save_last=False # 用来标记是否已经自动保存最近一次的数据
    cntt=0
    while True:
        random_arrange_surface.fill(GRAY)
        # 显示
        if not visual:
            pygame.draw.rect(random_arrange_surface,DARK_GRAY,stage_block)
            random_arrange_surface.blit(stage_word,stage_word_rect)
            for x in range(columns_number):
                for y in range(lines_number):
                    if seats[x][y]=="$BLANK$":
                        continue
                    pygame.draw.rect(random_arrange_surface,DARK_GRAY,seats_blocks[x][y])
                    random_arrange_surface.blit(seats_word[x][y],seats_word_rect[x][y])

                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.display.quit()
                            _exit(0)

                    pygame.display.update()
                    fps_clock.tick(3)
            visual=True
        # 维持
        else:
            # 自动保存最近一次的数据
            if not save_last:
                if not isdir(".\\files\\"):
                    system("mkdir .\\files\\")
                with open (".\\files\\last_rsd.rsd",mode="w",encoding="utf-8") as f:
                        f.write(str(columns_number)+"\n"+str(lines_number)+"\n"+str(seats)+"\n"+\
                                str(seats_change_mode)+"\n"+str(students_name))
                save_last=True

            # 座位
            pygame.draw.rect(random_arrange_surface,DARK_GRAY,stage_block)
            random_arrange_surface.blit(stage_word,stage_word_rect)
            for x in range(columns_number):
                for y in range(lines_number):
                    if x==handly_change_seat_first[0] and y==handly_change_seat_first[1]:
                        seats_word[x][y]=VERY_LITTLE_FONT.render(seats[x][y],True,YELLOW)
                    seats_word_rect[x][y]=seats_word[x][y].get_rect()
                    seats_word_rect[x][y].center=(85+75*x,70+45*y)

                    if seats[x][y]=="$BLANK$":
                        continue
                    pygame.draw.rect(random_arrange_surface,DARK_GRAY,seats_blocks[x][y])
                    random_arrange_surface.blit(seats_word[x][y],seats_word_rect[x][y])
            
            # 按钮
            random_arrange_surface.blit(save_rsd_button_word,save_rsd_button_word_rect)
            random_arrange_surface.blit(save_txt_button_word,save_txt_button_word_rect)
            random_arrange_surface.blit(change_seats_button_word,change_seats_button_word_rect)
            random_arrange_surface.blit(save_rsd_query_word,save_rsd_query_word_rect)
            random_arrange_surface.blit(confirm_button_word,confirm_button_word_rect)
            pygame.draw.circle(random_arrange_surface,save_rsd_query_circle_color,
                    (118+45*columns_number,45*lines_number+140),8,1)

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.display.quit()
                    _exit(0)

                # 鼠标悬停
                mouse_pos=pygame.mouse.get_pos()
                if IN(mouse_pos,save_rsd_button_word_rect.topleft,
                        save_rsd_button_word_rect.bottomright):
                    save_rsd_button_word=VERY_LITTLE_FONT.render("导出(.rsd)",True,YELLOW)
                else:
                    save_rsd_button_word=VERY_LITTLE_FONT.render("导出(.rsd)",True,WHITE)
                if IN(mouse_pos,save_txt_button_word_rect.topleft,
                        save_txt_button_word_rect.bottomright):
                    save_txt_button_word=VERY_LITTLE_FONT.render("导出(.txt)",True,YELLOW)
                else:
                    save_txt_button_word=VERY_LITTLE_FONT.render("导出(.txt)",True,WHITE)
                if IN(mouse_pos,change_seats_button_word_rect.topleft,
                        change_seats_button_word_rect.bottomright):
                    change_seats_button_word=VERY_LITTLE_FONT.render("轮换",True,YELLOW)
                else:
                    change_seats_button_word=VERY_LITTLE_FONT.render("轮换",True,WHITE)
                if IN(mouse_pos,save_rsd_query_word_rect.topleft,
                        save_rsd_query_word_rect.bottomright):
                    save_rsd_query_word=EXTREME_LITTLE_FONT.render("？",True,YELLOW)
                    save_rsd_query_circle_color=YELLOW
                else:
                    save_rsd_query_word=EXTREME_LITTLE_FONT.render("？",True,WHITE)
                    save_rsd_query_circle_color=WHITE
                if IN(mouse_pos,confirm_button_word_rect.topleft,
                        confirm_button_word_rect.bottomright):
                    confirm_button_word=VERY_LITTLE_FONT.render("确认",True,YELLOW)
                else:
                    confirm_button_word=VERY_LITTLE_FONT.render("确认",True,WHITE)
                # 在座位上
                for x in range(columns_number):
                    for y in range(lines_number):
                        if IN(mouse_pos,seats_blocks[x][y].topleft,
                                seats_blocks[x][y].bottomright):
                            seats_word[x][y]=VERY_LITTLE_FONT.render(seats[x][y],True,YELLOW)
                        else:
                            seats_word[x][y]=VERY_LITTLE_FONT.render(seats[x][y],True,WHITE)

                # 鼠标点击
                if event.type==MOUSEBUTTONUP:
                    if IN(mouse_pos,save_rsd_query_word_rect.topleft,
                            save_rsd_query_word_rect.bottomright):
                        show_info(".rsd格式是本程序专用数据格式，\n可导入到程序内以设置相关参数")
                    # 导出.rsd
                    elif IN(mouse_pos,save_rsd_button_word_rect.topleft,
                            save_rsd_button_word_rect.bottomright):
                        saveas_file_name=ask_saveas_file_name([("数据文件",".rsd")])
                        if saveas_file_name==".rsd":
                            continue
                        with open (saveas_file_name,mode="w",encoding="utf-8") as f:
                            f.write(str(columns_number)+"\n"+str(lines_number)+"\n"+str(seats)+"\n"+\
                                    str(seats_change_mode)+"\n"+str(students_name))
                        show_info("导出成功")
                    # 导出.txt
                    elif IN(mouse_pos,save_txt_button_word_rect.topleft,
                            save_txt_button_word_rect.bottomright):
                        saveas_file_name=ask_saveas_file_name([("文本文件",".txt")])
                        if saveas_file_name==".txt":
                            continue
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
                        show_info("导出成功")

                    # 轮换座位
                    elif IN(mouse_pos,change_seats_button_word_rect.topleft,
                            change_seats_button_word_rect.bottomright):
                        new_seats=[["" for j in range(lines_number)] for i in range(columns_number)]
                        for x in range(columns_number):
                            for y in range(lines_number):
                                new_seats[x][y]=seats[seats_change_mode[x][y][0]][
                                    seats_change_mode[x][y][1]] if not seats[seats_change_mode[x][y][0]
                                        ][seats_change_mode[x][y][1]]=="$BLANK$" else "$BLANK$"
                                
                        seats=new_seats
                        for x in range(columns_number):
                            for y in range(lines_number):
                                seats_word[x][y]=VERY_LITTLE_FONT.render(seats[x][y],True,WHITE)
                        save_last=False
                        handly_change_seat_first=(-1,-1) # 防止出现 bug
                    
                    # 在座位上
                    elif IN(mouse_pos,seats_blocks[0][0].topleft,
                        seats_blocks[columns_number-1][lines_number-1].bottomright):
                        break_flag=False
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if IN(mouse_pos,seats_blocks[x][y].topleft,
                                        seats_blocks[x][y].bottomright):
                                    break_flag=True
                                    if handly_change_seat_first==(-1,-1):
                                        handly_change_seat_first=(x,y)
                                    else:
                                        handly_change_seat_tmp=seats[x][y]
                                        seats[x][y]=seats[handly_change_seat_first[0]]\
                                            [handly_change_seat_first[1]]
                                        seats[handly_change_seat_first[0]]\
                                            [handly_change_seat_first[1]]=handly_change_seat_tmp
                                        seats_word[x][y]=VERY_LITTLE_FONT.render(seats[x][y],True,WHITE)
                                        seats_word[handly_change_seat_first[0]][handly_change_seat_first[1]]= \
                                            VERY_LITTLE_FONT.render(seats[handly_change_seat_first[0]] \
                                                [handly_change_seat_first[1]],True,WHITE)
                                        handly_change_seat_first=(-1,-1)
                                        save_last=False
                            if break_flag:
                                break
                                    
                    
                    # 确认
                    elif IN(mouse_pos,confirm_button_word_rect.topleft,
                            confirm_button_word_rect.bottomright):
                        pygame.display.quit()
                        return

        pygame.display.update()
        fps_clock.tick(LOW_FPS)
    return

# 导入后进行修改或进一步操作
def config_operate():
    global seats_change_mode,seats,columns_number,lines_number
    config_operate_surface=pygame.display.set_mode((200,200))
    pygame.display.set_caption("修改/操作")

    # 修改配置
    config_button_word=VERY_LITTLE_FONT.render("修改/查看配置",True,WHITE)
    config_button_word_rect=config_button_word.get_rect()
    config_button_word_rect.center=(100,50)
    # 查看座位表并进行进一步操作
    operate_button_word=VERY_LITTLE_FONT.render("显示座位表",True,WHITE)
    operate_button_word_rect=operate_button_word.get_rect()
    operate_button_word_rect.center=(100,100)
    # 直接随机排座位
    random_arrange_button_word=VERY_LITTLE_FONT.render("随机排座位",True,WHITE)
    random_arrange_button_word_rect=random_arrange_button_word.get_rect()
    random_arrange_button_word_rect.center=(100,150)
    
    CLICK:bool=False

    while True:
        config_operate_surface.fill(GRAY)
        config_operate_surface.blit(config_button_word,config_button_word_rect)
        config_operate_surface.blit(operate_button_word,operate_button_word_rect)
        config_operate_surface.blit(random_arrange_button_word,random_arrange_button_word_rect)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)

            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
            if IN(mouse_pos,config_button_word_rect.topleft,
                    config_button_word_rect.bottomright):
                config_button_word=VERY_LITTLE_FONT.render("修改/查看配置",True,YELLOW)
            else:
                config_button_word=VERY_LITTLE_FONT.render("修改/查看配置",True,WHITE)
            if IN(mouse_pos,operate_button_word_rect.topleft,
                    operate_button_word_rect.bottomright):
                operate_button_word=VERY_LITTLE_FONT.render("显示座位表",True,YELLOW)
            else:
                operate_button_word=VERY_LITTLE_FONT.render("显示座位表",True,WHITE)
            if IN(mouse_pos,random_arrange_button_word_rect.topleft,
                    random_arrange_button_word_rect.bottomright):
                random_arrange_button_word=VERY_LITTLE_FONT.render("随机排座位",True,YELLOW)
            else:
                random_arrange_button_word=VERY_LITTLE_FONT.render("随机排座位",True,WHITE)

            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                if IN(mouse_pos,config_button_word_rect.topleft,
                    config_button_word_rect.bottomright):
                    CLICK=True
                    original_columns_number=columns_number
                    original_lines_number=lines_number
                    choose_seats_numbers()
                    if original_columns_number==columns_number and original_lines_number==lines_number:
                        original_seats=[[seats[i][j] for j in range(lines_number)] 
                                for i in range(columns_number)]
                        is_same:bool=True
                        choose_blank_seats(mode="import")
                        for x in range(columns_number):
                            for y in range(lines_number):
                                if seats[x][y]=="$BLANK$" and not original_seats[x][y]=="$BLANK$" \
                                    or not seats[x][y]=="$BLANK$" and original_seats[x][y]=="$BLANK$":
                                    is_same=False
                        
                        if is_same:
                            seats=original_seats
                        if original_seats==seats:
                            set_change_mode(mode="import")
                        else:
                            set_change_mode(mode="new")
                    else:
                        choose_blank_seats(mode="new")
                        set_change_mode(mode="new")
                    get_name_file()
                    
                    
                elif IN(mouse_pos,operate_button_word_rect.topleft,
                    operate_button_word_rect.bottomright):
                    CLICK=True
                    random_arrange(visual=True)

                elif IN(mouse_pos,random_arrange_button_word_rect.topleft,
                        random_arrange_button_word_rect.bottomright):
                    CLICK=True
                    start_confirm()
                    random_arrange(visual=False)
        
        if not CLICK:
            pygame.display.update()
            fps_clock.tick(FPS)
        else:
            break
    config_operate()
    return
        

def main():
    global data_file_name,seats,seats_change_mode,already_get_lines_columns_number,lines_number,columns_number,students_name

    greet()
    sleep(0.2)
    mode=import_create_last()

    if mode=="import":
        successfully_imported=False
        while not successfully_imported:
            try:
                data_file_name=select_file([("数据文件","*.rsd")]) # ".rsd" 取自 random、seat、data 首字母
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
            except Exception as e:
                show_error("导入时出现错误：\n"+str(e))
        config_operate()

    elif mode=="new":
        choose_seats_numbers()
        if not already_get_lines_columns_number:
            _exit(0)
        seats=[["" for j in range(lines_number)] for i in range(columns_number)]
        seats_change_mode=[[(0,0) for j in range(lines_number)] for i in range(columns_number)]
         # seats[x][y]: x为行号，y为列号，后门处为[0][0]
        choose_blank_seats()
        set_change_mode()
        get_name_file()
        start_confirm()
        random_arrange()

    elif mode=="last":
        if not isfile(".\\files\\last_rsd.rsd"):
            show_error("找不到最近一次的资料")
        else:
            try:
                with open (".\\files\\last_rsd.rsd",mode="r",encoding="utf-8") as f:
                    flines=f.readlines()
                    columns_number=eval(flines[0])
                    lines_number=eval(flines[1])
                    seats=eval(flines[2])
                    seats_change_mode=eval(flines[3])
                    students_name=eval(flines[4])
                    test=seats[columns_number-1][lines_number-1]
                    test=seats_change_mode[columns_number-1][lines_number-1]
                    show_info("成功导入")
            except Exception as e:
                show_error("导入时出现错误：\n"+str(e))
            config_operate()

if __name__=='__main__':
    main()