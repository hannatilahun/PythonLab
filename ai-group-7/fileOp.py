
from counter import *

contents = str()
countLine = 0
with open("ai-group-7/textfiles.txt", encoding='utf8') as f:
    contents = f.read()
with open("ai-group-7/textfiles.txt", encoding='utf8') as f:
    for lines in f: countLine = countLine + 1

words = identifyWord(contents)

wordCountResult = wordFrequencyCounter(words)

CharResult = charFrequencyCounter(words)


def wordFrequencyDisplay():
    
    countLoop = 0

    print("\nDisplay words in decreasing order of their frequency:")
    for word,wordCount in wordCountResult[0].items():
        print("[",word,"]","=>",wordCount)

        countLoop = countLoop + 1

        if countLoop == 5: break

def charFrequencyDisplay():

    icount = 0

    print("\nFirst five most frequently occurring characters:")
    for Char,charCount in CharResult[0].items():
        print("[",Char,"]","=>",charCount)

        icount = icount + 1

        if icount == 5:
            break

def displayInfo():
    print("\nOverall result:","\n ",
          countLine, "total lines","\n ",
          wordCountResult[1], "total words","\n ",
                          CharResult[1], "total characters")

    
wordFrequencyDisplay()
charFrequencyDisplay()
displayInfo()