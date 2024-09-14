Overview
The Enhanced Calculator is a feature-rich desktop application built using Python's tkinter library. It provides a comprehensive calculator experience with support for basic arithmetic operations, square root calculations, exponentiation, and a history feature. The application also includes a light/dark theme toggle and handles keyboard input for added convenience.

Features
Basic Arithmetic Operations: Supports addition, subtraction, multiplication, and division.
Advanced Functions: Includes square root and power operations.
History: Tracks the last five calculations and allows users to view their calculation history.
Keyboard Input: Users can perform calculations using keyboard input.
Theme Toggle: Switch between dark and light themes for a personalized interface.
Error Handling: Displays error messages for invalid operations and zero division errors.
Interface:
Use the buttons to perform calculations.
Click "History" to view the last five calculations.
Click "Theme" to toggle between dark and light themes.
Use the keyboard for input and shortcuts.
Code Explanation
Imports:

tkinter for the GUI elements.
math for advanced mathematical operations.
Main Window Configuration:

The window is created and configured with a specific title, size, and background color.
Global Variables:

equation: Holds the current input or result.
history: Stores the last five calculations.
Functions:

show(value): Appends a character to the equation and updates the display.
clear(): Clears the current equation.
clear_last_entry(): Removes the last character from the equation.
calculate(): Evaluates the equation and handles errors.
show_history(): Displays the history of calculations in a new window.
sqrt_operation(): Computes the square root of the current equation.
power_operation(): Appends the power operator to the equation.
key_event_handler(event): Handles keyboard input for calculations.
toggle_theme(): Switches between dark and light themes.
Button Layout:

Buttons for digits, operations, and special functions are laid out in a grid format.
Special buttons include "C", "CE", "=" for clear operations and calculation, and "√", "^" for advanced functions.
Event Binding:

Keyboard events are bound to the key_event_handler function for seamless integration with keyboard input.
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements. Contributions are welcome!
