import random
import math
play_again = 'y'
while play_again == 'y':
    print("Welcome To Number Game")
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    number_to_guess = random.randint(lower, upper)
    x = int(math.log(upper - lower + 1, 2))
    print("\n\tYou've only ", x,"chances to guess the integer.\n")
    count = 1
    while count < math.log(upper - lower +1, 2):
            count += 1
            guess = int(input("Enter the guess: "))
            if number_to_guess == guess:
                print("Congo you did it in ", count-1, "try.")
                break
            elif number_to_guess >guess :
                print("Your guess lower than the number ")
            elif number_to_guess < guess :
                print("Your guess bigger than the number")
            if count >= math.log(upper - lower +1, 2):
                print("\nThe number is %d"%number_to_guess)
                print('\tBetter Luck Next Time!')
    play_again = input('Do You Want to Play Again? (y / n):  ')
    
            




