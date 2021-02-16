import unittest
from package1.login_test import LoginTest
from package1.signup_test import SignupTest

from package2.payment_test import PaymentTest
from package2.paymentreturn_test import PaymentReturnTest

#get all tests from all methords
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])  # sanity test suite
fuctionalTestSuite = unittest.TestSuite([tc3,tc4])  # functional test suite
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])  # master test suite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
