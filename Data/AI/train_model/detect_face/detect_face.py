import tensorflow as tf
import numpy as np
import cv2
import cvlib as cv

# tải model
model = tf.keras.models.load_model('saved_trained_model_anh_em.h5')

# mở webcam
cap = cv2.VideoCapture(0)

classes = ['son', 'lam','bao','than_rung','viet','Binh','ky','Rim',]


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

        # apply ảnh để suy luận
        conf = model.predict(face_crop)[0]  # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]

        # lấy nhãn của suy luận lớn nhất
        idx = np.argmax(conf)
        label = classes[idx]

        label = "{}: {:.2f}%".format(label, conf[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        # viết nhãn
        cv2.putText(frame, label, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # display output
    cv2.imshow("Detect Face", frame)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()