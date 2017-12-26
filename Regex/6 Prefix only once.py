import re

hero=re.compile(r'Bat(man|mobile|bat|copter)') #the part of pattern which will be returned is only contained inside brackets

mo=hero.search('My favorite hero owns a Batcopter, a Batmobile, he is Batman')

print(mo)

