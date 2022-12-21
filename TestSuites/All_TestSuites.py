import unittest

from Package 1.TC_loginTest import LoginTest
from Package1.TC_signup import signuptest
from package2.TC_Payment Test import paymentTest

tc1=unittest.TestLoader().LoadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().LoadTestsFromTestCase(signuptest)
tc3=unittest.TestLoader().LoadTestsFromTestCase(paymentTest)

sanityTestSuite=unittest.TestSuite([tc1,tc2])
functionalTestSuite=unittest.TestSuite([tc3])
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
