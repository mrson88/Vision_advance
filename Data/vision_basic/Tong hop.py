from tkinter import *

import numpy as np
from PIL import  Image, ImageTk
from tkinter import filedialog as f_d # mo foder
import  cv2



link = r'C:\Users\A0G\Desktop\HA HA DHB\\'
wd = Tk('')# tao cua so
wd.title('Lua chon')#dat ten anh
wd.geometry('650x800')# tao khung anh

def canh_bao():
    wd1 = Tk()  # tao cua so
    wd1.title('Canh Bao')  # dat ten anh
    wd1.geometry('200x200')  # tao khung anh
    # text_ng='NG'
    # cv2.putText(wd1, text_ng, (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 30, (255, 0, 255), 2)
    # lb.config(text=text_ng, fg='red')

    # wd1.mainloop()


fr1= Frame(wd,width=319,height=239) # phan vung trong khung anh (kich thuoc rong x cao)
fr1.grid(row=0,column=0) # Vi tri vung o dong 0 cot 0

fr2= Frame(wd,width=319,height=239)
fr2.grid(row=0,column=1)

fr3= Frame(wd,width=319,height=200)
fr3.grid(row=1,column=0)

fr4= Frame(wd,width=319,height=200)
fr4.grid(row=1,column=1)

fr5= Frame(wd,width=319,height=200)
fr5.grid(row=2,column=1)

global path1
global path2


#img = cv2.imread(link +'img_2.png') #doc anh
#img = cv2.resize(img,(640, 480))# quy chuan khich thuoc anh
#imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # quy chuan ve mau sac mong muon
#img1 = Image.fromarray(imgcv) #tao mang anh
#imgTk = ImageTk. PhotoImage(img1) #chuyen anh tu cv2
# lb = Label(wd, width=640, height=480)
# lb.pack(padx=1, pady=1)
# lb.config(image=imgTk)
 #canvas = Canvas(wd, width=640, height=400)
 #canvas.pack(padx=1, pady=1)
# canvas.create_image(0, 0, anchor=NW, image = imgTk)
# canvas.create_image(0, 0, image = imgTk)


def chonanh1():
    global path1
    file = f_d.askopenfile()#chon foder
    path1 = file.name
    # print(path1)
    # print(type(vision_basic.name))
    img = cv2.imread(path1)  # doc anh

    # imgline = img.copy()
    # tam = (50, 115)
    # trucY = (150, 50)
    #
    # tam1 = (50, 115)
    # text = 'HA HA'
    #
    # lower_green=np.array([0,108,200])
    # upper_green=np.array([10,255,255])

    # cv2.ellipse(img, tam, trucY, 0, 0, 360, (0, 255, 0), thickness=1)
    # cv2.putText(imgline, text, tam1, fontFace=cv2.FONT_ITALIC, fontScale=2.5, color=(255, 250, 0))
    # img = cv2.imread(link + 'img_2.png')  # doc anh

    img = cv2.resize(img, (319, 200))  # quy chuan khich thuoc anh
    # cv2.putText(img, text, tam1, fontFace=cv2.FONT_ITALIC, fontScale=2.5, color=(255, 250, 0))
    imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    # imgcv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    # Chin = cv2.inRange(imgcv,lower_green,upper_green)
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas1.create_image(0, 0, anchor = NW, image=imgTk)
    canvas1.mainloop()

def chonanh2():
    global path2
    file = f_d.askopenfile()  # chon foder
    path2 = file.name
    # print(type(vision_basic.name))
    img = cv2.imread(path2)  # doc anh
    # img = cv2.imread(link + 'img_2.png')  # doc anh

    img = cv2.resize(img, (319, 200))  # quy chuan khich thuoc anh
    # img = img[0:280, 2:330]

    imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas2.create_image(0, 0, anchor=NW, image=imgTk)
    canvas2.mainloop()

def Kiemtra():
    global path1,path2
    img_goc = cv2.imread(path1)  # doc anh
    img_sosanh = cv2.imread(path2)  # doc anh
    img_goc = cv2.resize(img_goc, (319, 200))
    img_sosanh = cv2.resize(img_sosanh, (319, 200))

    img_sub = cv2.subtract(img_goc,img_sosanh)  # quy chuan khich thuoc anh
    img = cv2.resize(img_sub,(319,200))

    imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas3.create_image(0, 0, anchor=NW, image=imgTk)
    canvas3.mainloop()



