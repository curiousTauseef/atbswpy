import pyperclip

text=pyperclip.paste()

list=text.split('\n')

#print(list)

for i in range(len(list)):

	list[i]=str(i+1)+'. '+list[i]

text='\n'.join(list)

pyperclip.copy(text)

