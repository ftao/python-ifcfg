# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Output from Ubuntu 16.04

LINUX = """1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s25: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether a0:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether a0:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
    inet 192.168.12.34/24 brd 192.168.12.255 scope global dynamic wlp3s0
       valid_lft 30124sec preferred_lft 30124sec
    inet6 fd37:a521:ada9::869/128 scope global
       valid_lft forever preferred_lft forever
    inet6 fd37:a521:ada9:0:b9f7:44f8:bb19:c78c/64 scope global temporary dynamic
       valid_lft 7188sec preferred_lft 1788sec
    inet6 fd37:a521:ada9:0:9073:a91:d14f:8087/64 scope global mngtmpaddr noprefixroute dynamic
       valid_lft 7188sec preferred_lft 1788sec
    inet6 fe80::205f:5d09:d0da:7aed/64 scope link
       valid_lft forever preferred_lft forever
6: wwp0s29u1u4i6: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether a0:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
8: enp6s0.2@enp6s0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 00:73:00:5c:09:9a brd ff:ff:ff:ff:ff:ff
    inet 10.2.2.253/24 scope global enp6s0.2
       valid_lft forever preferred_lft forever
    inet 10.1.1.253/24 scope global enp6s0.2
       valid_lft forever preferred_lft forever
"""

LINUX_MULTI_IPV4 = """
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether b8:27:eb:50:39:69 brd ff:ff:ff:ff:ff:ff
    inet 192.168.13.1/24 brd 192.168.13.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet 192.168.10.3/24 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::ba27:ebff:fe50:3969/64 scope link
       valid_lft forever preferred_lft forever
"""


ROUTE_OUTPUT = """
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    600    0        0 wlp3s0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 wlp3s0
192.168.12.0     0.0.0.0         255.255.255.0   U     600    0        0 wlp3s0
"""

ROUTE_OUTPUT_IPROUTE = """
default via 192.168.100.1 dev enp0s25 proto dhcp metric 100
10.8.0.0/24 via 10.8.0.2 dev tun0
10.8.0.2 dev tun0 proto kernel scope link src 10.8.0.1
169.254.0.0/16 dev enp0s25 scope link metric 1000
192.168.100.0/24 dev enp0s25 proto kernel scope link src 192.168.100.252 metric 100
"""
