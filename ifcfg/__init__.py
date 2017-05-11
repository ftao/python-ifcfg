import os
import platform
import re
from . import parser
from . import tools
from . import exc

__version__ = "0.10.1"

Log = tools.minimal_logger(__name__)


def get_parser(**kw):
    """
    Detect the proper parser class, and return it instantiated.
    
    Optional Arguments:
    
        parser
            The parser class to use instead of detecting the proper one.
            
        distro
            The distro to parse for (used for testing).
        
        kernel
            The kernel to parse for (used for testing).
        
        ifconfig
            The ifconfig (stdout) to pass to the parser (used for testing).
            
    """
    Parser = kw.get('parser', None)
    ifconfig = kw.get('ifconfig', None)
    if not Parser:
        distro = kw.get('distro', platform.system())
        full_kernel = kw.get('kernel', platform.uname()[2])
        split_kernel = full_kernel.split('.')[0:2]
        kernel_version = int(split_kernel[0])
        
        if len(split_kernel) > 1:
            kernel_major_rev = int(re.match('\d+', split_kernel[1]).group())
        else:
            kernel_major_rev = 0

        if distro == 'Linux':
            if kernel_version < 3 and kernel_major_rev < 3:
                from .parser import Linux2Parser
                Parser = Linux2Parser
            else:
                from .parser import LinuxParser
                Parser = LinuxParser
        elif distro in ['Darwin', 'MacOSX']:
            from .parser import MacOSXParser
            Parser = MacOSXParser
        else:
            raise exc.IfcfgParserError("Unknown distro type '%s'." % distro)
        Log.debug("Distro detected as '%s'" % distro)
        Log.debug("Using '%s'" % Parser)
        if not os.path.exists(Parser.get_command()[0]):
            Log.debug("Could not find 'ifconfig' cmd, falling back to 'ip' cmd")
            from .parser import UnixIPParser
            Parser = UnixIPParser

    return Parser(ifconfig=ifconfig)
    
def interfaces():
    """
    Return just the parsed interfaces dictionary from the proper parser.
    
    """
    parser = get_parser()
    return parser.interfaces

def default_interface():
    """
    Return just the default interface device dictionary.
    
    """
    parser = get_parser()
    return parser.default_interface

