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
        eq_(interfaces['wlp3s0']['inet4'], ['192.168.12.34'])
        eq_(interfaces['wlp3s0']['inet6'], ['fd37:a521:ada9::869', 'fd37:a521:ada9:0:b9f7:44f8:bb19:c78c', 'fd37:a521:ada9:0:9073:a91:d14f:8087', 'fe80::205f:5d09:d0da:7aed'])
        eq_(interfaces['wlp3s0']['broadcast'], '192.168.12.255')
        eq_(interfaces['wlp3s0']['netmask'], '/24')
        eq_(interfaces['wlp3s0']['mtu'], '1500')
        # Connected interface
        eq_(interfaces['enp6s0.2']['ether'], '00:73:00:5c:09:9a')
        eq_(interfaces['enp6s0.2']['inet'], '10.2.2.253')
        eq_(interfaces['enp6s0.2']['mtu'], '1500')
        eq_(interfaces['enp6s0.2']['inet4'], ['10.2.2.253', '10.1.1.253'])
        eq_(interfaces['enp6s0.2']['inet6'], [])

    def test_linux_multi_inet4(self):
        ifcfg.Parser = UnixIPParser
        parser = ifcfg.get_parser(ifconfig=ip_out.LINUX_MULTI_IPV4)
        interfaces = parser.interfaces
        # Connected interface
        eq_(interfaces['eth0']['ether'], 'b8:27:eb:50:39:69')
        eq_(interfaces['eth0']['inet'], '192.168.13.1')
        eq_(interfaces['eth0']['inet4'], ['192.168.13.1', '192.168.10.3'])
        eq_(interfaces['eth0']['broadcast'], '192.168.13.255')
        eq_(interfaces['eth0']['netmask'], '/24')
        eq_(interfaces['eth0']['mtu'], '1500')

    def test_default_interface(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = UnixIPParser
        res = ifcfg.default_interface(
            ifconfig=ip_out.LINUX,
            route_output=ip_out.ROUTE_OUTPUT_IPROUTE
        )
        ok_(res)
