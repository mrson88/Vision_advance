import cv2
import tkinter
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import continuous_threading
from PIL import  Image, ImageTk
from tkinter import filedialog as f_d # mo foder

# khai bao

link = r'C:\Users\sev_user\Desktop\Luu_anh\\'
global path1


#cua so
wd = Tk('') #khai bao cua so
wd.title('cua so anh') # dat ten cua so
wd.geometry('1300x800') # kich thuoc cua so


# tao o trong cua so
fr1= Frame(wd,width=600,height=400) # phan vung trong khung anh (kich thuoc rong x cao)
fr1.grid(row=0,column=0) # Vi tri vung o dong 0 cot 0

fr2= Frame(wd,width=600,height=400) # phan vung trong khung anh (kich thuoc rong x cao)
fr2.grid(row=0,column=1) # Vi tri vung o dong 0 cot 0

fr3= Frame(wd,width=600,height=400) # phan vung trong khung anh (kich thuoc rong x cao)
fr3.grid(row=1,column=0)

fr4= Frame(wd,width=600,height=400) # phan vung trong khung anh (kich thuoc rong x cao)
fr4.grid(row=1,column=1)

# cua so nhap toa do
lbx=Label(fr4,text="Toa do X")
lbx.grid(column=0,row=0)

lby=Label(fr4,text="Toa do Y")
lby.grid(column=0,row=1)

txtx=Entry(fr4,width=10)
txtx.grid(column=1,row=0)

txty=Entry(fr4,width=10)
txty.grid(column=1,row=1)

txtx.focus()
txty.focus()


def an ():

    thongbao.delete("1.0", "end")
    thongbao.insert(INSERT, 'Hay chon anh goc')
    thongbao.configure(fg='red')

    img=cv2.imread(path1)
    img = cv2.resize(img, (600, 400))

    # cv2.imshow('anh',img)
    # cv2.waitKey(0)

    x = txtx.get()
    y = txty.get()
    print(x)
    print(y)

    thongbao.delete("1.0", "end")
    thongbao.insert(INSERT, 'Chua nhap toa do X')
    thongbao.configure(fg='red')


    #Toa do anh label
    x1 = int(x)

    thongbao.delete("1.0", "end")
    thongbao.insert(INSERT, 'Chua nhap toa do Y')
    thongbao.configure(fg='red')

    y1 = int(y)-30
    x2 = int(x)+30
    y2 = int(y)+5
    thongbao.delete("1.0", "end")
    thongbao.insert(INSERT, 'Luu thanh cong')
    thongbao.configure(fg='green')

    # Cat anh lam anh label
    imglabel = img[y1:y2, x1:x2]
    imglabelR = cv2.resize(imglabel, (200, 200))
    # kernel2 = np.array([[-1, -1, -1],
    #                     [-1, 8, -1],
    #                     [-1, -1, -1]])
    # imglabelR = cv2.filter2D(src= imglabelR, ddepth=-1, kernel=kernel2)
    imglabelR = cv2.bilateralFilter(src=imglabelR, d=9,
                                          sigmaColor=75, sigmaSpace=75) # lamf net anh
    # imglabelR = cv2.bitwise_not(imglabelR, mask=None)
    imglabelCv = cv2.cvtColor(imglabelR, cv2.COLOR_RGB2BGR)
    img2 = Image.fromarray(imglabelCv)  # tao mang anh
    imgTk2 = ImageTk.PhotoImage(img2)  # chuyen anh tu cv2
    canvas2.create_image(0, 0, anchor=NW, image=imgTk2)


    # Toa do anh front
    xf1 = int(x)
    yf1 = int(y) + 40
    xf2 = int(x) + 30
    yf2 = int(y) + 5
    # Cat anh lam anh front
    imgfront = img[yf2:yf1, xf1:xf2]
    imgfrontR = cv2.resize(imgfront , (200, 200))
    # imgfrontR = cv2.bitwise_not(imgfrontR,mask=None)
    imgfrontCv = cv2.cvtColor(imgfrontR, cv2.COLOR_RGB2BGR)
    img3 = Image.fromarray(imgfrontCv)  # tao mang anh
    imgTk3 = ImageTk.PhotoImage(img3)  # chuyen anh tu cv2
    canvas3.create_image(0, 0, anchor=NW, image=imgTk3)

    # so sanh
    imgsub=cv2.subtract(imgfrontR,imglabelR)
    img4 = Image.fromarray(imgsub)  # tao mang anh
    imgTk4 = ImageTk.PhotoImage(img4)  # chuyen anh tu cv2
    canvas4.create_image(0, 0, anchor=NW, image=imgTk4)

    # Ve diem khac biet
    imgG = cv2.cvtColor(imgsub, cv2.COLOR_RGB2GRAY)

    img_blur = cv2.GaussianBlur(imgG, (5, 5), 0)  # lam mo
    img_blur = cv2.bilateralFilter(src=img_blur, d=9,
                                    sigmaColor=75, sigmaSpace=75)  # lamf net anh
    img_blur = cv2.bilateralFilter(src=img_blur, d=9,
                                   sigmaColor=75, sigmaSpace=75)  # lamf net anh


    edges = cv2.threshold(img_blur, 10, 255, cv2.THRESH_BINARY_INV)[1] # All mau tru mau trang
    edges = cv2.threshold(imgG, 5, 255, cv2.THRESH_BINARY)[1] # mau den

    contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_LIST,
                                           method=cv2.CHAIN_APPROX_NONE)  # tim duong vien
    # cv2.imshow('',edges)
    # cv2.waitKey(0)
    img_copy = imglabelCv.copy()
    for contour in contours:  # tim vung
        area = cv2.contourArea(contour)  # quy doi
        print(area,'neu') # in vung cua con tua
        # print(area)  # in vung cua con tua
        if  area > 20 and area <30000:  # chon vung lon hon 30000 thi ve vien
            duong_thang = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # Kieu duong
            count = len(duong_thang)
            # print(count)
            cv2.drawContours(image=img_copy, contours=contour, contourIdx=-1,
                             color=(0, 255, 0), thickness=5, lineType=cv2.LINE_4)  # Ve duong vien vao anh coppy
            text_ok = 'Da Co Label'
            lb.config(text=text_ok, fg='green')
            break
        # elif area >30000:
        #     edges = cv2.threshold(img_blur, 5, 255, cv2.THRESH_BINARY)[1]  # mau trang
        #
        #     contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_LIST,
        #                                            method=cv2.CHAIN_APPROX_NONE)  # tim duong vien
        #     # cv2.imshow('',edges)
        #     # cv2.waitKey(0)
        #     img_copy = imglabelCv.copy()
        #     for contour in contours:  # tim vung
        #         area = cv2.contourArea(contour)  # quy doi
        #         print(area)  # in vung cua con tua
        #         print(area,'lon hon 30k')
        #         if area < 30000:  # chon vung lon hon 30000 thi ve vien
        #             duong_thang = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # Kieu duong
        #             count = len(duong_thang)
        #             # print(count)
        #             cv2.drawContours(image=img_copy, contours=contour, contourIdx=-1,
        #                              color=(0, 255, 0), thickness=5, lineType=cv2.LINE_4)  # Ve duong vien vao anh coppy
        #             text_ok = 'Da Co Label'
        #             lb.config(text=text_ok, fg='blue')
        #         elif area>30000 :
        #             print(area,'lenh cuoi')

        else:
            print(area,'in no')
            text_ng = 'Chua dan tem'
            lb.config(text=text_ng, fg='red')
            # break


    img5 = Image.fromarray(edges)  # tao mang anh
    imgTk5 = ImageTk.PhotoImage(img5)  # chuyen anh tu cv2
    canvas5.create_image(0, 0, anchor=NW, image=imgTk5)

    img6 = cv2.resize(img_copy, (500, 300))
    img6 = Image.fromarray(img6)  # tao mang anh
    imgTk6 = ImageTk.PhotoImage(img6)  # chuyen anh tu cv2
    canvas6.create_image(0, 0, anchor=NW, image=imgTk6)


    canvas6.mainloop()


