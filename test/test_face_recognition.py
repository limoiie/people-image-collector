import unittest
import face_recognition

from PIL import Image

from apps.collector.utils import show_image


def convert_location_style(location):
    """
    convert location style from [top, right, bot, left] style to
    [top-left.x, top-left.y, bot-right.x, bot-right.y] style which
    used for PIL.Image objects
    """
    return [location[3], location[0], location[1], location[2]]


class TestFaceRecognition(unittest.TestCase):

    def test_face_extraction(self):
        images_with_faces = [r'./images/doctor.jpg']

        for image_file in images_with_faces:
            image = Image.open(image_file)
            image_pixels = face_recognition.load_image_file(image_file)

            show_image(image, 'SOURCE')

            face_locations = face_recognition.face_locations(image_pixels)
            self.assertGreater(len(face_locations), 0)

            for location in face_locations:
                location = convert_location_style(location)
                face_image = image.crop(location)
                show_image(face_image, 'FACE')

    def test_face_compare(self):
        doctor_path = r'./images/doctor.jpg'
        thor01_path = r'./images/Thor01.jpg'
        thor02_path = r'./images/Thor02.jpg'

        image_doctor = face_recognition.load_image_file(doctor_path)
        image_thor01 = face_recognition.load_image_file(thor01_path)
        image_thor02 = face_recognition.load_image_file(thor02_path)

        image_doctor_encoding = face_recognition.face_encodings(image_doctor)[0]
        image_thor01_encoding = face_recognition.face_encodings(image_thor01)[0]
        image_thor02_encoding = face_recognition.face_encodings(image_thor02)[0]

        result = face_recognition.compare_faces([image_thor01_encoding, image_doctor_encoding], image_thor02_encoding)

        self.assertEqual(len(result), 2)
        self.assertTrue(result[0])
        self.assertFalse(result[1])


if __name__ == '__main__':
    unittest.main()
