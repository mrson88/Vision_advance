import tensorflow as tf
import numpy as np
import cvlib as cv
import cv2
import continuous_threading
# tải model
# model = tf.keras.models.load_model('detect_face_1.h5')

# mở webcam
cap = cv2.VideoCapture(0)

# classes = ['man', 'woman']
t=0
def nothing():
    global t
    ret, img2 = cap.read()
    img2_cut=img2[startX:startY,endX:endY]
    t=t+1
    ten='son/'+str(t)+'.jpg'
    print(ten)
    cv2.imwrite(ten,img2_cut)
    if t == 1000:
        thread.stop()


while cap.isOpened():

    # đọc ảnh
    status, frame = cap.read()

    # Chạy hàm nhận diện khuôn mặt trên cvlib cho ảnh ầu vào
    face, confidence = cv.detect_face(frame)

    # lặp quá trình nhân diện khuôn mặt
    for id, f in enumerate(face):

        # get corner points of face rectangle
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # vẽ hình bao cho khuôn mặt
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

        # cắt khuôn mặt
        face_crop = np.copy(frame[startY:endY, startX:endX])

        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue

        # xoử lý ảnh để cho và model
        face_crop = cv2.resize(face_crop, (224, 224))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = tf.keras.preprocessing.image.img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)
    thread = continuous_threading.PeriodicThread(0.1, target=nothing)
    thread.start()


    # display output
    cv2.imshow("Detect Face", frame)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()