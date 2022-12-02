import re
import unittest

from Worker import ProductionWorker
from hamcrest import *
from Matcher import valid_email

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.temp = ProductionWorker("lastname", "firstname", "email@example.com", 2, 25.5)

    def testLastnameGetter(self):
        assert_that(self.temp.get_lastname(), equal_to("lastname"))

    def testLastnameSetter(self):
        self.temp.set_lastname("Mayer")
        assert_that(self.temp.get_lastname(), equal_to("Mayer"))

    def testLastnameSetsToNew(self):
        self.temp.set_lastname("Mayer")
        assert_that(self.temp.get_lastname(), not_("lsatname"))

    def testFirstnameNotEmpty(self):
        assert_that(self.temp.get_firstname(), not_none())

    def testEmailMatchRegexp(self):
        regexp = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert_that(self.temp.get_email(), matches_regexp(regexp))

    def testHourlyWageCloseTo(self):
        assert_that(self.temp.get_pay_hour(), close_to(25, 0.5))

    def testHourlyWageNotNull(self):
        assert_that(self.temp.get_pay_hour(), not_none())

    def testChangeNumberBetween1and2(self):
        assert_that(self.temp.get_change_number(), greater_than_or_equal_to(1), less_than_or_equal_to(2))

    def testOwnMatcher(self):
        assert_that(self.temp.get_email(), is_(valid_email()))
