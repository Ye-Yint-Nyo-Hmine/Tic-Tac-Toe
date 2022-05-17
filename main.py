import time
import random

run = True
win = False
draw = False

def AI():
    global tictactoebox
    global first
    global tries
    global again1
    global again2

    r0c0 = False
    r0c1 = False
    r0c2 = False

    r1c0 = False
    r1c1 = False
    r1c2 = False

    r2c0 = False
    r2c1 = False
    r2c2 = False

    if tictactoebox[0][0] != 'X' and tictactoebox[0][0] != 'O':
        r0c0 = True
    if tictactoebox[0][1] != 'X' and tictactoebox[0][1] != 'O':
        r0c1 = True
    if tictactoebox[0][2] != 'X' and tictactoebox[0][2] != 'O':
        r0c2 = True

    if tictactoebox[1][0] != 'X' and tictactoebox[1][0] != 'O':
        r1c0 = True
    if tictactoebox[1][1] != 'X' and tictactoebox[1][1] != 'O':
        r1c1 = True
    if tictactoebox[1][2] != 'X' and tictactoebox[1][2] != 'O':
        r1c2 = True

    if tictactoebox[2][0] != 'X' and tictactoebox[2][0] != 'O':
        r2c0 = True
    if tictactoebox[2][1] != 'X' and tictactoebox[2][1] != 'O':
        r2c1 = True
    if tictactoebox[2][2] != 'X' and tictactoebox[2][2] != 'O':
        r2c2 = True

    if again1:
        if r0c0:
            move = '0,0'
        else:
            if r0c1:
                move = '0,1'
            else:
                if r0c2:
                    move = '0,2'
                else:
                    if r1c0:
                        move = '1,0'
                    else:
                        if r1c1:
                            move = '1,1'
                        else:
                            if r1c2:
                                move = '1,2'
                            else:
                                if r2c0:
                                    move = '2,0'
                                else:
                                    if r2c1:
                                        move = '2,1'
                                    else:
                                        if r2c2:
                                            move = '2,2'

    if again2:
        if r0c0:
            move = '0,0'
        else:
            if r0c1:
                move = '0,1'
            else:
                if r0c2:
                    move = '0,2'
                else:
                    if r1c0:
                        move = '1,0'
                    else:
                        if r1c1:
                            move = '1,1'
                        else:
                            if r1c2:
                                move = '1,2'
                            else:
                                if r2c0:
                                    move = '2,0'
                                else:
                                    if r2c1:
                                        move = '2,1'
                                    else:
                                        if r2c2:
                                            move = '2,2'

    if first == 2:
        if tries == 1:
            move = '2,0'
        if tries == 3:
            if r0c0:
                move = '0,0'
            else:
                if r0c1:
                    move = '0,1'
                else:
                    if r0c2:
                        move = '0,2'
                    else:
                        if r1c0:
                            move = '1,0'
                        else:
                            if r1c1:
                                move = '1,1'
                            else:
                                if r1c2:
                                    move = '1,2'
                                else:
                                    if r2c0:
                                        move = '2,0'
                                    else:
                                        if r2c1:
                                            move = '2,1'
                                        else:
                                            if r2c2:
                                                move = '2,2'

    if first == 1:
        if tries == 2:
            if r0c0:
                move = '0,0'
            else:
                if r0c1:
                    move = '0,1'
                else:
                    if r0c2:
                        move = '0,2'
                    else:
                        if r1c0:
                            move = '1,0'
                        else:
                            if r1c1:
                                move = '1,1'
                            else:
                                if r1c2:
                                    move = '1,2'
                                else:
                                    if r2c0:
                                        move = '2,0'
                                    else:
                                        if r2c1:
                                            move = '2,1'
                                        else:
                                            if r2c2:
                                                move = '2,2'

        if tries == 4:

            if tictactoebox[0][0] == 'X' and tictactoebox[0][1] == 'X':
                move = '0,2'
            if tictactoebox[0][1] == 'X' and tictactoebox[0][2] == 'X':
                move = '0,0'
            if tictactoebox[0][0] == 'X' and tictactoebox[0][2] == 'X':
                move = '0,1'

            if tictactoebox[1][0] == 'X' and tictactoebox[1][1] == 'X':
                move = '1,2'
            if tictactoebox[1][1] == 'X' and tictactoebox[1][2] == 'X':
                move = '1,0'
            if tictactoebox[1][0] == 'X' and tictactoebox[1][2] == 'X':
                move = '1,1'

            if tictactoebox[2][0] == 'X' and tictactoebox[2][1] == 'X':
                move = '2,2'
            if tictactoebox[2][1] == 'X' and tictactoebox[2][2] == 'X':
                move = '2,0'
            if tictactoebox[2][0] == 'X' and tictactoebox[2][2] == 'X':
                move = '2,1'

            if tictactoebox[0][0] == 'X' and tictactoebox[1][0] == 'X':
                move = '2,0'
            if tictactoebox[1][0] == 'X' and tictactoebox[2][0] == 'X':
                move = '0,0'
            if tictactoebox[0][0] == 'X' and tictactoebox[2][0] == 'X':
                move = '1,0'

            if tictactoebox[0][1] == 'X' and tictactoebox[1][1] == 'X':
                move = '2,1'
            if tictactoebox[1][1] == 'X' and tictactoebox[2][1] == 'X':
                move = '0,1'
            if tictactoebox[0][1] == 'X' and tictactoebox[2][1] == 'X':
                move = '1,1'

            if tictactoebox[0][2] == 'X' and tictactoebox[1][2] == 'X':
                move = '2,2'
            if tictactoebox[1][2] == 'X' and tictactoebox[2][2] == 'X':
                move = '0,2'
            if tictactoebox[0][2] == 'X' and tictactoebox[2][2] == 'X':
                move = '1,2'

            if tictactoebox[0][0] == 'X' and tictactoebox[1][1] == 'X':
                move = '2,2'
            if tictactoebox[1][1] == 'X' and tictactoebox[2][2] == 'X':
                move = '0,0'
            if tictactoebox[0][0] == 'X' and tictactoebox[2][2] == 'X':
                move = '1,1'

            if tictactoebox[0][2] == 'X' and tictactoebox[1][1] == 'X':
                move = '2,0'
            if tictactoebox[1][1] == 'X' and tictactoebox[2][0] == 'X':
                move = '0,2'
            if tictactoebox[0][2] == 'X' and tictactoebox[2][0] == 'X':
                move = '1,1'

            if r0c0:
                move = '0,0'
            else:
                if r0c1:
                    move = '0,1'
                else:
                    if r0c2:
                        move = '0,2'
                    else:
                        if r1c0:
                            move = '1,0'
                        else:
                            if r1c1:
                                move = '1,1'
                            else:
                                if r1c2:
                                    move = '1,2'
                                else:
                                    if r2c0:
                                        move = '2,0'
                                    else:
                                        if r2c1:
                                            move = '2,1'
                                        else:
                                            if r2c2:
                                                move = '2,2'

    # move any algorithm

    if tictactoebox[0][0] == 'O' and tictactoebox[0][1] == 'O':
        move = '0,2'
    if tictactoebox[0][1] == 'O' and tictactoebox[0][2] == 'O':
        move = '0,0'
    if tictactoebox[0][0] == 'O' and tictactoebox[0][2] == 'O':
        move = '0,1'

    if tictactoebox[1][0] == 'O' and tictactoebox[1][1] == 'O':
        move = '1,2'
    if tictactoebox[1][1] == 'O' and tictactoebox[1][2] == 'O':
        move = '1,0'
    if tictactoebox[1][0] == 'O' and tictactoebox[1][2] == 'O':
        move = '1,1'

    if tictactoebox[2][0] == 'O' and tictactoebox[2][1] == 'O':
        move = '2,2'
    if tictactoebox[2][1] == 'O' and tictactoebox[2][2] == 'O':
        move = '2,0'
    if tictactoebox[2][0] == 'O' and tictactoebox[2][2] == 'O':
        move = '2,1'

    if tictactoebox[0][0] == 'O' and tictactoebox[1][0] == 'O':
        move = '2,0'
    if tictactoebox[1][0] == 'O' and tictactoebox[2][0] == 'O':
        move = '0,0'
    if tictactoebox[0][0] == 'O' and tictactoebox[2][0] == 'O':
        move = '1,0'

    if tictactoebox[0][1] == 'O' and tictactoebox[1][1] == 'O':
        move = '2,1'
    if tictactoebox[1][1] == 'O' and tictactoebox[2][1] == 'O':
        move = '0,1'
    if tictactoebox[0][1] == 'O' and tictactoebox[2][1] == 'O':
        move = '1,1'

    if tictactoebox[0][2] == 'O' and tictactoebox[1][2] == 'O':
        move = '2,2'
    if tictactoebox[1][2] == 'O' and tictactoebox[2][2] == 'O':
        move = '0,2'
    if tictactoebox[0][2] == 'O' and tictactoebox[2][2] == 'O':
        move = '1,2'

    if tictactoebox[0][0] == 'O' and tictactoebox[1][1] == 'O':
        move = '2,2'
    if tictactoebox[1][1] == 'O' and tictactoebox[2][2] == 'O':
        move = '0,0'
    if tictactoebox[0][0] == 'O' and tictactoebox[2][2] == 'O':
        move = '1,1'

    if tictactoebox[0][2] == 'O' and tictactoebox[1][1] == 'O':
        move = '2,0'
    if tictactoebox[1][1] == 'O' and tictactoebox[2][0] == 'O':
        move = '0,2'
    if tictactoebox[0][2] == 'O' and tictactoebox[2][0] == 'O':
        move = '1,1'

    # defend move

    if tictactoebox[0][0] == 'X' and tictactoebox[0][1] == 'X':
        move = '0,2'
    if tictactoebox[0][1] == 'X' and tictactoebox[0][2] == 'X':
        move = '0,0'
    if tictactoebox[0][0] == 'X' and tictactoebox[0][2] == 'X':
        move = '0,1'

    if tictactoebox[1][0] == 'X' and tictactoebox[1][1] == 'X':
        move = '1,2'
    if tictactoebox[1][1] == 'X' and tictactoebox[1][2] == 'X':
        move = '1,0'
    if tictactoebox[1][0] == 'X' and tictactoebox[1][2] == 'X':
        move = '1,1'

    if tictactoebox[2][0] == 'X' and tictactoebox[2][1] == 'X':
        move = '2,2'
    if tictactoebox[2][1] == 'X' and tictactoebox[2][2] == 'X':
        move = '2,0'
    if tictactoebox[2][0] == 'X' and tictactoebox[2][2] == 'X':
        move = '2,1'

    if tictactoebox[0][0] == 'X' and tictactoebox[1][0] == 'X':
        move = '2,0'
    if tictactoebox[1][0] == 'X' and tictactoebox[2][0] == 'X':
        move = '0,0'
    if tictactoebox[0][0] == 'X' and tictactoebox[2][0] == 'X':
        move = '1,0'

    if tictactoebox[0][1] == 'X' and tictactoebox[1][1] == 'X':
        move = '2,1'
    if tictactoebox[1][1] == 'X' and tictactoebox[2][1] == 'X':
        move = '0,1'
    if tictactoebox[0][1] == 'X' and tictactoebox[2][1] == 'X':
        move = '1,1'

    if tictactoebox[0][2] == 'X' and tictactoebox[1][2] == 'X':
        move = '2,2'
    if tictactoebox[1][2] == 'X' and tictactoebox[2][2] == 'X':
        move = '0,2'
    if tictactoebox[0][2] == 'X' and tictactoebox[2][2] == 'X':
        move = '1,2'

    if tictactoebox[0][0] == 'X' and tictactoebox[1][1] == 'X':
        move = '2,2'
    if tictactoebox[1][1] == 'X' and tictactoebox[2][2] == 'X':
        move = '0,0'
    if tictactoebox[0][0] == 'X' and tictactoebox[2][2] == 'X':
        move = '1,1'

    if tictactoebox[0][2] == 'X' and tictactoebox[1][1] == 'X':
        move = '2,0'
    if tictactoebox[1][1] == 'X' and tictactoebox[2][0] == 'X':
        move = '0,2'
    if tictactoebox[0][2] == 'X' and tictactoebox[2][0] == 'X':
        move = '1,1'


    return move

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

