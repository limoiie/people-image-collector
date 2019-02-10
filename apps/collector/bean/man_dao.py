import shelve

from apps.collector.bean.dao import DAO
from apps.collector.bean.man_bean import *
from apps.collector.utils import generate_an_random_string


class ManDAO(DAO):

    def __init__(self):
        self.__table_name = 'mans'
        self.__container = set()

        self.__db = shelve.open('local_db')
        self.__load_from_db()

    def __del__(self):
        self.__dump_to_db()
        self.__db.close()

    def __load_from_db(self):
        if self.__table_name in self.__db.keys():
            man_dict_objs = self.__db[self.__table_name]
            for man_dict in man_dict_objs:
                self.__container.add(dict_to_man_bean(man_dict))

    def __dump_to_db(self):
        self.__db[self.__table_name] = list()
        for man_bean in self.__container:
            self.__db[self.__table_name].append(man_bean_to_dict(man_bean))

    def create(self):
        man = ManBean()
        man.name = generate_an_random_string(10)
        return man

    def insert(self, bean: ManBean):
        self.__container.add(bean)
        pass

    def delete(self, bean: ManBean):
        self.__container.remove(bean)
        pass

    def update(self, bean: ManBean):
        self.__container.remove(bean)
        self.__container.add(bean)
        pass

    def fetch_all(self):
        return self.__container

    def clear(self):
        self.__container = set()
