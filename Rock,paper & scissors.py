import random

def play():
    user = input("What's your choice? 'r' for rock, 's' for scissors, 'p' for paper:  \n")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer :
        return 'tie'

    if winner(user, computer):
        return 'You Won!'

    return 'You Lost!'

def winner(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 


print(play())