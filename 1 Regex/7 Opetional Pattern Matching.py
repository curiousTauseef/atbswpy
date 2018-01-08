# ()? this matches optionally

import re
regObj=re.compile(r'Bat(wo)?man')
mo=regObj.search('My favorite super hero is Batwoman')
print(mo.group())
