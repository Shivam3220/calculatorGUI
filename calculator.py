from tkinter import *


# calculator functions
def userInteractWithNumbers(e):
    previousEntery=labelVar.get()
    labelVar.set(previousEntery+e)

def userInteractWithBackButton(e):
    previousEntery=labelVar.get()
    previousEntery=previousEntery[:-1]
    labelVar.set(previousEntery)

def userInteractWithOperator(e):
    previousEntery=labelVar.get()
    if e=="C":
        previousEntery=""
        labelVar.set(previousEntery)
    elif e=="%":
        previousEntery=eval((previousEntery)+"/100")
        labelVar.set(str(previousEntery)+"*")
    elif e=="=":    
        labelVar.set(eval(previousEntery))
    else:
        labelVar.set(previousEntery+e)



# main window of the calculator
window=Tk()
window.minsize(width=200, height=300)
window.maxsize(width=200, height=300)

labelVar=StringVar()

# first frame where we enter input and se output (screen of calculator)
inputFrame= Frame(window)
inputLabel=Label(inputFrame,textvariable=labelVar,font="bold 16",pady=3, height=2).pack(side=RIGHT)
inputFrame.pack(fill=X)

# digit frame of the calculator
digitFrame= Frame(window,height=90)

# first line of the entry frame
numberFrame=Frame(digitFrame)
# buttons of the first line
backButton= Button(numberFrame, text="<", padx=4,  font="bold 16",command=lambda:userInteractWithBackButton("<")).grid(row=0,column=0, padx=2)
clearButton= Button(numberFrame, text="C",  padx=4,  font="bold 16",command=lambda:userInteractWithOperator("C")).grid(row=0,column=1, padx=2)
percentageButton= Button(numberFrame, text="%",  padx=3,  font="bold 16",command=lambda:userInteractWithOperator("%")).grid(row=0,column=2, padx=2)
divideButton= Button(numberFrame, text="/", padx=14,  font="bold 16",command=lambda:userInteractWithOperator("/")).grid(row=0,column=3, padx=2)
numberFrame.pack(fill=X,pady=2)


# second line of the entry frame
numberFrame=Frame(digitFrame)
# buttons of the first line
num_7= Button(numberFrame, text="7", padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("7")).grid(row=0,column=0, padx=2)
num_8= Button(numberFrame, text="8",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("8")).grid(row=0,column=1, padx=2)
num_9= Button(numberFrame, text="9",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("9")).grid(row=0,column=2, padx=2)
multiplyButton= Button(numberFrame, text="X", padx=11,  font="bold 16",command=lambda:userInteractWithOperator("*")).grid(row=0,column=3, padx=2)
numberFrame.pack(fill=X,pady=2)


# third line of the entry frame
numberFrame=Frame(digitFrame)
# buttons of the first line
num_4= Button(numberFrame, text="4", padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("4")).grid(row=0,column=0, padx=2)
num_5= Button(numberFrame, text="5",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("5")).grid(row=0,column=1, padx=2)
num_6= Button(numberFrame, text="6",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("6")).grid(row=0,column=2, padx=2)
subtractButton= Button(numberFrame, text="-", padx=14,  font="bold 16",command=lambda:userInteractWithOperator("-")).grid(row=0,column=3, padx=2)
numberFrame.pack(fill=X,pady=2)


# forth line of the entry frame
numberFrame=Frame(digitFrame)
# buttons of the first line
num_1= Button(numberFrame, text="1", padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("1")).grid(row=0,column=0, padx=2)
num_2= Button(numberFrame, text="2",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("2")).grid(row=0,column=1, padx=2)
num_3= Button(numberFrame, text="3",  padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("3")).grid(row=0,column=2, padx=2)
addButton= Button(numberFrame, text="+", padx=12,  font="bold 16",command=lambda:userInteractWithOperator("+")).grid(row=0,column=3, padx=2)
numberFrame.pack(fill=X,pady=2)

# fifth line of the entry frame
numberFrame=Frame(digitFrame)
# buttons of the first line
num_0= Button(numberFrame, text="0", padx=5,  font="bold 16",command=lambda:userInteractWithNumbers("0")).grid(row=0,column=0, padx=2)
num_00= Button(numberFrame, text="00",  padx=0,  font="bold 16",command=lambda:userInteractWithNumbers("00")).grid(row=0,column=1, padx=2)
decimalButton= Button(numberFrame, text=".",  padx=7,  font="bold 16",command=lambda:userInteractWithNumbers(".")).grid(row=0,column=2, padx=2)
equalToButton= Button(numberFrame, text="=", padx=12,  font="bold 16",command=lambda:userInteractWithOperator("=")).grid(row=0,column=3, padx=2)
numberFrame.pack(fill=X,pady=2)


digitFrame.pack(fill=BOTH,expand=True,padx=8)



window.mainloop()
