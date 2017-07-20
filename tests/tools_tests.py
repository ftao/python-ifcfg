"""Tests for ifcfg.tools."""

import logging
import os
import unittest

import ifcfg
from nose.tools import eq_


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
