import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

# link = r'C:\Users\sev_user\Desktop\Luu_anh\\'
#
# img = cv2.imread(link+'img_0.png')
# plt.figure('')
# plt.imshow(img)
# plt.show()


wd = Tk('') #khai bao cua so
wd.title('cua so anh') # dat ten cua so
wd.geometry('800x600') # kich thuoc cua so

lbx=Label(wd,text="Toa do X")
lbx.grid(column=0,row=0)

lby=Label(wd,text="Toa do Y")
lby.grid(column=0,row=1)

txtx=Entry(wd,width=10)
txtx.grid(column=1,row=0)

txty=Entry(wd,width=10)
txty.grid(column=1,row=1)

txtx.focus()
txty.focus()

# x = txtx.get()
# y = txty.get()


def an ():
    x = txtx.get()
    y = txty.get()
    print(x)
    print(y)
    thongbao.insert(INSERT, 'Luu thanh cong')
    thongbao.configure(fg='green')
    # if x > 0 :
    #     thongbao.insert(INSERT, 'Luu thanh cong')
    #     thongbao.configure(fg=green)
    # else:
    #     thongbao.insert(INSERT, 'kiem tra lai')
    #     thongbao.configure(fg=red)



bt=Button(wd,text="Luu lai",bg='green', command= an)
bt.grid(column=0,row=2)
thongbao=Text(wd,height=1,width=20)
thongbao.grid(column=1,row=2)

# txt=Entry(wd,width=20,state='disabled')




wd.mainloop()