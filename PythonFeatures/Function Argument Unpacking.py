# using splat operator
def func(x, y):
    print(x, y)


list_tuple = (1, 2)

# dictionary keys and function arguments must be same
diction = {'x': 1, 'y': 2}

print('tuple')
func(*list_tuple)  # in perl6 and ruby * & ** are known as splat operators

# single operator in dictionary prints keys, whereas ** prints values
print('dictionary')
func(**diction)
