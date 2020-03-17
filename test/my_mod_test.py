# test/strings_test.py

import unittest
from lambdata_amindazad.my_mod import Amin_toolbox

class TestMyMod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOOOOOOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()