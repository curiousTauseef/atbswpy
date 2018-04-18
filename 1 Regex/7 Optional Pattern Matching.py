# ()? this matches optionally
# that means if particular pattern inside the brackets is available match it or match everything else
import re
regObj=re.compile(r'Bat(wo)?man')
mo=regObj.search('My favorite super hero is Batwoman')
print(mo.group(0))  #matches complete
print(mo.group(1))  #matches only optional
print(mo.group())   #matches complete
