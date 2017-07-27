"""Tests for Ifcfg."""

import unittest

import ifcfg
from ifcfg.parser import UnixIPParser
from nose.tools import eq_, ok_

from . import ip_out


class IpTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ifcfg(self):
        interfaces = ifcfg.interfaces()
        res = len(interfaces) > 0
        ok_(res)

    def test_linux(self):
        parser = ifcfg.get_parser(distro='Linux',
                                  ifconfig=ip_out.LINUX,
                                  parser=UnixIPParser)
        interfaces = parser.interfaces
        # Unconnected interface
        eq_(interfaces['enp0s25']['ether'], 'a0:00:00:00:00:00')
        eq_(interfaces['enp0s25']['inet'], None)
        # Connected interface
        eq_(interfaces['wlp3s0']['ether'], 'a0:00:00:00:00:00')
        eq_(interfaces['wlp3s0']['inet'], '192.168.12.34')
        eq_(interfaces['wlp3s0']['broadcast'], '192.168.12.255')
        eq_(interfaces['wlp3s0']['netmask'], '/24')

    def test_default_interface(self):
        res = ifcfg.default_interface()
        ok_(res)
