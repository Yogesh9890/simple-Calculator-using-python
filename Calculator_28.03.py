from tkinter import*

def ButtonClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=" "

def btnClear():
    global operator
    operator=" "
    text_Input.set("")
    

cal = Tk()
cal.title ("Calculator")
operator = " "
text_Input = StringVar()

textdisplay = Entry(cal, font=('Chilanka', 20, 'bold'), textvariable=text_Input, bg="powder blue", justify='right').grid(columnspan=4)

#=====================

btn7= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "7", bg="powder blue", justify='right', command=lambda:ButtonClick(7)).grid(column=0,row=2)

btn8= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "8", bg="powder blue", justify='right', command=lambda:ButtonClick(8)).grid(column=1,row=2)

btn9= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "9", bg="powder blue", justify='right', command=lambda:ButtonClick(9)).grid(column=2,row=2)

btnDivision= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "/", bg="powder blue", justify='right', command=lambda:ButtonClick("/")).grid(column=3,row= 2)

#=====================

btn4= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "4", bg="powder blue", justify='right', command=lambda:ButtonClick(4)).grid(column=0,row=3)

btn5= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "5", bg="powder blue", justify='right', command=lambda:ButtonClick(5)).grid(column=1,row=3)

btn6= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "6", bg="powder blue", justify='right', command=lambda:ButtonClick(6)).grid(column=2,row=3)

btnMultiplication= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "*", bg="powder blue", justify='right', command=lambda:ButtonClick("*")).grid(column=3,row=3)

#=====================

btn1= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "1", bg="powder blue", justify='right', command=lambda:ButtonClick(1)).grid(column=0,row=4)

btn2= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "2", bg="powder blue", justify='right', command=lambda:ButtonClick(2)).grid(column=1,row=4)

btn3= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "3", bg="powder blue", justify='right', command=lambda:ButtonClick(3)).grid(column=2,row=4)

btnSubtraction= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "-", bg="powder blue", justify='right', command=lambda:ButtonClick("-")).grid(column=3,row= 4)

#=====================

btn0= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "0", bg="powder blue", justify='right', command=lambda:ButtonClick(0)).grid(column=0,row=5)

btnClear= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "C", bg="powder blue", justify='right', command =btnClear).grid(column=1,row=5)

btnEqualsTo= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "=", bg="powder blue", justify='right',command = btnEquals).grid(column=2,row=5)

btnAddition= Button(cal, padx= 8, pady= 8, bd= 8, fg= "Black", font=('Chilanka', 20, 'bold'), text= "+", bg="powder blue", justify='right', command=lambda:ButtonClick("+")).grid(column=3,row=5)

#=====================

cal.mainloop()

