import zipfile

# Download zip vision_basic
#https://storage.googleapis.com/ztm_tf_course/food_vision/pizza_steak.zip

# giải nen vision_basic
# zip_ref = zipfile.ZipFile("pizza_steak.zip", "r")
# zip_ref.extractall()
# zip_ref.close()
import os
# Walk through pizza_steak directory and list number of files
# for dirpath, dirnames, filenames in os.walk("pizza_steak"):
#   print(f"Có {len(dirnames)} thư mục và {len(filenames)} ảnh trong '{dirpath}'.")

# num_steak_images_train = len(os.listdir("pizza_steak/train/steak"))
# print(num_steak_images_train)

import pathlib
import numpy as np
data_dir = pathlib.Path("../anh_train/pizza_steak/pizza_steak/train/") # biến đường dẫn đào tạo
class_names = np.array(sorted([item.name for item in data_dir.glob('*')])) #  tạo danh sách tên_lớp từ thư mục con
print(class_names)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def view_random_image(target_dir, target_class):
  # Thiết lập thư mục đích
  target_folder = target_dir+target_class

  # Nhận đường dẫn ảnh ngẫu nhiên
  random_image = random.sample(os.listdir(target_folder), 1)

  #  Đọc hình ảnh và vẽ đồ thị bằng matplotlib
  img = mpimg.imread(target_folder + "/" + random_image[0])
  plt.imshow(img)
  plt.title(target_class)
  plt.axis("off")
  plt.show()

  print(f"Image shape: {img.shape}") # hiển thị ảnh

  return img
img = view_random_image(target_dir="../anh_train/pizza_steak/pizza_steak/train/", target_class="steak")
img = img/255
print(img)
