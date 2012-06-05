
import ifcfg 
import json

i = ifcfg.parse()
print json.dumps(i.interfaces)