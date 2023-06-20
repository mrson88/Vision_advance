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

frame3 = Frame(window,width=319,height=239)
frame3.grid(row=1,column=0)

frame4 = Frame(window,width=319,height=239)
frame4.grid(row=1,column=1)

global path1,path2
count_OK = 0
count_NG = 0


#img = cv2.imread(link2 + 'img_1.png')
#img = cv2.resize(img,(640,480))
#imgCV = cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # convert anh sang RGB
#img1 = Image.fromarray(imgCV) # tao mang de chuyen anh
#imgTK = ImageTk.PhotoImage(img1) # chuyen anh tu cv2 sang tkiner

#lb = Label(window,width=640,height=300) # label trong tkiner
#lb.pack(padx=1,pady=1) # kich thuoc label
#lb.config(image=imgTK) # hien thi anh len tkiner

#canvas = Canvas(window,width=400,height=400)
#canvas.pack(pady=1,padx=1)
#canvas.create_image(0, 0, anchor = NW, image = imgTK) # anchor : Dong E (3h) Tay W (9h)  Nam(6h)S Bac N (12h)

# khai bao button tren tkiner
def chonanh1():
    global path1
    file = f_dialog.askopenfile()
    path1 = file.name

   # print(type(vision_basic.name))
    img = cv2.imread(path1)
    img = cv2.resize(img,(319,200))

    imgCV = cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # convert anh sang RGB
    #cv2.putText(imgCV, 'Ngua', (150, 50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color=(255, 0, 0))
    #cv2.rectangle(imgCV,(180,50),(50,150),(0,200,0), thickness=2)
    #cv2.circle(imgCV, (150, 50), 40, (255, 200, 0), thickness=1)
    #cv2.ellipse(imgCV, (150, 50), (100, 50), 0, 0, 360, (255, 0, 0), thickness=3)
    #imgCV= cv2.cvtColor(imgCV,cv2.COLOR_BGR2HSV)

    img1 = Image.fromarray(imgCV) # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1) # chuyen anh tu cv2 sang tkiner

    canvas1.create_image(0, 0, anchor= NW, image=imgTK)
    canvas1.mainloop()

def chonanh2():
    # mau do : (0,0,50) ~ (70,70,255)  HSV
    # mau blue : (197,100,117) ~ (117,255,255)
    # mau yellow : (0,50,50) ~ (50,255,255)
    global path2
    file = f_dialog.askopenfile()
    path2 = file.name

    img = cv2.imread(path2)
    img = cv2.resize(img, (319, 200))
   #img = img[0:100,10:500]

    imgCV = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    img1 = Image.fromarray(imgCV)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    canvas2.create_image(0, 0, anchor=NW, image=imgTK)
    canvas2.mainloop()
def kiemtra():
     global path1,path2
    # img_goc = cv2.imread(path1)
    # img_sosanh = cv2.imread(path2)
    #
    # sub_img = cv2.subtract(img_goc,img_sosanh)
    #
    # img = cv2.resize(sub_img, (319, 200))
    #
    # imgCV = cv2.cvtColor(img_goc, cv2.COLOR_RGB2BGR)  # convert anh sang RGB
    #
    # img1 = Image.fromarray(imgCV)  # tao mang de chuyen anh
    # imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    # canvas3.create_image(0, 0, anchor=NW, image=imgTK)
    # canvas3.mainloop()
