from types import resolve_bases
import unittest
import reeb


class testing(unittest.TestCase):
    
    def get_data(size):
        matrix2 =   [
                    [1,7,12,13],
                    [9,2,6,5 ],
                    [14,8,11,10],
                    [15,16,4,3]
                    ]
        return np.random.randint(1,16,size=(4,4))      
    
    def test_graph(self):
        matrix1 = [  [1, 6, 3],
                                    [2, 7, 4],
                                    [5, 8, 9]
                                ]
        reference_parent = [-1, 2, 5, 4, 6, 7, 7, 8, 9]
        self.assertEqual(reeb.get_reeb(matrix1),reference_parent)
       



