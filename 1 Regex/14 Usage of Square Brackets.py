import re
print('Printing Vowels')
vowelReg = re.compile(r'[aeiouAEIOU]')
mo1 = vowelReg.findall('my name is mayank singh and i love programming ')
print(mo1)


print('Printing Consonents')
consoReg = re.compile(r'[^aeiouAEIOU]')
mo2 = consoReg.findall('my name is mayank singh and i love programming ')
print(mo2)

# Caret Symbol ^ is used in making patterns to match the beginning of something
# $ dollar symbol is used to match the end of something
