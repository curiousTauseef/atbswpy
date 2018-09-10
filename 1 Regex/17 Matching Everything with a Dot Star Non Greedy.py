# non greedy dot star

import re
ro = re.compile(r'<.*?>')
mo = ro.search('<My name is Mayank> all is nice>')
print(mo.group())
