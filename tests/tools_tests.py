"""Tests for ifcfg.tools."""

import locale
import logging
import os
import sys
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


    @unittest.skipIf(sys.version[0] != '2',
                     "Python 2 only supports non-unicode stuff")
    def test_command_non_unicode(self):
        getpreferredencoding_orig = locale.getpreferredencoding
        locale.getpreferredencoding = lambda: "ISO-8859-1"
        output, __, __ = exec_cmd("echo -n 'this is a test'")
        self.assertEqual(output, "this is a test")
        locale.getpreferredencoding = getpreferredencoding_orig
