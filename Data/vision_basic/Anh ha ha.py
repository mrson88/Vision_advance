import cv2
img = cv2.imread(r'C:\Users\A0G\Desktop\HA HA DHB\img.png')
cv2.imshow('image',img)
cv2.imwrite('A1.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
