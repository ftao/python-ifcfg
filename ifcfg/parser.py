
import os
import re
import socket

from .tools import exec_cmd, hex2dotted, minimal_logger

Log = minimal_logger(__name__)


class IfcfgParser(object):

    def __init__(self, *args, **kw):
        self._interfaces = {}
        self.ifconfig_data = kw.get('ifconfig', None)
        self.encoding = kw.get('encoding', 'latin1')
        self.parse(self.ifconfig_data)

    @classmethod
    def get_command(cls):
        ifconfig_cmd = 'ifconfig'
        for path in ['/sbin','/usr/sbin','/bin','/usr/bin']:
            if os.path.exists(os.path.join(path, ifconfig_cmd)):
                ifconfig_cmd = os.path.join(path, ifconfig_cmd)
                break
        return [ifconfig_cmd, '-a']

    @classmethod
    def get_patterns(cls):
        return [
            '(?P<device>^[a-zA-Z0-9]+): flags=(?P<flags>.*) mtu (?P<mtu>.*)',
            '.*(inet )(?P<inet>[^\s]*).*',
            '.*(inet6 )(?P<inet6>[^\s]*).*',
            '.*(broadcast )(?P<broadcast>[^\s]*).*',
            '.*(netmask )(?P<netmask>[^\s]*).*',
            '.*(ether )(?P<ether>[^\s]*).*',
            '.*(prefixlen )(?P<prefixlen>[^\s]*).*',
            '.*(scopeid )(?P<scopeid>[^\s]*).*',
            '.*(ether )(?P<ether>[^\s]*).*',
        ]

    def parse(self, ifconfig=None):
        """
        Parse ifconfig output into self._interfaces.

        Optional Arguments:

            ifconfig
                The data (stdout) from the ifconfig command.  Default is to
                call exec_cmd(self.get_command()).

        """
        _interfaces = []
        if not ifconfig:
            ifconfig, __, __ = exec_cmd(self.get_command())
        if hasattr(ifconfig, 'decode'):
            ifconfig = ifconfig.decode(self.encoding)
        self.ifconfig_data = ifconfig
        cur = None
        all_keys = []

        for line in self.ifconfig_data.splitlines():
            for pattern in self.get_patterns():
                m = re.match(pattern, line)
                if m:
                    groupdict = m.groupdict()
                    # Special treatment to trigger which interface we're
                    # setting for if 'device' is in the line.  Presumably the
                    # device of the interface is within the first line of the
                    # device block.
                    if 'device' in groupdict:
                        cur = groupdict['device']
                        if not cur in self._interfaces:
                            self._interfaces[cur] = {}

                    for key in groupdict:
                        if key not in all_keys:
                            all_keys.append(key)
                        self._interfaces[cur][key] = groupdict[key]

        # fix it up
        self._interfaces = self.alter(self._interfaces)

        # standardize
        for key in all_keys:
            for device,device_dict in self._interfaces.items():
                if key not in device_dict:
                    self._interfaces[device][key] = None
                if type(device_dict[key]) == str:
                    self._interfaces[device][key] = device_dict[key].lower()


    def alter(self, interfaces):
        """
        Used to provide the ability to alter the interfaces dictionary before
        it is returned from self.parse().

        Required Arguments:

            interfaces
                The interfaces dictionary.

        Returns: interfaces dict

        """
        # fixup some things
        for device,device_dict in interfaces.items():
            if 'inet' in device_dict:
                try:
                    host = socket.gethostbyaddr(device_dict['inet'])[0]
                    interfaces[device]['hostname'] = host
                except socket.herror:
                    interfaces[device]['hostname'] = None

        return interfaces

    @property
    def interfaces(self):
        """
        Returns the full interfaces dictionary.

        """
        return self._interfaces

    @property
    def default_interface(self):
        """
        Returns the default interface device.

        """
        out, __, __ = exec_cmd(['/sbin/route', '-n'])
        lines = out.splitlines()
        for line in lines[2:]:
            if line.split()[0] == '0.0.0.0':
                iface = line.split()[-1]

        for interface in self.interfaces:
            if interface == iface:
                return self.interfaces[interface]
        return None # pragma: nocover


class UnixParser(IfcfgParser):
    def __init__(self, *args, **kw):
        super(UnixParser, self).__init__(*args, **kw)


class LinuxParser(UnixParser):
    @classmethod
    def get_patterns(cls):
        return super(LinuxParser, cls).get_patterns() + [
            '(?P<device>^[a-zA-Z0-9:]+)(.*)Link encap:(.*).*',
            '(.*)Link encap:(.*)(HWaddr )(?P<ether>[^\s]*).*',
            '.*(inet addr:)(?P<inet>[^\s]*).*',
            '.*(inet6 addr: )(?P<inet6>[^\s\/]*/(?P<prefixlen>[\d]*)).*',
            '.*(P-t-P:)(?P<ptp>[^\s]*).*',
            '.*(Bcast:)(?P<broadcast>[^\s]*).*',
            '.*(Mask:)(?P<netmask>[^\s]*).*',
            '.*(Scope:)(?P<scopeid>[^\s]*).*',
            '.*(RX bytes:)(?P<rxbytes>\d+).*',
            '.*(TX bytes:)(?P<txbytes>\d+).*',
        ]

    def alter(self, interfaces):
        return interfaces


class Linux2Parser(LinuxParser):
    pass


class UnixIPParser(IfcfgParser):
    """
    Because ifconfig is getting deprecated, we can use ip address instead
    """

    @classmethod
    def get_command(cls):
        ifconfig_cmd = 'ip'
        for path in ['/sbin','/usr/sbin','/bin','/usr/bin']:
            if os.path.exists(os.path.join(path, ifconfig_cmd)):
                ifconfig_cmd = os.path.join(path, ifconfig_cmd)
                break
        return [ifconfig_cmd, 'address', 'show']
    
    @classmethod
    def get_patterns(cls):
        return [
            '\s*[0-9]+:\s+(?P<device>[a-zA-Z0-9]+):.*mtu (?P<mtu>.*)',
            '.*(inet )(?P<inet>[^/]+).*',
            '.*(inet6 )(?P<inet6>[^/]*).*',
            '.*(ether )(?P<ether>[^\s]*).*',
            '.*inet\s.*(brd )(?P<broadcast>[^\s]*).*',
            '.*(inet )[^/]+(?P<netmask>[/][0-9]+).*',
            #'.*(prefixlen )(?P<prefixlen>[^\s]*).*',
            #'.*(scopeid )(?P<scopeid>[^\s]*).*',
            #'.*(ether )(?P<ether>[^\s]*).*',
        ]


class MacOSXParser(UnixParser):

    @classmethod
    def get_patterns(cls):
        return super(MacOSXParser, cls).get_patterns() + [
            '.*(status: )(?P<status>[^\s]*).*',
            '.*(media: )(?P<media>.*)',
        ]

    def parse(self, *args, **kw):
        super(MacOSXParser, self).parse(*args, **kw)

        # fix up netmask address for mac
        for device,device_dict in self.interfaces.items():
            if device_dict['netmask'] is not None:
                netmask = self.interfaces[device]['netmask']
                self.interfaces[device]['netmask'] = hex2dotted(netmask)
