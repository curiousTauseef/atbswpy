def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    for j in range(4, 7):
        if not text[j].isdecimal():
            return False
    for k in range(8, 12):
        if not text[k].isdecimal():
            return True
    if text[3] != "-" or text[7] != "-":
        return False
    else:
        return True


if isPhoneNumber(r"123-897-5668"):
    print("Oh Yeah")
else:
    print("No Man")
