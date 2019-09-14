import re

ro = re.compile(r"B11\n[0-9][.][0-9]{6}", re.DOTALL | re.VERBOSE)
mo = ro.findall(r""" """)
print(mo)
