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


MACOSX2 = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
        options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
        inet 127.0.1.99 netmask 0xff000000
        nd6 options=201<PERFORMNUD,DAD>
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        ether 8c:85:90:00:aa:bb
        inet6 fe80::1c8b:e7cc:c695:a6de%en0 prefixlen 64 secured scopeid 0x6
        inet 10.0.1.12 netmask 0xffff0000 broadcast 10.0.255.255
        inet6 2601:980:c000:7c5a:da:6a59:1e94:b03 prefixlen 64 autoconf secured
        inet6 2601:980:c000:7c5a:fdb3:b90c:80d6:abcd prefixlen 64 deprecated autoconf temporary
        inet6 2601:980:c000:7c5a:34b0:676d:93f7:0123 prefixlen 64 autoconf temporary
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect
        status: active
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
        options=60<TSO4,TSO6>
        ether 7a:00:48:a1:b2:00
        media: autoselect <full-duplex>
        status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
        ether 0e:85:90:0f:ab:cd
        media: autoselect
        status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
        ether 2e:51:48:37:99:0a
        inet6 fe80::2c51:48ff:fe37:86f8%awdl0 prefixlen 64 scopeid 0xc
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect
        status: active
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=63<RXCSUM,TXCSUM,TSO4,TSO6>
        ether 7a:00:48:c8:aa:bd
        Configuration:
                id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
                maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
                root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
                ipfilter disabled flags 0x2
        member: en1 flags=3<LEARNING,DISCOVER>
                ifmaxaddr 0 port 7 priority 0 path cost 0
        member: en2 flags=3<LEARNING,DISCOVER>
                ifmaxaddr 0 port 8 priority 0 path cost 0
        member: en3 flags=3<LEARNING,DISCOVER>
                ifmaxaddr 0 port 9 priority 0 path cost 0
        member: en4 flags=3<LEARNING,DISCOVER>
                ifmaxaddr 0 port 10 priority 0 path cost 0
        nd6 options=201<PERFORMNUD,DAD>
        media: <unknown type>
        status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
        inet6 fe80::ebb7:7d4a:49e8:e4fc%utun0 prefixlen 64 scopeid 0xe
        nd6 options=201<PERFORMNUD,DAD>
vboxnet0: flags=8842<BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        ether 0a:00:27:00:00:00
en5: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        ether ac:de:48:00:22:11
        inet6 fe80::aede:48ff:fe00:2211%en5 prefixlen 64 scopeid 0x5
        nd6 options=281<PERFORMNUD,INSECURE,DAD>
        media: autoselect
        status: active
"""

# See: https://github.com/ftao/python-ifcfg/issues/40
LINUX_VLAN = """
br2       Link encap:Ethernet  HWaddr 08:00:27:7c:6d:9d
          inet addr:10.0.0.1  Bcast:10.0.0.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe7c:6d9d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:20 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:1528 (1.4 KiB)

br4       Link encap:Ethernet  HWaddr 08:00:27:7c:6d:9d
          inet addr:10.0.2.1  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe7c:6d9d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:727 errors:0 dropped:0 overruns:0 frame:0
          TX packets:643 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:88547 (86.4 KiB)  TX bytes:890348 (869.4 KiB)

brlan     Link encap:Ethernet  HWaddr 08:00:27:d8:78:41
          inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fed8:7841/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:6905 errors:0 dropped:0 overruns:0 frame:0
          TX packets:20 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:351150 (342.9 KiB)  TX bytes:1568 (1.5 KiB)

eth0      Link encap:Ethernet  HWaddr 08:00:27:d8:78:41
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:7353 errors:0 dropped:433 overruns:0 frame:0
          TX packets:20 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:482610 (471.2 KiB)  TX bytes:1568 (1.5 KiB)

eth1      Link encap:Ethernet  HWaddr 08:00:27:f2:d0:cb
          inet addr:172.16.25.205  Bcast:172.16.25.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fef2:d0cb/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:65901 errors:0 dropped:0 overruns:0 frame:0
          TX packets:36638 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:80272939 (76.5 MiB)  TX bytes:5598473 (5.3 MiB)

eth2      Link encap:Ethernet  HWaddr 08:00:27:7c:6d:9d
          inet6 addr: fe80::a00:27ff:fe7c:6d9d/64 Scope:Link
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:7200 errors:0 dropped:431 overruns:0 frame:0
          TX packets:111 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:471382 (460.3 KiB)  TX bytes:8368 (8.1 KiB)

eth2.2    Link encap:Ethernet  HWaddr 08:00:27:7c:6d:9d
          inet6 addr: fe80::a00:27ff:fe7c:6d9d/64 Scope:Link
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:31 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:2278 (2.2 KiB)

eth2.4    Link encap:Ethernet  HWaddr 08:00:27:7c:6d:9d
          inet6 addr: fe80::a00:27ff:fe7c:6d9d/64 Scope:Link
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:52 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:3704 (3.6 KiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:12786 errors:0 dropped:0 overruns:0 frame:0
          TX packets:12786 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:1853178 (1.7 MiB)  TX bytes:1853178 (1.7 MiB)
"""


ROUTE_OUTPUT = """
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    600    0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 eth0
"""
