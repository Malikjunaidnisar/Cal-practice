from flask import Flask, render_template, request
import random

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        layer = int(request.form['layer'])
        row = int(request.form['row'])
        col = int(request.form['col'])
        card = game_board[layer-1][row-1][col-1]

        if card is not None and card != 0:
            game_board[layer-1][row-1][col-1] = None
            moves_left -= 1

    return render_template('index.html', game_board=game_board, moves_left=moves_left)

if __name__ == '__main__':
    app.run(debug=True)
