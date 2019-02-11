import shelve
import json
import pickle

from apps.collector.bean.dao import DAO
from apps.collector.bean.man_bean import *
from apps.collector.utils import generate_an_random_string


class ManDAO(DAO):

    def __init__(self, database_file):
        self.__database_file = database_file
        self.__bean_set = set()
        self.__load_from_db()

    def __load_from_db(self):
        try:
            with open(self.__database_file, 'r') as db:
                man_beans = json.load(db)
                for man_dict in man_beans:
                    man_bean = dict_to_man_bean(man_dict)
                    self.__bean_set.add(man_bean)

        except Exception as e:
            pass

    def __dump_to_db(self):
        with open(self.__database_file, 'w') as db:
            man_dict_list = list()
            for man_bean in self.__bean_set:
                man_dict_list.append(man_bean_to_dict(man_bean))

            json.dump(man_dict_list, db)

    def create(self):
        man = ManBean()
        man.name = generate_an_random_string(10)
        return man

    def insert(self, bean: ManBean):
        self.__bean_set.add(bean)
        pass

    def delete(self, bean: ManBean):
        self.__bean_set.remove(bean)
        pass

    def update(self, bean: ManBean):
        self.__bean_set.remove(bean)
        self.__bean_set.add(bean)
        pass

    def fetch_all(self):
        return self.__bean_set.copy()

    def clear(self):
        self.__bean_set = set()

    def flush(self):
        self.__dump_to_db()
        pass
