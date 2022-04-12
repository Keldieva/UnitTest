import unittest
from Test_Case.utils import perimeter_of_square
from Test_Case.utils import merge_and_sort_two_lists
from Test_Case.utils import greet
from Test_Case.utils import sum_of_numbers_in_string


class Test_Cases(unittest.TestCase):
    def test_perimeter_of_square(self):
        self.assertEqual(perimeter_of_square(3), 12)

    def test_perimeter_of_square_str(self):
        self.assertRaises(ValueError, perimeter_of_square, 'str')

    def test_merge_and_sort_two_lists(self):
        self.assertEqual(merge_and_sort_two_lists([1, 4, 2], [5, 2, 4]), [1, 2, 2, 4, 4, 5])



    def test_greet_Johnny(self):
        self.assertEqual(greet("Johnny"), "Hello, my love!")

    def test_greet_other_names(self):
        self.assertEqual(greet("Adam"), "Hello, Adam!")




    def test_sum_of_numbers_in_string(self):
        self.assertEqual(sum_of_numbers_in_string("hgfghshm45261"), 18)

    def test_sum_of_numbers_in_string2(self):
        self.assertEqual(sum_of_numbers_in_string("hgfghshm22gfhg"), 4)



if __name__ == '__main__':
    unittest.main()
