import matplotlib.pyplot as plt
import cv2

link = 'C:\\Users\\dsfg\\Desktop\\anh\\'

img = cv2.imread(link + 'bgr.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

plt.figure()
plt.imshow(img)
plt.show()