'''Write a program that generates a random number and asks the users to guess it. If the 
    player's guess is higher than the actual number, the program displays "Lower number please"
    If the guess is too high, the program displays "Higher number please". When the user guesses
    the correct number, the program displays the number of guesses the player used to arrive at 
    the number'''


import random

goal = random.randint(1, 10)    #genearting a random number between 1 to 10
guesses = 0     #counter for counting number of guesses
while True: #loop for continuous guessing
    user_guess = int(input("Guess a number between 1 and 10: "))    #takinmg user's input
    if user_guess < goal:   #if user's guess is smaller
        print("Higher number please")   #prompt him to guess higher
    elif user_guess > goal:     #if user's guess is higher
        print("Lower number please")   #prompt him to guess lower
    else:
        print(f"Congratulations, you guessed the number {goal} in {guesses + 1} guesses!")     #if the number matches
        #display win and number of guesses
        break

    guesses+=1  #increment the guesses counter


