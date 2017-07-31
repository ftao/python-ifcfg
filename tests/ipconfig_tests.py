import ifcfg
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
        ifcfg.distro = "win32"
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
        eq_(interfaces['Ethernet adapter Ethernet']['ether'], '11:11:11:11:a1:fa')
