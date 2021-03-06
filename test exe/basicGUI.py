﻿# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from trig import givenLengths, givenPoints
from C2F import C_to_F_converter, F_to_C_converter, k_to_c_converter, c_to_k_converter
from dictionary import dictionary
from PIL import ImageTk, Image
from calc import startCalc

#Create new label with output value on specified page
def newLabel(strOut, pageNum):
    if(pageNum == page3):
        wrapNum = 500
    else:
        wrapNum = 0
    Label(pageNum, text = strOut, wraplength = wrapNum).pack()

#Function called when button pressed if points of triangle are entered (page1)
def enterValuesPoints():
    #Get triangle type from givenLengths in main.py
    finalAnswerPoints = givenPoints(getx1.get(), gety1.get(), getx2.get(), gety2.get(), getx3.get(), gety3.get())
    print(finalAnswerPoints)

    #Add lengths and triangle type as new labels in GUI
    newLabel("Side 1: " + str(finalAnswerPoints[0]) +
            "\nSide 2: " + str(finalAnswerPoints[1]) +
            "\nSide 3: " + str(finalAnswerPoints[2]) +
            "\nType: " + str(finalAnswerPoints[3]),
            page1)

#Function called when button pressed if lengths of sides are entered (page1)
def enterValuesLength():
    print("LENGTHS:")
    print(str(getSide1) + str(getSide2) + str(getSide3))
    #Get triangle type from givenLengths using main.py
    finalAnswerLength = givenLengths(getSide1.get(), getSide2.get(), getSide3.get())
    print(finalAnswerLength)

    #Add triangle type as a new label in GUI
    newLabel(finalAnswerLength, page1)

#Creates input field/labels/buttons for length input (page1)
def lengthInput():
    #Labels/input fields for GUI (side lengths)
    for x in range (1, 4):
        newLabel("Side " + str(x), page1)
        if(x == 1):
            sideNeeded = getSide1
        elif(x == 2):
            sideNeeded = getSide2
        else:
            sideNeeded = getSide3
        Entry(page1, textvariable = sideNeeded).pack()

    #Submit button in GUI (side lengths)
    Button(page1, text = "Submit Lengths", command = enterValuesLength, fg = "white", bg = "black").pack()

#Creates input field/labels/buttons for point input (page1)
def pointInput():
    #Labels/input fields for GUI (points given)
    for x in range (1, 4):
        if(x == 1):
            nums = "x1", "y1"
            textVar = getx1, gety1
        elif(x == 2):
            nums = "x2", "y2"
            textVar = getx2, gety2
        elif(x == 3):
            nums = "x3", "y3"
            textVar = getx3, gety3

        newLabel(nums[0], page1)
        Entry(page1, textvariable = textVar[0]).pack()
        newLabel(nums[1], page1)
        Entry(page1, textvariable = textVar[1]).pack()

    Button(page1, text = "Submit Points", command = enterValuesPoints, fg = "white", bg = "black").pack()


#Function called when button pressed if degrees entered (page2)
def enterDegree(dType):
    #dType 1 = C to F
    #dType 2 = F to C
    #dType 3 = K to C
    #dType 4 = C to K
    def whatToDo(convType, strType, strInv):
        finalDeg = convType(getC.get())
        print(finalDeg)
        newLabel(str(getC.get()) + "°" + strType + " = " + str(finalDeg) + "°" + strInv, page2) #str(finalF) + "°F", page2)

    if(dType == 1):
        whatToDo(C_to_F_converter, "C", "F")
    elif(dType == 2):
        whatToDo(F_to_C_converter, "F", "C")
    elif(dType == 3):
        whatToDo(k_to_c_converter, "K", "C")
    else:
        whatToDo(c_to_k_converter, "C", "K")

#Creates input field/labels/buttons for degree input (page2)
'''v = tk.IntVar()'''
def degreeInput():
    newLabel("Degrees to convert", page2)
    mEntry = Entry(page2, textvariable = getC).pack()
    Button(page2, text = "Submit °C Value To °F", command = lambda : enterDegree(1), fg = "white", bg = "black").pack()
    Button(page2, text = "Submit °F Value To °C", command = lambda : enterDegree(2), fg = "white", bg = "black").pack()
    Button(page2, text = "Submit °K Value To °C", command = lambda : enterDegree(3), fg = "white", bg = "black").pack()
    Button(page2, text = "Submit °C Value To °K", command = lambda : enterDegree(4), fg = "white", bg = "black").pack()
    '''tk.Radiobutton(mGUI, text="Python", padx = 20, variable=v, value=1).pack(anchor=tk.W)'''


#Function called when button pressed to enter word (page3)
def enterWord(event = None):
    wordDef = ((str(dictionary(getWord.get())).strip('[]'))).strip("''")
    if(wordDef == "Not found in dictionary."):
        newLabel(wordDef, page3)
    else:
        newLabel(getWord.get() + " = " + wordDef, page3)
    print(wordDef)
    print(getWord.get())

#Creates input field/labels/buttons for word input (page3)
def wordInput():
    newLabel("Word: ", page3)
    Entry(page3, textvariable = getWord).pack()
    WI = Button(page3, text = "Submit Word", command = enterWord, fg = "white", bg = "black")
    WI.pack()



#Works good enough
def mainCalc():
    Button(page4, text = "Open Calculator", command = startCalc, fg = "white", bg = "black").pack()

#Setting up GUI (and tabs) and variables for input
mGUI = tk.Tk()
mGUI.iconbitmap('icon.ico')
nb = ttk.Notebook(mGUI)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
nb.add(page1, text = "Triangle Calculator")
nb.add(page2, text = "Degree Converter")
nb.add(page3, text = "Dictionary")
nb.add(page4, text = "Calculator")
nb.pack(expand = 1, fill = "both")

#Values if given lengths
getSide1 = IntVar()
getSide2 = IntVar()
getSide3 = IntVar()

#Values if given points
getx1 = IntVar()
gety1 = IntVar()
getx2 = IntVar()
gety2 = IntVar()
getx3 = IntVar()
gety3 = IntVar()

#Values for degree conversion
getC = IntVar()
getF = IntVar()

#Values for Dictionary
getWord = StringVar()

#Run functions to display in window
lengthInput()
pointInput()
degreeInput()
wordInput()
mainCalc()

mGUI.bind('<Return>', enterWord)

#Run/setup GUI
mGUI.geometry("600x900")
mGUI.configure(background="green")
mGUI.title("A bunch of things that seem useful")
mGUI.mainloop()