ai_or_not = input('Do you want to play with ai? y/n: ')
if ai_or_not == 'y':
    ai_ = True
else:
    ai_ = False

first = random.choice([1, 2])

if ai_:
    if first == 1:
        print('You are player1')
    else:
        print('You are player2')

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
            if ai_:
                if first == 1:
                    move1 = input('player1: ')
                    Move(1, move1)
                if first == 2:
                    print('AI move is done')
                    Move(1, AI())
            else:
                move1 = input('player1: ')
                Move(1, move1)
    if again1:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            if ai_:
                if first == 1:
                    move1 = input('player1: ')
                    Move(1, move1)
                if first == 2:
                    print('AI move is done')
                    Move(1, AI())
            else:
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
            if ai_:
                if first == 1:
                    print('AI move is done')
                    Move(2, AI())
                if first == 2:
                    move2 = input('player2: ')
                    Move(2, move2)
            else:
                move2 = input('player2: ')
                Move(2, move2)
    if again2:
        if not win and not draw:
            tictactoe_display(tictactoebox)
            if ai_:
                if first == 1:
                    print('AI move is done')
                    Move(2, AI())
                if first == 2:
                    move2 = input('player2: ')
                    Move(2, move2)
            else:
                move2 = input('player2: ')
                Move(2, move2)
            again2 = False

    tries += 1
print("Bye!")
