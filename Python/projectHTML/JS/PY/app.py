from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

selected_word = ""
guessed_letters = []
wrong_guesses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global selected_word, guessed_letters, wrong_guesses
    data = request.get_json()
    selected_word = data.get("word", "").upper()
    guessed_letters = []
    wrong_guesses = []

    display_word = " ".join(["_" for _ in selected_word])
    return jsonify(success=True, display_word=display_word)

@app.route('/guess', methods=['POST'])
def guess():
    global guessed_letters, wrong_guesses
    letter = request.json.get("letter", "").upper()
    if not letter or letter in guessed_letters or letter in wrong_guesses:
        return jsonify(success=False, message="Invalid or duplicate guess")

    if letter in selected_word:
        guessed_letters.append(letter)
    else:
        wrong_guesses.append(letter)

    display_word = " ".join([l if l in guessed_letters else "_" for l in selected_word])
    won = "_" not in display_word
    lost = len(wrong_guesses) >= 6

    return jsonify(
        display_word=display_word,
        wrong_guesses=wrong_guesses,
        won=won,
        lost=lost,
        success=True
    )

if __name__ == "__main__":
    app.run(debug=True)
