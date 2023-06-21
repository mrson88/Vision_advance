import tensorflow as tf
import matplotlib.pyplot as plt
# giá trị ngẫu nhiên cố định
import pathlib
import numpy as np

tf.random.set_seed(42)
data_dir = pathlib.Path("../anh_train/human_dataset/train")  # biến đường dẫn đào tạo
class_names = np.array(sorted([item.name for item in data_dir.glob('*')]))  # tạo danh sách tên_lớp từ thư mục con
# print(class_names)
# # Dữ liệu tiền xử lý (lấy tất cả các giá trị pixel từ 1 đến 0, còn được gọi là chia tỷ lệ/chuẩn hóa)
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)
valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

# Nhập dữ liệu từ các thư mục và biến nó thành các lô
train_dir = "../anh_train/human_dataset/train/"
test_dir = "../anh_train/human_dataset/test/"

# Nhập dữ liệu từ các thư mục và biến nó thành các lô
train_data = train_datagen.flow_from_directory(train_dir,
                                               batch_size=32,  # số ảnh cần xử lý tại một thời điểm
                                               target_size=(224, 224),  # chuyển đổi tất cả ảnh thành 224 x 224
                                               class_mode="binary",  # phân loại nhị phân
                                               seed=42)

valid_data = valid_datagen.flow_from_directory(test_dir,
                                               batch_size=32,
                                               target_size=(224, 224),
                                               class_mode="binary",
                                               seed=42)


def load_and_prep_image(filename, img_shape=224):
    # Đọc trong tệp đích (một hình ảnh)
    img = tf.io.read_file(filename)

    # # Giải mã vision_basic đọc thành tensor & đảm bảo 3 kênh màu
    img = tf.image.decode_image(img, channels=3)

    # Thay đổi kích thước hình ảnh
    img = tf.image.resize(img, size=[img_shape, img_shape])

    # Thay đổi tỷ lệ hình ảnh (nhận tất cả các giá trị từ 0 đến 1)
    img = img / 255.
    return img


loaded_model_11 = tf.keras.models.load_model("saved_trained_model_4")
print(loaded_model_11.evaluate(valid_data))
# Tải  hình ảnh

def predict(img):
    pred = loaded_model_11.predict(tf.expand_dims(img, axis=0))
    pred_class = class_names[int(tf.round(pred)[0][0])]
    # print(pred_class)
    # plt.imshow(img)
    # plt.title(pred_class)
    # plt.axis(False)
    # plt.show()
    return pred_class
# img = load_and_prep_image("../anh_test/pizza3.jpeg")
#
# # dự đoán
# pred = loaded_model_11.predict(tf.expand_dims(img, axis=0))
#
# # Khớp lớp dự đoán với xác suất dự đoán cao nhất
# pred_class = class_names[int(tf.round(pred)[0][0])]
# print(pred_class)
# plt.imshow(img)
# plt.title(pred_class)
# plt.axis(False)
# plt.show()
