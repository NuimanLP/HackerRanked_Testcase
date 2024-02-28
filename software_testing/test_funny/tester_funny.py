from software_testing.funny_string.funny_string import funny_String
import unittest

class Funny_or_not(unittest.TestCase):

    def test_give_acxz(self):
        self.assertEqual(funny_String('acxz'), 'Funny')

    def test_give_aba(self):
        self.assertEqual(funny_String('aba'), 'Funny')

    def test_give_empty_string(self):
        self.assertEqual(funny_String(""), 'Funny')

    def test_give_aaa(self):
        self.assertEqual(funny_String("aaaa"), 'Funny')

    def test_give_symmetric(self):
        self.assertEqual(funny_String("azbz"), 'Not Funny')

    def test_give_a(self):
        self.assertEqual(funny_String("a"), 'Funny')

    def test_give_121(self):
        self.assertEqual(funny_String("121"), 'Funny')

    def test_give_special(self):
        self.assertEqual(funny_String("!@!"), 'Funny')

    def test_give_palindrome(self):
        self.assertEqual(funny_String("madam"), 'Funny')

    def test_symmetric_num(self):
        self.assertEqual(funny_String("1a2b2a1"), 'Funny')
