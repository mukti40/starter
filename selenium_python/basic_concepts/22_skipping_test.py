import unittest

class Apptesting(unittest.TestCase):
    
    def test_search(self):
        print("This is search Test")

    def test_advanceSearch(self):
        print("This is Advanced test Search")

    def test_prepaidRecharge(self):
        print("This is Prepaid Recharge")

    @unittest.skipIf(1==1,"anything comment")  # skipping based on condition
    def test_postpaidRecharge(self):
        print("This is Postpaid Recharge")

    @unittest.SkipTest                      # Skipping Test
    def test_loginByGmail(self):
        print("This is email Login")

    @unittest.skip("Skipping for reason 1") # Skipping Test with giving certain comment
    def test_loginByTwitter(self):
        print("This is twitter Login")



if __name__ == "__main__":
    unittest.main()