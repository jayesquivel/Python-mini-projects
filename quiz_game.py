# Greet the users to what my game is
print("Welcome to the game about history!")

# Ask the user if they want to play my game.
play = input("Would you like to play? ")

if play != "yes":
    quit()

print("Sweet. Let's play :)")

# Add a score tracker to the game.
score = 0

# Start asking the questions
answer = input("Who attacked peral harbor in 1941? ").lower()
if answer.lower() == "japan":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("From what years did the great depression take place? ")
if answer.lower() == "1929 - 1941":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What year did John F Kennedy become president? ")
if answer.lower() == "1961":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What year did the soviet union fall? ")
if answer.lower() == "1991":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")


# Let them know the results of the tests.
print("You got " + str(score) + " questions correct.")

# Also let them know the precentage of the tests.
print("You got " + str((score/4) * 100) + "%")






