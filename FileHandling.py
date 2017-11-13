fo=open('a.txt','w+')
text=input("enter text to display :")
fo.write(text)
fo.close()

fo=open('a.txt','r+')
str=fo.read(50)
print('read string is: ',str)

fo.close()
