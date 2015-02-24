from pyfactorie.parsers import FactorieParser
from os import environ
from unittest import TestCase

class Tester(TestCase):

    def setUp(self):
        self.factorie = FactorieParser()   

    def test_true(self):
        # should fail if no factorie server is running
        # make sure node stuff works (add child)
        # parse sentence should throw error is no server is running
        # for now, just leaving no tests
        self.assertTrue(True)
