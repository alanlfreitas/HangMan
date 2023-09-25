# -------------------- HangMan Project -------------------- #
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel", "gorilla", "kangaroo", "duck", "spider"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Creating variable to set the amount of lives
lives = 6

#Testing the code
print(f'The random word is: {chosen_word}.')

#Create the list with blanks
display = []
for _ in range(word_length):
  display += "_"
end_game = False

#Adding a loop until user to complete the word.
while not end_game:
  guess = input("Guess a letter: ").lower()
  
#Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_game = True
      print("You lose.")
  print(display)
  print(stages[lives])
  if "_" not in display:
    end_game = True
    print("You win.")
print(stages[lives])