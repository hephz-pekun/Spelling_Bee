# Spelling Bee Game

## Background and Rules

Congratulations! You’re a new software engineer for The New York Times and you’ve been tasked to create a new word game called **Spelling Bee**. In the game Spelling Bee, the user is trying to create as many words as they can out of 7 letters. The user will type in a word that is at least 4 letters long, and contains a required letter, and the computer will convert said word to some point value. Pangrams, words that contain all seven letters, give the user bonus points.

The goal of the game is to get as high of a score as possible by guessing as many words as possible. As your score increases, you get a ranking, and the goal of the game is to get as close to the “Genius” ranking as you can.

You can also play the game online at Spelling Bee to see more examples.

## Sample Game Flow

Below is a sample game flow. Please make sure your code uses the exact text as shown in the game flow; our autograding relies on this.

1. **Prompt the user to enter the 7 letters they want to use with the message:**
   ```
   Welcome to Spelling Bee! Enter your 7 letters, separated by commas:
   ```

2. **Prompt the user to select which of the 7 letters will be the required letter with the message:**
   ```
   Which of these 7 letters [‘H’,’A’,’B’,’I’,’T’,’U’,’L’] will be your required letter?
   ```

3. **If the letter the user enters is not one of the letters they entered before, tell them:**
   ```
   {letter} is not an available letter. Please choose from the following: {letters}
   ```

4. **Prompt the user to input their guess with the message:**
   ```
   Enter your word:
   ```

5. **If the user’s guess is invalid, say the proper messaging and then ask the user to input their guess with the message:**
   ```
   Enter your word: again.
   ```

   A guess is invalid if:
   - The guess has less than 4 letters
   - The required letter is not in the guess
   - The guess contains letters that are not in the list of letters given
   - The guess has already been used.

6. **If the user enters ‘END’, then end the game and display their score.**

7. **If the user enters a valid guess, calculate their score for the guess using the following rubric:**
   - Each letter in the guess is worth 1 point
   - If the guess is a pangram, add an additional 7 points (the guess is a pangram if the guess contains all the letters listed at least once)

## Sample Game

Here is a sample game. The text in italics and highlights are not in the actual game output; it is just there to provide more context. Note that this is only a sample, your solutions will be graded on more test cases than is provided.

### GAME 1:

**Computer:** Welcome to Spelling Bee! Enter your 7 letters, separated by commas:  
**User:** H,A,B,I,T,U,L  
**Computer:** Which of these 7 letters [‘H’,’A’,’B’,’I’,’T’,’U’,’L’] will be your required letter?  
**User:** T  
**Computer:** Enter your guess:  
**User:** HABIT  
**Computer:** HABIT  
**Computer:** Enter your guess:  
**User:** HILL  
**Computer:** T must be in the word. The score is not updated since the word is invalid.  
**Computer:** Enter your guess:  
**User:** HABITUAL  
**Computer:** HABITUAL - Pangram!  
**Computer:** Enter your guess:  
**User:** BAT  
**Computer:** Your word must be at least 4 letters long. The score is not updated since the word is invalid.  
**Computer:** Enter your guess:  
**User:** TILDA  
**Computer:** D is not a letter you can use. The only letters you can use are [‘H’,’A’,’B’,’I’,’T’,’U’,’L’]. The score is not updated since the word is invalid.  
**Computer:** Enter your guess:  
**User:** END  
**Computer:** Your final score is 20.
