import os

board = {
    'A1': ' ', 'B1': ' ', 'C1': ' ',
    'A2': ' ', 'B2': ' ', 'C2': ' ',
    'A3': ' ', 'B3': ' ', 'C3': ' '
}

user = 1
last_verification = 0
all_moves = 0

        
def win_verification():
    if board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X':
        print('User one won !')
        return 1
    if board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X':
        print('User One Won!!')
        return 1
    if board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X':
        print('User One Won!!')
        return 1
    if board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X':
        print('User One Won!!')
        return 1
    if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X':
        print('User One Won!!')
        return 1
    if board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
        print('User One Won!!')
        return 1
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
        print('Player One Won!!')
        return 1
   

    
    if board['A1'] == 'O' and board['B1'] == 'O' and board['C1'] == 'O':
        print('User Two Won!!')
        return 1  
    if board['A2'] == 'O' and board['B2'] == 'O' and board['C2'] == 'O':
        print('User Two Won!!')
        return 1
    if board['A3'] == 'O' and board['B3'] == 'O' and board['C3'] == 'O':
        print('User Two Won!!')
        return 1
    if board['A1'] == 'O' and board['B2'] == 'O' and board['C3'] == 'O':
        print('User Two Won!!')
        return 1
    if board['A1'] == 'O' and board['A2'] == 'O' and board['A3'] == 'O':
        print('User Two Won!!')
        return 1
    if board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O':
        print('User Two Won!!')
        return 1
    if board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O':
        print('User Two Won!!')
        return 1
    return 0 



print(' ')
print('Welcome to the PROTicTacToe Game !')
print(' ')
print('A1|B1|C1')
print('- +- +-')
print('A2|B2|C2')
print('- +- +-')
print('A3|B3|C3')
print('***************************')

while True:
    print(board['A1']+'|'+board['B1']+'|'+board['C1'])
    print('-+-+-')
    print(board['A2'] + '|' + board['B2'] + '|' + board['C2'])
    print('-+-+-')
    print(board['A3'] + '|' + board['B3'] + '|' + board['C3'])
    last_verification = win_verification()
    if all_moves == 9 or last_verification == 1:
        break
    while True:     
        if user == 1:  
            u1_input = input('User one(X): ')
            if u1_input.upper() in board and board[u1_input.upper()] == ' ':
                board[u1_input.upper()] = 'X'
                user = 2
                break
            
            else:
                print('Invalid input, please try again')
                continue
        else:
            u2_input = input('User two(O): ')
            if u2_input.upper() in board and board[u2_input.upper()] == ' ':
                board[u2_input.upper()] = 'O'
                user = 1
                break
            else:  
                print('Invalid input, please try again')
                continue
    all_moves += 1
    print('***************************')
    print()

menu()
    