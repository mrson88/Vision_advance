import threading
import time
import cv2
from tkinter import *
from tkinter import filedialog as f_dialog # lien quan thu muc
import numpy as np
from PIL import Image, ImageTk
import  continuous_threading
import matplotlib.pyplot as plt
import time
import serial

global out
global x
global y

out = ''
# ket noi COM
ser = serial.Serial(
    port = 'COM3',
    baudrate= 115200,
    # parity=serial.PARITY_ODD,
    # stopbits=serial.STOPBITS_TWO,
    # bytesize=serial.SEVENBITS
)
if ser.isOpen():
    print('Cong com da duoc mo')

cap = cv2.VideoCapture(1)
if  cap.isOpened():
    print('nhan dien duoc CAM')




window = Tk()
window.title('VIDEO MRBAT')
window.geometry('810x800') # tao khung anh



frame1 = Frame(window,width=400,height=300)
frame1.grid(row=0,column=0)

frame2 = Frame(window,width=400,height=300)
frame2.grid(row=1,column=0)

frame3 = Frame(window,width=810,height=200)
frame3.grid(row=2,column=0)

label1 = Label(frame2, width=10, height=3, fg='blue', font=('Timenewroman', 14, 'bold'))
label1.grid(row=1,column=0)

label1.config(text=out)

# Tao vung dang nhap
lbx=Label(frame3,text="Toa do X")
lbx.grid(column=0,row=0)

lby=Label(frame3,text="Toa do Y")
lby.grid(column=0,row=1)

txtx=Entry(frame3,width=10)
txtx.grid(column=1,row=0)

txty=Entry(frame3,width=10)
txty.grid(column=1,row=1)

txtx.focus()
txty.focus()
# ket thuc vung dang nhap

def Luutoado():
    global x,y
    x = txtx.get()
    y = txty.get()
    print(x)
    print(y)
    thongbao.insert(INSERT, 'Luu thanh cong')
    thongbao.configure(fg='green')
# an luu toa do
bt=Button(frame3,text="Luu lai",bg='green', command= Luutoado)
bt.grid(column=0,row=2)
thongbao=Text(frame3,height=1,width=20)
thongbao.grid(column=1,row=2)

def takeimg():
    # global  path
    # vision_basic = f_dialog.askopenfile()
    # path = vision_basic.name
    # img = cv2.imread(path)
    while True:
        ret, img = cap.read()  # lay anh chup
        img = cv2.resize(img,(400,250))


        imgCV = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
        img1 = Image.fromarray(imgCV)  # tao mang de chuyen anh
        imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

        # plt.figure('anh nguon')
        # plt.imshow(img)
        # plt.show()
        # canvas1.create_image(0, 0, anchor=NW, image=imgTK)
        # canvas1.mainloop()

        # label4.config(image=imgTK)
        # label4.after(10,imgTK)


