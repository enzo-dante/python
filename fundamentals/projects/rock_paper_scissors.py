# to generate random integer
# import random

# since only using randint(a, b)
from random import randint

p1_wins = 'player 1 wins!'
p2_wins = 'player 2 wins!'
computer_wins = 'computer wins!'

draw = 'the game ends in a draw'
bad_input = 'something went wrong...'

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

# Player vs Computer

rand_num = randint(0, 2)

if rand_num == 0:
    computer = rock
elif rand_num == 1:
    computer = paper
else:
    computer = scissors

p1 = input("Player 1: rock, paper, or scissors:\n").lower()

if p1 != rock and p1 != paper and p1 != scissors:
    print(bad_input)
elif computer != rock and computer != paper and computer != scissors:
    print(bad_input)
else:
    print(f'computer chose: {computer}\n')
    if p1 == computer:
        print(draw)
    
    elif p1 == rock and computer == scissors:
        print(p1_wins)
    
    elif p1 == paper and computer == rock:
        print(p1_wins)
    
    elif p1 == scissors and computer == paper:
        print(p1_wins)
    
    else:
        print(computer_wins)

# PvP

# p1 = input("Player 1: rock, paper, or scissors:\n").lower()
# p2 = input("Player 2: rock, paper, or scissors:\n").lower()

# if p1 != rock and p1 != paper and p1 != scissors:
#     print(bad_input)
# elif p2 != rock and p2 != paper and p2 != scissors:
#     print(bad_input)
# else:
#     if p1 == p2:
#         print(draw)
#     
#     elif p1 == rock and p2 == scissors:
#         print(p1_wins)
#     
#     elif p1 == paper and p2 == rock:
#         print(p1_wins)
#     
#     elif p1 == scissors and p2 == paper:
#         print(p1_wins)
#     
#     else:
#         print(p2_wins)
