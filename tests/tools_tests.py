"""Tests for ifcfg.tools."""

import os
import logging
import unittest
from nose.tools import ok_, eq_, raises

import ifcfg
    
class IfcfgToolsTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_minimal_logger(self):
        os.environ['IFCFG_DEBUG'] = '1'
        log = ifcfg.tools.minimal_logger(__name__)
        eq_(log.level, logging.DEBUG)
        os.environ['IFCFG_DEBUG'] = '0'