def Checking():
    global path
    global x,y
    print(x)
    print(y)
    # vung dan tem
    x1 = int(x) - 35
    y1 = int(y) - 35
    x2 = int(x) + 35
    y2 = int(y) - 2

    # vung khong dan tem
    xf1 = int(x) - 35
    yf1 = int(y) + 35
    xf2 = int(x) + 35
    yf2 = int(y) + 5



    # img = cv2.imread(path) # test
    ret, img = cap.read() # lay anh chup
    img= cv2.resize(img,(400,250))

    img_copy = img.copy()
    # model 1
    # img_src = img[125:160,280:350] # model 1
    # # img_src = img[160:195, 280:350]
    # img_ss = img_copy[160:195,280:350] # model 1

    #model 2
    img_src = img[y1:y2, x1:x2]  # model 1
    # img_src = img[180:216, 280:350]
    img_ss = img_copy[yf2:yf1, xf1:xf2]  # model 1

    # cv2.imshow('da lb',img_src)
    # cv2.imshow('front',img_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    img_src = cv2.resize(img_src, (400, 250))
    img_ss = cv2.resize(img_ss, (400, 250))




    img_check = cv2.subtract(img_src,img_ss,mask=None)
    img_check = cv2.resize(img_check,(400,250))
    img_check= cv2.cvtColor(img_check,cv2.COLOR_BGR2GRAY)
    img_check = cv2.threshold(img_check,5,255,cv2.THRESH_BINARY)[1]
    # img_check = cv2.bitwise_not(img_check)

    Contours, Contour_thresh = cv2.findContours(img_check, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    Contour_thresh_coppy = img_copy.copy()
    Contour_thresh_coppy = cv2.resize(Contour_thresh_coppy, (400, 250))

    # phat hien blobs
    # params = cv2.SimpleBlobDetector_Params()
    # params.filterByArea = True
    # params.minArea = 60
    # params.maxArea = 15000
    # params.filterByCircularity = True
    # params.minCircularity = 0.001
    # params.filterByConvexity = True
    # params.minConvexity = 0.01
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01
    # detector = cv2.SimpleBlobDetector_create(params)
    # keypoints = detector.detect(img_check)
    # blanks = np.zeros((1, 1))
    # blobs = cv2.drawKeypoints(img_check, keypoints, blanks, (255, 0, 0), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
    # print(f'len keypoints : {len(keypoints)} ')
    # if len(keypoints) > 0:
    #     cv2.putText(Contour_thresh_coppy, 'OK - DA DAN TEM ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    #     ser.write(b'OK')
    #
    # else:
    #     cv2.putText(Contour_thresh_coppy, 'NG -  CHUA DAN TEM ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    #     ser.write(b'NG')

    for contour in Contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 30000:
            print('Da Dan Tem')
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            count = len(approx)
            cv2.drawContours(Contour_thresh_coppy, contour, -1, (0, 255, 0), 1, cv2.LINE_4)
            M = cv2.moments(contour)
            # print(M)
            # tinh toan tam
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(Contour_thresh_coppy, 'OK - DA DAN TEM ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            break
        elif area >100000:
            print('Chua dan tem')
            cv2.putText(Contour_thresh_coppy, 'NG -  CHUA DAN TEM ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)




    imgCV1 = cv2.cvtColor(img_src, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img1 = Image.fromarray(imgCV1)  # tao mang de chuyen anh
    imgTK1 = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    imgCV2 = cv2.cvtColor(img_ss, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img2 = Image.fromarray(imgCV2)  # tao mang de chuyen anh
    imgTK2 = ImageTk.PhotoImage(img2)  # chuyen anh tu cv2 sang tkiner

    imgCV3 = cv2.cvtColor(Contour_thresh_coppy, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img3 = Image.fromarray(imgCV3)  # tao mang de chuyen anh
    imgTK3 = ImageTk.PhotoImage(img3)  # chuyen anh tu cv2 sang tkiner

    imgCV4 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img4 = Image.fromarray(imgCV4)  # tao mang de chuyen anh
    imgTK4 = ImageTk.PhotoImage(img4)  # chuyen anh tu cv2 sang tkiner

    canvas2.create_image(0, 0, anchor=NW, image=imgTK1)

    canvas3.create_image(0, 0, anchor=NW, image=imgTK2)

    canvas4.create_image(0, 0, anchor=NW, image=imgTK3)

    canvas1.create_image(0, 0, anchor=NW, image=imgTK4)

    # canvas3.mainloop()
    # canvas2.mainloop()
    # canvas4.mainloop()
    label1.after(1000000,imgTK1)
    label2.after(1000000,imgTK2)
    label3.after(1000000,imgTK3)
    label4.after(1000000,imgTK4)







def ReadCom():
    global out, bytesWaiting
    while (True):
        while ser.inWaiting() > 0:
            out = ser.read_all()
        if out != '':
            print(out)
        if out == b'V':
            Checking()
        out = ''

def video():
    while True:
        ret, frame = cap.read()
        if not ret:
            print('khong nhan duoc hinh anh')
        cv2.imshow('cam', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
    frame = cv2.resize(frame, (400, 250))
    plt.figure('Toa do')
    plt.imshow(frame)
    plt.show()


btn_src = Button(frame1,width=10,height=4,text='Video',command=video)
btn_src.grid(row=0,column=0)

btn_check = Button(frame1,width=10,height=4,text='Checking',command=Checking)
btn_check.grid(row=0,column=1)

canvas1 = Canvas(frame1, width=400, height=250)
canvas1.grid(row=1,column=0)
label4 = Label(frame1)
label4.grid(row=2,column=0)


canvas2 = Canvas(frame1, width=400, height=250)
canvas2.grid(row=1,column=1)

canvas3 = Canvas(frame2, width=400, height=250)
canvas3.grid(row=1,column=0)
canvas4 = Canvas(frame2, width=400, height=250)
canvas4.grid(row=1,column=1)

label2 = Label(frame2)
label2.grid(row=2,column=0)
label3 = Label(frame2)
label3.grid(row=2,column=1)

T_readcom = threading.Thread(name='Readcom',target=ReadCom)
T_readcom.start()

# T_TakePhoto = continuous_threading.PeriodicThread(3,chupanh) # 3s chup anh 1 lan
# T_TakePhoto.start()


# frame3.mainloop()
window.mainloop()