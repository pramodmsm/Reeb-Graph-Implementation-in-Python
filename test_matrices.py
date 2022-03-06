from pkgutil import get_data
from types import resolve_bases
import unittest
import numpy as np
import reeb

class testing(unittest.TestCase):
     
    
    def get_data(self,random=False,size=(3,3)):
        if not random and size==(3,3):
            return np.array(  [   
                    [1, 6, 3],
                    [2, 7, 4],
                    [5, 8, 9]
                    ])
        elif not random and size==(4,4):
            return np.array(  [
                    [1,7,12,13],
                    [9,2,6,5 ],
                    [14,8,11,10],
                    [15,16,4,3]
                    ])
        else:
            return np.random.randint(1,16,size=(4,4))   

    def test_graph(self):
        reference_parent = [-1, 2, 5, 4, 6, 7, 7, 8, 9]
        self.assertEqual(reeb.get_reeb(self.get_data(size=(3,3))),reference_parent)
       



