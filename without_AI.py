import time
import random

run = True
win = False
draw = False


def wincheck():
    global run
    global win
    global draw
    global tictactoebox

    if ''.join(tictactoebox[0]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join(tictactoebox[1]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join(tictactoebox[2]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join([tictactoebox[0][0], tictactoebox[1][0], tictactoebox[2][0]]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join([tictactoebox[0][1], tictactoebox[1][1], tictactoebox[2][1]]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join([tictactoebox[0][2], tictactoebox[1][2], tictactoebox[2][2]]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join([tictactoebox[0][0], tictactoebox[1][1], tictactoebox[2][2]]) == 'OOO':
        print('Player1 wins')
        win = True
    if ''.join([tictactoebox[0][2], tictactoebox[1][1], tictactoebox[2][0]]) == 'OOO':
        print('Player1 wins')
        win = True

    if ''.join(tictactoebox[0]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join(tictactoebox[1]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join(tictactoebox[2]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join([tictactoebox[0][0], tictactoebox[1][0], tictactoebox[2][0]]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join([tictactoebox[0][1], tictactoebox[1][1], tictactoebox[2][1]]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join([tictactoebox[0][2], tictactoebox[1][2], tictactoebox[2][2]]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join([tictactoebox[0][0], tictactoebox[1][1], tictactoebox[2][2]]) == 'XXX':
        print('Player2 wins')
        win = True
    if ''.join([tictactoebox[0][2], tictactoebox[1][1], tictactoebox[2][0]]) == 'XXX':
        print('Player2 wins')
        win = True

    if not win and tictactoebox[0][0] != '' and tictactoebox[0][1] != '' and tictactoebox[0][2] != '' and \
            tictactoebox[1][0] != '' and tictactoebox[1][1] != '' and tictactoebox[1][2] != '' and tictactoebox[2][
        0] != '' and tictactoebox[2][1] != '' and tictactoebox[2][2] != '':
        print('It is a tie')
        draw = True


again1 = False
again2 = False


def invalidmove(player):
    global again1
    global again2
    if player == 1:
        again1 = True
    if player == 2:
        again2 = True


def Move(player, move):
    global tictactoebox
    global moves_li
    wincheck()
    if player == 1:
        if move in moves_li:
            if move == '0,0':
                if tictactoebox[0][0] == '':
                    tictactoebox[0][0] = tictactoebox[0][0].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '0,1':
                if tictactoebox[0][1] == '':
                    tictactoebox[0][1] = tictactoebox[0][1].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '0,2':
                if tictactoebox[0][2] == '':
                    tictactoebox[0][2] = tictactoebox[0][2].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '1,0':
                if tictactoebox[1][0] == '':
                    tictactoebox[1][0] = tictactoebox[1][0].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '1,1':
                if tictactoebox[1][1] == '':
                    tictactoebox[1][1] = tictactoebox[1][1].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '1,2':
                if tictactoebox[1][2] == '':
                    tictactoebox[1][2] = tictactoebox[1][2].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '2,0':
                if tictactoebox[2][0] == '':
                    tictactoebox[2][0] = tictactoebox[2][0].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '2,1':
                if tictactoebox[2][1] == '':
                    tictactoebox[2][1] = tictactoebox[2][1].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
            if move == '2,2':
                if tictactoebox[2][2] == '':
                    tictactoebox[2][2] = tictactoebox[2][2].replace('', 'O')
                else:
                    print('The move is invalid')
                    invalidmove(1)
        else:
            print('The move is invalid')
            invalidmove(1)
    if player == 2:
        if move in moves_li:
            if move == '0,0':
                if tictactoebox[0][0] == '':
                    tictactoebox[0][0] = tictactoebox[0][0].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '0,1':
                if tictactoebox[0][1] == '':
                    tictactoebox[0][1] = tictactoebox[0][1].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '0,2':
                if tictactoebox[0][2] == '':
                    tictactoebox[0][2] = tictactoebox[0][2].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '1,0':
                if tictactoebox[1][0] == '':
                    tictactoebox[1][0] = tictactoebox[1][0].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '1,1':
                if tictactoebox[1][1] == '':
                    tictactoebox[1][1] = tictactoebox[1][1].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '1,2':
                if tictactoebox[1][2] == '':
                    tictactoebox[1][2] = tictactoebox[1][2].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '2,0':
                if tictactoebox[2][0] == '':
                    tictactoebox[2][0] = tictactoebox[2][0].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '2,1':
                if tictactoebox[2][1] == '':
                    tictactoebox[2][1] = tictactoebox[2][1].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
            if move == '2,2':
                if tictactoebox[2][2] == '':
                    tictactoebox[2][2] = tictactoebox[2][2].replace('', 'X')
                else:
                    print('The move is invalid')
                    invalidmove(2)
        else:
            print('The move is invalid')
            invalidmove(2)


def tictactoe_display(tictactoebox):
    for i in range(len(tictactoebox)):
        print(tictactoebox[i])


tictactoebox = [['', '', ''],
                ['', '', ''],
                ['', '', '']]

tictactoe_displaybox = [['0,0', '0,1', '0,2'],
                        ['1,0', '1,1', '1,2'],
                        ['2,0', '2,1', '2,2']]

moves_li = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']

tictactoe_display(tictactoe_displaybox)

print('Player1 = O')
print('Player2 = X')

tries = 1

while run:
    wincheck()
    if win:
        tictactoe_display(tictactoebox)
        break
    if draw:
        tictactoe_display(tictactoebox)
        break
    if not again1:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            move1 = input('player1: ')
            Move(1, move1)
    if again1:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            move1 = input('player1: ')
            Move(1, move1)
            again1 = False

    tries += 1

    wincheck()
    if win:
        tictactoe_display(tictactoebox)
        break
    if draw:
        tictactoe_display(tictactoebox)
        break
    if not again2:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            move2 = input('player2: ')
            Move(2, move2)
    if again2:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            move2 = input('player2: ')
            Move(2, move2)
            again2 = False

    tries += 1
