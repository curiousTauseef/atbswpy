from sys import argv
script,filename=argv
print('we are going to erase everything from the file')
print('file opening...')
file_open=open(filename,'w')
file_open.truncate()
print('previous content removed..')
paragraph1=input('enter any para to write in the file\n>>> ')
paragraph2=input('enter any other paragraph to write in the file\n>>> ')
file_open.write(paragraph1)
file_open.write("\n")
file_open.write(paragraph2)
print('you have given input to the file, bye')
file_open.close()




