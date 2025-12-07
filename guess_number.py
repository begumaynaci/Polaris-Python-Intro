from random import randint

number = randint(1, 100)
counter = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < 1 or guess > 100:
            print("Please enter a number within the range 1 to 100.")
            continue
        counter += 1
        
        if guess < number:
            print("Go higher!")

        elif guess > number:
            print("Go lower!")

        else:
            print("Congratulations! You've guessed the number in", counter , "tries.")
            break

    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 100.")

