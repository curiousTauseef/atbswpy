def func(array):
    for num in array:
        if num % 2 == 0:
            print(num)
            break
    else:
        print('no call for break')


print('1st Case')
a = [5]
func(a)
