from tkinter import *
from PIL import  Image, ImageTk
from tkinter import filedialog as f_d # mo foder
import  cv2
link = r'C:\Users\A0G\Desktop\HA HA DHB\\'
wd = Tk('')# tao cua so
wd.title('show anh image')#dat ten anh
wd.geometry('460x480')# tao khung anh
img = cv2.imread(link +'img_2.png') #doc anh
img = cv2.resize(img,(640, 480))# quy chuan khich thuoc anh
imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # quy chuan ve mau sac mong muon
img1 = Image.fromarray(imgcv) #tao mang anh
imgTk = ImageTk. PhotoImage(img1) #chuyen anh tu cv2
# lb = Label(wd, width=640, height=480)
# lb.pack(padx=1, pady=1)
# lb.config(image=imgTk)
 canvas = Canvas(wd, width=640, height=480)
 canvas.pack(padx=1, pady=1)
# canvas.create_image(0, 0, anchor=NW, image = imgTk)
# canvas.create_image(0, 0, image = imgTk)
def chonanh():
    file = f_d.askopenfile()#chon foder
    print(type(file.name))
bt = Button(wd, width=15, height=3, text='Chon Anh', command=chonanh)
bt.pack()



wd.mainloop()