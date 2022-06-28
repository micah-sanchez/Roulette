import random
from time import sleep
import sys

#roulette numbers
red_numbers = [19, 21, 23, 25, 27, 30, 32, 34, 36, 1, 3, 5, 7, 9, 12, 14, 16, 18]
black_numbers = [20, 22, 24, 26, 28, 29, 31, 33, 35, 2, 4, 6, 8, 10, 11, 13, 15, 17]
green_numbers = [0]

#balance = 5000

#intro
print("Hello! You have recently recieved an inheritance from a distant uncle! You've been left $5,000 with the caveat that you spend it all on roulette.")
name = input("What is your name?")

#game type function to determine if you want to bet on a number or color
def get_game_type():
    game_type = input("Good luck, {name}! Would you like to guess a number or color?".format(name=name))
    if game_type == "number":
        return 1
    if game_type == "color":
        return 2
    
#wager function - allows player to wager an amount from their balance
def get_wager():   
    wager_value = int(input("How much would you like to wager(do not include punctuation)?"))
    try:
        if wager_value > 5000:
            print("You don't have that much money to bet! Run the program again and choose $5000 or less.")
        else:
            return wager_value
    except NameError:
        print("")

#guess function - allows user to guess a number
def get_number_guess():
    guess_value = int(input("You can only bet on a number between 0 and 36 - which number would you like to place your wager on?"))
    if guess_value < 0 or guess_value > 36:
        print("You didn't select a number in the range - try again!")
    return guess_value

#ball_landed function - randomized number for where the ball landed
def get_ball_landed():
    ball_landed_value = random.randint(0,36)
    return ball_landed_value

def get_color_guess():
    guess_value = input("red or black or green?")
    if guess_value == "red":
        return 1
    elif guess_value == "black":
        return 2
    elif guess_value == "green:":
        return 3
    else:
        return "Error - did not match red or black"

balance = 5000 

#while loop to continue playing and add the balance
while True:    

    game_choice = get_game_type()

#number guess flow
    if game_choice == 1:
        wager_result = get_wager()
        guess_result = get_number_guess()
        bl_result = get_ball_landed()
        print("The board and ball are spinning...")
        sleep(2)

        if guess_result == bl_result:
            money_won = wager_result * 35
            balance += money_won
            print("Congratulations! You chose {guess_result} and that is the correct number! You win ${money_won} and now have ${balance}!".format(guess_result = guess_result, money_won = money_won, balance = balance))
        elif guess_result == bl_result and bl_result == 0:
            money_won = wager_result * 18
            balance += money_won
            print("Congratulations! You chose {guess_result} and that is the correct number! You win ${money_won} and now have ${balance}!".format(guess_result = guess_result, money_won = money_won, balance = balance))
        else:
            balance -= wager_result
            print("Shoot! You chose {guess_result} and the ball landed on {bl_result}! You lost ${wager_result} and now have ${balance}!".format(guess_result = guess_result, bl_result = bl_result, wager_result = wager_result, balance = balance))

#color guess flow 
    elif game_choice == 2:
        wager_result = get_wager()
        guess_result = get_red_black_guess()
        bl_result = get_ball_landed()
        print("The board and ball are spinning...")
        sleep(2)

        if guess_result in red_numbers:
            money_won = wager_result * 2
            balance += money_won
            print("Congratulations! The ball landed on {bl_result} red! You doubled your wager and now have ${balance}.".format(balance = balance, bl_result= bl_result))
        elif guess_result in black_numbers:
            money_won = wager_result * 2
            balance += money_won
            print("Congratulations! The ball landed on {bl_result} black! You doubled your wager and now have ${balance}.".format(balance = balance, bl_result= bl_result))
        elif guess_result in green_numbers:
            money_won = wager_result * 35
            balance += money_won
            print("Congratulations! The ball landed on {bl_result} green! You doubled your wager and now have ${balance}.".format(balance = balance, bl_result= bl_result))    
        else:
            balance -= wager_result
            print("You guessed wrong. You lost your ${wager_result} and have a new balance of ${balance}".format(wager_result=wager_result,balance = balance))
    
# to play again 
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
            print("Thanks for playing, {name}!".format(name = name))
            break

