import datetime


class FaceRecordBean:

    def __init__(self):
        self.img_path = str()
        self.record_time = datetime.datetime.now()


def face_record_bean_to_dict(face_record_bean: FaceRecordBean):
    return {
        'img_path': face_record_bean.img_path,
        'record_time': face_record_bean.record_time
    }


def dict_to_face_record_bean(dict_obj):
    bean = FaceRecordBean()
    bean.img_path = dict_obj['img_path']
    bean.record_time = dict_obj['record_time']
    return bean


def create_face_record(img_path, record_time):
    bean = FaceRecordBean()
    bean.img_path = img_path
    bean.record_time = record_time
