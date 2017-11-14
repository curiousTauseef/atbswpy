line=input('enter a line, to find frequency of characters : ')

count={}

for character in line:
	count.setdefault(character,0)
	count[character]+=1
print(count.items())

