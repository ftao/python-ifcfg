# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ifcfg
from ifcfg.parser import LinuxParser, NullParser
from nose.tools import eq_, ok_, raises

from . import ifconfig_out
from .base import IfcfgTestCase


class IfcfgTestCase(IfcfgTestCase):

    def test_ifcfg(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        interfaces = ifcfg.interfaces(ifconfig=ifconfig_out.LINUX)
        res = len(interfaces) > 0
        ok_(res)

    def test_unknown(self):
        ifcfg.distro = 'Bogus'
        ifcfg.Parser = ifcfg.get_parser_class()
        self.assertTrue(issubclass(ifcfg.Parser, NullParser))

    @raises(RuntimeError)
    def test_illegal(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        ifcfg.get_parser(ifconfig=ifconfig_out.ILLEGAL_OUTPUT)

    def test_linux(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux2(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX2)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux3(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX3)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linuxdocker(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUXDOCKER)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 7)
        eq_(interfaces['enp0s31f6']['ether'], '54:e1:ad:76:c8:cb')
        eq_(interfaces['enp0s31f6']['inet'], '192.168.1.94')
        eq_(interfaces['enp0s31f6']['broadcast'], '192.168.1.255')
        eq_(interfaces['enp0s31f6']['netmask'], '255.255.255.0')
        eq_(interfaces['br-736aa253dd57']['ether'], '02:42:9c:fe:60:db')
        eq_(interfaces['br-736aa253dd57']['inet'], '172.19.0.1')
        eq_(interfaces['br-736aa253dd57']['broadcast'], '0.0.0.0')
        eq_(interfaces['br-736aa253dd57']['netmask'], '255.255.0.0')

    def test_vlan(self):
        """
        Regression test for: https://github.com/ftao/python-ifcfg/issues/40
        """
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX_VLAN)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 9)
        eq_(interfaces['eth2.2']['ether'], '08:00:27:7c:6d:9d')

    def test_macosx(self):
        ifcfg.distro = 'MacOSX'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.MACOSX)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['en0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['en0']['inet'], '192.168.0.1')
        eq_(interfaces['en0']['broadcast'], '192.168.0.255')
        eq_(interfaces['en0']['netmask'], '255.255.255.0')

    def test_macosx2(self):
        ifcfg.distro = 'MacOSX'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.MACOSX2)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 9)
        eq_(interfaces['lo0']['inet'], '127.0.0.1')
        eq_(interfaces['lo0']['inet4'], ['127.0.0.1', '127.0.1.99'])
        eq_(interfaces['lo0']['netmask'], '255.0.0.0')

    def test_default_interface(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = LinuxParser
        route_output = ifconfig_out.ROUTE_OUTPUT
        res = ifcfg.default_interface(
            ifconfig=ifconfig_out.LINUX3, route_output=route_output
        )
        ok_(res)
