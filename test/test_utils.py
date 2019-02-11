import unittest

from apps.collector.utils import *


def create_a_folder_sturcture(test_folder, test_sub_folder):
    folder = '%s/%s' % (test_folder, test_sub_folder)
    if os.path.exists(folder):
        os.rmdir(folder)

    os.makedirs(folder)
    with open(test_folder + '/test.file', 'w') as file:
        pass
    with open(folder + '/test.file', 'w') as file:
        pass


class TestUtils(unittest.TestCase):

    def test_generate_an_non_exist_file_path(self):
        test_folders = ['.']

        pre_file_path = 'test.test'
        for test_folder in test_folders:
            file_path = generate_an_non_exist_file_path(test_folder, '%s.test')

            abs_test_folder = os.path.abspath(test_folder)
            abs_file_path = os.path.abspath(file_path)

            self.assertIn(abs_test_folder, abs_file_path)
            self.assertFalse(os.path.exists(file_path))
            self.assertNotEqual(file_path, pre_file_path)

            pre_file_path = file_path

    def test_generate_an_random_string(self):
        test_lens = [10, 10, 12, 14]
        for test_len in test_lens:
            self.__test_generate_an_random_string(test_len)

    def test_delete_folder(self):
        test_folder = 'test_test_folder'
        test_sub_folder = 'sub_folder'
        create_a_folder_sturcture(test_folder, test_sub_folder)

        delete_folder(test_folder)
        self.assertFalse(os.path.exists(test_folder))

    def __test_generate_an_random_string(self, string_len):
        pre_string = 'random string'
        count = 10
        while count > 0:
            string = generate_an_random_string(string_len)

            self.assertEqual(len(string), string_len)

            # TODO: when the string_len is small, say equals to 1, it is
            # TODO: possible that string equals to pre_string. so consider
            # TODO: change a test strategy
            self.assertNotEqual(string, pre_string)

            pre_string = string
            count -= 1


if __name__ == '__main__':
    unittest.main()
