from tkinter import *
from tkinter import filedialog as f_dialog # lien quan thu muc
import cv2
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


#w_d = Tk()
#w_d.title('show anh Image')
#w_d.geometry('500x300')

#canvas1 = Canvas(w_d, width=500, height=300)
#canvas1.pack()

link = 'C:\\Users\\dsfg\\Desktop\\anh\\'
def roation():
    img = cv2.imread(link + 'img_1.png')
    height,width = img.shape[:2]
    center = (width/2,height/2)
    img_rotation = cv2.getRotationMatrix2D(center=center,angle=45,scale=1)
    imgcv = cv2.warpAffine(img,img_rotation,(width,height))
    #imgCV = cv2.resize(img_rotation,(200,300))
    #imgCV = cv2.cvtColor(img_rotation, cv2.COLOR_RGB2BGR)  # convert anh sang RGB

    img1 = Image.fromarray(imgcv)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    canvas1.create_image(0, 0, anchor=NW, image=imgTK)
    canvas1.mainloop()

def dichanh():
    img = cv2.imread(link + 'img_1.png')

    height = img.shape[0]
    width = img.shape[1]
    print(height)
    print(width)
    tx,ty = (50,80)
    M1 = np.array([[1,0,tx],[0,1,ty]],dtype= np.float32)
    center = (width/2,height/2)
    roatation_img = cv2.warpAffine(img,M1,(width,height))
    imgcv = roatation_img
    img1 = Image.fromarray(imgcv)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner

    canvas1.create_image(0, 0, anchor=NW, image=imgTK)
    canvas1.mainloop()
def biendoiAffine():
    img = cv2.imread(link + 'img_13.png')
    rows,cols,ch = img.shape

    pts1 = np.float32([[536,232],[1029,351],[898,408]])
    pts2 = np.float32([[506,371],[1029,351],[898,408]])

    M = cv2.getAffineTransform(pts1,pts2)
    img_affine = cv2.warpAffine(img,M,(cols,rows))
    plt.subplots(1),plt.imshow(img),plt.title('Input')
    for(x,y) in pts1:
        plt.scatter(x,y,s=50,c='White',marker='x')
    plt.subplots(1),plt.imshow(img_affine),plt.title('Output')
    for(x,y) in pts2:
        plt.scatter(x,y,s=50,c='White',marker='x')
    plt.show()
def chuthichanh():
    img = cv2.imread(link + 'img_13.png')
    img_line = img.copy()
    img_circle = img.copy()
    img_rectang = img.copy()
    img_elip = img.copy()
    img_text = img.copy()

    pointA = (400,120)
    pointB = (800,120)
    img_note = cv2.line(img_line,pointA,pointB,(255,255,0),thickness=3)
    img_circle = cv2.circle(img_circle,(600,195),150,(0,200,0),thickness=3)
    img_rectang = cv2.rectangle(img_rectang,(400,195),(800,350),(0,200,0), thickness=3)
    img_elip = cv2.ellipse(img_elip,(600,195),(150,100),0,0,360,(255,0,0), thickness= 3)
    img_text = cv2.putText(img_text,'Ngua',(600,195),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1.5,color=(255,0,0))
    plt.figure()
    plt.imshow(img_circle)
    plt.figure()
    plt.imshow(img_elip)
    plt.figure()
    plt.imshow(img_rectang)
    plt.figure()
    plt.imshow(img_text)
    plt.show()
#roation()
#dichanh()
#biendoiAffine()
chuthichanh()