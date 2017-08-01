# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ifcfg
from ifcfg.parser import NullParser
from nose.tools import eq_, ok_, raises

from . import ifconfig_out
from .base import IfcfgTestCase


class IfcfgTestCase(IfcfgTestCase):

    def test_ifcfg(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
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
        ifcfg.Parser = ifcfg.get_parser_class()
        ifcfg.get_parser(ifconfig=ifconfig_out.ILLEGAL_OUTPUT)

    def test_linux(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux2(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX2)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux3(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX3)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

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

    def test_default_interface(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        route_output = ifconfig_out.ROUTE_OUTPUT
        res = ifcfg.default_interface(
            ifconfig=ifconfig_out.LINUX3, route_output=route_output
        )
        ok_(res)
