import tkinter as tk

def create_widgets():
    label1 = tk.Label(window, text="Widget 1")
    label1.grid(row=0, column=0)

    label2 = tk.Label(window, text="Widget 2")
    label2.grid(row=1, column=0)

    label3 = tk.Label(window, text="Widget 2")
    label3.grid(row=0, column=1)

window = tk.Tk()
window.title("Widgets Below Each Other")

create_widgets()

window.mainloop()