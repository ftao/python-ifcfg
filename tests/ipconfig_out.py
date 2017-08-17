# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This example contains a bunch of virtual devices and one configured ethernet
# device. The unconfigured devices should not figure in parsed results.
WINDOWS_10_ETH = """
Windows IP Configuration

   Host Name . . . . . . . . . . . . : TEST-COMPUTER
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : lan

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : Realtek PCIe GBE Family Controller
   Physical Address. . . . . . . . . : 11-11-11-11-A1-FA
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : abcd:1234:a123::123(Preferred)
   Lease Obtained. . . . . . . . . . : Thursday, July 13, 2017 7:14:10 PM
   Lease Expires . . . . . . . . . . : Sunday, September 2, 2153 11:24:49 PM
   IPv6 Address. . . . . . . . . . . : abcd:1234:1234::1:abcd:1234:abcd:123(Preferred)
   Temporary IPv6 Address. . . . . . : abcd:1234:1234::1:abcd:1234:abcd:123(Preferred)
   Link-local IPv6 Address . . . . . : abcd::abcd:1234:a123:123%6(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.1.2(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Thursday, July 27, 2017 11:53:27 AM
   Lease Expires . . . . . . . . . . : Thursday, July 27, 2017 11:53:25 PM
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DHCPv6 IAID . . . . . . . . . . . : 160443188
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1F-2D-93-7D-90-2B-34-D1-AC-F7
   DNS Servers . . . . . . . . . . . : abcd:1234:1234::1
                                       192.168.1.1
   NetBIOS over Tcpip. . . . . . . . : Enabled
   Connection-specific DNS Suffix Search List :
                                       lan

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : AB-12-AB-12-AB-12
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Hosted Network Virtual Adapter
   Physical Address. . . . . . . . . : AB-12-AB-12-AB-12
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : ASUS PCE-N15 11n Wireless LAN PCI-E Card
   Physical Address. . . . . . . . . : AB-12-AB-12-AB-12
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter isatap.lan:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter Teredo Tunneling Pseudo-Interface:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Teredo Tunneling Pseudo-Interface
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : 2001:0:5ef5:79fb:102f:fbfe:678c:7875(Preferred)
   Link-local IPv6 Address . . . . . : fe80::102f:fbfe:678c:7875%13(Preferred)
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 503316480
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1F-2D-93-7D-90-2B-34-D1-AC-F7
   NetBIOS over Tcpip. . . . . . . . : Disabled"""


WINDOWS_10_WLAN = """
Windows IP Configuration

   Host Name . . . . . . . . . . . . : TEST-PC
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : lan

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : some_old_cached_result.com
   Description . . . . . . . . . . . : Controller i Realtek PCIe FE-serien
   Physical Address. . . . . . . . . : 12-34-56-78-ab-cd
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter LAN-forbindelse* 11:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Virtuelt kort til Microsoft Wi-Fi Direct
   Physical Address. . . . . . . . . : 23-45-67-89-ab-cd
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : Broadcom 802.11 netværksadapter
   Physical Address. . . . . . . . . : 23-45-67-89-ab-cd
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : fd37:a521:ada9::c69(Preferred)
   Lease Obtained. . . . . . . . . . : 27. juli 2017 13:31:59
   Lease Expires . . . . . . . . . . : 2. september 2153 23:39:45
   IPv6 Address. . . . . . . . . . . : fd37:a521:ada9:0:959f:2086:5992:3d86(Preferred)
   Temporary IPv6 Address. . . . . . : fd37:a521:ada9:0:e4b6:6195:75af:f121(Preferred)
   Link-local IPv6 Address . . . . . : fe80::959f:2086:5992:3d86%20(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.40.219(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 27. juli 2017 13:32:00
   Lease Expires . . . . . . . . . . : 28. juli 2017 01:32:00
   Default Gateway . . . . . . . . . : 192.168.40.1
   DHCP Server . . . . . . . . . . . : 192.168.40.1
   DHCPv6 IAID . . . . . . . . . . . : 267696098
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-19-D8-06-36-F4-B7-E2-F4-9E-1F
   DNS Servers . . . . . . . . . . . : fd37:a521:ada9::1
                                       192.168.40.1
   NetBIOS over Tcpip. . . . . . . . : Enabled
   Connection-specific DNS Suffix Search List :
                                       lan

Ethernet adapter Bluetooth-netværksforbindelse:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Bluetooth-enhed (Personal Area Network)
   Physical Address. . . . . . . . . : F4-B7-E2-F4-9E-20
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter isatap.lan:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter LAN-forbindelse* 13:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Teredo Tunneling Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : 2001:0:5ef5:79fb:2c7a:b7e:678c:7875(Preferred)
   Link-local IPv6 Address . . . . . : fe80::2c7a:b7e:678c:7875%6(Preferred)
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 553648128
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-19-D8-06-36-F4-B7-E2-F4-9E-1F
   NetBIOS over Tcpip. . . . . . . . : Disabled

"""


WINDOWS_7_VM = """
Windows IP Configuration


Ethernet adapter Local Area Connection 2:

   Connection-specific DNS Suffix  . : lan
   Link-local IPv6 Address . . . . . : fe80::cad:9321:168e:83e3%13
   IPv4 Address. . . . . . . . . . . : 10.0.2.15
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.0.2.2

Tunnel adapter isatap.lan:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : lan

Tunnel adapter Teredo Tunneling Pseudo-Interface:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2001:0:5ef5:79fb:2002:2dbb:f5ff:fdf0
   Link-local IPv6 Address . . . . . : fe80::2002:2dbb:f5ff:fdf0%14
   Default Gateway . . . . . . . . . : ::

"""


WINDOWS_10_WITH_2_ETHERNETS = """
Windows IP Configuration

   Host Name . . . . . . . . . . . . : MSEDGEWIN10
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) PRO/1000 MT Desktop Adapter
   Physical Address. . . . . . . . . : 08-00-27-CC-BE-AF
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e59b:7afd:78a6:d073%4(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.0.2.15(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : jueves, 3 de agosto de 2017 1:00:44
   Lease Expires . . . . . . . . . . : viernes, 4 de agosto de 2017 1:00:59
   Default Gateway . . . . . . . . . : 10.0.2.2
   DHCP Server . . . . . . . . . . . : 10.0.2.2
   DHCPv6 IAID . . . . . . . . . . . : 34078759
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1F-22-AC-9F-08-00-27-CC-BE-AF
   DNS Servers . . . . . . . . . . . : 89.150.129.22
                                       89.150.129.10
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet 2:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) PRO/1000 MT Desktop Adapter #2
   Physical Address. . . . . . . . . : 08-00-27-0D-9A-0B
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::99e0:2790:ba60:20e1%5(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.56.101(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : jueves, 3 de agosto de 2017 1:00:44
   Lease Expires . . . . . . . . . . : jueves, 3 de agosto de 2017 1:20:59
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 192.168.56.100
   DHCPv6 IAID . . . . . . . . . . . : 151519271
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1F-22-AC-9F-08-00-27-CC-BE-AF
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter isatap.{ADDEF65B-69BD-40F2-A0E6-4B67361ECE85}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter isatap.{BFDBE788-14F2-499A-9D83-CDCD34CDE463}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter #2
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
"""
