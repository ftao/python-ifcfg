"""Tests for Ifcfg."""

import unittest
from nose.tools import ok_, eq_, raises
from nose import SkipTest

import ifcfg
from . import ifconfig_out
    
class IfcfgTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_ifcfg(self):
        interfaces = ifcfg.interfaces()
        res = len(interfaces) > 0
        ok_(res)

    @raises(ifcfg.exc.IfcfgParserError)
    def test_unknown(self):
        parser = ifcfg.get_parser(distro='Bogus', kernel='55')
        
    def test_linux(self):
        parser = ifcfg.get_parser(distro='Linux', kernel='4',
                                  ifconfig=ifconfig_out.LINUX)
        interfaces = parser.interfaces
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')
        
    def test_linux2(self):
        parser = ifcfg.get_parser(distro='Linux', kernel='2.6', 
                                  ifconfig=ifconfig_out.LINUX2)
        interfaces = parser.interfaces
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')
        
    def test_linux3(self):
        parser = ifcfg.get_parser(distro='Linux', kernel='3.3', 
                                  ifconfig=ifconfig_out.LINUX3)
        interfaces = parser.interfaces
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')
        
    def test_macosx(self):
        parser = ifcfg.get_parser(distro='MacOSX', kernel='11.4.0',
                                  ifconfig=ifconfig_out.MACOSX)
        interfaces = parser.interfaces
        eq_(interfaces['en0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['en0']['inet'], '192.168.0.1')
        eq_(interfaces['en0']['broadcast'], '192.168.0.255')
        eq_(interfaces['en0']['netmask'], '255.255.255.0')
    
    def test_default_interface(self):
        res = ifcfg.default_interface()
        ok_(res)