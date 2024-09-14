import tkinter as tk
from tkinter import *
import math

root = Tk()  
root.title("Enhanced Calculator")
root.geometry("570x700+100+200") 

# Configure the window background color
root.configure(bg="#16325B")

equation = ""
history = []

# Function to update the equation when a button is clicked
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

# Function to clear the equation
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

# Function to clear last entry (CE)
def clear_last_entry():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

# Function to calculate the equation
def calculate():
    global equation, history
    try:
        result = str(eval(equation))  
        history.append(f"{equation} = {result}")
        if len(history) > 5: 
            history.pop(0)
        label_result.config(text=result)
        equation = result  
    except ZeroDivisionError:
        label_result.config(text="Cannot divide by zero")
        equation = ""
    except:
        label_result.config(text="Syntax Error")
        equation = ""  

# Function to show calculation history
def show_history():
    history_window = Toplevel(root)
    history_window.title("Calculation History")
    for idx, h in enumerate(history):
        Label(history_window, text=h, font=("arial", 14)).pack()

# Function for square root operation
def sqrt_operation():
    global equation
    try:
        result = str(math.sqrt(float(equation)))
        label_result.config(text=result)
        equation = result
    except:
        label_result.config(text="Error")
        equation = ""

# Function for power operation
def power_operation():
    global equation
    equation += "**"  # Power operation in Python
    label_result.config(text=equation)

# Function to handle keyboard input
def key_event_handler(event):
    key = event.char
    if key.isdigit() or key in "+-*/%.":
        show(key)
    elif key == '\r':  # Enter key for equal
        calculate()
    elif key == '\x08':  # Backspace key for clearing
        clear()

# Function to toggle between dark and light themes
def toggle_theme():
    current_bg = root.cget("bg")
    if current_bg == "#16325B":  # Dark mode
        root.configure(bg="#ffffff")
        label_result.configure(bg="#ffffff", fg="#000000")
        # Update button colors for light mode
    else:  # Light mode
        root.configure(bg="#16325B")
        label_result.configure(bg="#ffffff", fg="#000000")
        # Update button colors for dark mode

# Label to show results
label_result = Label(root, width=25, height=2, text="", font=("arial", 30), bg="#ffffff")
label_result.pack(pady=20)

# Button layout for the calculator
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#0B2F9F", command=clear).place(x=10, y=100)
Button(root, text="CE", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#0B2F9F", command=clear_last_entry).place(x=150, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("/")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#FEAE6F", command=calculate).place(x=430, y=400)

Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show("0")).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=lambda: show(".")).place(x=290, y=500)

# Adding sqrt and power buttons
Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=sqrt_operation).place(x=10, y=600)
Button(root, text="^", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=power_operation).place(x=150, y=600)

# History and Theme buttons
Button(root, text="History", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=show_history).place(x=290, y=600)
Button(root, text="Theme", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#55679C", command=toggle_theme).place(x=430, y=600)

# Prevent window from being resized
root.resizable(False, False)

# Bind the keypress event to the handler for keyboard input
root.bind("<Key>", key_event_handler)

# Main event loop
root.mainloop()
