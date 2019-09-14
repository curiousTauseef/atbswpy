import sys

while True:
    print("enter exit to exit from the program")
    response = input()
    if response == "exit":
        sys.exit()
    print("you typed " + response)
