import tkinter as tk

# Create a simple window
root = tk.Tk()
root.title("My First Tkinter App")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Start the Tkinter event loop
root.mainloop()