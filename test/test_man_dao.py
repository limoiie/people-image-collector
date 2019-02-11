import os
import unittest

from apps.collector.bean.man_dao import ManDAO


class TestManDAO(unittest.TestCase):

    def test_create_insert_fetch_all(self):
        test_db_file = r'./test_db'

        man_dao = ManDAO(test_db_file)
        bean = man_dao.create()
        man_dao.insert(bean)
        man_dao.flush()

        del man_dao

        man_dao = ManDAO(test_db_file)
        bean_set = man_dao.fetch_all()

        self.assertEqual(len(bean_set), 1)
        bean2 = bean_set.pop()

        self.assertEqual(bean2.name, bean.name)
        self.assertEqual(bean2.create_time, bean.create_time)

        os.remove(test_db_file)

    def test_delete(self):
        raise NotImplemented()


if __name__ == '__main__':
    unittest.main()
