import cv2
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

url = 'https://i.imgur.com/1vzDG2J.jpg'


def _downloadImage(url):
    resp = requests.get(url)
    img = np.asarray(bytearray(resp.content), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img


img = _downloadImage('https://i0.wp.com/cdn-images-1.medium.com/max/2400/1*LmxW8FDfXZJl5yvESvjP7Q.jpeg?resize=660%2C373&ssl=1')
# Chuyển đổi sang ảnh gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Chuyển sang ảnh nhị phân
_, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
plt.imshow(img)
# Tìm kiếm contours trên ảnh nhị phân
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#plt.show()

# Tìm ra diện tích của toàn bộ các contours
area_cnt = [cv2.contourArea(cnt) for cnt in contours]
area_sort = np.argsort(area_cnt)[::-1]
# Top 5 contour có diện tích lớn nhất
print(area_sort[:5])


# Vẽ bounding box cho contours có diện tích lớn thứ 2
cnt = contours[area_sort[7]]
x,y,w,h = cv2.boundingRect(cnt)
print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
plt.imshow(img)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(100,100,100),2)
plt.imshow(img)

(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)
plt.imshow(img)
plt.show()
