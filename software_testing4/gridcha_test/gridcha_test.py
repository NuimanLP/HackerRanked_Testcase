from software_testing4.grid_cha.grid_cha import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    
    def test_grid_with_identical_rows(self):
        self.assertEqual(gridChallenge(['aaa', 'aaa', 'aaa']), 'YES')
    
    def test_empty_grid(self):
        self.assertEqual(gridChallenge([]), 'YES')
    
    def test_complex_unsortable_grid(self):
        self.assertEqual(gridChallenge(['zyx', 'wvu', 'tsr']), 'NO')
    
    def test_grid1_l(self):
        grid = ['l']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_empty_grid(self):
        self.assertEqual(gridChallenge([]), 'YES')

    
    def test_grid1__int_number(self):
        grid = ['321','222','533']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_Special_Str(self):
        grid = ['!','@','$']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_input_but_have_3_num_of_str(self):
        grid = ['abc','hjk','msq','rtx']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_input_but_have_4_num_of_str(self):
        grid = ['mpxz','abcd','wlmf']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid_with_non_alpha_characters(self):
        self.assertEqual(gridChallenge(['@#$', '123', 'abc']), 'NO')