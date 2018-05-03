# -*- coding: utf-8 -*-
from __future__ import unicode_literals

LINUX2 = """
eth0      Link encap:Ethernet  HWaddr 1a:2b:3c:4d:5e:6f
          inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::4240:36ff:fe38:a121/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:4041381 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3851783 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1123058554 (1.0 GiB)  TX bytes:737462074 (703.2 MiB)
          Interrupt:24

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:126491 errors:0 dropped:0 overruns:0 frame:0
          TX packets:126491 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:43170341 (41.1 MiB)  TX bytes:43170341 (41.1 MiB)
"""

LINUX3 = """
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::4240:36ff:fe38:a121  prefixlen 64  scopeid 0x20<link>
        ether 1a:2b:3c:4d:5e:6f  txqueuelen 1000  (Ethernet)
        RX packets 251031  bytes 146644544 (139.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 141266  bytes 28028187 (26.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 16436
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 1462  bytes 112866 (110.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1462  bytes 112866 (110.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

LINUXDOCKER = """
br-736aa253dd57: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.19.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        inet6 fe80::42:9cff:fefe:60db  prefixlen 64  scopeid 0x20<link>
        ether 02:42:9c:fe:60:db  txqueuelen 0  (Ethernet)
        RX packets 120327  bytes 1571313930 (1.5 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 121053  bytes 23186380 (23.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

br-c4d6dd0473e5: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.18.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        ether 02:42:a4:85:da:bd  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

br-c75cf3b1db15: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.20.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        ether 02:42:97:dd:9a:dd  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        ether 02:42:2a:ec:97:79  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s31f6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.94  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 2a01:cb19:810a:da00:59d7:a6e1:8596:12f3  prefixlen 64  scopeid 0x0<global>
        inet6 2a01:cb19:810a:da00:1e2b:9b33:6f04:df10  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::1487:95e4:d852:11aa  prefixlen 64  scopeid 0x20<link>
        ether 54:e1:ad:76:c8:cb  txqueuelen 1000  (Ethernet)
        RX packets 37234442  bytes 45411193577 (45.4 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 17430466  bytes 12618211757 (12.6 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xec200000-ec220000

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 2385680  bytes 1832529401 (1.8 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2385680  bytes 1832529401 (1.8 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:e2:85:a9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

LINUX = LINUX3


# Something out of order that we cannot parse
ILLEGAL_OUTPUT = """
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
"""

MACOSX = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
  options=2b<RXCSUM,TXCSUM,VLAN_HWTAGGING,TSO4>
  ether 1a:2b:3c:4d:5e:6f
  inet6 fe80::4240:36ff:fe38:a121%en0 prefixlen 64 scopeid 0x5
  inet 192.168.0.1 netmask 0xffffff00 broadcast 192.168.0.255
  media: autoselect (100baseTX <full-duplex>)
  status: active
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
  options=3<RXCSUM,TXCSUM>
  inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
  inet 127.0.0.1 netmask 0xff000000
  inet6 ::1 prefixlen 128
"""  # noqa


ROUTE_OUTPUT = """
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    600    0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 eth0
"""
