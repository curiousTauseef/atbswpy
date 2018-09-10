def spam(divideBy):
    try:
        return 22/divideBy
    except ZeroDivisionError:
        print('Error! Invalid Division')


print(spam(22))
print(spam(1))
print(spam(13))
print(spam(0))
print(spam(4))
print(spam(14))
