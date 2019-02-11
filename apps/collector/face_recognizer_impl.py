import face_recognition
import numpy

from apps.collector.face_recognizer import FaceRecognizer


class FaceRecognizerImpl(FaceRecognizer):

    def extract_face_locations(self, image: numpy.array):
        return face_recognition.face_locations(image)

    def compare_faces(self, candidate_faces: list, face_to_test: numpy.array):
        encoded_candidate_faces = []
        for candidate_face in candidate_faces:
            face_location = [0, candidate_face.shape[1], candidate_face.shape[0], 0]
            encoded_candidate_faces.append(face_recognition.face_encodings(
                candidate_face, known_face_locations=[face_location])[0])

        face_location = [0, face_to_test.shape[1], face_to_test.shape[0], 0]
        encoded_face_to_test = face_recognition.face_encodings(
            face_to_test, known_face_locations=[face_location])[0]

        return face_recognition.compare_faces(encoded_candidate_faces, encoded_face_to_test)
