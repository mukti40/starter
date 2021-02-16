import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("this is Email signup test")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("this is Facebook signup test")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("this is Twitter signup test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()