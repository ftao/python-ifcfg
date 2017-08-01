"""Tests for ifcfg.tools."""

import logging
import os
import unittest

import ifcfg
from ifcfg.tools import exec_cmd
from nose.tools import eq_


class IfcfgToolsTestCase(unittest.TestCase):

    def test_minimal_logger(self):
        os.environ['IFCFG_DEBUG'] = '1'
        log = ifcfg.tools.minimal_logger(__name__)
        eq_(log.level, logging.DEBUG)
        os.environ['IFCFG_DEBUG'] = '0'

    def test_command(self):
        output, __, __ = exec_cmd("echo -n 'this is a test'")
        self.assertEqual(output, "this is a test")
