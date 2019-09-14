while True:
    print("Who are you")
    name = input()
    if name != "Mayank":
        continue
    print("Hello " + name + " What is your password")
    password = input()
    if password == "swordfish":
        print("Welcome")
        break
print("Access Granted!")
