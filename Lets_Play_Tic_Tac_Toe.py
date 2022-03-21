from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+  '|'+ board[8]+'|'+ board[9]      )
    print(board[4]+  '|'+ board[5]+'|'+ board[6]       )
    print( board[1]+ '|'+ board[2]+'|'+board[3] )
 
 
board=['#','X','O','O','X','O','X','O','X','X']
display_board(board)
display_board(board)
display_board(board)

def choose_marker():
    #output=Player1,Player2
    marker=''
    while marker not in ['X','O']:
        marker=input('Player1:Choose X or O: ').upper()
        
        if marker=='X':
            return('X','O')
        else:
            return('O','X')
            
def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):
    #check rows
    #check colums
    #check diagonals
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark))
    
    
import random

def choose_player():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
        
def space_check(board,position):
    return board[position]==' '
    
    
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    
def players_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Please put a valid number:(1-9)' ))
    return position    
    
def replay():
    choice=input('Do you want to play?:Yes or No ')
    return choice=='Yes'
    
#Bringing together all the functions
print('Welcome to Tic Tac Toe')
while True:
#USE WHILE LOOP
#SET UP GAME
    the_board=[' ']*10
    player1,player2=choose_marker()
    turn=choose_player()
    print(turn + ' will go first')
    play_game=input('Ready to Play? y or n ')
    if play_game.lower()[0]=='y':
         game_on=True
    else:
         game_on=False
    while game_on:
        if turn=='Player 1':
    #PLAYER 1
            display_board(the_board)
            position=players_choice(the_board)
            place_marker(the_board,player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print('Player 1 wins!')
                game_on=False
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on=False
                else:
                    turn='Player 2'
        else:
    #PLAYER 1
            display_board(the_board)
            position=players_choice(the_board)
            place_marker(the_board,player2,position)
            if win_check(the_board,player2):
                print('Player 2 wins!')
                game_on=False
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on=False
                else:
                    turn='Player 1'
    if not replay():
        break
                
                
                
                
            
            
        
        
        
            
        
    
    
    
    #PLAYER 2





#USE REPLAY FUNCTION
