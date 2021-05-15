from unittest import TestCase

from server.repositories.base_repository import Repository


class BaseRepositoryTest(TestCase):

    def test_base_repository_methods_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            # method is not implemented
            Repository().map_result(None)

    def test_map_rt_private_room(self):
        input = 'Private room'
        expectation = 1
        self.assertEqual(expectation, Repository().map_rt(input))

    def test_map_rt_entire_home_apt(self):
        input = 'Entire home/apt'
        expectation = 2
        self.assertEqual(expectation, Repository().map_rt(input))

    def test_map_rt_shared_room(self):
        input = 'Shared Room'
        expectation = 3
        self.assertEqual(expectation, Repository().map_rt(input))

    def test_map_rt_unexpected_input(self):
        input = 'House'
        expectation = 0
        self.assertEqual(expectation, Repository().map_rt(input))

    def test_map_rt_input_none(self):
        input = None
        expectation = 0
        self.assertEqual(expectation, Repository().map_rt(input))
