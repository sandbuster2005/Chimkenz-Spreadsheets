from terminal import Tbackground  #¯\_(ツ)_/¯
import os

def printscreen(spreadsheet,originX,originY,collumnSize):
    """prints a state of the spreadsheet"""
    screenSize = os.get_terminal_size()
    printList = []
    collumnAmmount = screenSize[0]//collumnSize
    collumns = []
    for line in range(originY,(len(spreadsheet),originY+screenSize[1])):
        collumns.append()

def makeSquarePrintable(value,collumnSize):
    """
    ya give this the value of a square and your options and it gives you wat to print and how many lines
    """
    valueSTR = str(value)
    finalList = []
    while len(valueSTR) > collumnSize:
        finalList.append(valueSTR[:collumnSize])
        valueSTR = valueSTR[collumnSize:]
        
    finalSTR = " "*(collumnSize-len(valueSTR)) + valueSTR
    finalList.append(finalSTR)
    return finalList

def makeLinePrintable(valuesList,collumnSize):
    """
    beeg list of all the values is given
    gives a list of lists
    the first list represents all the lines of the terminal that your line will take
    the deeper list repressents all the values in each line
    """
    middleList = []
    for value in valuesList:
        middleList.append(makeSquarePrintable(value,collumnSize))
    
    finalList = invertDimentions(middleList)
    for line in finalList:
        for val in line:
            if line == None:
                line = " "*collumnSize
    return finalList

def generateHeader(originX,collumnAmmount,collumnSize):
    return [Tbackground(196,196,196," "*collumnSize)]













def invertDimentions(liste):
    """
    give it a 2-dimentional list and it'll invert those dimensions
    """
    finalList = []
    shouldContinue = True
    counter = 0
    while shouldContinue:
        tempList = []
        shouldContinue = False
        for i in range(len(liste)):
            if counter < len(liste[i]):
                tempList.append(liste[i][counter])
                shouldContinue = True
            else:
                tempList.append(None)
            
        finalList.append(tempList)
        counter += 1
    finalList.pop(-1)
    return finalList
    
    
    
    
    
    