import re  # importing regex module
# compiling regex pattern to return regex object  ( \d for integral values )
pattern = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')
# making match object mo
mo = pattern.search('My phone number is 0751-4028060')
print(mo.group())  # returns a list of several groups of matched patterns
