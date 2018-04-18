import re
ro=re.compile(r'(\d){3}(\.|\-|\s)(\d){3}(\.|\-|\s)(\d){4}')
#\s is space character
mo=ro.search('My Phone number is 423 222 4444')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(4))
print(mo.group(5))

#output
'''
423 222 4444
3           #the last value in the group (\d){3}

2

4
'''
