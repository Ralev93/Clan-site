from django.test import TestCase

from .assign_members import *


class AssignAlgTests(TestCase):

    def test_get_users_1_elem(self):
        expected = ['Wilhelm']
        returned = get_users('0', 1, hypothesis_all)
        self.assertCountEqual(returned, expected)

    def test_get_users_2_elem(self):
        expected2 = ['Daniel', 'John']
        returned2 = get_users('4', 2, hypothesis_all)
        self.assertCountEqual(returned2, expected2)

 
    def test_get_users_0_elem(self):
        expected3 = []
        returned3 = get_users('0', 2, hypothesis_all)
        self.assertCountEqual(returned3, expected3)

    # def test_get_users_Key_error(self):
    #     self.assertRaises(KeyError, get_users('11', 2, hypothesis_all))



    def test_Count_member_daniel(self):
        r = count_member('Daniel', tmp_result)
        e = 3
        self.assertEqual(r,e)


    def test_Count_member_John(self):
        r = count_member('John', tmp_result)
        e = 4
        self.assertEqual(r,e)