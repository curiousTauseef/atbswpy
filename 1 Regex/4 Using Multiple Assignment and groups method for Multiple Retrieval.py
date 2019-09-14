import re

regexobj = re.compile(r"(\d\d\d\d)-(\d\d\d\d\d\d\d)")
# be default pattern inside the Parenthesis is macthed
mo = regexobj.search("hey my phone number with the state code is 0751-4028060")
print("my number is " + mo.group(2) + " my state code is " + mo.group(1))

# Mutliple Assignment Trick
# Mutliple Assignment is done using groups() method in this case
statecode, number = mo.groups()
print(statecode, number)

# Matching Parenthesis
print("Matching Parenthesis")
regexobj2 = re.compile(r"(\(\d\d\d\d\))-(\d\d\d\d\d\d\d)")
# to match Parenthesis seperately write symbol in raw pattern using \Symbol -- \(
mo2 = regexobj2.search("hey my phone number with the state code is (0751)-4028060")
print("my number is " + mo2.group(2) + " my state code is " + mo2.group(1))

# Mutliple Assignment Trick
statecode2, number2 = mo2.groups()
print(statecode2, number2)
