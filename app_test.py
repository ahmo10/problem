
from create_app import create_app
from app import  api
from app import myDiary


import unittest


class BasicTestCase(unittest.TestCase):
#test for get all entries

    def setUp(self):
        app = create_app('testing')
        self.tester = app.test_client()

    def test_get_all(self):
        
        print(api.url_for(myDiary))
        pass

if __name__ == '__main__':
    unittest.main()