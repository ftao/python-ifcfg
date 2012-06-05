"""Tests for Ifcfg."""

import unittest
from nose.tools import ok_, eq_, raises
from nose import SkipTest

import ifcfg
    
class IfcfgTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_ifcfg(self):
        # do something to test Ifcfg
        parser = ifcfg.parse()