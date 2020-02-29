import unittest
import sys
#sys.path.insert(0, "/Users/kylewilson/IdeaProjects/Py_moduletest/app/test/")
from app.test.main import this_T


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    print(this_T())
    unittest.main()