# DO NOT REMOVE
from get_word import get_word                 #
from score import get_point_value               # 
#################################################
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
