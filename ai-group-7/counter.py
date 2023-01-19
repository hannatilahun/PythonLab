import re

def identifyWord(content):
    text = re.sub(r'[^\w\s]','',content)

    words = re.findall(r'\b\w+\b',text)

    return words

def wordFrequencyCounter(wordList):

    counts = {}
    countWord = 0
    for word in wordList:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        countWord = countWord + 1
        
    sortedWordCounts = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))
    return [sortedWordCounts, countWord]


def charFrequencyCounter(strList):
    result = {}
    
    charCountResult = 0

    str = ""

    str = str.join(strList)

    for letter in str:
   
        if letter.isalpha() :
            count = str.count(letter)
            result[letter] = count

            charCountResult = charCountResult + 1

    sortedCharResult = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))
    return [sortedCharResult, charCountResult]