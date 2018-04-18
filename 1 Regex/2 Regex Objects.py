import re                                               #importing regex module
pattern=re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')          #compiling regex pattern to return regex object  ( \d for integral values )
mo=pattern.search('My phone number is 0751-4028060')    #making match object mo
print(mo.group())                                       #returns a list of several groups of matched patterns
