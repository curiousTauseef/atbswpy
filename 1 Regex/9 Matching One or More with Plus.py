import re
ro=re.compile(r'Bat(wo)+man')
mo=ro.search('Hey there, the Batwowowowowoman is awesome')
print(mo.group())   #Batwowowowowoman
print(mo.group(1))   #wo


mo2=ro.search('Hey there, the Batwoman is awesome')
print(mo2.group())  #Batwoman
print(mo2.group(1)) #wo

mo3=ro.search('Hey there, the Batman is awesome')
#print(mo3.group())  #gives an error
