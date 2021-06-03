import json
import hints

#get data from JSON file
def get_json_data():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)
data = get_json_data()

#count words in json
number_of_words = len(data['words'])
#select only all words from json
all_words = []
for i in range(number_of_words):
    all_words += [data['words'][i]['word']]
    i += 1

#select one random word
varRandomWord = hints.funRandomWord(all_words)

#select hints from random word
for word in data["words"]:
    if word['word'] == varRandomWord:
        hint_one = word['hint_one']
        hint_two = word['hint_two']
        break

##########      HINTS       ################
    #length of guessing word
lengthHint = hints.funWordLength(varRandomWord) 

    #1 - Random letter of guessing word 
letterHint = hints.funRandomLetter(lengthHint)
letterPositionHint = letterHint+1



##########      START A GAME        ################

#1st round
print("Hello, welcome in game 'GUESS THE WORD!\n")
print("\t -Guessing word has: '" +  str(lengthHint) + "' letters \n")
hints.funSplitWordByLetters(varRandomWord)
userInput = hints.userInputFunction()
result = hints.resultFun(userInput ,varRandomWord)
if result == True:
    print("YOU WON THIS GAME")
else:
    #2nd round
    print("\t -First letter is '" +  varRandomWord[0] + "'")
    userInput = hints.userInputFunction()
    result = hints.resultFun(userInput ,varRandomWord)
    if result == True:
        print("YOU WON THIS GAME")
    else:
        #3rd round
        print("\t -On position '" + str(letterPositionHint) + "'" + "is letter '" + varRandomWord[letterHint] + "'")
        userInput = hints.userInputFunction()
        result = hints.resultFun(userInput ,varRandomWord)
        if result == True:
            print("YOU WON THIS GAME")
        else:
            #4th round
            letterHint2 = hints.funRandomLetter(lengthHint)
            letterPositionHint2 = letterHint2+1
            if letterHint2 != letterHint:
                print("\t -On position '" + str(letterPositionHint2) + "'" + "is letter '" + varRandomWord[letterHint2] + "'")
            else:
                while letterHint2 == letterHint:
                    letterHint2 = hints.funRandomLetter(lengthHint)     
                    if letterHint2 != letterHint:
                        letterPositionHint2 = letterHint2+1
                        print("\t -On position '" + str(letterPositionHint2) + "'" + "is letter '" + word[letterHint2] + "'")
            userInput = hints.userInputFunction()
            result = hints.resultFun(userInput ,varRandomWord)
            if result == True:
                print("YOU WON THIS GAME")
            else:
                #5th round
                print("\t" + hint_one)
                userInput = hints.userInputFunction()
                if result == True:
                    print("YOU WON THIS GAME")
                else:
                    #6th round
                    print("\t" + hint_two)
                    userInput = hints.userInputFunction()
                    result = hints.resultFun(userInput ,varRandomWord)
                    if result == True:
                        print("YOU WON THIS GAME")
                    else:
                        print("SORRY, YOU LOST THIS GAME")

''''
#execution
print("hint #1 \n"  + hint_one + " \n hint #2 \n" + hint_two)
'''