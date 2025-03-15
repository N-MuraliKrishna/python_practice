import re
s='engineering'
print(re.match('en',s))
print(re.search('e',s))
print(re.findall('e',s))
print(re.split('e',s,1))
print(re.subn('e','p',s))
print(list(re.finditer('e',s)))


import re
s='aAbcdfefg\n123\t@#$%'
print(re.findall('$',s))




