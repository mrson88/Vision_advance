import cv2
import matplotlib.pyplot as plt
import tkinter as tk

link = 'C:\\Users\\dsfg\\Desktop\\anh\\'
link2 = r'C:\Users\dsfg\Desktop\anh\\'

img = cv2.imread(link + 'img.png')
scale_up_x = 1.2
scale_up_y = 1.2
scale_down = 2
scaled_f_down = cv2.resize(img,None,fx=scale_down,fy=scale_down,interpolation=cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(img,None,fx=scale_up_x,fy=scale_up_y,interpolation=cv2.INTER_LINEAR)
res_inter_nearest = cv2.resize(img,None,fx=scale_down,fy=scale_down,interpolation=cv2.INTER_NEAREST)
res_inter_linenear = cv2.resize(img,None,fx=scale_down,fy=scale_down,interpolation=cv2.INTER_LINEAR)
res_inter_area = cv2.resize(img,None,fx=scale_down,fy=scale_down,interpolation=cv2.INTER_AREA)
#cv2.imshow('nearest',res_inter_nearest)
#cv2.imshow('linear',res_inter_linenear)
#cv2.imshow('area',res_inter_area)

print(img.shape)

#cv2.imshow('Anh Thu Nho',scaled_f_down)
#cv2.imshow('Anh Phong To',scaled_f_up)
#img1 = cv2.imread(link + 'img_1.png')
#img2 = cv2.imread(link + 'img_3.png')

#addimage = cv2.addWeighted(img1,0.5,img2,0.5,10)
down_point = (300,200)
img1 = cv2.imread(link + 'img_22.png')
img1 = cv2.resize(img1,down_point,interpolation=cv2.INTER_LINEAR)
img2 = cv2.imread(link + 'img_23.png')
img2 = cv2.resize(img2,down_point,interpolation=cv2.INTER_LINEAR)

#addimage = cv2.subtract(img1,img2) # tru anh
addimage = cv2.bitwise_and(img1,img2,mask= None)
#addimage = cv2.bitwise_or(img1,img2,mask= None)
#addimage = cv2.bitwise_xor(img1,img2,mask= None)
#addimage = cv2.bitwise_not(img1,mask= None)



cv2.imshow('MRBAT',addimage)
#img1 = cv2.imread(link2 + 'img_1.jpg')
#RGB_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#cv2.imwrite('mrbat5.png',img)
#cv2.imshow('image',img)
#cv2.imshow('MRBAT',img1)
#plt.figure()
#plt.imshow(img)
#plt.figure()
#plt.imshow(RGB_img)
#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

