def func(x,y):
	print(x,y)

list_tuple=(1,2)

diction={'x':1,'y':2}	#dictionary keys and function arguments must be same

print('tuple')
func(*list_tuple)	#in perl6 and ruby * & ** are known as splat operators

print('dictionary')	#single operator in dictionary prints keys, whereas ** prints values
func(**diction)

