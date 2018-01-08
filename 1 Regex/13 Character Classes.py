import re
ro=re.compile(r'\d+\s\w+')
mo=ro.findall('1 AAA 2 BBB 3 CCC 4 DDD 5 EEE')
print(mo)
