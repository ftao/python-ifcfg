
import re
import socket
    
from .meta import MetaMixin
from .tools import exec_cmd, hex2dotted

class IfcfgParser(MetaMixin):
    class Meta:
        ifconfig_cmd_args = ['ifconfig', '-a']
        patterns = [
            '(?P<name>^[a-zA-Z0-9]+): flags=(?P<flags>.*) mtu (?P<mtu>.*)',
            '.*(inet )(?P<inet>[^\s]*).*',
            '.*(inet6 )(?P<inet6>[^\s]*).*',
            '.*(broadcast )(?P<broadcast>[^\s]*).*',
            '.*(netmask )(?P<netmask>[^\s]*).*',    
            '.*(ether )(?P<ether>[^\s]*).*',
            '.*(prefixlen )(?P<prefixlen>[^\s]*).*',
            '.*(scopeid )(?P<scopeid>[^\s]*).*',
            '.*(ether )(?P<ether>[^\s]*).*',
            ]
        override_patterns = []
        
    def __init__(self, *args, **kw):
        super(IfcfgParser, self).__init__(*args, **kw)
        self._interfaces = {}
        self.ifconfig_data = None
        self.parse()
        
    def _get_patterns(self):
        return self._meta.patterns + self._meta.override_patterns
            
    def parse(self):
        _interfaces = {}
        out, err, retcode = exec_cmd(self._meta.ifconfig_cmd_args)
        self.ifconfig_data = out
        cur = None
        all_keys = []
        
        for line in self.ifconfig_data.splitlines():
            for pattern in self._get_patterns():
                m = re.match(pattern, line)
                if m:
                    groupdict = m.groupdict()
                    # Special treatment to trigger which interface we're 
                    # setting for if 'name' is in the line.  Presumably the
                    # name of the interface is within the first line of the
                    # device block.
                    if 'name' in groupdict:
                        cur = groupdict['name']
                        if not self._interfaces.has_key(cur):
                            self._interfaces[cur] = {}
                    
                    for key in groupdict:
                        if key not in all_keys:
                            all_keys.append(key)
                        self._interfaces[cur][key] = groupdict[key]
                    
        # fixup some things
        for device,device_dict in self.interfaces.items():
            if 'inet' in device_dict:
                try:
                    host = socket.gethostbyaddr(device_dict['inet'])[0]
                    self.interfaces[device]['hostname'] = host
                except socket.herror as e:
                    self.interfaces[device]['hostname'] = None
                
        # standardize
        for key in all_keys:
            for device,device_dict in self.interfaces.items():
                if key not in device_dict:
                    self.interfaces[device][key] = None
                if type(device_dict[key]) == str:
                    self.interfaces[device][key] = device_dict[key].lower()
                    
            
    def interface_names(self):
        names = []
        for line in self.ifconfig_data.splitlines():
            m = re.match(self._meta.re_name, line)
            if m:
                names.append(m.group(1))
        return names
        
    @property
    def interfaces(self):
        return self._interfaces
        
class UnixParser(IfcfgParser):
    def __init__(self, *args, **kw):
        super(UnixParser, self).__init__(*args, **kw)

class LinuxParser(UnixParser):
    def __init__(self, *args, **kw):
        super(LinuxParser, self).__init__(*args, **kw)

class MacOSXParser(UnixParser):
    class Meta:
        override_patterns = [
            '.*(status: )(?P<status>[^\s]*).*',
            '.*(media: )(?P<media>.*)',
            ]
            
    def __init__(self, *args, **kw):
        super(MacOSXParser, self).__init__(*args, **kw)
    
    def parse(self, *args, **kw):
        super(MacOSXParser, self).parse(*args, **kw)
        
        # fix up netmask address for mac
        for device,device_dict in self.interfaces.items():
            if device_dict['netmask'] is not None:
                netmask = self.interfaces[device]['netmask']
                self.interfaces[device]['netmask'] = hex2dotted(netmask)
