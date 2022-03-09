# Set the choices for the user to pick from
choices = ["rock", "paper", "scissors"]

# Make users choose from the list of choices as well as make a while loop.
player1 = input("Player 1, enter rock, paper or scissors:\n")
player2 = input("Player 2, enter rock, paper or scissors:\n")
players = player1 + player2

# Now we make the conditions for the game.
if player1 == "rock":             # Player1 rock if
    if player2 == "paper":
        print("Player 2 wins. Paper covers rocks.")
    if player2 == "scissors":
        print("Player 1 wins. Rocks dull scissors.")
    if player2 == player1:
        print("Neither player wins. Tie with rocks.")
elif player1 == "paper":            # Player 1 paper elif
    if player2 == "scissors":
        print("Player 2 wins. Scissors cut paper.")
    if player2 == "rock":
        print("Player 1 wins. Paper covers rocks.")
    if player2 == "paper":
        print("Neither player wins. Tie with paper.")
elif player1 == "scissors":         # Player 1 scissors elif
    if player2 == "rock":
        print("Player 2 wins. Rocks dull scissors.")
    if player2 == "paper":
        print("Player 1 wins. Scissors cut paper.")
    if player2 == "scissors":
        print("Neither player wins. Tie with scissors.")
else:
    print("Illegal entry occurred.")