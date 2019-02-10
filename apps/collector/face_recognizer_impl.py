import face_recognition
import numpy

from apps.collector.face_recognizer import FaceRecognizer


class FaceRecognizerImpl(FaceRecognizer):

    def extract_face_locations(self, image: numpy.array):
        return face_recognition.face_locations(image)

    def compare_faces(self, candidate_faces: list, face_to_test: numpy.array):
        return face_recognition.compare_faces(candidate_faces, face_to_test)


def test():
    doctor_path = '../../resources/images/doctor.jpg'
    image_doctor = face_recognition.load_image_file(doctor_path)
    impl = FaceRecognizerImpl()
    locations = impl.extract_face_locations(image_doctor)
    print(locations)


if __name__ == '__main__':
    test()
    pass
