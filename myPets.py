myPets = ["catty", "mat", "patty"]
print("enter a cat name to search")
name = input()
if name not in myPets:
    print("No I dont own cat named : " + name)
else:
    print("I have cat with same name : " + name)
