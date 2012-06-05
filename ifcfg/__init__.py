
import platform

def parse(parser=None):
    if not parser:
        s = platform.system()
        if s == 'Linux':
            from .parser import LinuxParser
            parser = LinuxParser()
        elif s == 'Darwin':
            from .parser import MacOSXParser
            parser = MacOSXParser()
        else:
            raise IfcfgParserError("Unknown system type '%s'." % s)
            
    return parser
    
