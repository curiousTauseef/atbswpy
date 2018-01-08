import re
regexobj=re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d)')
mo=regexobj.search('hey my phone number with the state code is 0751-4028060')
print('my number is '+mo.group(2)+' my state code is '+mo.group(1))

#Mutliple Assignment Trick
#Mutliple Assignment is done using groups() method 
statecode,number=mo.groups()
print(statecode,number)

#Matching Parenthesis
print('Matching Parenthesis')
regexobj2=re.compile(r'(\(\d\d\d\d\))-(\d\d\d\d\d\d\d)')

mo2=regexobj2.search('hey my phone number with the state code is (0751)-4028060')
print('my number is '+mo2.group(2)+' my state code is '+mo2.group(1))

#Mutliple Assignment Trick
statecode2,number2=mo2.groups()
print(statecode2,number2)

