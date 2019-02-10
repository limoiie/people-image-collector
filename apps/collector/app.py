import face_recognition
from PIL import Image
import matplotlib.pyplot as plt

from apps.collector.bean.man_dao import ManDAO
from apps.collector.face_collector import FaceCollector
from apps.collector.face_recognizer_impl import FaceRecognizerImpl
from apps.collector.man_face_manager import ManFaceManager


def convert_location_style(location):
    """
    convert location style from [top, right, bot, left] style to
    [top-left.x, top-left.y, bot-right.x, bot-right.y] style which
    used for PIL.Image objects
    """
    return [location[3], location[0], location[1], location[2]]


def show_image(image, title):
    plt.figure('IMAGE')
    plt.imshow(image)
    plt.title(title)
    plt.show()


def test_face_location(image_file: str):
    image = Image.open(image_file)
    image_pixels = face_recognition.load_image_file(image_file)

    show_image(image, 'SOURCE')
    face_locations = face_recognition.face_locations(image_pixels)
    for location in face_locations:
        location = convert_location_style(location)
        face_image = image.crop(location)
        show_image(face_image, 'FACE')
    else:
        print('no face')


def test_face_compare():
    doctor_path = '../../resources/images/doctor.jpg'
    thor01_path = '../../resources/images/Thor01.jpg'
    thor02_path = '../../resources/images/Thor02.jpg'
    image_doctor = face_recognition.load_image_file(doctor_path)
    image_thor01 = face_recognition.load_image_file(thor01_path)
    image_thor02 = face_recognition.load_image_file(thor02_path)

    image_doctor_encoding = face_recognition.face_encodings(image_doctor)[0]
    image_thor01_encoding = face_recognition.face_encodings(image_thor01)[0]
    image_thor02_encoding = face_recognition.face_encodings(image_thor02)[0]

    result = face_recognition.compare_faces([image_thor01_encoding, image_doctor_encoding], image_thor02_encoding)
    print(result)


def di():
    face_recognizer = FaceRecognizerImpl()
    man_dao = ManDAO()
    faces_dir = r'E:\projects\pycharm\people-image-collector\test\faces-image-dir'

    man_face_manager = ManFaceManager(man_dao, face_recognizer, faces_dir)
    face_collector = FaceCollector(man_face_manager)

    return face_collector


if __name__ == '__main__':
    collector = di()
    collector.monitoring()
