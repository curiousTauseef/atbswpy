theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}


def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])


print()
print('top-L'+'|'+'top-M'+'|'+'top-R')
print('  -  +  -  +  -')
print('mid-L'+'|'+'mid-M'+'|'+'mid-R')
print('  -  +  -  +  -')
print('low-L'+'|'+'low-M'+'|'+'low-R')
print()
turn = 'X'
for i in range(9):
    print('turn for '+turn+' move to which space : ')
    print()
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    printBoard(theBoard)
