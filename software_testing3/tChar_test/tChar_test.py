from software_testing3.two_Char.two_Char import alternate 
import unittest

class TwoCharacterTest(unittest.TestCase):
    def test_beabeefeab(self):
        text = 'beabeefeab'
        result = alternate(text)
        self.assertEqual(result, 5)
    
    def test_afafafafafafaf(self):
        text = 'afafafafafafaf'
        result = alternate(text)
        self.assertEqual(result, 14)
    
    def test_my_nickname(self):
        text = 'Nile'
        result = alternate(text)
        self.assertEqual(result, 2)
    
    def test_my_name(self):
        text = 'Chavatik Thorarit'
        result = alternate(text)
        self.assertEqual(result, 4)
    
    def test_xyxyxyxxyxwx(self):
        text = 'xyxyxyxxyxwx'
        result = alternate(text)
        self.assertEqual(result, 0)
    
    def test_bugbunnie(self):
        text = 'bugbunnie'
        result = alternate(text)
        self.assertEqual(result, 4)
    
    def test_specialChar1(self):
        text = '@@@@@@@@@@@@@@@@@@@@@'
        result = alternate(text)
        self.assertEqual(result, 0)
    
    def test_abababab(self):
        text = 'abababab'
        result = alternate(text)
        self.assertEqual(result, 8)
    
    def test_4spacebar(self):
        text = '    '
        result = alternate(text)
        self.assertEqual(result, 0)
    
    def test_str_and_spacebar(self):
        text = 'F O O T A G E'
        result = alternate(text)
        self.assertEqual(result, 2)
    
    def test_number(self):
        text = '1232123212321'
        result = alternate(text)
        self.assertEqual(result, 7)
    
    def test_1Char(self):
        text = 'b'
        result = alternate(text)
        self.assertEqual(result, 0)

