# Project TwitterTracker
# readtext.py
# Beryce Garcia
# June 27, 2018

import re

def getDates(textFile):
    '''Returns a list of all the dates in the text file. Text file must
    be in string format.'''
    
    with open(textFile, 'r') as inputFile:
        lines = inputFile.read()
        dateList = []
        
        pattern = re.compile(r'(Date:.*) at')
        matches = pattern.findall(lines)
        
        for match in matches:
            date = match.split(':')[1].strip()
            dateList.append(date)
        
    return dateList

def getKeywords(textFile):
    '''Returns a list of all the keywords in text file. Text file must be
    in string format.'''
    
    with open(textFile, 'r') as inputFile:
        lines = inputFile.read()
        keywordList = []
        
        pattern = re.compile(r'Keyword:.*')
        matches = pattern.findall(lines)
        
        for match in matches:
            keyword = match.split(':')[1].strip()
            keywordList.append(keyword[1:-1]) # getting rid of quotes
        
        return keywordList

def getKeywordDict(textFile):
    '''Returns a dictionary of all keywords as keys and their frequencies
    as values.'''
    
    keywordList = getKeywords(textFile)
    keyFreqDict = dict()
    
    for keyword in keywordList:
        if keyword not in keyFreqDict:
            keyFreqDict[keyword] = 1
        else:
            keyFreqDict[keyword] += 1
    
    return keyFreqDict
    
def getUnigramDict(textFile):
    '''Returns a dictionary of unigrams and their frequencies.'''
    # FIX
    
    with open(textFile, 'r') as inputFile:
        lines = inputFile.read()
        unigramDict = dict()
        
        pattern = re.compile(r'@?\w+\n\d+', re.MULTILINE)
        matches = pattern.findall(lines)
        
        for match in matches:
            unigram, frequency = match.split()[0], int(match.split()[1])
                                 
            if unigram not in unigramDict:
                unigramDict[unigram] = frequency
            else:
                unigramDict[unigram] += frequency
        
        return unigramDict

def getBigramDict(textFile):
    '''Returns a dictionary of bigrams and their frequencies.'''
    
    with open(textFile) as inputFile:
        lines = inputFile.read()
        # print(lines[:10])
        bigramDict = dict()

        pattern = re.compile(r'.?\w+ .?\w+\n\d+',re.MULTILINE)
        matches = pattern.findall(lines)
        
        for match in matches:
            bigram, freq = match.split('\n')[0], int(match.split('\n')[1])
            
            if bigram not in bigramDict:
                bigramDict[bigram] = freq
            else:
                bigramDict[bigram] += freq
        
        return bigramDict

def getHashtagDict(textFile):
    '''Returns a dictionary hashtags found in textFile. as keys and 
    frequencies as values '''
    
    with open(textFile, 'r') as inputFile:
        lines = inputFile.read()
        hashtagDict = dict()
        
        pattern = re.compile(r'#\w+\n\d+', re.MULTILINE)
        matches = pattern.findall(lines)
        
        for match in matches:
            hashtag, frequency = match.split('\n')[0], \
                                    int(match.split('\n')[1])
                                    
            if hashtag not in hashtagDict:
                hashtagDict[hashtag] = frequency
            else:
                hashtagDict[hashtag] += frequency
        
        return hashtagDict

def hashtagFormat(hashtagDict):
    '''Turns hashtag dictionary into a list of dictionaries with
    hashtag and frequency as keys.'''
    
    hashtagList = []
    
    for hashtag in hashtagDict:
        dictionary = dict()
        dictionary["hashtag"] = hashtag
        dictionary["frequency"] = hashtagDict[hashtag]
        hashtagList.append(dictionary)
    
    return hashtagList

def keywordFormat(keywordDict):
    '''Turns keyword dictionary into a formatted JSON.'''
    
    keywordList = []
    
    for keyword in keywordDict:
        dictionary = dict()
        dictionary["keyword"] = keyword
        dictionary["frequency"] = keywordDict[keyword]
        keywordList.append(dictionary)
    
    return keywordList
        
    
    
print keywordFormat(getKeywordDict('April18.txt'))