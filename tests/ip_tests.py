# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ifcfg
from ifcfg.parser import UnixIPParser
from nose.tools import eq_, ok_

from . import ip_out
from .base import IfcfgTestCase


class IpTestCase(IfcfgTestCase):

    def test_ifcfg(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = UnixIPParser
        interfaces = ifcfg.interfaces(ifconfig=ip_out.LINUX)
        res = len(interfaces) > 0
        ok_(res)

    def test_linux(self):
        ifcfg.Parser = UnixIPParser
        parser = ifcfg.get_parser(ifconfig=ip_out.LINUX)
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
        ifcfg.distro = 'Linux'
        ifcfg.Parser = UnixIPParser
        res = ifcfg.default_interface(
            ifconfig=ip_out.LINUX,
            route_output=ip_out.ROUTE_OUTPUT
        )
        ok_(res)
