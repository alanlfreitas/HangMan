# -------------------- HangMan Project -------------------- #
import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
from replit import clear
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Setting the condition for the game to end
end_game = False
#Creating variable to set the amount of lives
lives = 6
#importing the logo and printing it at the start

print(logo)

#Testing the code
#print(f'The random word is: {chosen_word}.')

#Create the list with blanks
display = []
for _ in range(word_length):
  display += "_"

#Adding a loop until user to complete the word.
while not end_game:
  guess = input("Guess a letter: ").lower()
  clear()
  #Returning if the letter was given before
  if guess in display:
    print(f"You've already {guess} right!")
  
#Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    print(f"You guessed {guess}, and it's wrong. You lose a life.")
    lives -= 1
    if lives == 0:
      end_game = True
      print("You lose.")
      print(f"The word was: {chosen_word}")
  #joining all elements in the list and turning it into a string
  print(f"{''.join(display)}")
  
  #Checking if the user got all the letters
  if "_" not in display:
    end_game = True
    print("You win.")
  print(stages[lives])