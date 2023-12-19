import tkinter as tk

def existing_code(name):
    # Your existing Python code here
    result = f"Hello, {name}! Welcome to Tkinter."
    return result

def on_button_click():
    user_input = entry.get()
    result = existing_code(user_input)
    label.config(text=result)

# Create the main application window
root = tk.Tk()
root.title("Integrate Tkinter with Existing Code")

# Create a label widget
label = tk.Label(root, text="Enter your name:")

# Create an entry widget for text input
userInput = tk.Entry(root)

# Create a button widget
button = tk.Button(root, text="Submit", command=on_button_click)

# Pack the widgets into the window
label.pack()
userInput.pack()
button.pack()

# Start the Tkinter event loop
root.mainloop()
