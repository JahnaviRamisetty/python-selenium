import unittest

class AppTesting(unittest.TestCase):
    def setUp(self):
        print("this is login")

    def test_search(self):
        print("this is search test")

    def test_advancedsearch(self):
        print("this is advanced search")

    def test_prepaidsearch(self):
        print("this is prepaidsearch")

    def test_postpaidsearch(self):
        print("this is postpaidsearch")


    if __name__=="__main__":
        unittest.main()