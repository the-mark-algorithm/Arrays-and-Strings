# import src.oneAway
import os
import sys
import unittest

class TestOneAway(unittest.TestCase):

    def test_insert_character(self):
        s1 = "elphant"
        s2 = "elephants"

        dirs = os.scandir(os.getcwd())
        
        for d in dirs:
            print(d.path)

        print("SYSPATH: ")

        for item in sys.path:
            print(item)

        # self.assertEqual(oneAway(s1, s2), True, "Should be True")

if __name__ == '__main__':
    unittest.main()