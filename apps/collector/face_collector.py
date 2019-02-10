import cv2 as cv
import time

from apps.collector.man_face_manager import ManFaceManager


class FaceCollector:
    def __init__(self, man_face_manager: ManFaceManager):
        self.__man_face_manager = man_face_manager
        self.__sleep_duration_in_seconds_between_two_processing = 0.1

    def set_frames_collected_every_10_seconds(self, num_frames):
        self.__sleep_duration_in_seconds_between_two_processing = 10 / num_frames

    def monitoring(self):
        camera = cv.VideoCapture(0)

        while True:
            success, frame = camera.read()
            if success:
                self.__processing_frame(frame)
            time.sleep(self.__sleep_duration_in_seconds_between_two_processing)
        pass

    def __processing_frame(self, frame):
        self.__man_face_manager.collect_faces_in_image_by_man(frame)
        pass


def test():
    camera = cv.VideoCapture(0)
    success, frame = camera.read()
    if success:
        print(frame)
    else:
        print('oh no~~~')
    pass


if __name__ == '__main__':
    test()
