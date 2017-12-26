import re
regexobj=re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d)')
mo=regexobj.search('hey my phone number with the state code is 0751-4028060')
print('my number is '+mo.group(2)+' my state code is '+mo.group(1))

