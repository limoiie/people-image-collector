import os
from datetime import datetime

from apps.collector.bean.dao import DAO
from apps.collector.bean.face_record_bean import *
from apps.collector.bean.man_bean import ManBean
from apps.collector.face_recognizer import FaceRecognizer
from apps.collector.utils import *


def fetch_faces_from_man(man_bean: ManBean, num: int=10):
    face_paths = [face.img_path for face in man_bean.faces][:num]
    return load_images_from_file_paths(face_paths)


class ManFaceManager:

    def __init__(self, man_dao: DAO, face_recognizer: FaceRecognizer, faces_dir: str):
        self.__man_dao = man_dao
        self.__face_recognizer = face_recognizer
        self.__faces_dir = faces_dir
        os.makedirs(self.__faces_dir)

    def __store_image(self, img: numpy.array):
        image = Image.fromarray(img)
        image_path = generate_an_non_exist_file_path(self.__faces_dir, '%s.jpg')
        image.save(image_path)
        return image_path

    def __extract_faces_from_image(self, image: numpy.array):
        faces = list()
        face_locations = self.__face_recognizer.extract_face_locations(image)
        for loc in face_locations:
            top, right, bot, left = loc[0], loc[1], loc[2], loc[3]
            faces.append(crop_image(image, [top, bot+1], [left, right+1]))
        return faces

    def __is_face_from_man(self, man, face):
        faces_of_man = fetch_faces_from_man(man)
        results = self.__face_recognizer.compare_faces(faces_of_man, face)

        similar_faces_count = 0
        for is_similar in results:
            if is_similar:
                similar_faces_count += 1

        over_half_faces_similar_with_testing_face = \
            similar_faces_count + similar_faces_count > len(results)
        return over_half_faces_similar_with_testing_face

    def collect_faces_in_image_by_man(self, image: numpy.array):
        # TODO: for now we just use the first face, you may want to use all of the faces
        faces = self.__extract_faces_from_image(image)
        if 0 == len(faces):
            return

        face = faces[0]
        stored_img_path = self.__store_image(face)

        for man in self.__man_dao.fetch_all():
            if self.__is_face_from_man(man, face):
                face_record = create_face_record(stored_img_path, datetime.now())
                man.faces.append(face_record)
                self.__man_dao.update(man)
                break
        else:
            new_man = self.__man_dao.create()
            face_record = create_face_record(stored_img_path, datetime.now())
            new_man.faces.append(face_record)
            self.__man_dao.insert(new_man)
