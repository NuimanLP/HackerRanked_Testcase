from software_testing1.alternating.alternating import alternatingChar
import unittest

class AlterTest(unittest.TestCase):
    def test_alter_CCCC_num(self):
        text = 'CCCC'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '3')
    
    def test_alter_Nuiman(self):
        text = 'Nuiman'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '0')
    
    def test_alter_Chavatik_num(self):
        text = 'Chavaatik'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '1')

    def test_alter_manyChar_num(self):
        text = 'aaabbb'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '4')
    
    def test_alter_7777_num(self):
        text = '7777'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '4')
    
    def test_alter_4321_num(self):
        text = '4321'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '0')
    
    def test_alter_special(self):
        text = '///////'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '6')
    
    def test_alter_special_char2_num(self):
        text = '#@$())*'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '1')