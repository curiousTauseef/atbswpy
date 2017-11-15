import pyperclip

text=pyperclip.paste()

list=text.split('\n')

#print(list)

for i in range(len(list)):

	list[i]='## '+list[i]

text='\n'.join(list)

pyperclip.copy(text)

