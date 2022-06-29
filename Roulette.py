import random
from time import sleep
import sys

#roulette numbers
red_numbers = [19, 21, 23, 25, 27, 30, 32, 34, 36, 1, 3, 5, 7, 9, 12, 14, 16, 18]
black_numbers = [20, 22, 24, 26, 28, 29, 31, 33, 35, 2, 4, 6, 8, 10, 11, 13, 15, 17]
green_numbers = [0]

#balance = 5000

#intro
balance = int(input("Welcome to Vegas!! Time to play some roulette - how much did you bring to bet?"))
name = input("What is your name?")

#game type function to determine if you want to bet on a number or color
def get_game_type():
    game_type = input("Good luck, {name}! Would you like to guess a 1) color or 2) numbers?".format(name=name))
    if game_type == "1":
        return 1
    if game_type == "2":
        return 2
    
#wager function - allows player to wager an amount from their balance
def get_wager():   
    wager_value = int(input("How much would you like to wager(do not include punctuation)?"))
    try:
        if wager_value > balance:
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

#get color guess - gets red/black/green guess from user
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

#multi numbers - gets the numbers the user wants
def get_multi_number_guess():
    print("Which numbers would you like to bet on? Pick as many numbers as you would like between 0 and 36. Hit ENTER between numbers and type q when you are done.")
    number_guesses = []
    while True:
        guess_values = input()
        if guess_values == "q":
            break
        number_guesses.append(int(guess_values))
    return number_guesses

#multi numbers - gets the wager for each number the user wants to bet on

def get_multi_number_bets(number_guesses):
    l = len(number_guesses)
    user_bets = []
    for index in number_guesses:
        print("How much would you like to bet on {index}?".format(index = index))
        bet_values = int(input())
        user_bets.append(bet_values)
    return user_bets
            
#ball_landed function - randomized number for where the ball lanßded
def get_ball_landed():
    ball_landed_value = random.randint(0,36)
    return ball_landed_value

#while loop to continue playing and add the balance
while True:    

    game_choice = get_game_type()

#color guess flow 
    if game_choice == 1:
        wager_result = get_wager()
        guess_result = get_color_guess()
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
    
#multi-number choice flow    
    elif game_choice == 2:
        bl_result = get_ball_landed()
        number_guesses = get_multi_number_guess()
        user_bets = get_multi_number_bets(number_guesses)
        combined_guesses_and_bets = dict(zip(number_guesses, user_bets))
        total_bet = sum(user_bets)

        #print bets and spin
        print("Here are your bets:")
        for guess in combined_guesses_and_bets:
            print("\t You bet ${bet} on {guess}".format(guess = guess, bet = combined_guesses_and_bets[guess]))
        print("\t Total: ${total_bet}".format(total_bet=total_bet))
        print("The board and ball are spinning...")
        sleep(2)
        
        if total_bet > balance:
            print("You only have ${balance}, but made ${total_bet} worth of total bets. The casino made you sit out this round.".format(balance=balance, total_bet=total_bet))
        elif bl_result not in number_guesses:
            balance -= total_bet
            print("The ball landed on {number} and lost your bet of ${total_bet}. Your new balance is ${balance}".format(number = bl_result, total_bet = total_bet, balance = balance))
        elif bl_result in number_guesses:
            winning_guess = number_guesses.index(bl_result)
            #winning_bet_index = user_bets.index(winning_guess)
            winning_bet = user_bets[winning_guess] + (user_bets[winning_guess] * 35)
            winning_result = "One of your numbers hit! The ball landed on {number} and you won ${winning_bet}! ".format(number = bl_result, winning_bet=winning_bet) 
            if total_bet > winning_bet:
                total_loss = total_bet - winning_bet
                balance -= total_loss
                print(winning_result + ("Unfortunately, you still came out behind and lost ${total_loss}. Your new balance is ${balance}.".format(total_loss= total_loss,balance= balance)))
            elif winning_bet > total_bet:
                total_gain = winning_bet -  total_bet
                balance += total_gain
                print(winning_result + "Congratulations! You are ${total_gain} ahead after this spin! Youre new balance is ${balance}.".format(total_gain=total_gain, balance= balance))
            else:
                print(winning_result + "Your total bets equaled the amount you won and you broke even on this spin! You're balance stayed the same at ${balance}".format(balance= balance))
#play again 
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
            print("Thanks for playing, {name}!".format(name = name))
            break

#NO LONGER USED - COVERED IN MULTI_CHOICE FLOW
#number guess flow - 
    #if game_choice == 1:
        #wager_result = get_wager()
        #guess_result = get_number_guess()
        #bl_result = get_ball_landed()
        #print("The board and ball are spinning...")
        #sleep(2)

        #if guess_result == bl_result:
        #    money_won = wager_result * 35
        #    balance += money_won
        #    print("Congratulations! You chose {guess_result} and that is the correct number! You win ${money_won} and now have ${balance}!".format(guess_result = guess_result, money_won = money_won, balance = balance))
        #elif guess_result == bl_result and bl_result == 0:
        #    money_won = wager_result * 18
        #    balance += money_won
        #    print("Congratulations! You chose {guess_result} and that is the correct number! You win ${money_won} and now have ${balance}!".format(guess_result = guess_result, money_won = money_won, balance = balance))
        #else:
        #    balance -= wager_result
        #    print("Shoot! You chose {guess_result} and the ball landed on {bl_result}! You lost ${wager_result} and now have ${balance}!".format(guess_result = guess_result, bl_result = bl_result, wager_result = wager_result, balance = balance))
