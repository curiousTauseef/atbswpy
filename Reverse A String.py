stri = input("enter a string")
length = len(stri)
stri2 = ""
i = -1
while i >= -length:
    stri2 = stri2 + stri[i]
    i -= 1
print(stri2)
