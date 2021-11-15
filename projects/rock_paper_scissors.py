# to generate random integer
# import random

# since only using randint(a, b)
from random import randint

player_score = 0
computer_score = 0
winning_score = 3

# OPTION 2: loop with win tracking
while player_score < winning_score and computer_score < winning_score:
    print(
        f"\nPlayer Score: {player_score}\nComputer Score: {computer_score}\n")

# OPTION 1: loop with no win tracking
# for each round in a range of 3 epochs
# for round in range(3):

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

    if p1 == "quit" or p1 == "q":
        break

    if p1 != rock and p1 != paper and p1 != scissors:
        print(bad_input)
    elif computer != rock and computer != paper and computer != scissors:
        print(bad_input)
    else:
        print(f'computer chose: {computer}\n')
        if p1 == computer:
            print(draw)

        elif p1 == rock and computer == scissors:
            player_score += 1
            print(p1_wins)

        elif p1 == paper and computer == rock:
            player_score += 1
            print(p1_wins)

        elif p1 == scissors and computer == paper:
            player_score += 1
            print(p1_wins)

        else:
            computer_score += 1
            print(computer_wins)

print(f"\nPlayer Score: {player_score}\nComputer Score: {computer_score}\n")

if player_score > computer_score:
    print("Congratulations Player!")
elif player_score == computer_score:
    print("The game ends in a tie...")
else:
    print("The robot apocalypse has begun!")

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
