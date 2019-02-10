import abc
import numpy


class FaceRecognizer(abc.ABC):

    @abc.abstractmethod
    def extract_face_locations(self, image: numpy.array):
        """
        Extract face locations, which are rectangles represented in the style of
        [top-left.x, top-left.y, bot-right.x, bot-right.y], from :param image

        :param image: image contains faces which going to be extracted
        :return: face locations
        """
        pass

    @abc.abstractmethod
    def compare_faces(self, candidate_faces: list, face_to_test: numpy.array):
        """
        Compare face_to_test with the candidate_faces to see if face_to_test
        is an image of the same candidate face

        :param candidate_faces: a list of candidate faces
        :param face_to_test: face going to be compared with the candidate_faces
        :return: a list of bool values, each of them indicates that if the
        candidate face is from the same guy with face_to_test or not
        """
        pass
