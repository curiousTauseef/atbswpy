import re
ro=re.compile(r'Bat(wo)+man')
mo=ro.search('Hey there, the Batwowowowowoman is awesome')
print(mo.group())

mo2=ro.search('Hey there, the Batwoman is awesome')
print(mo2.group())
