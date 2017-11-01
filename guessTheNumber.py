import random
print('I am thinking of a number between 1-9')
flag=random.randint(1,9)
count=1
while True:
	print('Take a Guess')
	guess=int(input())
	if guess<flag:
		print('Your guess is too low')
	elif guess>flag:
		print('Your guess is too high')
	else:
		print('Congrats You win this Game in '+str(count)+' Guesses')
		break
	count+=1

