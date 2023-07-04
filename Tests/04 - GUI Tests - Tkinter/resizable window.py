# Tkinter hello world with a resizable window and interactive buttons

import tkinter as tk

root = tk.Tk() # Create the window

root.title("Hello World!") # Set the title of the window
root.geometry("400x300") # Set the size of the window

label = tk.Label(root, text="Hello World!") # Create a label with the text "Hello World!"
label.pack() # Pack the label into the window



# Functionality for the button to make it print a message into the console
def button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click me!") # Create a button with the text "Click me!"
button.config(command=button_click) # Set the command of the button to the function button_click
button.pack() # Pack the button into the window

root.mainloop()
