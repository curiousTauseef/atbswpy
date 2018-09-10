from random import *
from sys import *


def getFortune(num):
    if num == 1:
        print('hey 1')
    elif num == 2:
        print('hey 2')
    elif num == 3:
        print('hey 3')
    elif num == 4:
        print('hey 4')
    elif num == 5:
        print('hey 5')
    elif num == 6:
        print('hey 6')
    elif num == 7:
        print('hey 7')
    elif num == 8:
        print('hey 8')
    elif num == 9:
        print('hey 9')
    else:
        print('bye! bye!')
        exit()


getFortune(randint(0, 9))
