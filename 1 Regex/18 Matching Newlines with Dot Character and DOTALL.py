# using re.DOTALL to match newlines

import re

ro = re.compile(r".*", re.DOTALL)
mo = ro.search("I am Mayank.\nI love Programming.\nI love Photoshop")
print(mo.group())

# without re.DOTALL the pattern will be matched only upto the first newline character
