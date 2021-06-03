import random

# random word from array
def funRandomWord(all_words):
    varRandomWord = random.choice(all_words)
    return varRandomWord

# lenght of random word (number of characters)
def funWordLength(varRandomWord):
    varWordLength = len(varRandomWord)
    return varWordLength

# random letter from random word
def funRandomLetter(varRandomWord):
    varRandomLetter = random.randint(1, (varRandomWord-1))
    return varRandomLetter

# splti word to letters
def funSplitWordByLetters(varRandomWord):
    shufle = list(varRandomWord)
    print(random.shuffle(shufle))

#user input
def userInputFunction():
    userInput = input("Please enter world what you guess:\n")
    if userInput.isalpha():
        print("you have written '" + userInput + "'")
        return userInput
    else:
        while not userInput.isalpha():
            userInput = str(input("Please enter only alphabetical symbols:\n"))
            if userInput.isalpha():
                print("you have written '" + userInput + "'")
                return userInput

#result
def resultFun(userInput,varRandomWord):
    if (userInput == varRandomWord):
        print ("\nCORRECT !! YOU WON\n")
        won = True
        return won
    else:
        print ("\nSORRY :( bad word\n")
