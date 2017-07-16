#!/usr/bin/python
import pythonwhois
import json
import sys

#Usage: python [whois.py] [result.txt]

f_domain = open('domain.txt','r') #input domain
domain_data = f_domain.read().split()

def date_handler(obj):      #this funciton in order to catch timeerror
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

f_result = open(sys.argv[1],'w')

for line in domain_data:
    data = pythonwhois.get_whois(line)
    json_data = json.dumps(data,default=date_handler)
    f_result.write(str(json_data))
print "Complete!!\nCheck result.txt!"
f_result.close()
f_domain.close()
