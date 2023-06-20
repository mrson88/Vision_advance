from tkinter import *
from tkinter import filedialog as f_dialog # lien quan thu muc
import cv2
import numpy as np
from PIL import Image, ImageTk

link2 = r'C:\Users\dsfg\Desktop\anh\\'
window = Tk()
window.title('show anh Image')
window.geometry('650x550') # tao khung anh

frame1 = Frame(window,width=319,height=239)
frame1.grid(row=0,column=0)
frame2 = Frame(window,width=319,height=239)
frame2.grid(row=0,column=1)

# mau do : (0,0,50) ~ (70,70,255)  HSV
# mau blue : (197,100,117) ~ (117,255,255)
# mau yellow : (0,50,50) ~ (50,255,255)

def chonanh1():
    global path1
    file = f_dialog.askopenfile()
    path1 = file.name

    # print(type(vision_basic.name))
    img = cv2.imread(path1)
    img = cv2.resize(img, (319, 200))

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    bgr= cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    red_mask = cv2.inRange(img,np.array([0,0,50]),np.array([70,70,255]))
    blue_mask =cv2.inRange(bgr,np.array([255,200,70]),np.array([0,0,0]))
    Yellow_mask = cv2.inRange(img,np.array([0,50,50]),np.array([50,255,255]))
    # phat hien vat su dung blobs

    # xac dinh hinh dang
    # approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    # count = len(approx)
    # print(count)
    thres_red = cv2.threshold(red_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_red, Contour_thresh = cv2.findContours(thres_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    thres_yellow = cv2.threshold(Yellow_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_yellow, Contour_thresh = cv2.findContours(thres_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    thres_blue = cv2.threshold(blue_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_blue, Contour_thresh = cv2.findContours(thres_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    Contour_thresh_coppy = img.copy()
    print(Contours_blue)
    for contour in Contours_red:
        area_red =cv2.contourArea(contour)
        # print(area_red)
        if area_red > 2200:
            Contour_thresh_coppy = cv2.cvtColor(Contour_thresh_coppy, cv2.COLOR_BGR2RGB)
            cv2.drawContours(Contour_thresh_coppy, Contours_red, -1, (0, 255, 0), 2, cv2.LINE_4)
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(Contour_thresh_coppy, 'Mau Do', (cx - 70, cy - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    for contour in Contours_yellow:
        area_yellow =cv2.contourArea(contour)
        # print(area_yellow)
        if area_yellow > 2100:
            Contour_thresh_coppy = cv2.cvtColor(Contour_thresh_coppy, cv2.COLOR_BGR2RGB)
            cv2.drawContours(Contour_thresh_coppy, Contours_yellow, -1, (0, 255, 0), 2, cv2.LINE_4)
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(Contour_thresh_coppy, 'Mau Vang', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    for contour in Contours_blue:
        area_blue =cv2.contourArea(contour)
        print(area_blue)
        if area_blue > 2100:
            Contour_thresh_coppy = cv2.cvtColor(Contour_thresh_coppy, cv2.COLOR_HSV2BGR)
            cv2.drawContours(Contour_thresh_coppy,Contours_blue, -1, (0, 255, 0), 2, cv2.LINE_4)
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(Contour_thresh_coppy, 'Mau Xanh ', (cx + 70, cy + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    img1 = Image.fromarray(Contour_thresh_coppy)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    canvas1.create_image(0, 0, anchor=NW, image=imgTK)
    canvas1.mainloop()


buton1 = Button(frame1,width=10,height=3,text='Chon Anh 1',command=chonanh1)
buton1.pack()
canvas1 = Canvas(frame1, width=319, height=200)
canvas1.pack()

window.mainloop()