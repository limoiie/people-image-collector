import logging

import cv2 as cv
import time

from apps.collector.man_face_manager import ManFaceManager


class FaceCollector:
    def __init__(self, man_face_manager: ManFaceManager):
        self.__man_face_manager = man_face_manager
        self.__sleep_duration_in_seconds_between_two_processing = 0.1
        self.__monitoring = True

    def set_frames_collected_every_10_seconds(self, num_frames):
        self.__sleep_duration_in_seconds_between_two_processing = 10 / num_frames

    def stop_monitoring(self):
        self.__monitoring = False

    def monitoring(self):
        camera = cv.VideoCapture(0)

        logging.info('Start monitoring...')

        self.__monitoring = True
        while self.__monitoring:
            success, frame = camera.read()
            # codes commented will be used to test in case there is no camera
            # success = True
            # image_path = r'E:\Project\remote\python\people-image-collector\resources\images\doctor.jpg'
            # frame = face_recognition.load_image_file(image_path)
            if success:
                self.__processing_frame(frame)
            else:
                logging.warning('Cannot get the frame from the camera, '
                                'make sure you have the permission to access the camera')
            time.sleep(self.__sleep_duration_in_seconds_between_two_processing)

        self.__man_face_manager.finish()
        camera.release()

        logging.info('Finish monitoring')

    def __processing_frame(self, frame):
        self.__man_face_manager.collect_faces_in_image_by_man(frame)
        pass
