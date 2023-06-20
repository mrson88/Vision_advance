import cv2
import tkinter
import numpy as np
import matplotlib.pyplot as plt
import continuous_threading

link = r'C:\Users\sev_user\Desktop\Python\\'
link1 = r'C:\Users\sev_user\Desktop\Python\anh\\'

img = cv2.imread(link+'img_2.png')

def doi_mau_cv2 ():# doi mau bang opencv
    img=cv2.imread(link+'img_2.png') #doc anh
    RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #doi ve mau RGB resd-green-blue
    BGR=cv2.cvtColor(img,cv2.COLOR_RGB2BGR) #doi ve mau BGR blue-Green-read
    Gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # doi ve mau xam
    #
    cv2.imshow('Anh_Goc',img) #hien thij anh
    cv2.imshow('RGB',RGB)
    cv2.imshow('BGR',BGR)
    cv2.imshow('Gray',Gray)
    cv2.waitKey(0) # thoi gian hien thi ( =0 la hien thij den khi nao tat)
    cv2.destroyAllWindows() # tu tat khi tat chuong trinh

# doi_mau_cv2()

def doi_mau_Plt ():
    img = cv2.imread(link + 'img_2.png')  # doc anh
    Gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # doi ve mau xam
    plt.figure() # tao truc x,y
    # plt.imshow(img) # hien thi anh
    plt.imshow(Gray)
    plt.show()

def phep_toan ():
    img1=cv2.imread(link+'img_1.png')
    img2=cv2.imread(link+'img_3.png')
    img1=cv2.resize(img1,(400,200))
    img2=cv2.resize(img2,(400,200))
    # Phep cong
    phep_cong=cv2.addWeighted(img1,1,img2,0.5,28)
    # #phep tru
    phep_tru=cv2.subtract(img1,img2)

    imgand = cv2.bitwise_and(img1,img2,mask=None)


    cv2.imshow('anh1',img1)
    cv2.imshow('anh2',img2)
    cv2.imshow('anh cong',phep_cong)
    cv2.imshow('anh tru',phep_tru)
    cv2.imshow('and',imgand)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # if cv2.waitKey(0) & 0xff == 27:
    #     cv2.destroyAllWindows()

# phep_toan()

