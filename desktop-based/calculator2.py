import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Shahbaz's Calculator")

# Create an entry widget for displaying the input/output
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define a function to handle button clicks
def button_click(char):
    """Appends the clicked character to the entry widget."""
    current = entry.get()  # Get the current text in the entry
    entry.delete(0, tk.END)  # Clear the entry
    entry.insert(0, current + char)  # Insert the new text
    
    
def clear():
    """Clears the entry widget."""
    entry.delete(0, tk.END)
    
    
def equal():
    """Evaluates the expression in the entry widget and displays the result."""
    expression = entry.get() # Get expression from entry
    result = eval(expression) # Evaluate it using eval(). Be mindful of security risks with eval() in real-world apps.
    entry.delete(0, tk.END) # Clear Entry
    entry.insert(0, result) # Display result.


# Create number buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click('1'))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click('2'))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click('3'))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click('4'))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click('5'))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click('6'))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click('7'))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click('8'))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click('9'))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click('0'))

# Create operator buttons
button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click('+'))
button_sub = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click('-'))
button_mul = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click('*'))
button_div = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click('/'))

# Create control buttons
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear) # Clear Button
button_equal = tk.Button(root, text="=", padx=20, pady=20, command=equal) # Equals Button



# Place the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_div.grid(row=4, column=3)



# Start the Tkinter event loop
root.mainloop()
