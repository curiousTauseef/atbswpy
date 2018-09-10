while True:
    age = input("enter your age : ")
    if age.isdecimal():
        break
    else:
        print("Please Enter Numeric Age ")
while True:
    password = input("enter your password : [LETTERS AND NUMBERS ONLY] : ")
    if password.isalnum():
        if(password == 'googly123'):
            print('Welcome to the Party !')
        else:
            print('Wrong Password !!')
        break
    print('Passwords can only have letters and numbers')
