import tkinter as tk #GUI library
import tkinter.ttk as ttk
from datetime import date


window = tk.Tk()
window.title("Revision planner")
window.geometry("500x500")

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
        self.task_counter = 0  #For rest of values, creates empty lists, variables etc.
        self.task_names = []
        self.task_values = []


    def class_input(self):
        clearGUI()

        #Title
        self.heading = tk.Message(window, text=self.name)
        self.line_seperator = ttk.Separator(window, orient="horizontal")

        #Deadline input
        self.question_prompt1 = tk.Message(window, text="Days until test")
        self.deadline = tk.Entry(window, textvariable=self.string)

        #Tasks input
        self.task_heading = tk.Message(window, text="Tasks")

        def tasks_add():
            task_grid = tk.Frame(window)
            print("task counter = ",self.task_counter)

            task_name_entry = tk.Entry(task_grid)
            task_name_entry.grid(row=self.task_counter, column=0)
            self.task_names.append(task_name_entry)

            task_value_entry = tk.Entry(task_grid)
            task_value_entry.grid(row=self.task_counter, column=1)
            self.task_values.append(task_value_entry)

            self.task_counter += 1

            task_grid.pack()
            pack_widgets()


        self.add_task = tk.Button(window, text="+", command=tasks_add)

        print("pack all widgets")

        def pack_widgets():
            self.heading.pack()
            self.line_seperator.pack(fill="x")
            self.question_prompt1.pack()
            self.deadline.pack()
            self.task_heading.pack()
            self.add_task.pack()

        pack_widgets()

    def deadline_input(self):
        clearGUI()



        self.submit = tk.Button(window, text="Submit", command=self.tasks_input)

        self.question_prompt.pack()
        self.deadline.pack()
        self.submit.pack()

        #self.deadline = int(self.string.get())


    def tasks_input(self):
        clearGUI()








def subject_class_handling(number_of_subjects):
    counter = 0
    subjects = [""] * number_of_subjects

    def create_class(subject_name,counter):
        subjects[counter] = subject(subject_name)
        print("Create class")
        subjects[counter].class_input()

    def new_class():
        if counter < number_of_subjects:
            clearGUI()
            question_prompt = tk.Message(window, text=f"What is the name of subject {counter+1}?")
            subject_name = tk.Entry(window)
            submit = tk.Button(window, text="Submit", command=lambda: create_class(subject_name.get(),counter))

            question_prompt.pack()
            subject_name.pack()
            submit.pack()

    new_class()

def controlFunction(): #Main function which calls other functions
    getGeneralInputs()


controlFunction()
window.mainloop()