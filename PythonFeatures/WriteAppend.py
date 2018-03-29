from sys import argv

script,filename=argv

print('file opening...')
file_open=open(filename,'a+')

print('reading file in append mode')
#important line to remember
file_open.seek(0)
print(file_open.read())

paragraph1=input('enter any para to write in the file\n>>> ')
paragraph2=input('enter any other paragraph to write in the file\n>>> ')
file_open.write(paragraph1)
file_open.write(" ")
file_open.write(paragraph2)

print("you have given input to the file, let's read it")
file_open.seek(0)
print(file_open.read())

file_open.close()




