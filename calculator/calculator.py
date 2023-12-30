#!/usr/bin/python3

from tkinter import Tk, Entry, Button, StringVar

# Define the Calculator class
class Calculator:
    def __init__(self, master):
        # Set up the main window
        master.title("Calculator")
        master.geometry('357x420+0+0')  # Set window size and position
        master.config(bg='gray')
        master.resizable(False, False)  # Disable window resizing

        # Initialize variables
        self.equation = StringVar()
        self.entry_value = ''

        # Create the entry widget for displaying the equation
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Create number and operator buttons
        Button(master, text='1', command=lambda: self.show(1)).place(x=0, y=100)
        Button(master, text='2', command=lambda: self.show(2)).place(x=70, y=100)
        Button(master, text='3', command=lambda: self.show(3)).place(x=140, y=100)
        Button(master, text='+', command=lambda: self.show('+')).place(x=210, y=100)
        Button(master, text='4', command=lambda: self.show(4)).place(x=0, y=170)
        Button(master, text='5', command=lambda: self.show(5)).place(x=70, y=170)
        Button(master, text='6', command=lambda: self.show(6)).place(x=140, y=170)
        Button(master, text='-', command=lambda: self.show('-')).place(x=210, y=170)
        Button(master, text='7', command=lambda: self.show(7)).place(x=0, y=240)
        Button(master, text='8', command=lambda: self.show(8)).place(x=70, y=240)
        Button(master, text='9', command=lambda: self.show(9)).place(x=140, y=240)
        Button(master, text='*', command=lambda: self.show('*')).place(x=210, y=240)
        Button(master, text='C', command=self.clear).place(x=0, y=310)
        Button(master, text='0', command=lambda: self.show(0)).place(x=70, y=310)
        Button(master, text='=', command=self.solve).place(x=140, y=310)
        Button(master, text='/', command=lambda: self.show('/')).place(x=210, y=310)

    # Method to update the equation display with a value
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    # Method to clear the equation
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    # Method to evaluate and display the result
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")


# Create the main Tkinter window
root = Tk()

# Create an instance of the Calculator class
calculator = Calculator(root)

# Start the Tkinter event loop
root.mainloop()