def catanh():
    # lay duong dan anh va doc anh tren cv2
    global path1,path2, count_OK, count_NG
    img_goc = cv2.imread(path1)
    img_sosanh_goc = cv2.imread(path2)
    img_test = img_goc
    # chuyen anh sang he mau Gray
    img_goc = cv2.cvtColor(img_goc,cv2.COLOR_RGB2GRAY)
    img_sosanh = cv2.cvtColor(img_sosanh_goc,cv2.COLOR_RGB2GRAY)
    img_test_gray = cv2.cvtColor(img_test,cv2.COLOR_RGB2GRAY)
    # dua anh ve cung 1 kich co
    img_goc = cv2.resize(img_goc,(319,200))
    img_sosanh = cv2.resize(img_sosanh,(319,200))
    img_test = cv2.resize(img_test,(319,200))
    img_test_gray = cv2.resize(img_test_gray,(319,200))
    # tao anh hien thi can so sanh
    img_sosanh_goc = cv2.resize(img_sosanh_goc,(319,200))
    img_sosanh_goc = cv2.cvtColor(img_sosanh_goc,cv2.COLOR_RGB2BGR)
    # loc lam mo anh
    img_goc =cv2.GaussianBlur(img_goc,(5,5),0,0)
    img_sosanh = cv2.GaussianBlur(img_sosanh,(5,5),0,0)

    # so sanh anh goc vs anh can so sanh
    img_sub_Thuan = cv2.subtract(img_goc,img_sosanh)
    img_sub_Nghich = cv2.subtract(img_sosanh,img_goc)
    #img_sub_1 = cv2.bitwise_and(img_goc,img_sosanh,mask=img_sub)
    # threshold de nhan biet diem sai khac
    img_sub_Thuan = cv2.threshold(img_sub_Thuan, 150, 255, cv2.THRESH_BINARY_INV)[1]
    img_sub_Nghich = cv2.threshold(img_sub_Nghich,150,255,cv2.THRESH_BINARY_INV)[1]



    lower_green = np.array([150, 0, 0])
    upper_green = np.array([255, 255, 255])
    kernel1 = np.array([[0,0,0],[0,1,0],[0,0,0]])
    kernel2 = np.ones((5,5), np.float32)/25
    kernel3 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    kernel4 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    img = cv2.imread(path1)
    img = cv2.resize(img, (319, 200))

    #imgCV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert anh sang RGB
    imgCV = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    indentity = cv2.filter2D(imgCV,-1,kernel2)
    img_mask = cv2.inRange(imgCV, lower_green, upper_green)
    Average = cv2.blur(imgCV,(5,5))
    Gaus = cv2.GaussianBlur(imgCV,(5,5),0,0)
    indentity_frame = cv2.filter2D(imgCV,-1,kernel3)
    median = cv2.medianBlur(indentity_frame,5)
    indentity_net = cv2.filter2D(imgCV,-1,kernel4)
    bilater_filter = cv2.bilateralFilter(imgCV,9,75,75)
    indentity_frame1 = cv2.filter2D(bilater_filter,-1,kernel3)
    Gaus1 = cv2.GaussianBlur(indentity_frame1,(1,1),0,0)

    convert_nhiphan = cv2.cvtColor(Gaus1,cv2.COLOR_RGB2GRAY)
    #__ , nguong_nhi_phan = cv2.threshold(convert_nhiphan,100,255,cv2.THRESH_BINARY)
    nguong_nhi_phan = cv2.threshold(convert_nhiphan, 100, 255, cv2.THRESH_BINARY)[1]
    nguong_nhi_phan_not = cv2.threshold(convert_nhiphan,100,255,cv2.THRESH_BINARY_INV)[1]
    nguong_nhi_phan_trunc = cv2.threshold(convert_nhiphan,150,255,cv2.THRESH_TRUNC)[1]
    nguong_nhi_phan_tozero = cv2.threshold(convert_nhiphan,80,255,cv2.THRESH_TOZERO)[1]
    nguong_nhi_phan_tozero_inv = cv2.threshold(convert_nhiphan, 200, 255, cv2.THRESH_TOZERO_INV)[1]
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 0.1
    params.maxArea = 15000
    params.filterByCircularity = True
    params.minCircularity = 0.001
    params.filterByConvexity = True
    params.minConvexity = 0.01
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img_sub_Thuan)
    blank = np.zeros((7,7))
    blobs = cv2.drawKeypoints(img_sosanh_goc,keypoints,blank,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # them anh so sanh
    #blobs_sosanh = cv2.drawKeypoints(img_sosanh_goc,keypoints,blank,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    number_of_blobs = len(keypoints)
    text = 'Totall Error  ' + str(len(keypoints))
    #cv2.putText(blobs,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),1)
    if number_of_blobs >0:
        count_NG +=1
        text_NG = "NG"
        text1 = 'Totall Error  : ' + str(count_NG)
        text3 = 'OK ' + str(count_OK) +    '  ' +   'NG ' + str(count_NG)
        label.config(text=text_NG,fg='red')
        label_error.config(text=text1,fg= 'black')
        #label3.config(text=text3)
    else:
        keypoints1 = detector.detect(img_sub_Nghich)
        blank = np.zeros((7, 7))
        blobs = cv2.drawKeypoints(img_sosanh_goc, keypoints1, blank, (255, 0, 0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        number_of_blobs1 = len(keypoints1)
        if number_of_blobs1 >0:
            count_NG += 1
            text_NG = "NG"
            text3 = 'OK ' + str(count_OK)  + '  ' +  'NG ' + str(count_NG)
            text2 = 'Totall Error   : ' + str(count_NG)
            label.config(text=text_NG, fg='red')
            label_error.config(text=text2, fg='black')
            #label3.config(text=text3)
        else:
            count_OK += 1
            text3 = 'OK ' + str(count_OK) + ' '+ 'NG ' + str(count_NG)
            text_OK = 'OK'
            label.config(text=text_OK,fg='blue')
            #label3.config(text=text3)


    # phat hien canh theo sobel : chuyen anh ve gray roi loc nhieu
    sobelx = cv2.Sobel(convert_nhiphan,cv2.CV_64F,0,1,10)
    # phat hien canh theo candy
    candy_blur = cv2.GaussianBlur(img_test_gray,(5,5),0)
    Creat_nhiphan = cv2.threshold(candy_blur, 120, 200, cv2.THRESH_BINARY_INV)[1]
    edges = cv2.Canny(candy_blur,0,255)
    # edges = cv2.bitwise_not(edges)
    # phat hien va ve duong vien trong openCV
    ############################################
    ret,thresh = cv2.threshold(candy_blur,200,255,cv2.THRESH_BINARY)
    Contours,Contour_thresh = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    Contour_thresh_coppy = img_test.copy()
    # tinh dien tich cac diem muc dich la loai bo cac dien tich nho
    for contour in Contours:

        area = cv2.contourArea(contour)
        print(area)
        if area > 100:
         # xac dinh hinh dang bang xap xi duong vien
         approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
         count = len(approx)
         print(count)
         cv2.drawContours(Contour_thresh_coppy, contour, -1, (0, 255, 0), 1, cv2.LINE_4)
         M = cv2.moments(contour)
         print(M)
         # tinh toan tam
         cx = int(M['m10']/M['m00'])
         cy = int(M['m01']/M['m00'])
         cv2.putText(Contour_thresh_coppy,'DOG',(cx+50,cy+50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
         cv2.rectangle(Contour_thresh_coppy,((cx-50),(cy+60)),((cx+50),(cy-10)),(0,0,255),2)


    # nhan dien hinh anh bang mo dun DNN
    ##########################################
    img1 = Image.fromarray(Contour_thresh_coppy)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    canvas4.create_image(0, 0, anchor=NW, image=imgTK)
    canvas4.mainloop()

buton1 = Button(frame1,width=10,height=3,text='Chon Anh 1',command=chonanh1)
buton1.pack()
#buton1.grid(row=0,column=0)

buton2 = Button(frame2,width=10,height=3,text='Chon Anh 2',command=chonanh2)
buton2.pack()
#buton2.grid(row=0,column=1)

# buton3 = Button(frame3,width=10,height=3,text='Kiem Tra',command=kiemtra)
# buton3.grid(row=0,column=0)
label1 = Label(frame3, width=10, height=3, fg='blue', font=('Timenewroman', 14, 'bold'))
label1.grid(row=0,column=0)
label1.config(text="KET QUA",fg='green')
label = Label(frame3, width=10, height=3, fg='blue', font=('Timenewroman', 28, 'bold'))
label.grid(row=2,column=0)
label_error = Label(frame3, width=10, height=3, fg='black', font=('Timenewroman', 12, 'bold'))
label_error.grid(row=1,column=0)
# label3 = Label(frame3, width=10, height=3, fg='blue', font=('Timenewroman', 12, 'bold'))
# label3.grid(row=2,column=0)


buton4 = Button(frame4,width=10,height=3,text='Kiem Tra',command=catanh)
buton4.pack()

canvas1 = Canvas(frame1, width=319, height=200)
canvas1.pack()
#canvas1.grid(row=1,column=0)

canvas2 = Canvas(frame2, width=319, height=200)
canvas2.pack()
#canvas2.grid(row=1,column=1)
# canvas3 = Canvas(frame3, width=319, height=200)
# canvas3.pack()

canvas4 = Canvas(frame4, width=319, height=200)
canvas4.pack()


window.mainloop()