from software_testing2.caesar_Cipher.caesar_Cipher import caesarCipher
import unittest

class CaesarTest(unittest.TestCase):
    def test_caesar_XXXX(self):
        text = 'XXXX'
        num_k = 9
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'GGGG')
    
    def test_caesar_froggwer(self):
        text = 'froggwer'
        num_k = 26
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'froggwer')
    
    def test_caesar_zero(self):
        text = '0'
        num_k = 70
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'0')

    def test_caesar_specialChar(self):
        text = '#f@&G'
        num_k = 12
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'#r@&S')
    
    def test_caesar_emty(self):
        text = ''
        num_k = 100
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'')
    
    def test_caesar_Subject1(self):
        text = 'Fick Me Baby One More Time'
        num_k = 20
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'Zcwe Gy Vuvs Ihy Gily Ncgy')

    def test_caesar_specialFocus(self):
        text = 'N^uIg@tes'
        num_k = 2
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'P^wKi@vgu')