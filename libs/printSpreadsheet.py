from terminal import Tbackground  #¯\_(ツ)_/¯
import os

def printscreen(spreadsheet,originX,originY,collumnSize):
    """
    prints a state of the spreadsheet
    i cant be bothered to make a proper code
    ik this is ugly af, i just hope it'll work and i wont have to come back to it
    """
    screenSize = os.get_terminal_size()
    printList = []                          #list of all the terminal lines it COULD print, might not print them all
    collumnAmmount = screenSize[0]//collumnSize
    usefulLines = []
    for line in range(originY,(len(spreadsheet),originY+screenSize[1])):
        usefulLines.append(line[originX:min(originX+screenSize,len(line)-1)])
    
    for line in usefulLines:
        for termLine in makeLinePrintable(line):
            printList.append(termLine)
            
    for i in range(min(len(printList),screenSize[1])):
        print(printList[i])
        
        
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
    gives a list of strings
    each string is a line to print in the terminal
    """
    middleList = []
    for value in valuesList:
        middleList.append(makeSquarePrintable(value,collumnSize))
    
    finalList = []
    middleList = invertDimentions(middleList)
    for line in middleList:
        linestring = ""
        for val in line:
            if val == None:
                linestring = linestring + " "*collumnSize
            else:
                linestring = linestring + val
        finalList.append(linestring)
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
    
    
    
    
    
    