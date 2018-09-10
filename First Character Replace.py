a = input("enter a string\n")  # input a string
stri = list(a)  # convert string to a list ( basically character array )
length = len(stri)  # find the length of stri( stri is a variable name )
charz = stri[0]  # find the first character of stri
for i in range(1, length):  # using the loop
    if stri[i] == charz:  # as it is clear by the condition
        stri[i] = '$'  # replacing here
# "".join() function is used to convert list back to string
stringfinal = "".join(stri)
print(stringfinal)  # clear !
