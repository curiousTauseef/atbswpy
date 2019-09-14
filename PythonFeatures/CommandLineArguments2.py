from sys import argv

script, username = argv
prompt = ">> "

print("Hey" + username + " I am " + script + " script")
print("enter your original name")
org_name = input(prompt)

print("Hey " + username + " so your original name is " + org_name)

print("Argument 1: %s,\nArgument 2: %s\n" % (script, username))
