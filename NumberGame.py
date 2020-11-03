print("Welcome the Number Guessing game")
print("You have 5 attempts to guess the number")
user_attempts = 0
while(user_attempts != 5):
    user_input = int(input("Input Your guess: "))
    if user_input > num:
        print("You have entered a large number. Decrease it")
    elif user_input < num:
        print("You have entered a small number. increase it")
    else:
        print("Congrats! you guessed the Number")
        print("You have taken",user_attempts,"attempt to guess the word")
        break
    user_attempts += 1
    print("You have",5 - user_attempts,"attempts left")
    if user_attempts == 5:
        print("Game over")
        break