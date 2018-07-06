# Project TwitterTracker
# charts.py
# Beryce Garcia
# July 5, 2018

import matplotlib.pyplot as plt
import numpy as np
import readtext
import pandas as pd
import sqlite3

# connecting to the database
# connection = sqlite3.connect("emails_db.db")

# cursor
# crsr = connection.cursor()

# SQL command to create a table in the database
# sql_command = """CREATE TABLE unigrams (
# unigram VARCHAR(1000),
# frequency INTEGER
# );"""

# executing the statement
# crsr.execute(sql_command)

# SQL command to insert the data in the table
# sql_command = """INSERT INTO hashtagtable VALUES ("#mueller", 224);"""
# crsr.execute(sql_command)

# connection.commit()
# connection.close()

# d = readtext.getHashtagDict('June18.txt')
# obj3 = pd.Series(d)
# obj3.index.name = 'hashtags'
# print obj3
# 
# df = pd.DataFrame(data=obj3)

# print df

# df = pd.DataFrame(data=d, index=[0])
# print df


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
    
    print month, year

def hashtagTable(textFile):
    '''Returns a table of hashtags and their frequencies.'''
    
    data = {'hashtag': readtext.getHashtagDict(textFile).keys(), 
            'frequency': readtext.getHashtagDict(textFile).values()}
    frame = pd.DataFrame(data)
    
    columnsTitles = ["hashtag","frequency"]
    frame = frame.reindex(columns=columnsTitles)
    
    frame.style.set_properties(**{'text-align': 'left'})
    
    return frame
    
print hashtagTable('June18.txt')


    
    


