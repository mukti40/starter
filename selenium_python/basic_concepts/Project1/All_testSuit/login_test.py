import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("this is Email login test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("this is Facebook login test")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("this is Twitter login test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()