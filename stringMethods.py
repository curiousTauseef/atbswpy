spam = "Hello World!"
print(spam)
# upper
print('spam.upper() : '+spam.upper())
# lower
print('spam.lower() : '+spam.lower())
# isupper
print("'H'.isupper() : "+str('H'.isupper()))
print("'h' isupper() : "+str('h'.isupper()))
# islower
print('spam.lower().islower() : ' + str(spam.lower().islower()))
# isalpha
print("'123'.isalpha() : "+str('123'.isalpha()))
# isdecimal
print("'123'.isdecimal() : "+str('123'.isdecimal()))
# isalnum --> Alpha Numeric
print("'alpha123'.isalnum() : "+str('alpha123'.isalnum()))
# ispace
print("' '.isspace() : "+str(' '.isspace()))
# startswith
print("spam.startswith('Hello') : "+str(spam.startswith('Hello')))
# endswith
print("spam.endswith('!') : "+str(spam.endswith('!')))
# split --> splits the string in a list according to words
print("Hello World! : "+str(spam.split()))
print("HelloMaxWorld! : "+str("HelloMaxWorld!".split("Max")))
# for making a character array use list(string)
# join --> joins the list into string
print(str(spam.split())+' : '+str(' '.join(spam.split())))
# strip() lstrip() rstrip()
spam = "       Hey Man       "
print(spam.strip())
print(spam.rstrip())
print(spam.rstrip())
spam1 = "spamspamHAHAHAspamspam"
print(spam1.strip('spam'))
