# import os
# for dirpath,dirnames,filenames in os.walk("pizza_steak"):
#     print(f"Có {len(dirnames)} thư mục và {len(filenames)} ảnh trong '{dirpath}'.")
import os
import pathlib
import random
import tensorflow as tf

# import numpy as np
# data_dir=pathlib.Path('pizza_steak/train/')
# class_names=np.array(sorted([item.name for item in data_dir.glob('*')]))
# print(class_names)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def view_random_img(taget_dir,target_class):
    target_folder=taget_dir+target_class
    random_img=random.sample(os.listdir(target_folder),1)

    img=mpimg.imread(target_folder+ "/" + random_img[0])
    plt.imshow(img)
    plt.title(target_class)
    plt.axis('off')
    plt.show()
    print(f"Image shape: {img.shape}")

    return img
# img= view_random_img(taget_dir="pizza_steak/train/",target_class="steak")
# img=img/255
# print(img)

tf.random.set_seed(42)

train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
valid_datagen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_dir="pizza_steak/train/"
test_dir="pizza_steak/test/"



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


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=10, # số lượng bộ lọc
                         kernel_size=3, #kích thước nhân
                         activation="relu",
                         input_shape=(224, 224, 3)), # lớp đầu tiên chỉ định hình dạng đầu vào
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=2,
                            padding="valid"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),

    tf.keras.layers.MaxPool2D(pool_size=2,
                              padding="valid"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),

    tf.keras.layers.MaxPool2D(pool_size=2,
                              padding="valid"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),

    tf.keras.layers.MaxPool2D(pool_size=2,
                              padding="valid"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),

    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(4096, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1, activation="sigmoid") # 1 đầu ra  kích hoạt nhị phân
])

# biên dịch model
model_1.compile(loss="binary_crossentropy",
              optimizer=tf.keras.optimizers.Adam(),
              metrics=["accuracy"])

# Fit model
history_1 = model_1.fit(train_data,
                        epochs=5,
                        steps_per_epoch=len(train_data),
                        validation_data=valid_data,
                        validation_steps=len(valid_data))

model_1.summary()
model_1.save("saved_trained_model_1")
loaded_model_1 = tf.keras.models.load_model("saved_trained_model_1")
loaded_model_1.evaluate(valid_data)
def plot_loss_curves(history):
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']

  epochs = range(len(history.history['loss']))

  # Plot mất mát
  plt.plot(epochs, loss, label='training_loss')
  plt.plot(epochs, val_loss, label='val_loss')
  plt.title('Loss')
  plt.xlabel('Epochs')
  plt.legend()

  # Plot độ chính xác
  plt.figure()
  plt.plot(epochs, accuracy, label='training_accuracy')
  plt.plot(epochs, val_accuracy, label='val_accuracy')
  plt.title('Accuracy')
  plt.xlabel('Epochs')
  plt.legend()
  plt.show()
plot_loss_curves(history_1)