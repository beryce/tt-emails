# Project TwitterTracker
# charts.py
# Beryce Garcia
# July 5, 2018

import matplotlib.pyplot as plt
import numpy as np
import readtext
import pandas as pd
import sqlite3
import json

def keywordsBar(textFile):
    '''Returns a bar chart of the top keywords.'''
    
    # gets top ten keywords and their values
    keywords = readtext.getKeyFreq(textFile).keys()
    values = readtext.getKeyFreq(textFile).values()
    
    date = readtext.getDates(textFile)
    month, year = date[0].split(' ')[0], date[0].split(' ')[-1]
    
    # unsure what this does -- ask
    position = np.arange(len(values))
    
    # creating the bar graph    
    plt.barh(position,values,0.5,align='center')
    plt.yticks(position,keywords)
    plt.title('Top Keywords in ' + month + ' ' + year)
    plt.xlabel('Frequency')
    plt.ylabel('Keywords')
    
    # adding the number values to top of the bars
    for i, v in enumerate(values):
        plt.text(v + .10, i, str(v), color='black', fontweight='bold')
    
    plt.show()

def hashtagTable(textFile):
    '''Returns a table with all the hashtags.'''
    
    data = {'hashtag': readtext.getHashtagDict(textFile).keys(),
            'frequency': readtext.getHashtagDict(textFile).values()}
    frame = pd.DataFrame(data)
    
    columnTitles = ["hashtag", "frequency"]
    frame = frame.reindex(columns=columnTitles)
    
    return frame # how to make it left aligned?

def createHashtagJSON(textFile, newFileName):
    """Creates a JSON file for hashtags."""
    with open(newFileName, 'w') as outputFile:
        dictionary = readtext.getHashtagDict(textFile)
        json.dump(readtext.hashtagFormat(dictionary), outputFile)

def createHashtagDB(jsonFile):
    """Creates a database!"""
    with open(jsonFile,'r') as inputFile:
        jsonList = json.load(inputFile)
        
        # connecting to the database
        connection = sqlite3.connect("hashtags.db")
        
        # creating a cursor to allow SQL commands
        crsr = connection.cursor()
        
        # inserting data
        for element in jsonList:
            hashtag = element['hashtag']
            freq = element['frequency']
            
            crsr.execute("INSERT INTO hashtagtable VALUES (?, ?)",
                (hashtag, freq))
            
            connection.commit()

def createKeywordJSON(textFile, newFileName):
    '''Creates a new JSON file for keywords.'''
    with open(newFileName, 'w') as outputFile:
        dictionary = readtext.getKeywordDict(textFile)
        json.dump(readtext.keywordFormat(dictionary), outputFile)

createKeywordJSON('May18.txt', 'keywordDBMay18.json')


        
# crsr.execute("SELECT * FROM hashtagtable WHERE frequency=?", (7,))
# print(crsr.fetchall())


