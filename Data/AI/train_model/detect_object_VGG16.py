from tkinter import *
from GUI_pre_model import *
import numpy as np
from PIL import  Image, ImageTk
from tkinter import filedialog as f_d # mo foder
import  cv2
import continuous_threading
link = r'C:\Users\A0G\Desktop\HA HA DHB\\'
wd = Tk('')# tao cua so
wd.title('Lua chon')#dat ten anh
wd.geometry('650x800')# tao khung anh
fr1= Frame(wd,width=319,height=239) # phan vung trong khung anh (kich thuoc rong x cao)
fr1.grid(row=0,column=0) # Vi tri vung o dong 0 cot 0
fr2= Frame(wd,width=319,height=239) # phan vung trong khung anh (kich thuoc rong x cao)
fr2.grid(row=1,column=0) # Vi tri vung o dong 0 cot 0
cap=cv2.VideoCapture(0)
def detect_cam():
    global path1
    # file = f_d.askopenfile()#chon foder
    # path1 = file.name

    ret, img = cap.read()  # ret : bien nhan biet cam co doc duoc khong , frame : bien anh doc tu cam
    if not ret:
        print('khong nhan duoc khung hinh')
    # img_predict=load_and_prep_image(cap)
    # img_predict=continuous_threa   nding.PeriodicThread(3,load_and_prep_image(img))
    # class_name_predict=predict(img_predict)
    # print(class_name_predict)

    img_rs = cv2.resize(img, (600, 600))  # quy chuan khich thuoc anh
    imgcv = cv2.cvtColor(img_rs, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    lb1.imgTK = imgTk
    lb1.config(image=imgTk)
    lb1.after(5, detect_cam)
    # img_predict=load_and_prep_image(img)
    # # img_predict=continuous_threading.PeriodicThread(3,load_and_prep_image(img))
    # class_name_predict=predict(img_predict)
    # print(class_name_predict)


    # canvas1.create_image(0, 0, anchor = NW, image=imgTk)
    # lb.config(text=class_name_predict, fg='green',font=("Arial,10,10"))
    canvas1.mainloop()

# def detect_img(img):
#     img_predict=load_and_prep_image(img)
#     img_predict=continuous_threading.PeriodicThread(3,load_and_prep_image(img))
#     class_name_predict=predict(img_predict)
#     print(class_name_predict)
def chonanh():
    global path1
    file = f_d.askopenfile()#chon foder
    path1 = file.name
    img = cv2.imread(path1)  # doc anh
    img_predict=load_and_prep_image(path1)
    class_name_predict=predict(img_predict)
    print(class_name_predict)
    img = cv2.resize(img, (600, 600))  # quy chuan khich thuoc anh
    imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas1.create_image(0, 0, anchor = NW, image=imgTk)
    lb2.config(text=class_name_predict, fg='green',font=("Arial,10,10"))
    canvas1.mainloop()

bt1 = Button(fr1, width=10, height=1, text='Chon Anh', command=chonanh)
#bt1.grid(row=0,column=0)#Chia rong va cot
bt1.grid(row=0,column=0)
bt2 = Button(fr1, width=10, height=1, text='Detect Camera', command=detect_cam)
bt2.grid(row=1,column=0)
canvas1 = Canvas(fr1,width=600,height=480)
canvas1.grid(row=2,column=0)
lb1=Label(fr1)
lb1.grid(row=2,column=0)
lb2 = Label(fr2,width=10)
lb2.grid(row=3,column=0)

wd.mainloop()