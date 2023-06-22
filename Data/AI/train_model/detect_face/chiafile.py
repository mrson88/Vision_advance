import numpy as np
import cv2
import cvlib as cv
import os
import shutil
path1="D:\\pythonProject3\\Anh em\\train\\"
path2="D:\\pythonProject3\\Anh em\\test\\"
t=os.listdir(path1)
for i in t:
    oldforder=path1+i
    newfolder=path2+i
    os.makedirs(newfolder)
    t1=os.listdir(oldforder)
    for j in range(0,300):
        file1=os.path.join(oldforder,t1[j])
        file2=os.path.join(newfolder,t1[j])
        shutil.move(file1,file2)
