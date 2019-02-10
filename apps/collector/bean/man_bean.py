import datetime

from apps.collector.bean.face_record_bean import *


class ManBean:

    def __init__(self):
        self.name = str()
        self.create_time = datetime.datetime.now()
        self.faces = list()


def man_bean_to_dict(man_bean: ManBean):
    return {
        'name': man_bean.name,
        'create_time': man_bean.create_time,
        'faces': [face_record_bean_to_dict(bean) for bean in man_bean.faces]
    }


def dict_to_man_bean(dict_obj):
    bean = ManBean()
    bean.name = dict_obj['name']
    bean.create_time = dict_obj['create_time']
    bean.faces = [dict_to_face_record_bean(face_record_dict) for face_record_dict in dict_obj['faces']]
    return
