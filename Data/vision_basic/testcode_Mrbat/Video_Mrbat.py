import cv2
from tkinter import *
from tkinter import filedialog as f_dialog # lien quan thu muc
import numpy as np
from PIL import Image, ImageTk
import  continuous_threading

# Khai bao tkiner

ink2 = r'C:\Users\dsfg\Desktop\anh\\'
window = Tk()
window.title('VIDEO MRBAT')
window.geometry('800x550') # tao khung anh

frame1 = Frame(window,width=600,height=500)
frame1.grid(row=0,column=0)

frame2 = Frame(window,width=600,height=500)
frame2.grid(row=1,column=0)


label = Label(frame1)
label.pack()
# label_count = Label(window,width=10, height=3, fg='blue', font=('Timenewroman', 28, 'bold'))
# label_count.grid(row=2,column=0)
label_vuong_red =Label(frame2,width=10, height=3, fg='red', font=('Timenewroman', 6, 'bold'))
label_vuong_red.grid(row=0,column=0)
label_vuong_blue =Label(frame2,width=10, height=3, fg='blue', font=('Timenewroman', 6, 'bold'))
label_vuong_blue.grid(row=0,column=1)
label_vuong_yellow =Label(frame2,width=10, height=3, fg='yellow', font=('Timenewroman', 6, 'bold'))
label_vuong_yellow.grid(row=0,column=2)

label_Tron_red =Label(frame2,width=10, height=3, fg='red', font=('Timenewroman', 6, 'bold'))
label_Tron_red.grid(row=1,column=0)
label_Tron_blue =Label(frame2,width=10, height=3, fg='blue', font=('Timenewroman', 6, 'bold'))
label_Tron_blue.grid(row=1,column=1)
label_Tron_yellow =Label(frame2,width=10, height=3, fg='yellow', font=('Timenewroman', 6, 'bold'))
label_Tron_yellow.grid(row=1,column=2)

label_tamgiac_red =Label(frame2,width=10, height=3, fg='red', font=('Timenewroman', 6, 'bold'))
label_tamgiac_red.grid(row=2,column=0)
label_tamgiac_blue =Label(frame2,width=10, height=3, fg='blue', font=('Timenewroman', 6, 'bold'))
label_tamgiac_blue.grid(row=2,column=1)
label_tamgiac_yellow =Label(frame2,width=10, height=3, fg='yellow', font=('Timenewroman', 6, 'bold'))
label_tamgiac_yellow.grid(row=2,column=2)


count_red_number = 0
count_red_Tamgiac = 0
count_red_hinhvuong =0
count_red_Hinhtron = 0

count_yellow_Tamgiac =0
count_yellow_hinhvuong = 0
count_yellow_Hinhtron = 0

count_blue_Tamgiac =0
count_blue_hinhvuong = 0
count_blue_Hinhtron = 0

