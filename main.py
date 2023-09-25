# -------------------- HangMan Project -------------------- #
#Step 1 
import random
word_list = ["aardvark", "baboon", "camel", "gorilla", "kangaroo", "duck", "spider"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

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
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
  
  print(display)
  if "_" not in display:
    end_game = True
    print("You win.")