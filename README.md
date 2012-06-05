Python Wrapper Around the Ifconfig Utility on Unix/Linux/MacOSX
=============================================================================

Ifcfg is a cross-platform (*nix) library for parsing 'ifconfig' output in
Python.  It is useful for pulling information such as IP, Netmask, MAC Address, 
Hostname, etc.

Some Limitations:

 * Targeted for Unix-like operating systems including Linux and Mac OSX
 * Relies on parsing 'ifconfig' output
    
    
Usage
-----

    import ifcfg
    parser = ifcfg.parse()
    
    for interface in parser.interfaces:
        print interface['name']
        print interface['ether']
        print interface['inet']
        print interface['inet6]
        print interface['netmask']
        print interface['flags']
        print interface['hostname']
        print interface['mtu']

    
License
-------

The dRest library is Open Source and is distributed under the BSD License 
(three clause).  Please see the LICENSE file included with this software.  