import tensorflow as tf

import matplotlib.pyplot as plt
# giá trị ngẫu nhiên cố định
tf.random.set_seed(42)

# # Dữ liệu tiền xử lý (lấy tất cả các giá trị pixel từ 1 đến 0, còn được gọi là chia tỷ lệ/chuẩn hóa)
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

# Nhập dữ liệu từ các thư mục và biến nó thành các lô
train_dir = "../anh_train/pizza_steak/pizza_steak/train/"
test_dir = "../anh_train/pizza_steak/pizza_steak/test/"

# Nhập dữ liệu từ các thư mục và biến nó thành các lô
train_data = train_datagen.flow_from_directory(train_dir,
                                               batch_size=32, # số ảnh cần xử lý tại một thời điểm
                                               target_size=(224, 224), # chuyển đổi tất cả ảnh thành 224 x 224
                                               class_mode="binary", # phân loại nhị phân
                                               seed=42)

valid_data = valid_datagen.flow_from_directory(test_dir,
                                               batch_size=32,
                                               target_size=(224, 224),
                                               class_mode="binary",
                                               seed=42)

model_3 = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=(224, 224, 3)),
  tf.keras.layers.Dense(100, activation='relu'),
  tf.keras.layers.Dense(100, activation='relu'),
  tf.keras.layers.Dense(100, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model_3.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.Adam(),
              metrics=["accuracy"])

# Fit the model
history_3 = model_3.fit(train_data,
                        epochs=5,
                        steps_per_epoch=len(train_data),
                        validation_data=valid_data,
                        validation_steps=len(valid_data))

model_3.summary()
