import tkinter as tk #GUI library
from datetime import date


window = tk.Tk()
window.title("Revision planner")

Subject_entries = []
date = date.today()


def clearGUI():
    print("Clear gui")
    for widget in window.winfo_children():
        widget.destroy()





def getGeneralInputs():
    clearGUI()
    print("Get General inputs")

    input_var = tk.StringVar() #creates empty string variable
    question_prompt = tk.Message(window, text="How many subjects do you take?")
    number_of_subjects = tk.Entry(window, textvariable=input_var)

    question_prompt.pack()
    number_of_subjects.pack()

    def submit(number_of_subjects):
        number_of_subjects = int(input_var.get())
        subject_class_handling(number_of_subjects)

    Submit_Button = tk.Button(window, text="Submit", command=lambda: submit(number_of_subjects))
    Submit_Button.pack()





class subject:
    def __init__(self,name):
        self.name = name
        self.string = tk.StringVar()  # Creates empty string variable so input is not type entry

    def tasks_input(self):
        clearGUI()


    def deadline_input(self):
        clearGUI()


        self.question_prompt = tk.Message(window, text="Please enter how many days until your test")
        self.deadline = tk.Entry(window, textvariable=self.string)
        self.submit = tk.Button(window, text="Submit", command=self.tasks_input)

        self.question_prompt.pack()
        self.deadline.pack()
        self.submit.pack()

        #self.deadline = int(self.string.get())








def subject_class_handling(number_of_subjects):
    counter = 0
    subjects = [""] * number_of_subjects

    def create_class(subject_name,counter):
        subjects[counter] = subject(subject_name)
        print("Create class")
        subjects[counter].deadline_input()

    def new_class():
        if counter < number_of_subjects:
            clearGUI()
            question_prompt = tk.Message(window, text=f"What is the name of subject {counter+1}?")
            subject_name = tk.Entry(window)
            submit = tk.Button(window, text="Submit", command=lambda: create_class(subject_name,counter))

            question_prompt.pack()
            subject_name.pack()
            submit.pack()

    new_class()

def controlFunction(): #Main function which calls other functions
    getGeneralInputs()


controlFunction()
window.mainloop()