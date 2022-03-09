# First were going to import the random module so the computer can pick a random number
import random

# Ask the user to guess a number.
top_range = input("Pick a number: ")

# Make an if statement to make sure the user actually picks a number as well as it's greater than 0
if top_range.isdigit():             # isdigit() checks if the input is actually a number
    top_range = int(top_range)

    if top_range <= 0:          # This if statement makes sure that the number is greater than or equal to zero
        print("Please select a number larger than 0")
        quit()
else:
    print("please select a number next time.")
    quit()


random_number = random.randint(0, top_range)
guess_counter = 0
# Now make a while loop to make the user guess a number.
while True:
    guess_counter += 1
    users_guess = input("Make a guess: ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print("please select a number next time.")
        continue

    if users_guess == random_number:        # Checks if the users guess is correct.
        print("Congratulations! You got it!")
        break
    elif users_guess > random_number:       # Let's the user know if they are above the correct number or below it.
            print("You're above the number.")
    else:
        print("You're below the number.")

print("You got it in", guess_counter, "guesses")