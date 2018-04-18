# * means matching 0 or more repetitions whereas + means matching one or more repetitions
import re
heroRegex=re.compile(r'Bat(wo)*?man')
mo=heroRegex.search('works is Batwowowowoman')
print(mo.group(0))  #output complete - Batwowowowoman
print(mo.group(1))  #output - wo ] of which it matches 0 or more of the repetitions
