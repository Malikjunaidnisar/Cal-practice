import random

# Initialize the 3D game board
game_board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(3)]

# Initialize the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

# Deal the cards
for layer in range(3):
    for row in range(4):
        for col in range(4):
            game_board[layer][row][col] = deck.pop()

# Initialize the move counter
moves_left = 100

# Game logic
while True:
    # Display the game board
    print("Layer 1:")
    for row in game_board[0]:
        print(row)
    print("Layer 2:")
    for row in game_board[1]:
        print(row)
    print("Layer 3:")
    for row in game_board[2]:
        print(row)

    # Get user input
    layer = int(input("Enter the layer (1-3): "))
    row = int(input("Enter the row (1-4): "))
    col = int(input("Enter the column (1-4): "))
    card = game_board[layer-1][row-1][col-1]

    # Check if the move is valid
    if card is not None and card != 0:
        # Perform the move
        game_board[layer-1][row-1][col-1] = None
        moves_left -= 1
        print(f"Move {moves_left} left.")
    else:
        print("Invalid move. Try again!")

    # Check if the game is won
    if all(all(all(cell == 0 for cell in row) for row in layer) for layer in game_board):
        print("Congratulations! You won!")
        break

    # Check if the game is lost
    if moves_left == 0:
        print("Game over! You lost.")
        break
