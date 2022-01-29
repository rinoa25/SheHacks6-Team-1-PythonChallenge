# Aranya Sutharsan
# Rinoa Malapaya
# Kainat Rashid
# Sania Salim

import random


# Main Functions - calls all functions
def main():
    global secretWord
    global alphabet
    global attempt
    global correctLetters
    global wrongLetters
    global usedLetters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    attempt = 0
    correctLetters = ''
    wrongLetters = ''
    usedLetters = ''
    welcomingUser()
    askWord()


def welcomingUser():
    print("Welcome to Hangman")
    print("User 1 it's your turn")
    print()


# Asks the user the length of word
def askWord():
    global secretWord
    secretWord = input("Enter your secret word: ")
    verifyWord()


def verifyWord():
    global secretWord
    if secretWord.isalpha():
        askGuessNum()
    else:
        print("Please enter only letters!")
        print()
        askWord()


# Asks the user the number of guesses
def askGuessNum():
    global numOfGuesses
    print()
    numOfGuesses = input("Enter the number of guesses: ")
    verifyGuessValue()


# Checks if the input is a number
def verifyGuessValue():
    global numOfGuesses
    if numOfGuesses.isdigit():
        if int(numOfGuesses) <= 0:
            print("Please enter a number greater than 0!")
            askGuessNum()
        else:
            encryptWord()
    else:
        print("Please enter a digit!")
        askGuessNum()


# Display
def encryptWord():
    print()
    global encrypted
    global secretWord
    encrypted = "_" * len(secretWord.lower())
    # print(secretWord)  # ANSWER HERE
    print("Word is:", encrypted)
    askUserToGuess()


def askUserToGuess():
    global userGuess
    global attempt
    global numOfGuesses
    global lenOfWord
    global guessesLeft
    global userGuess
    print("User 2 it's your turn")
    notifyUserOfRemainingGuesses()
    checkUserStatus()
    if int(guessesLeft) > 0:
        userGuess = input("Choose a letter to guess: ")
        verifyUserGuess()


def notifyUserOfRemainingGuesses():
    global numOfGuesses
    global guessesLeft
    guessesLeft = int(numOfGuesses) - int(attempt)
    if attempt == 0:
        print("Guesses Left: ", numOfGuesses)
    else:
        print("Guesses Left: ", guessesLeft)
    print("Previous Guesses:", usedLetters)


def checkUserStatus():
    global secretWord
    global lettersFound
    global guessNum
    lettersFound = True
    for i in range(len(secretWord.lower())):
        if secretWord.lower()[i] not in correctLetters:
            lettersFound = False
    if lettersFound:
        print("Congratulations! You won!")
    if lettersFound == False and guessesLeft == 0:
        print("No more guesses left. You lost! Try again next time.")


def verifyUserGuess():
    global userGuess
    global alphabet
    if len(userGuess.lower()) != 1 or userGuess.lower() not in alphabet:
        print(userGuess, "is an invalid input.")
        print()
        print("Word is:", encrypted)
        askUserToGuess()
    else:
        repeatedLetters()


def checkForCorrectLetters():
    global encrypted
    global secretWord
    global guessesLeft
    global attempt
    for ch in range(len(secretWord.lower())):  # replace blanks with correctly guessed letters
        if secretWord.lower()[ch] in userGuess.lower():
            encrypted = encrypted[:ch] + secretWord.lower()[ch] + encrypted[ch + 1:]
    print("Word is:", encrypted)
    attempt += 1
    askUserToGuess()


def showLettersUsed():
    global correctLetters
    global secretWord
    global wrongLetters
    global usedLetters
    global userGuess
    global attempt
    if userGuess.lower() in secretWord.lower() and lettersFound == False:
        if not userGuess.lower() in correctLetters:
            print("Correct! '" + str(userGuess.lower()) + "' is in the word!")
            print()
            correctLetters = correctLetters + userGuess.lower()
    if not userGuess.lower() in secretWord.lower() and lettersFound == False:
        if not userGuess.lower() in wrongLetters:
            print("Incorrect! '" + str(userGuess.lower()) + "' is NOT in the word!")
            print()
            wrongLetters = wrongLetters + userGuess.lower()
    usedLetters = wrongLetters
    checkForCorrectLetters()


def repeatedLetters():
    global userGuess
    global attempt
    global wrongLetters
    global correctLetters
    if userGuess.lower() in wrongLetters and not lettersFound:
        print()
        print("'" + str(userGuess.lower()) + "' is NOT in the word and has been guessed before")
        print("Guesses Left: ", guessesLeft)
        userGuess = input("Choose a letter to guess: ")
        verifyUserGuess()
    if userGuess.lower() in correctLetters and not lettersFound:
        print()
        print("'" + str(userGuess.lower()) + "' is PRESENT in the word but has been guessed before")
        print("Guesses Left: ", guessesLeft)
        userGuess = input("Choose a letter to guess: ")
        verifyUserGuess()
    else:
        showLettersUsed()


main()