def Hien_thi():
    global path1, path2
    img_goc = cv2.imread(path1)  # doc anh
    img_sosanh = cv2.imread(path2)  # doc anh
    img_goc = cv2.resize(img_goc, (319, 200))
    img_sosanh = cv2.resize(img_sosanh, (319, 200))

    img_sub = cv2.subtract(img_goc, img_sosanh)  # quy chuan khich thuoc anh

    # img_sub=cv2.bitwise_xor(img_goc,img_sosanh,mask=None)
    # img = cv2.resize(img_sub, (319, 200))


    img2 = cv2.cvtColor(img_sub, cv2.COLOR_RGB2GRAY)
    thresh2 = 100
    maxValue = 255
    nguong_ve_ko = cv2.threshold(img2, thresh2, maxValue, cv2.THRESH_BINARY)[1]
    nguong_ve_ko = cv2.bitwise_not(nguong_ve_ko)


    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 0.1
    params.maxArea = 15000

    params.filterByCircularity = True
    params.minCircularity = 0.001

    params.filterByConvexity = True
    params.minConvexity = 0.01

    params.filterByInertia= True
    params.minInertiaRatio = 0.1

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(nguong_ve_ko)
    blank = np.zeros((1, 1))
    # blobs = cv2.drawKeypoints(img_sosanh, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    blobs = cv2.drawKeypoints(nguong_ve_ko, keypoints, blank, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



    number_of_blobs = len(keypoints)
    text = "total block" + str(number_of_blobs)
    cv2.putText(blobs, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    if number_of_blobs >0 :
        text_ng = 'NG'
        cv2.putText(blobs, text_ng, (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
        lb.config(text=text_ng,fg='red')
        canh_bao()
    else:
        text_OK = 'OK'
        cv2.putText(blobs, text_OK, (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        lb.config(text=text_OK,fg='green')
        # canh_bao()

    # cv2.imshow('anh goc', img)
    # cv2.imshow('anh block', blobs)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img1 = Image.fromarray(blobs)  # tao mang anh
    imgtk = ImageTk.PhotoImage(img1)
    canvas4.create_image(0, 0, anchor=NW, image=imgtk)
    canvas4.mainloop()

def Ket_qua():
    global path2
    file = f_d.askopenfile()  # chon foder
    path2 = file.name
    # print(type(vision_basic.name))
    img = cv2.imread(path2)  # doc anh
    # img = cv2.imread(link + 'img_2.png')  # doc anh

    img = cv2.resize(img, (319, 200))  # quy chuan khich thuoc anh
    # img = img[0:280, 2:330]

    imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # quy chuan ve mau sac mong muon
    img1 = Image.fromarray(imgcv)  # tao mang anh
    imgTk = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2
    canvas5.create_image(0, 0, anchor=NW, image=imgTk)
    canvas5.mainloop()

bt1 = Button(fr1, width=10, height=1, text='Chon Anh 1', command=chonanh1)
#bt1.grid(row=0,column=0)#Chia rong va cot
bt1.grid(row=0,column=0)

bt2= Button(fr2, width=10, height=1, text= 'chon Anh 2',command= chonanh2)
#bt2.grid(row=0,column=1)
bt2.grid(row=0,column=0)

bt3= Button(fr3, width=10, height=2, text= 'Kiem Tra',command= Kiemtra)
bt3.grid(row=0,column=0)

bt4= Button(fr4, width=10, height=2, text= 'Hien thi',command= Hien_thi)
bt4.grid(row=0,column=0)

#Label= Button(fr5, width=10, height=2, text= 'Ket qua',command= Ket_qua)
bt5= Button(fr5, width=10, height=2, text= 'Ket qua',command=Ket_qua)
bt5.grid(row=0,column=0)

# bt6= Button(fr5, width=10, height=2, text= 'canh bao',command=canh_bao)
# bt6.grid(row=1,column=0)
# bt3.pack()
#bt3 = Button(wd, width=15,height=3,text='chon foder', command=foder)

canvas1 = Canvas(fr1, width=319, height=200)
canvas1.grid(row=1,column=0)

canvas2 = Canvas(fr2, width=319, height=200)
canvas2.grid(row=1,column=0)

canvas3 = Canvas(fr3, width=319, height=200)
canvas3.grid(row=1,column=0)

canvas4 = Canvas(fr4, width=319, height=200)
canvas4.grid(row=1,column=0)

canvas5= Canvas(fr5, width=319, height=200)
canvas5.grid(row=3,column=0)

lb = Label(fr5)
lb.grid(row=1,column=0)

wd.mainloop()



