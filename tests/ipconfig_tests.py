# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import binascii
import subprocess

import ifcfg
import mock
from ifcfg import tools
from ifcfg.parser import WindowsParser
from nose.tools import eq_, ok_

from . import ipconfig_out
from .base import IfcfgTestCase


class WindowsTestCase(IfcfgTestCase):

    def test_interfaces(self):
        ifcfg.Parser = WindowsParser
        interfaces = ifcfg.interfaces(ifconfig=ipconfig_out.WINDOWS_10_ETH)
        res = len(interfaces) > 0
        ok_(res)

    def test_windows10(self):
        ifcfg.distro = "Windows"
        ifcfg.Parser = ifcfg.get_parser_class()

        self.assertTrue(issubclass(ifcfg.Parser, WindowsParser))

        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_10_ETH)
        interfaces = parser.interfaces

        self.assertIn("Ethernet adapter Ethernet", interfaces.keys())
        self.assertIn("Wireless LAN adapter Local Area Connection* 2", interfaces.keys())
        self.assertIn("Wireless LAN adapter Local Area Connection* 3", interfaces.keys())
        self.assertIn("Wireless LAN adapter Wi-Fi", interfaces.keys())
        self.assertIn("Tunnel adapter isatap.lan", interfaces.keys())
        self.assertIn("Tunnel adapter Teredo Tunneling Pseudo-Interface", interfaces.keys())

        self.assertEqual(len(interfaces.keys()), 6)

        eq_(interfaces['Ethernet adapter Ethernet']['inet'], '192.168.1.2')
        eq_(interfaces['Ethernet adapter Ethernet']['inet4'][0], '192.168.1.2')
        eq_(interfaces['Ethernet adapter Ethernet']['ether'], '11:11:11:11:a1:fa')
        eq_(interfaces['Ethernet adapter Ethernet']['default_gateway'], '192.168.1.1')
        eq_(interfaces['Ethernet adapter Ethernet']['netmask'], '255.255.255.0')

    def test_default_interface_windows10(self):
        ifcfg.distro = 'Windows'
        ifcfg.Parser = ifcfg.get_parser_class()

        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_10_ETH)
        default = parser.default_interface
        ok_(default)
        eq_(default['inet'], '192.168.1.2')
        eq_(default['default_gateway'], '192.168.1.1')
        eq_(default['netmask'], '255.255.255.0')

    def test_windows10_w_2_ethernets(self):
        ifcfg.distro = "Windows"
        ifcfg.Parser = ifcfg.get_parser_class()

        self.assertTrue(issubclass(ifcfg.Parser, WindowsParser))

        parser = ifcfg.get_parser(
            ifconfig=ipconfig_out.WINDOWS_10_WITH_2_ETHERNETS
        )
        interfaces = parser.interfaces

        # Check that the first adapter is present
        self.assertIn("Ethernet adapter Ethernet", interfaces.keys())

        # Check that the second adapter is present
        self.assertIn("Ethernet adapter Ethernet 2", interfaces.keys())

        self.assertEqual(len(interfaces.keys()), 4)

        # Check that properties of both adapters are correct

        # Adapter 1
        eq_(interfaces['Ethernet adapter Ethernet']['inet'], '10.0.2.15')
        eq_(interfaces['Ethernet adapter Ethernet']['ether'], '08:00:27:cc:be:af')
        eq_(interfaces['Ethernet adapter Ethernet']['inet6'], [])
        eq_(interfaces['Ethernet adapter Ethernet']['netmask'], '255.255.254.0')

        # Adapter 2
        eq_(interfaces['Ethernet adapter Ethernet 2']['inet'], '192.168.56.101')
        eq_(interfaces['Ethernet adapter Ethernet 2']['ether'], '08:00:27:0d:9a:0b')
        eq_(interfaces['Ethernet adapter Ethernet 2']['inet6'], [])
        eq_(interfaces['Ethernet adapter Ethernet 2']['netmask'], '255.255.255.0')

    def test_default_interface_windows10_w_2_ethernets(self):
        ifcfg.distro = 'Windows'
        ifcfg.Parser = ifcfg.get_parser_class()

        parser = ifcfg.get_parser(
            ifconfig=ipconfig_out.WINDOWS_10_WITH_2_ETHERNETS
        )
        default = parser.default_interface
        ok_(default)
        eq_(default['inet'], '10.0.2.15')
        eq_(default['default_gateway'], '10.0.2.2')
        eq_(default['netmask'], '255.255.254.0')

    def test_windows7vm(self):
        ifcfg.distro = "Windows"
        ifcfg.Parser = ifcfg.get_parser_class()

        self.assertTrue(issubclass(ifcfg.Parser, WindowsParser))

        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_7_VM)
        interfaces = parser.interfaces

        self.assertIn("Ethernet adapter Local Area Connection 2", interfaces.keys())
        self.assertIn("Tunnel adapter isatap.lan", interfaces.keys())
        self.assertIn("Tunnel adapter Teredo Tunneling Pseudo-Interface", interfaces.keys())

        self.assertEqual(len(interfaces.keys()), 3)

        eq_(interfaces['Ethernet adapter Local Area Connection 2']['inet'], '10.0.2.15')
        self.assertEqual(
            len(interfaces['Ethernet adapter Local Area Connection 2']['inet6']),
            0
        )

    def test_default_interface_windows7vm(self):
        ifcfg.distro = 'Windows'
        ifcfg.Parser = ifcfg.get_parser_class()

        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_7_VM)
        default = parser.default_interface
        ok_(default)
        eq_(default['inet'], '10.0.2.15')
        eq_(default['default_gateway'], '10.0.2.2')
        eq_(default['netmask'], '255.255.254.0')

    def test_default_interface_windows10_wlan(self):
        ifcfg.distro = 'Windows'
        ifcfg.Parser = ifcfg.get_parser_class()

        parser = ifcfg.get_parser(ifconfig=ipconfig_out.WINDOWS_10_WLAN)
        default = parser.default_interface
        ok_(default)
        eq_(default['inet'], '192.168.40.219')
        eq_(default['default_gateway'], '192.168.40.1')
        eq_(default['netmask'], '255.255.255.0')

    # Add a character that's known to fail in cp1252 encoding
    # Patching `wait` is needed because on CI, these process (for Windows) don't really exist and cannot be executed
    # `wait` sets the returncode which must be 0 for the parser to run
    @mock.patch.object(subprocess.Popen, 'wait', lambda __: 0)
    @mock.patch.object(subprocess.Popen, 'communicate', lambda __: [ipconfig_out.WINDOWS_7_VM.encode('cp1252') + binascii.unhexlify("81"), "".encode('cp1252')])
    @mock.patch.object(tools, 'system_encoding', "cp1252")
    def test_cp1252_encoding(self):
        """
        Tests that things are still working when using this bizarre encoding
        """

        ifcfg.distro = "Windows"
        ifcfg.Parser = ifcfg.get_parser_class()

        self.assertTrue(issubclass(ifcfg.Parser, WindowsParser))

        parser = ifcfg.get_parser()
        interfaces = parser.interfaces

        self.assertIn("Ethernet adapter Local Area Connection 2", interfaces.keys())
        self.assertIn("Tunnel adapter isatap.lan", interfaces.keys())
        self.assertIn("Tunnel adapter Teredo Tunneling Pseudo-Interface", interfaces.keys())

        self.assertEqual(len(interfaces.keys()), 3)

        eq_(interfaces['Ethernet adapter Local Area Connection 2']['inet'], '10.0.2.15')
        self.assertEqual(
            len(interfaces['Ethernet adapter Local Area Connection 2']['inet6']),
            0
        )

    # Add a character that's known to fail in unicode encoding
    # https://github.com/ftao/python-ifcfg/issues/17
    @mock.patch.object(subprocess.Popen, 'wait', lambda __: 0)  # See test_cp1252_encoding's mocks as well
    @mock.patch.object(subprocess.Popen, 'communicate', lambda __: [ipconfig_out.WINDOWS_7_VM.encode('cp1252') + binascii.unhexlify("84"), "".encode('cp1252')])
    @mock.patch.object(tools, 'system_encoding', "cp1252")
    def test_cp1252_non_utf8_byte(self):
        """
        Tests that things are still working when using this bizarre encoding
        """

        ifcfg.distro = "Windows"
        ifcfg.Parser = ifcfg.get_parser_class()

        self.assertTrue(issubclass(ifcfg.Parser, WindowsParser))

        parser = ifcfg.get_parser()
        interfaces = parser.interfaces

        self.assertIn("Ethernet adapter Local Area Connection 2", interfaces.keys())
        self.assertIn("Tunnel adapter isatap.lan", interfaces.keys())
        self.assertIn("Tunnel adapter Teredo Tunneling Pseudo-Interface", interfaces.keys())

        self.assertEqual(len(interfaces.keys()), 3)

        eq_(interfaces['Ethernet adapter Local Area Connection 2']['inet'], '10.0.2.15')
        self.assertEqual(
            len(interfaces['Ethernet adapter Local Area Connection 2']['inet6']),
            0
        )
