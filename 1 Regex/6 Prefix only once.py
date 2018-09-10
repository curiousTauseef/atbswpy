import re
# the part of pattern which will be returned is only contained inside brackets
hero = re.compile(r'Bat(man|mobile|bat|copter)')
mo = hero.search(
    'My favorite hero owns a Batcopter, a Batmobile, he is Batman')
print(mo.group(0))  # Batcopter
print(mo.group(1))  # copter
print(no.group(2))  # Batcopter
# since only the first macthing string is returned when we use a pipe character
