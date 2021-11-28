import unittest

from result.services import * 

class ServicesTestCase(unittest.TestCase):
    def test_can_read_csv_file(self):
        expected = {'Rabin':'073BEL329'}
        output = read_csv('result/test.csv')
        self.assertEqual(output,expected)

