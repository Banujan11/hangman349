import random

class Hangman:
    def __init__(self, Word_list, num_lives=5):
        self.Word_list = Word_list
        self.num_lives = num_lives
        self.list_of_guesses =[]
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def pick_random_word(self):

        return random.choice(self.Word_list)
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for letter_in_word, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[letter_in_word] = guess

            self.num_letters -=1

        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess)== 1):
                print("Invalid letter. Please enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)

                self.list_of_guesses.append(guess)
                break

def play_game(Word_list):
    num_lives = 5

    game = Hangman(Word_list, num_lives)

    print("Word:", " ".join(game.word_guessed))
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break

        if game.num_letters >0:
            game.ask_for_input()

            print("Word:", " ".join(game.word_guessed))

        else:
            print("Congratulations. You won the game!")
            break

Word_list = ["apple","banana", "cherry", "pear", "mango"]
play_game(Word_list)