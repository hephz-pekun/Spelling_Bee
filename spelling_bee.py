# DO NOT REMOVE
from valid_word import is_valid_word
from pangram import is_pangram #DO NOT MODIFY
from get_word import get_word                 #
from score import get_point_value               # 
#################################################

def is_valid_word(word, letters, required_letter, used_words):
  if word == "END": #checks if the user ends the game
    return True
  if len(word) < 4: #checks for the least amount of word that has to be inputed
    print ("Your word must be at least 4 letters long")
    return False
  if required_letter not in word: # checks if required letter is in inputed word
    print (f"Your word must contain the letter {required_letter}") 
    return False
  for letter in word: #checks each letter in word
     if letter not in letters: #checks if letter is in the list of letter that the user can use
      print(f"{letter} is not a letter you can use. The only letters you can use are {letters}")
      return False
  if word in used_words: #checks if the word has already been used
   print("Already used")
   return False
  return True

# Write the get_word function here.
def get_word(letters, required_letter, used_words):
  word = input("Enter your word: \n").upper() #asks users to input a word
  #check if word is valid based on the is_valid function, as long as it is not, user has to input word
  while not is_valid_word(word, letters, required_letter, used_words) and word != "END":
    word = input("Enter your word: \n").upper()
    #print(word)
  used_words.append(word) #add valid word to the used words list
  return word

def is_pangram(guess, letters):
  for letter in letters:#goes through each letter in the list filled with letters
    if letter not in guess: #check if letter is in the guess word
      return False
  return True

def get_point_value(word,letters):
  points = 0 #start value of the point system
  for letter in word: #add a point for each letter that makes up the word
    points += 1
  if is_pangram(word, letters): #check if word is a pangram
    points += 7 #add 7 points if it is
    print (f"{word} - Pangram!") # print statement to show that word is a pangram explaining the extra points
  elif word == "END": # check if user ends the game
    points = 0 #so as not to count the letters in the words, as it is a command nog an input
  else: 
    print(f"{word}") 
  return points #show point value
  

def pspelling_bee():
 #emoty/new variable
  score = 0 #start value of score - complied point value
  used_words = [] # placeholder for the list of used_words
  word = "" #placeholder for word inputs 
  #welcome statement to start the game player
  greeting = input("Welcome to Spelling Bee! Enter your 7 letters, separated by commas: \n")
  letters = greeting.split(",")#convert users letters to a list
  #choose the required_letter
  required_letter = input(f"Which of these 7 letters {letters} will be your required letter?\n")
  while required_letter not in letters:#check that the required_letter is in the list of letters
    #so long as required_letter is not in list of letters, keep asking for another letter
    print(f"{required_letter} is not an available letter. Please choose from the following: {letters}")
    required_letter = input(f"Which of these 7 letters {letters} will be your required letter?\n")
  #so long as the user doesn't end the game, check if word is valid and tally points
  while word != "END": 
    word = get_word(letters, required_letter, used_words)
    score += get_point_value(word,letters)
  print (f"Your final score is {score}") #when game is ended print final score
  
def spelling_bee():
  pspelling_bee() #call game

spelling_bee() # DO NOT REMOVE
