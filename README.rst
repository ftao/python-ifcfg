Python Ifconfig Wrapper for Unix/Linux/MacOSX
=============================================

.. image:: https://badge.fury.io/py/ifcfg.svg
   :target: https://pypi.python.org/pypi/ifcfg/
.. image:: https://travis-ci.org/learningequality/python-ifcfg.svg
  :target: https://travis-ci.org/learningequality/python-ifcfg
.. image:: http://codecov.io/github/learningequality/python-ifcfg/coverage.svg?branch=master
  :target: http://codecov.io/github/learningequality/python-ifcfg?branch=master

Ifcfg is a cross-platform (\*nix) library for parsing 'ifconfig' output
in Python. It is useful for pulling information such as IP, Netmask, MAC
Address, Hostname, etc.

Some Limitations:

-  Targeted for Unix-like operating systems including Linux and Mac OSX
-  Relies on parsing ``ifconfig`` or ``ip address`` output

Usage
-----

::

    import ifcfg
    import json

    for interface in ifcfg.interfaces:
        # do something with interface
        print interface['device']
        print interface['inet']
        print interface['inet6']
        print interface['netmask']
        print interface['broadcast']

    default = ifcfg.default_interface()

The output of 'ifcfg.interfaces' dumped to JSON looks something like the
following:

::

    $ python test.py | python -mjson.tool
    {
        "eth0": {
            "broadcast": "172.16.217.255",
            "ether": "00:0c:29:0c:da:5d",
            "flags": "4163<up,broadcast,running,multicast> ",
            "hostname": "derks-vm.local",
            "inet": "172.16.217.10",
            "inet6": "fe80::20c:29ff:fe0c:da5d",
            "mtu": "1500",
            "name": "eth0",
            "netmask": "255.255.255.0",
            "prefixlen": "64",
            "scopeid": "0x20<link>"
        },
        "lo": {
            "ether": null,
            "flags": "73<up,loopback,running> ",
            "hostname": "localhost",
            "inet": "127.0.0.1",
            "inet6": "::1",
            "mtu": "16436",
            "name": "lo",
            "netmask": "255.0.0.0",
            "prefixlen": "128",
            "scopeid": "0x10<host>"
        },
        "virbr0": {
            "broadcast": "192.168.122.255",
            "ether": "52:54:00:5b:70:0d",
            "flags": "4099<up,broadcast,multicast> ",
            "hostname": "derks-vm.local",
            "inet": "192.168.122.1",
            "inet6": null,
            "mtu": "1500",
            "name": "virbr0",
            "netmask": "255.255.255.0",
        }
    }


Release notes
-------------

0.11 (unreleased)
_________________

This release seeks to clean up the codebase (sparingly!) and introduce
Windows compatibility.

* Removing ill-defined ``encoding`` keyword arg from ``ifcfg.get_parser``
* Removed no-op Linux Kernel 2.x parsing and ``kernel`` keyword arg
* Removed class ``ifcfg.IfcfgParser``, use ``UnixParser`` instead
* All strings are UTF-8, also in Py 2.7
* Only cross-platform features are now guaranteed to be in the result set:
  ``['inet', 'ether', 'inet6', 'netmask']``
* IPv6 addresses are now stored in a list.
* Removed prefixlen, as it should be added to one IPv6 address, not the
  interface


0.10.1
______

* Fixed encoding issues, preventing ``default_interface`` to be detected


0.10
____

* Support for Unix systems w/o ``ifconfig``, for instance newer Ubuntu/Debian
* Refactored to use  ``src/`` hierarchy



License
-------

The Ifcfg library is Open Source and is distributed under the BSD
License (three clause). Please see the LICENSE file included with this
software.
