"""Tests for Ifcfg."""

import unittest

import ifcfg
from ifcfg.parser import WindowsParser
from nose.tools import eq_, ok_

from . import ipconfig_out


class WindowsTestCase(unittest.TestCase):

    def test_interfaces(self):
        ifcfg.Parser = WindowsParser
        interfaces = ifcfg.interfaces()
        res = len(interfaces) > 0
        ok_(res)

    def test_windows10(self):
        ifcfg.distro = "win32"
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_10_ETH)
        interfaces = parser.interfaces
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')
