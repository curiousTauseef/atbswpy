import re

# pipe character matches singe item
heroRegex = re.compile(r"Mayank|Munks Singh")
# out of multiple alternations

# if both patterns are matched only the first occuring string will be returned
mo1 = heroRegex.search("Mayank and Munks Singh.")
print(mo1.group())

mo2 = heroRegex.search("Munks Singh and Mayank")
print(mo2.group())
