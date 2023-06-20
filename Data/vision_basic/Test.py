from tkinter import *

import numpy as np
from PIL import  Image, ImageTk
from tkinter import filedialog as f_d # mo foder
import  cv2


# link=r'C:\Users\sev_user\Desktop\Python\\'
#test
window = Tk()
window.title('VIDEO MRBAT')
window.geometry('800x550') # tao khung anh

frame1 = Frame(window,width=600,height=500)
frame1.grid(row=0,column=0)

frame2 = Frame(window,width=600,height=500)
frame2.grid(row=1,column=0)


label = Label(frame1)
label.grid(row=0,column=0)
#test den day

def video():
    #buoc1 mo camera
    cap= cv2.VideoCapture(0)
    if not cap.isOpened():
        print('khong nhan camera')
    while True:
        ret, frame = cap.read()
        if not ret:
            print('khong nhan duoc hinh anh')

        # # cv2.imshow('cam',frame)
        # img=cv2.imread(link+'img_10.png')

        # cv2.imshow('truoc_loc', img)
        # cv2.imshow('anh_loc', identity)
        # cv2.imshow('loc_song_phuong.png', loc_song_phuong)
        # cv2.imshow('lam_mo', mo)
        # # img = cv2.imread(frame)
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # imgcv = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        imgcv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        # mg_xam = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # chuyen anh ve mau xam
        # img_blur = cv2.GaussianBlur(img_xam, (5, 5), 0)  # lam mo
        # img_xam = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # chuyen anh ve mau xam
        # img_blur = cv2.GaussianBlur(img_xam, (5, 5), 0)  # lam mo

        red_mask = cv2.inRange(frame, np.array([0, 0, 50]), np.array([70, 70, 255]))
        blue_mask = cv2.inRange(imgcv, np.array([70,100, 117]), np.array([117, 255, 255]))
        # blue_mask = cv2.inRange(imgcv, np.array([10,10, 117]), np.array([117, 255, 255]))
        yellow_mask = cv2.inRange(frame, np.array([0, 50, 50]), np.array([50, 255, 255]))
        # yellow_mask = cv2.inRange(frame, np.array([14, 201, 100]), np.array([50, 255, 255]))

        # Buoc 3 ti ve vien
        # RED


        # edges = cv2.Canny(image=img_blur, threshold1=255, threshold2=10)  # chuyen ve anh den trang
        # doi_mau = cv2.threshold(img, thresh, maxValue, cv2.THRESH_BINARY_INV)[1]
        edges = cv2.threshold(red_mask, 0, 255, cv2.THRESH_BINARY_INV)[1]
        contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_LIST,
                                               method=cv2.CHAIN_APPROX_NONE)  # tim duong vien

        # vien blue
        edges = cv2.threshold(blue_mask, 0, 255, cv2.THRESH_BINARY)[1]
        edges = cv2.threshold(blue_mask, 0, 255, cv2.THRESH_BINARY_INV)[1]
        contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_LIST,
                                               method=cv2.CHAIN_APPROX_NONE)  # tim duong vien
        # vien yellow
        edges = cv2.threshold(yellow_mask, 100, 255, cv2.THRESH_BINARY_INV)[1]
        contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_LIST,
                                               method=cv2.CHAIN_APPROX_NONE)  # tim duong vien



        img_copy = frame.copy()
        #Lua chon kich thuoc
        for contour in contours:  # tim vung
            area = cv2.contourArea(contour)  # quy doi
            print(area) #in vung cua con tua
            if area > 0 and area < 1000000:  # chon vung lon hon 30000 thi ve vien
                duong_thang = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # Kieu duong
                count = len(duong_thang)
                # print(count)
                cv2.drawContours(image=img_copy, contours=contour, contourIdx=-1,
                                 color=(255, 90, 255), thickness=1, lineType=cv2.LINE_4)  # Ve duong vien vao anh coppy


        #buoc xac dinh vien


        # cv2.imshow('img canh', frame)
        # cv2.imshow('img goc',img)
        # cv2.imshow('red',red_mask)
        # cv2.imshow('bl',blue_mask)
        # cv2.imshow('yl',yellow_mask)
        # # cv2.imshow('img vien', img_copy)
        # if cv2.waitKey(1) == ord('q'):
        #     break
        #     # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        #test
        img1 = Image.fromarray(img_copy)  # tao mang de chuyen anh
        imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner
        label.imgTK = imgTK
        label.config(image=imgTK)
        label.after(10, video)
        #test den day


video()
window.mainloop()