def phep_toan_nhi_phan ():

    img1 = cv2.imread(link + 'img_1.png')
    img2 = cv2.imread(link + 'img_5.png')
    img1 = cv2.resize(img1, (400, 200))
    img2 = cv2.resize(img2, (400, 200))

    imgand = cv2.bitwise_and(img1, img2, mask=None)
    imgor=cv2.bitwise_or(img1,img2,mask=None)
    imgxor=cv2.bitwise_xor(img1,img2,mask=None)
    imgnot=cv2.bitwise_not(img2,mask=None)

    # cv2.imshow('anh1', img1)
    # cv2.imshow('anh2', img2)
    cv2.imshow('and', imgand)
    cv2.imshow('or',imgor)
    cv2.imshow('xor',imgxor)
    cv2.imshow('not',imgnot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def phep_toan_nhi_phan1 ():

    img1 = cv2.imread(link1 + '20230512114323_GrabImage.bmp')
    img2 = cv2.imread(link1 + '20230512114323_GrabImage.bmp')
    img1 = cv2.resize(img1, (800, 600))
    img2 = cv2.resize(img2, (800, 600))

    imgand = cv2.bitwise_and(img1, img2, mask=None)
    imgor=cv2.bitwise_or(img1,img2,mask=None)
    imgxor=cv2.bitwise_xor(img1,img2,mask=None)
    imgnot=cv2.bitwise_not(img2,mask=None)

    # cv2.imshow('anh1', img1)
    # cv2.imshow('anh2', img2)
    cv2.imshow('and', imgand)
    cv2.imshow('or',imgor)
    cv2.imshow('xor',imgxor)
    cv2.imshow('not',imgnot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

phep_toan_nhi_phan1()

def thay_doi_kich_thuoc_anh ():

    img = cv2.imread(link + 'img_2.png')  # doc anh
    img_thu_nho=cv2.resize(img,(300,200),interpolation=cv2.INTER_AREA) #thu nho
    img_phong_to=cv2.resize(img,(1920,1080),interpolation=cv2.INTER_CUBIC)#phong to
    img_ti_le_tang=cv2.resize(img,None,fx=1.5,fy=1.2,interpolation=cv2.INTER_LINEAR)
    nearest_ti_le_giam = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
    linear_ti_le_giam = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    area_ti_le_giam = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('anh goc',img)
    # cv2.imshow('Thu nho',img_thu_nho)
    # cv2.imshow('phong to',img_phong_to)
    cv2.imshow('N',nearest_ti_le_giam)
    cv2.imshow('L',linear_ti_le_giam)
    cv2.imshow('A',area_ti_le_giam)
    # cv2.imshow('tang',img_ti_le_tang)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def in_anh():
    img = cv2.imread(link + 'img_2.png')  # doc anh

    print(img.shape) # in ra mau sac RGB
    cv2.imshow('Anh',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def toa_do():
    img = cv2.imread(link + 'img_10.png')
    imgcv=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    plt.figure('Toa mau sac')
    plt.imshow(img)
    # plt.show()
    cv2.imshow('goc',img)
    cv2.imshow('imgcv',imgcv)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cat_anh():

    path=r'C:\Users\sev_user\Desktop\Luu_anh\\'
    img = cv2.imread(link + 'img_10.png')
    catanh= img[350:570,410:700]
    plt.figure()
    plt.imshow(img)

    cv2.imshow('sau cat', catanh)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite(f'{path}img_1000.png',catanh)

# cat_anh()

def xoay_anh():
    height,width = img.shape[:2]
    tam = (width/2, height/2)


    xoay_anh = cv2.getRotationMatrix2D(center=tam, angle=45, scale=1)
    img_xoay = cv2.warpAffine(src=img, M=xoay_anh, dsize=(width,height))
    cv2.imshow('ko xoay',img)
    cv2.imshow('xoay',img_xoay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('xoay.png',img_xoay)

# xoay_anh()

def dich_anh():
    cao=img.shape[0]
    rong=img.shape[1]
    print(cao)
    print(rong)
    tx, ty = (400,200)

    M1 = np.array([[1,0,tx],
                   [0,1,ty]],dtype=np.float32)
    tam =(cao/1,rong/1)
    dich_anh = cv2.warpAffine(src=img, M=M1, dsize=(rong,cao))
    plt.figure('goc') # ten hien thi anh goc
    plt.imshow(img) # nguon anh
    plt.figure('dichj_anh') # ten hien thi anh dic
    plt.imshow(dich_anh) # nguon anh dich
    cv2.imshow('dich_anh',dich_anh) # hien thi anh dic = cv2
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# dich_anh()


def bien_doi():

    rows,cols,ch = img.shape
    pts1 = np.float32([[50,50], [200,50], [50,200]])
    pts = np.float32([[50,50], [350,50], [50,350],[500,500]])

    pts2 = np.float32([[50,300],[200,150],[150,400]])

    M= cv2.getAffineTransform(pts2,pts1)
    M1= cv2.getPerspectiveTransform(pts,pts)

    img_bien_doi = cv2.warpAffine(img,M,(cols,rows))
    img_bien_doi1 = cv2.warpPerspective(img,M1,(700,500))


    plt.subplot(2,2,1),plt.imshow(img),plt.title('Input')
    for (x,y) in pts1:
        plt.scatter(x,y,s=50,c='white',marker='x')

    plt.subplot(2,2,2),plt.imshow(img_bien_doi),plt.title('Output')
    for (x,y) in pts2:
        plt.scatter(x,y,s=50, c='white', marker='x')

    plt.subplot(2, 2, 3), plt.imshow(img_bien_doi1), plt.title('Output1')
    for (x, y) in pts2:
        plt.scatter(x, y, s=50, c='white', marker='x')

    plt.show()


# bien_doi()

def coppy():
    img=cv2.imread(link+'img_6.png')
    imgline=img.copy()
    print(imgline)
    cv2.imshow('',imgline)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# coppy()


def ve_duong_thang():
    img = cv2.imread(link + 'img_6.png')
    imgline = img.copy()
    pointA=(200,80)
    pointB=(450,80)
    cv2.line(imgline,pointA,pointB,(255,255,0),thickness=1)
    cv2.imshow('', imgline)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ve_duong_thang()



def duong_tron():
    img = cv2.imread(link + 'img_6.png')
    imgline = img.copy()
    tam_duong_tron=(315,190)
    duong_kinh=50
    cv2.circle(imgline,tam_duong_tron,duong_kinh,(0,0,255),thickness=-1)
    cv2.circle(imgline,(315,190),100,(0,255,0),thickness=2)
    cv2.imshow('', imgline)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# duong_tron()


def hinh_chu_nhat():
    img = cv2.imread(link + 'img_6.png')
    imgline = img.copy()
    start_point =(291,81)
    end_point=(520,388)

    cv2.rectangle(imgline,start_point,end_point,(0,255,0),thickness=1)
    cv2.imshow('Hinh chu nhat', imgline)
    plt.figure()
    plt.imshow(imgline)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# hinh_chu_nhat()


def elip():
    img = cv2.imread(link + 'img_6.png')
    imgline = img.copy()
    tam =(419,224)
    trucY=(100,150)

    tam1 = (400, 52)
    text='Dog'

    cv2.ellipse(imgline,tam,trucY,0,360,0,(0,255,0),thickness=1)
    cv2.putText(imgline,text,tam1,fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,250,0))

    cv2.imshow('Elip', imgline)
    plt.figure()
    plt.imshow(imgline)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('elip.jpg',imgline)

# elip()


def ko_gian_Mau():
    img = cv2.imread(link + 'img.png')
# Khai bao
    lower_green = np.array([0, 108, 200])
    upper_green = np.array([10, 255, 255])

    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv,lower_green,upper_green)
    res= cv2.bitwise_and(img,img,mask=mask)


    plt.figure()#bang

    plt.subplot(3,3,1)
    plt.imshow(img)
    plt.title('img')

    plt.subplot(3, 3, 4)
    plt.imshow(mask)
    plt.title('Mask_img')

    plt.subplot(3, 3, 2)
    plt.imshow(hsv)
    plt.title('hsv_img')

    plt.subplot(3, 3, 3)
    plt.imshow(res)
    plt.title('res_img')


    plt.show()


# ko_gian_Mau()


def loc_hinh_anh():
    img=cv2.imread(link+'img_6.png')

    kernel1= np.array([[0,0,0],
                       [0,1,0],
                       [0,0,0]])

    identity = cv2.filter2D(src=img,ddepth=-1,kernel=kernel1)

    kernel2 = np.array([[-1, -1, -1],
                        [-1, 8, -1],
                        [-1, -1, -1]])
    dentity1 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel2)


    loc_song_phuong=cv2.bilateralFilter(src=img,d=9,
                                        sigmaColor=75,sigmaSpace=75)

    lam_mo = np.ones((5, 5), np.float32) / 25
    mo = cv2.filter2D(src=img,ddepth=-1,kernel=lam_mo)

    cv2.imshow('truoc_loc',img)
    cv2.imshow('anh_loc',identity)
    cv2.imshow('anh_loc1',dentity1)
    cv2.imshow('loc_song_phuong.png',loc_song_phuong)
    cv2.imshow('lam_mo',mo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('lam_mo.png',mo)


# loc_hinh_anh()


def nguong_cua_anh():

    src=cv2.imread(link+'img_12.png')
    img=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
    thresh=128
    thresh1 = 50
    maxValue=255
    dst = cv2.threshold(img,thresh,maxValue,cv2.THRESH_BINARY)[1]
    res = cv2.bitwise_and(src, src, mask=dst)
    doi_mau=cv2.threshold(img,thresh,maxValue,cv2.THRESH_BINARY_INV)[1]
    nguong_cat_bot = cv2.threshold(img, thresh1, maxValue, cv2.THRESH_TRUNC)[1]

    thresh2 = 180
    nguong_ve_ko = cv2.threshold(img, thresh2, maxValue, cv2.THRESH_TOZERO)[1]

    # so sanh
    so_sanh = cv2.bitwise_and(dst, nguong_ve_ko, mask=None)
    so_sanh = cv2.bitwise_and(src, res, mask=None)
    # so_sanh=cv2.subtract(doi_mau,nguong_ve_ko)
    # imgor = cv2.bitwise_or(img1, img2, mask=None)
    # imgxor = cv2.bitwise_xor(img1, img2, mask=None)
    # imgnot = cv2.bitwise_not(img1, img2, mask=None)



    plt.subplot(3,3,1)
    plt.imshow(src)
    plt.title('anh goc')

    plt.subplot(3,3,2)
    plt.imshow(dst)
    plt.title('anh den trang')

    plt.subplot(3,3,3)
    plt.imshow(doi_mau)
    plt.title('anh trang den')

    plt.subplot(3,3,4)
    plt.imshow(res)
    plt.title('mat la')

    plt.subplot(3,3,5)
    plt.imshow(nguong_cat_bot)
    plt.title('cat bot')

    plt.subplot(3,3,6)
    plt.imshow(img)
    plt.title('con vot')

    plt.subplot(3,3,7)
    plt.imshow(nguong_ve_ko)
    plt.title('ve khong')





    cv2.imshow('goc',src)
    cv2.imshow('den trang',dst)
    cv2.imshow('trang den',doi_mau)
    cv2.imshow('Mat la',res)
    cv2.imshow('cat bot',nguong_cat_bot)
    cv2.imshow('Cv',img)
    cv2.imshow('ve ko',nguong_ve_ko)
    cv2.imshow('so sanh',so_sanh)

    # plt.show()

    cv2.waitKey(0)
    # if cv2.waitKey(0) & 0xff==27:
    #     cv2.destroyAllWindows()


# nguong_cua_anh()

def block():
    img=cv2.imread(link+'img_9.png',cv2.IMREAD_COLOR)
    params=cv2.SimpleBlobDetector_Params()
    params.filterByArea=True
    params.minArea=0.1
    params.maxArea=1500

    params.filterByCircularity=True
    params.minCircularity=0.001

    params.filterByConvexity=True
    params.minConvexity=0.01

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints=detector.detect(img)
    blank = np.zeros((1,1))
   # blobs = cv2.drawKeypoints(img,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

    number_of_blobs=len(keypoints)
    text="dog"+str(number_of_blobs)
    cv2.putText(blobs,text,(10,100),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

    cv2.imshow('anh goc',img)
    cv2.imshow('anh block',blobs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# block()

def so_sanh():
    img1=cv2.imread(link+'img_4.png')
    img2=cv2.imread(link+'img_5.png')
    va=cv2.bitwise_and(img1,img2,mask=None)

    cv2.imshow('',va)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

# so_sanh()

def phat_hien_canh():
    img=cv2.imread(link+'img_6.png')
    img_xam=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)#chuyen anh ve mau xam
    img_blur=cv2.GaussianBlur(img_xam,(5,5),0)#lam mo
    edges=cv2.Canny(image=img_blur, threshold1=255,threshold2=10)# chuyen ve anh den trang
    # doi_mau = cv2.threshold(img, thresh, maxValue, cv2.THRESH_BINARY_INV)[1]
    edges=cv2.threshold(img_blur,100,255,cv2.THRESH_BINARY)[1]
    contours, hierarchy=cv2.findContours(image=edges,mode=cv2.RETR_LIST,
                                         method=cv2.CHAIN_APPROX_NONE)#tim duong vien
    img_copy=img.copy()
    for contour in contours: #tim vung
        area=cv2.contourArea(contour)# quy doi
        print(area) #in vung cua con tua
        if area >30000: # chon vung lon hon 30000 thi ve vien
            duong_thang=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) # Kieu duong
            count=len(duong_thang)
            print(count)
            cv2.drawContours(image=img_copy, contours=contour, contourIdx=-1,
                             color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)  # Ve duong vien vao anh coppy
            # M=cv2.moments(contours)
            # print(f'gia tri cua contourn0':{M}')
            #tinh toan tam cua contourn0
            # cx=int()




    cv2.imshow('img canh',edges)
    cv2.imshow('img goc',img)
    cv2.imshow('lam mo',img_blur)
    cv2.imshow('img vien',img_copy)
    cv2.waitKey(0)
    # print(img_copy)

# phat_hien_canh()

def video():
    cap= cv2.VideoCapture(0) # lenh mo camera
    if not cap.isOpened():
        print('khong nhan camera')
    while True:
        ret, frame = cap.read()
        if not ret:
            print('khong nhan duoc hinh anh')
        cv2.imshow('cam',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

# video()

cap = cv2.VideoCapture(0)


# i = 0 # so de luu anh
def chup_anh():
    # wd1 = Tk()  # tao cua so
    # wd1.title('Canh Bao')  # dat ten anh
    # wd1.geometry('200x200')  # tao khung anh


    global i
    ret, img = cap.read() # doc anh
    path= r'C:\Users\sev_user\Desktop\Luu_anh\\' # Dia chi luu anh
    if ret:
        cv2.imwrite(f'{path}img_{i}.png',img) # Lwnh ghi anh
    # chup_anh()

# thread= continuous_threading.PeriodicThread(2,chup_anh)# thoi gian chup 2 giay, truong trinh chup anh
# thread.start()



