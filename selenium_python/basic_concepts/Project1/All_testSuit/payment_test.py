import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentinDollar(self):
        print("this is payment in Dollar test")
        self.assertTrue(True)

    def test_paymentinRupees(self):
        print("this is payment in Rupees test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()