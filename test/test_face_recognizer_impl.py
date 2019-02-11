import unittest

import numpy
from PIL import Image

from apps.collector.face_recognizer_impl import FaceRecognizerImpl


def get_recognizer():
    return FaceRecognizerImpl()


def open_image_in_np_array(image_file):
    image = Image.open(image_file)
    return numpy.array(image)


class TestFaceRecognizer(unittest.TestCase):

    def test_face_extraction(self):
        images_with_faces = [r'./images/doctor.jpg']
        instance = get_recognizer()

        for image_file in images_with_faces:
            image = Image.open(image_file)
            image_pixels = numpy.array(image)

            face_locations = instance.extract_face_locations(image_pixels)
            self.assertGreater(len(face_locations), 0)

    def test_face_compare(self):
        doctor_path = r'./images/doctor.jpg'
        thor01_path = r'./images/Thor01.jpg'
        thor02_path = r'./images/Thor02.jpg'
        instance = get_recognizer()

        image_doctor = open_image_in_np_array(doctor_path)
        image_thor01 = open_image_in_np_array(thor01_path)
        image_thor02 = open_image_in_np_array(thor02_path)

        result = instance.compare_faces([image_thor01, image_doctor], image_thor02)

        self.assertEqual(len(result), 2)
        self.assertTrue(result[0])
        self.assertFalse(result[1])


if __name__ == '__main__':
    unittest.main()
