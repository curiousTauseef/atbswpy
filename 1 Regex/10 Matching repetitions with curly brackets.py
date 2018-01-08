import re
ro=re.compile(r'(\d){3}(\.|\-|\s)(\d){3}(\.|\-|\s)(\d){4}')
mo=ro.search('My Phone number is 111 222 4444')
print(mo.group())