count_yellow_number = 0
# khai bao CAM : Vi tri cam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Khong nhan dien duoc CAM')
def Video():
    global  count_red_number,count_yellow_number,count_red_Tamgiac,count_red_hinhvuong,count_red_Hinhtron
    global  count_yellow_Hinhtron,count_yellow_hinhvuong,count_yellow_Tamgiac
    global  count_blue_Tamgiac,count_blue_Hinhtron,count_blue_hinhvuong
    # doc tung khung hinh
    ret,img = cap.read() # ret : bien nhan biet cam co doc duoc khong , frame : bien anh doc tu cam
    if not ret:
        print('khong nhan duoc khung hinh')
    # img = cv2.resize(img,(500,400)) # dua ve cung kich co size anh
    # tao mat na
    red_mask = cv2.inRange(img, np.array([0, 0, 50]), np.array([70, 70, 255]))
    blue_mask = cv2.inRange(img, np.array([255, 200, 70]), np.array([0, 0, 0]))
    Yellow_mask = cv2.inRange(img, np.array([0, 50, 50]), np.array([50, 255, 255]))

    thres_red = cv2.threshold(red_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_red, Contour_thresh = cv2.findContours(thres_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    thres_yellow = cv2.threshold(Yellow_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_yellow, Contour_thresh = cv2.findContours(thres_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    thres_blue = cv2.threshold(blue_mask, 150, 255, cv2.THRESH_BINARY)[1]
    Contours_blue, Contour_thresh = cv2.findContours(thres_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)[1]
    contours,HHH = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    img_copy = img.copy()
    img_copy = cv2.cvtColor(img_copy,cv2.COLOR_BGR2RGB)

    # thu lai
    # for test in contours:
    #     area_test = cv2.contourArea(test)
    #     print(test)
    #     if area_test > 2000:


    for contour in Contours_red:
        area_red = cv2.contourArea(contour)
        #print(area_red)
        if area_red > 10000 and area_red < 100000:
            for abc in contours:
                area_abc = cv2.contourArea(abc)
                if area_abc > 3000:
                    approx_red = cv2.approxPolyDP(abc, 0.01 * cv2.arcLength(abc, True), True)
                    count_red = len(approx_red)
                    print(count_red)
                    M = cv2.moments(abc)
                    x_red = approx_red.ravel()[0]
                    y_red = approx_red.ravel()[1]
                    # #cv2.putText(img_copy, 'Mau Do', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 2)
                    # count_red_number += 1
                    # # xac dinh hinh dang
                    # approx = cv2.approxPolyDP(abc, 0.01 * cv2.arcLength(abc, True), True)
                    # count = len(approx)
                    cv2.drawContours(image=img_copy, contours=Contours_red, contourIdx=-1, color=(0, 255, 0), thickness=2,
                                     lineType=cv2.LINE_4)
                    if count_red > 3 and count_red < 9:
                        cv2.putText(img_copy, 'Tam Giac', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), thickness=2,
                                    lineType=cv2.LINE_4)
                        count_red_Tamgiac +=1
                    elif count_red > 10 and count_red <12:
                        cv2.putText(img_copy, 'Hinh Vuong', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), thickness=2,
                                    lineType=cv2.LINE_4)
                        count_red_hinhvuong +=1
                    elif count_red >= 20 and count_red < 100:
                        cv2.putText(img_copy, 'Hinh Tron', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_4)
                        count_red_Hinhtron +=1

    for contour in Contours_yellow:
        area_yellow = cv2.contourArea(contour)
       # print(area_yellow)
        if area_yellow > 3000:
            for abcd in contours:
                area_abcd = cv2.contourArea(abcd)
                if area_abcd > 8000:
                    area_yellow_draw = cv2.approxPolyDP(abcd, 0.01 * cv2.arcLength(abcd, True), True)
                    count_yellow = len(area_yellow_draw)
                    M = cv2.moments(abcd)
                    x_yellow = area_yellow_draw.ravel()[0]
                    y_yellow = area_yellow_draw.ravel()[1]
                    # cv2.putText(img_copy, 'Mau Do', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 2)
                    count_yellow_number += 1
                    # xac dinh hinh dang
                    approx = cv2.approxPolyDP(abcd, 0.01 * cv2.arcLength(abcd, True), True)
                    count = len(approx)
                    cv2.drawContours(image=img_copy, contours=Contours_yellow, contourIdx=-1, color=(0, 255, 0), thickness=2,
                                     lineType=cv2.LINE_4)
                    if count == 3:
                        cv2.putText(img_copy, 'Tam Giac', (x_yellow, y_yellow), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_4)
                        count_yellow_Tamgiac += 1
                    elif count == 4:
                        cv2.putText(img_copy, 'Hinh Vuong', (y_yellow, y_yellow), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_4)
                        count_yellow_hinhvuong += 1
                    elif count >= 25 and count < 30:
                        cv2.putText(img_copy, 'Hinh Tron', (y_yellow, y_yellow), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_AA)
                        count_yellow_Hinhtron += 1
    for contour in Contours_blue:
        area_blue = cv2.contourArea(contour)
       # print(area_blue)
        if area_blue > 2200 and area_blue < 50000:
            for abcde in contours:
                area_abcde = cv2.contourArea(abcde)
                if area_abcde > 2000:
                    area_blue = cv2.approxPolyDP(abcde, 0.01 * cv2.arcLength(abcde, True), True)
                    count_yellow = len(area_blue)
                    M = cv2.moments(abcde)
                    x_blue = area_blue.ravel()[0]
                    y_blue = area_blue.ravel()[1]
                    # cv2.putText(img_copy, 'Mau Do', (x_red, y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 2)
                    count_yellow_number += 1
                    # xac dinh hinh dang
                    approx = cv2.approxPolyDP(abcde, 0.01 * cv2.arcLength(abcde, True), True)
                    count = len(approx)
                    cv2.drawContours(image=img_copy, contours=Contours_blue, contourIdx=-1, color=(0, 255, 0), thickness=2,
                                     lineType=cv2.LINE_4)
                    if count == 3:
                        cv2.putText(img_copy, 'Tam Giac', (x_blue, y_blue), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_AA)
                        count_blue_Tamgiac += 1
                    elif count == 4:
                        cv2.putText(img_copy, 'Hinh Vuong', (x_blue, y_blue), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_AA)
                        count_blue_hinhvuong += 1
                    elif count >= 16 and count < 30:
                        cv2.putText(img_copy, 'Hinh Tron', (x_blue, y_blue), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
                                    thickness=2,
                                    lineType=cv2.LINE_AA)
                        count_blue_Hinhtron += 1



    #img_cvt = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # chuyen sang he mau chuan BGR tren tkniner
    img1 = Image.fromarray(img_copy)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner
    label.imgTK = imgTK
    label.config(image=imgTK)
    label.after(10,Video)

    label_tamgiac_red.config(text=f'Tam giac do : {count_red_Tamgiac}')
    label_tamgiac_blue.config(text=f'Tam giac xanh : {count_blue_Tamgiac}')
    label_tamgiac_yellow.config(text=f'Tam giac vang : {count_yellow_Tamgiac}')
    label_Tron_red.config(text=f'Tron do : {count_red_Hinhtron}')
    label_Tron_blue.config(text=f'Tron Xanh : {count_blue_Hinhtron}')
    label_Tron_yellow.config(text=f'Tron Vang : {count_yellow_Hinhtron}')
    label_vuong_red.config(text=f'Vuong Do : {count_red_hinhvuong}')
    label_vuong_blue.config(text=f'Vuong Xanh : {count_blue_hinhvuong}')
    label_vuong_yellow.config(text=f'Vuong Vang : {count_yellow_hinhvuong}')
    # cv2.imshow('Do',thres_red)
    # cv2.imshow('VAng',thres_yellow)
    # cv2.imshow('XAnh',thres_blue)

Video()
i = 0
def chupanh():
    global  i
    ret, img = cap.read()
    path = r'C:\Users\dsfg\Desktop\anh\anh chup\\'
    # if ret :
    #     img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #     thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
    #     contours,contour_thress = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    #     img_copy = img.copy()
    #     for contour in contours:
    #         area = cv2.contourArea(contours)
    #         print(area)
    #         if area >1000:
    #             approx =cv2.approxPolyDP(contours,0.01*cv2.arcLength(contours,True),True)
    #             count = len(approx)
    #             cv2.drawContours(image=img_copy,contours=contours,contourIdx=-1,color= (0,255,0),thickness=2,lineType=cv2.LINE_4)
    #             x = approx.ravel()[0]
    #             y = approx.ravel()[1]
    #             if count == 3:
    #                 cv2.putText(img_copy,'Tam Giac',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),thickness=2,lineType=cv2.LINE_AA)
    #             elif count == 4:
    #                 cv2.putText(img_copy, 'Hinh Vuong', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), thickness=2,
    #                             lineType=cv2.LINE_AA)
    #             else:
    #                 cv2.putText(img_copy, 'Hinh Tron', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255),
    #                             thickness=2,
    #                             lineType=cv2.LINE_AA)

    cv2.imwrite(f'{path}img_{i}.png',img)
    i +=1

# buton1 = Button(window,width=10,height=3,text='Chon Anh 1',command=chupanh)
# buton1.grid(row=0,column=0)

# thread = continuous_threading.PeriodicThread(3,chupanh) # 3s chup anh 1 lan
# thread.start()
window.mainloop()

# cv2.imshow('frame',frame)
# if cv2.waitKey(1) & 0xff == ord('q'):
#     cv2.destroyAllWindows()
#     cap.release()



