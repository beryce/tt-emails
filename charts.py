# Project TwitterTracker
# charts.py
# Beryce Garcia
# July 5, 2018

import matplotlib.pyplot as plt
import numpy as np
import readtext

def keywordsBar(textFile):
    '''Returns a bar chart of the top keywords.'''
    
    # gets top ten keywords and their values
    keywords = readtext.getKeyFreq(textFile).keys()
    values = readtext.getKeyFreq(textFile).values()
    
    # unsure what this does -- ask
    position = np.arange(len(values))
    
    # creating the bar graph    
    plt.barh(position,values,0.5,align='center')
    plt.yticks(position,keywords)
    plt.title('Top Keywords in June')
    plt.xlabel('Frequency')
    plt.ylabel('Keywords')
    
    # adding the number values to top of the bars
    for i, v in enumerate(values):
        plt.text(v + .10, i, str(v), color='black', fontweight='bold')
    
    plt.show()

def unigramsBar(textFile):
    '''Returns a bar chart of the top ten unigrams.'''
    
    unigrams = readtext.getUnigramDict(textFile).keys()
    return unigrams
    

    
print unigramsBar('June18.txt')
# print(readtext.getKeywords("June18.txt"))