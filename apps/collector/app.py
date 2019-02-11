import getopt
import logging
from threading import Thread

import os
import sys

# append current project root dir into PATH to make sure import
# modules in current project correctly
sys.path.append('.')

from apps.collector.bean.man_dao import ManDAO
from apps.collector.face_collector import FaceCollector
from apps.collector.face_recognizer_impl import FaceRecognizerImpl
from apps.collector.man_face_manager import ManFaceManager


project_root_directory = r'E:/Project/remote/python/people-image-collector'


def print_help():
    print('app.py -f <faces store folder> -d <database file path>')


def parse_argv(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:d:", ["faces_store_folder=", "database="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    faces_store_folder = None
    database_file = None

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-f", "--faces_store_folder"):
            faces_store_folder = arg
        elif opt in ("-d", "--database"):
            database_file = arg

    if faces_store_folder is None:
        faces_store_folder = os.path.join(project_root_directory, 'runtime/faces-image-dir')

    if database_file is None:
        database_file = os.path.join(project_root_directory, 'runtime/local_db')

    return faces_store_folder, database_file


def init_logger():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=log_format)


def dependency_injection(faces_store_folder, database_file):
    face_recognizer = FaceRecognizerImpl()
    man_dao = ManDAO(database_file)

    print(os.path.abspath(faces_store_folder))

    man_face_manager = ManFaceManager(man_dao, face_recognizer, faces_store_folder)
    face_collector = FaceCollector(man_face_manager)

    return face_collector


def run_app(argv):
    init_logger()
    faces_store_folder, database_file = parse_argv(argv)
    collector = dependency_injection(faces_store_folder, database_file)

    td = Thread(target=collector.monitoring)
    td.start()

    input('Type return to exit\n')
    collector.stop_monitoring()
    td.join()

    logging.info('Exit')


if __name__ == '__main__':
    run_app(sys.argv[1:])
