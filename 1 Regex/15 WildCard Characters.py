# . dot character in regular expressions is known as wildcard character
# it maches character except newline
import re
atRegex=re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)
