import re
# the first group will have the first letter of the word after Agent
ro = re.compile(r'Agent (\w)\w*')
# we can access the first group using \1 then make a subtitution pattern
mo = ro.sub(
    r'\1*****', 'Agent Alice told Agent Carter that Agent Hill was Awesome')
# print the substituted string
print(mo)
