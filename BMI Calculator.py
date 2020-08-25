from tkinter import *

root = Tk()

#Logic 
def done():
    top = Toplevel()
    top.title("Result")
    top.geometry("650x70")
    top.minsize(650,70)
    top.maxsize(650,70)

    a = weight.get()
    b = height.get()

    if 18.5 >= a / (b * b):
        Label(top , text = "You are UNDERWEIGHT!!" , font="lucida 15 bold").pack()
        Label(top , text = "You should eat 'HEALTHY INGREDIENTS'" , font="lucida 15 bold").pack()
    
    elif a / (b * b) >= 25:
        Label(top , text = "You are OVERWEIGHT!!" , font="lucida 15 bold").pack()
        Label(top , text = "You should EXIRCISE daily and eat 'HEALTHY INGREDIENTS only'" , font="lucida 15 bold").pack()
    
    elif a / (b * b) > 18.5 and a / (b * b) < 25:
        Label(top , text = "You are HEALTHY!!" , font="lucida 15 bold").pack()
        Label(top , text = "GOOD!! Maintain this weight" , font="lucida 15 bold").pack()

#Displaying a window of 500x500 with a title BMI CALCULATOR
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.title("BMI CALCULATOR")

#Displaying BMI Calculator
Label(root, text="BMI Calculator" , pady=20 , padx=20, font="lucida 50 bold" , bg="pink").pack(pady=10)

#Height & Weight
Label(root , text="Height in metres" , font="comicsansms 15 italic").pack(anchor=W,pady=25)

height = DoubleVar()
heighte = Entry(root ,textvariable = height)
heighte.pack(anchor=W, padx=10)

Label(root , text="Weight in kgs" , font="comicsansms 15 italic").pack(anchor=W,pady=25)

weight = IntVar()
weighte = Entry(root ,textvariable = weight)
weighte.pack(anchor=W, padx=10)

Button(root,text="SUBMIT",command=done).pack(pady=50)

root.mainloop()