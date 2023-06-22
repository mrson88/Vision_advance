import cv2
from tkinter import *
from PIL import Image, ImageTk
import continuous_threading
def video():
    ret,img1 = cap.read()
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(img1)  # tao mang de chuyen anh
    imgTK = ImageTk.PhotoImage(img1)  # chuyen anh tu cv2 sang tkiner
    label.imgTK = imgTK
    label.config(image=imgTK)
    label.after(10, video)
def nothing():
    global t
    ret, img2 = cap.read()
    t=t+1
    ten='ky/'+str(t)+'.jpg'
    print(ten)
    cv2.imwrite(ten,img2)
    if t == 1000:
        thread.stop()
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Khong nhan dien duoc CAM')
t=0
wd = Tk()
label = Label(wd, width=800, height=600)
label.pack()
thread=continuous_threading.PeriodicThread(0.1, target=nothing)
thread.start()

video()
wd.mainloop()
