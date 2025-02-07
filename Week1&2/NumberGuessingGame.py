import random

attempts = 0
while True:
    random_num = random.randint(1, 100)
    user_guess = int(input("Guess the number: "))
    user_input = ""
    attempts = attempts + 1 
    if(user_guess == random_num):
        print("You guessed correctly!")
        print(f"Your guess: {user_guess}")
        print(f"Number generated: {random_num}")
        print(f"Total attempts: {attempts}")
        user_input = input("Would you like to play again?")
    elif (random_num - user_guess >= 20):
        print("Too low")
    elif (user_guess - random_num <= 20):
        print("Too high")
    else :
        print("Try again")
    
    if (attempts == 10):
        print(random_num)
        print("So many attempts. Better luck next time.")
        user_input = input("Would you like to play again?")

    if (user_input == "no"):
        print("Exiting....")
        break

        