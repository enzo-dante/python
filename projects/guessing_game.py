# handle user guess
#       if they guessed correctly, notify they won
#       otherwise, notify them they are too high or too low
#
# allow for multiple playthroughs

import random;

# random.randint(a, b) is inclusive unlike ranges()
random_number = random.randint(1, 10) # numbers 1 through and including 10
user_res = None
play_again_res = None

while user_res != random_number:

    user_res = input("Guess a number between 1 and 10\n")
    converted_user_res = int(user_res)

    print(f"Your guess was {converted_user_res}")
    if type(converted_user_res) != int or converted_user_res not in range(1, 10):
        print("Not a valid guess")
    if int(converted_user_res) == random_number:
        print("YOU WON!\n")
        play_again_res = input("Would you like to play again, Y or N?\n")

        if play_again_res.lower() == "y":
            user_res = None
        elif play_again_res.lower() == "n" or play_again_res.lower() != "y":
            break

    elif converted_user_res >= random_number:
        print("TOO HIGH!")
    else:
        print("TOO LOW!")

    

