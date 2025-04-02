import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x450")

        self.word_list = [
            "PYTHON", "JAVA", "JAVASCRIPT", "RUBY", "SWIFT", 
            "KOTLIN", "TYPESCRIPT", "GOLANG", "RUST", "HASKELL",
            "PROGRAMMING", "DEVELOPER", "COMPUTER", "ALGORITHM",
            "FUNCTION", "VARIABLE", "DATABASE", "NETWORK"
        ]
        
        self.selected_word = ""
        self.guessed_letters = []
        self.wrong_guesses = []

        self.title_label = tk.Label(root, text="Hangman Game", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.word_display = tk.Label(root, text="", font=("Arial", 20))
        self.word_display.pack(pady=10)

        self.canvas = tk.Canvas(root, width=200, height=250, bg="black", bd=2, relief="sunken")
        self.canvas.pack(side="left", padx=20)

        self.wrong_guesses_label = tk.Label(root, text="Wrong guesses: ", font=("Arial", 14))
        self.wrong_guesses_label.pack(pady=50)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=20)

        self.letter_entry = tk.Entry(self.input_frame, font=("Arial", 18), width=5)
        self.letter_entry.pack(side="left", padx=5)

        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.make_guess)
        self.guess_button.pack(side="left", padx=5)

        self.message_label = tk.Label(root, text="", font=("Arial", 16))
        self.message_label.pack()

        self.start_new_game()

    def start_new_game(self):
        self.selected_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.wrong_guesses = []
        self.update_display()
        self.draw_base_structure()
        self.message_label.config(text="Guess a letter!")
        self.wrong_guesses_label.config(text="Wrong guesses: ")
        self.letter_entry.focus_set()

    def update_display(self):
        display_word = " ".join([l if l in self.guessed_letters else "_" for l in self.selected_word])
        self.word_display.config(text=display_word)
        self.wrong_guesses_label.config(text=f"Wrong guesses: {', '.join(self.wrong_guesses)}")

    def draw_base_structure(self):
        self.canvas.delete("all")
        self.canvas.create_line(20, 230, 180, 230)
        self.canvas.create_line(50, 230, 50, 20)
        self.canvas.create_line(50, 20, 130, 20)
        self.canvas.create_line(130, 20, 130, 50) 

    def draw_hangman(self):
        wrong_count = len(self.wrong_guesses)
        if wrong_count > 0:
            self.canvas.create_oval(110, 50, 150, 90)
        if wrong_count > 1:
            self.canvas.create_line(130, 90, 130, 150)
        if wrong_count > 2:
            self.canvas.create_line(130, 110, 100, 130)
        if wrong_count > 3:
            self.canvas.create_line(130, 110, 160, 130)
        if wrong_count > 4:
            self.canvas.create_line(130, 150, 100, 190)
        if wrong_count > 5:
            self.canvas.create_line(130, 150, 160, 190)

    def make_guess(self):
        letter = self.letter_entry.get().upper()
        self.letter_entry.delete(0, tk.END)

        if not letter or len(letter) != 1 or not letter.isalpha():
            self.message_label.config(text="Please enter a single letter!")
            return
            
        if letter in self.guessed_letters + self.wrong_guesses:
            self.message_label.config(text="You already guessed that letter!")
            return

        if letter in self.selected_word:
            self.guessed_letters.append(letter)
        else:
            self.wrong_guesses.append(letter)

        self.update_display()
        self.draw_hangman()

        if all(l in self.guessed_letters for l in self.selected_word):
            self.message_label.config(text="Congratulations! You win! Restarting...")
            self.root.after(2000, self.start_new_game)
        elif len(self.wrong_guesses) >= 6:
            self.message_label.config(text=f"Game Over! The word was: {self.selected_word}. Restarting...")
            self.root.after(2000, self.start_new_game)


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()