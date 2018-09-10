import re
ro = re.compile('mayANk SinGH', re.IGNORECASE)
mo = ro.search('My name is Mayank Singh')
print(mo.group())