bt=Button(fr4,text="Luu lai",bg='green', command= an)
bt.grid(column=0,row=2)
thongbao=Text(fr4,height=1,width=20)
thongbao.grid(column=1,row=2)


def chon_anh():

    global path1
    file = f_d.askopenfile()  # chon foder
    path1 = file.name
    img = cv2.imread(path1)
    imgr = cv2.resize(img, (600, 400))
    imgcv = cv2.cvtColor(imgr, cv2.COLOR_RGB2BGR)
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas1.create_image(0, 0, anchor=NW, image=imgTk)

    plt.figure('tao do')
    plt.imshow(imgr)
    plt.show()
    canvas1.mainloop()

bt1 = Button(fr1, width=10, height=1, text='Anh Goc', command=chon_anh)
bt1.grid(row=0,column=0)

canvas1 = Canvas(fr1, width=600, height=400)
canvas1.grid(row=1,column=0)

lbtem=Label(fr2,text="Vung Label",bg='blue')
lbtem.grid(row=0,column=0)

canvas2 = Canvas(fr2, width=300, height=200)
canvas2.grid(row=0,column=1)

lbfront=Label(fr2,text="Vung Front",bg='blue')
lbfront.grid(row=1,column=0)

canvas3 = Canvas(fr2, width=300, height=200)
canvas3.grid(row=1,column=1)

lbsosanh=Label(fr2,text="Vung So Sanh",bg='blue')
lbsosanh.grid(row=0,column=2)

canvas4 = Canvas(fr2, width=300, height=200)
canvas4.grid(row=0,column=3)

lbdentrang=Label(fr2,text="Vung Den Trang",bg='blue')
lbdentrang.grid(row=1,column=2)

canvas5 = Canvas(fr2, width=300, height=200)
canvas5.grid(row=1,column=3)

canvas6 = Canvas(fr3, width=500, height=300)
canvas6.grid(row=1,column=0)

lb = Label(fr3)
lb.grid(row=0,column=0)


fr4.mainloop()
wd.mainloop()
