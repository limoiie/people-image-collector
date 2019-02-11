import os
import unittest

import face_recognition

from apps.collector.bean.man_dao import ManDAO
from apps.collector.face_recognizer_impl import FaceRecognizerImpl
from apps.collector.man_face_manager import ManFaceManager
from apps.collector.utils import delete_folder


def get_instance(database_file, faces_store_folder):
    face_recognizer = FaceRecognizerImpl()
    man_dao = ManDAO(database_file)

    man_face_manager = ManFaceManager(man_dao, face_recognizer, faces_store_folder)
    return man_face_manager, man_dao


class TestManFaceManager(unittest.TestCase):

    def test_collect_faces_in_image_by_man(self):
        database = 'test_db'
        faces_folder = './test_faces_folder'

        face_files = [
            './images/doctor.jpg',
            './images/Thor01.jpg',
            './images/Thor02.jpg'
        ]

        expect_man_nums = [
            1, 2, 2
        ]

        instance, dao = get_instance(database, faces_folder)

        for face, man_num in zip(face_files, expect_man_nums):
            face_pixels = face_recognition.load_image_file(face)
            instance.collect_faces_in_image_by_man(face_pixels)

            mans = dao.fetch_all()
            # make sure recognizing man correctly
            self.assertEqual(len(mans), man_num)

        # make sure that the faces of the man have been stored into local folder
        for man in dao.fetch_all():
            self.assertGreater(len(man.faces), 0)
            for face in man.faces:
                self.assertTrue(os.path.exists(face.img_path))

        del instance
        del dao

        if os.path.exists(database):
            os.remove(database)
        delete_folder(faces_folder)


if __name__ == '__main__':
    unittest.main()
