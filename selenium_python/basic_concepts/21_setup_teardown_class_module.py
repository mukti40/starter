import unittest

#def setUpModule():                                 # module operations are declared outside the class.
    #Print("I will execute at every module start")

#def tearDownModule():
    #Print("I will execute at every module's End")

class AppTesting(unittest.TestCase):
    
    @classmethod                               # this is decorator class methord
    def setUp(self):                           # using setUp methord, executed for every fuction in a class at start
        print("This is Login Test")

    @classmethod
    def tearDown(self):                        # using tearDown methord, executed for every fuction in a class at end
        print("This is LogOut Test")

    @classmethod
    def setUpClass(cls):                       # using tearDown methord, executed for every class in a module at start
        print("This is App Login")

    @classmethod
    def tearDownClass(cls):                    # using tearDown methord, executed for every class in a module at End
        print("This is App Logout")


    def test_search(self):                     # Defining Functions
        print("This is search Test")

    def test_advanceSearch(self):
        print("This is Advanced test Search")

    def test_prepaidRecharge(self):
        print("This is Prepaid Recharge")

    def test_postpaidRecharge(self):
        print("This is Postpaid Recharge")

if __name__ == "__main__":
    unittest.main()
