import cv2
from tkinter import *
from tkinter import filedialog as f_dialog # lien quan thu muc
import numpy as np
from PIL import Image, ImageTk
import  continuous_threading
import matplotlib.pyplot as plt
import time
import serial


out=''
# ket noi COM
# ser = serial.Serial(
#     port = 'COM7',
#     baudrate= 9600,
#     parity=serial.PARITY_ODD,
#     stopbits=serial.STOPBITS_TWO,
#     bytesize=serial.SEVENBITS
# )
# ser.isOpen()
# while ser.inWaiting() > 0:
#     out += ser.read(1)
# if out != '':
#     print
# ">>" + out



window = Tk()
window.title('VIDEO MRBAT')
window.geometry('810x600') # tao khung anh


frame1 = Frame(window,width=400,height=300)
frame1.grid(row=0,column=0)

frame2 = Frame(window,width=400,height=300)
frame2.grid(row=1,column=0)

def takeimg():
    global  path
    file = f_dialog.askopenfile()
    path = file.name
    img = cv2.imread(path)
    img = cv2.resize(img,(400,250))



    imgCV = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img1 = Image.fromarray(imgCV)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    # plt.figure('anh nguon')
    # plt.imshow(img)
    # plt.show()


    canvas1.create_image(0, 0, anchor=NW, image=imgTK)
    canvas1.mainloop()

def Checking():
    global path
    img = cv2.imread(path)
    img= cv2.resize(img,(400,250))
    img_copy = img.copy()
    img_src = img[125:160,280:350]
    img_ss = img_copy[160:195,280:350]
    img_src = cv2.resize(img_src, (400, 250))
    img_ss = cv2.resize(img_ss, (400, 250))



    img_check = cv2.subtract(img_src,img_ss,mask=None)
    img_check = cv2.resize(img_check,(400,250))
    img_check= cv2.cvtColor(img_check,cv2.COLOR_BGR2GRAY)
    img_check = cv2.threshold(img_check,20,255,cv2.THRESH_BINARY)[1]
    img_check = cv2.bitwise_not(img_check)

    Contours, Contour_thresh = cv2.findContours(img_check, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    Contour_thresh_coppy = img_copy.copy()
    Contour_thresh_coppy = cv2.resize(Contour_thresh_coppy, (400, 250))

    for contour in Contours:
        area = cv2.contourArea(contour)
        #print(area)
        if area > 100:
            print('Da Dan Tem')

            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            count = len(approx)
            cv2.drawContours(Contour_thresh_coppy, contour, -1, (0, 255, 0), 1, cv2.LINE_4)
            M = cv2.moments(contour)
            print(M)
            # tinh toan tam
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(Contour_thresh_coppy, 'NG - DA DAN TEM ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            break
        else:
            print('Chua dan tem')



    imgCV1 = cv2.cvtColor(img_src, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img1 = Image.fromarray(imgCV1)  # tao mang de chuyen anh
    imgTK1 = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    imgCV2 = cv2.cvtColor(img_ss, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img2 = Image.fromarray(imgCV2)  # tao mang de chuyen anh
    imgTK2 = ImageTk.PhotoImage(img2)  # chuyen anh tu cv2 sang tkiner

    #imgCV3 = cv2.cvtColor(img_check, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img3 = Image.fromarray(Contour_thresh_coppy)  # tao mang de chuyen anh
    imgTK3 = ImageTk.PhotoImage(img3)  # chuyen anh tu cv2 sang tkiner

    canvas2.create_image(0, 0, anchor=NW, image=imgTK1)

    canvas3.create_image(0, 0, anchor=NW, image=imgTK2)

    canvas4.create_image(0, 0, anchor=NW, image=imgTK3)

    canvas3.mainloop()

btn_src = Button(frame1,width=10,height=4,text='Anh Nguon',command=takeimg)
btn_src.grid(row=0,column=0)

btn_check = Button(frame1,width=10,height=4,text='Checking',command=Checking)
btn_check.grid(row=0,column=1)

canvas1 = Canvas(frame1, width=400, height=250)
canvas1.grid(row=1,column=0)

canvas2 = Canvas(frame1, width=400, height=250)
canvas2.grid(row=1,column=1)

canvas3 = Canvas(frame2, width=400, height=250)
canvas3.grid(row=1,column=0)
canvas4 = Canvas(frame2, width=400, height=250)
canvas4.grid(row=1,column=1)

mainloop()