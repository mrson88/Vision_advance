import tensorflow as tf
import matplotlib.pyplot as plt

# giá trị ngẫu nhiên cố định
# tf.random.set_seed(42)

# # Dữ liệu tiền xử lý (lấy tất cả các giá trị pixel từ 1 đến 0, còn được gọi là chia tỷ lệ/chuẩn hóa)
train_datagen_augmented = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, rotation_range=20,
                                                                          shear_range=0.2,
                                                                          zoom_range=0.2,
                                                                          width_shift_range=0.2,
                                                                          height_shift_range=0.2,
                                                                          horizontal_flip=True)
valid_datagen_augmented = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, rotation_range=20,
                                                                          shear_range=0.2,
                                                                          zoom_range=0.2,
                                                                          width_shift_range=0.2,
                                                                          height_shift_range=0.2,
                                                                          horizontal_flip=True)
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)
valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

# Nhập dữ liệu từ các thư mục và biến nó thành các lô
train_dir = "../anh_train/human_hourse/horse-or-human/train"
test_dir = "../anh_train/human_hourse/horse-or-human/validation"

# Nhập dữ liệu từ các thư mục và biến nó thành các lô

train_data_augmented = train_datagen_augmented.flow_from_directory(train_dir,
                                                         batch_size=32,  # số ảnh cần xử lý tại một thời điểm
                                                         target_size=(224, 224),
                                                         # chuyển đổi tất cả ảnh thành 224 x 224
                                                         class_mode="binary",  # phân loại nhị phân
                                                         shuffle=True
                                                         )

valid_data_augmented = valid_datagen_augmented.flow_from_directory(test_dir,
                                                         batch_size=32,
                                                         target_size=(224, 224),
                                                         class_mode="binary",
                                                         shuffle=True
                                                         )

model_4 = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=10,  # số lượng bộ lọc
                           kernel_size=3,  # kích thước nhân
                           activation="relu",
                           input_shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation="sigmoid"),  # 1 đầu ra  kích hoạt nhị phân
])
# biên dịch model
model_4.compile(loss="binary_crossentropy",
                optimizer=tf.keras.optimizers.Adam(),
                metrics=["accuracy"])

# Fit model
history_4 = model_4.fit(train_data_augmented,
                        epochs=25,
                        steps_per_epoch=len(train_data_augmented),
                        validation_data=valid_data_augmented,
                        validation_steps=len(valid_data_augmented))

model_4.summary()
model_4.save("saved_trained_model_human_hourse")

loaded_model_4 = tf.keras.models.load_model("saved_trained_model_human_hourse")
loaded_model_4.evaluate(valid_data_augmented)


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


# plot_loss_curves(history_1)
plot_loss_curves(history_4)
