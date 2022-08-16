from feat import Detector

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='svm',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)





def predict_img(img_path):
    prediction = detector.detect_image(img_path)
    ret = dict()
    for k in prediction:
        ret[k] = str(prediction[k][0])
    return ret