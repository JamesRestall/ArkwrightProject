import tkinter as tk #GUI library
import tkinter.ttk as ttk
from datetime import date


window = tk.Tk()
window.title("Revision planner")
window.geometry("500x500")

Subject_entries = []
date = date.today()
subject_number = 0




def clearGUI():
    print("Clear gui")
    for widget in window.winfo_children():
        widget.destroy()




def getGeneralInputs():
    clearGUI()
    print("Get General inputs")

    input_var = tk.StringVar() #creates empty string variable
    question_prompt = tk.Message(window, text="How many subjects do you take?")
    number_of_subjects_entry = tk.Entry(window, textvariable=input_var)

    question_prompt.pack()
    number_of_subjects_entry.pack()

    def submit():
        global number_of_subjects
        number_of_subjects = int(input_var.get())
        subject_class_handling()

    Submit_Button = tk.Button(window, text="Submit", command=submit)
    Submit_Button.pack()





class subject:
    def __init__(self,name):
        self.name = name
        self.string = tk.StringVar()  # Creates empty string variable so input is not type entry
        self.task_counter = 0  #For rest of values, creates empty lists, variables etc.
        self.task_names = []
        self.task_values = []
        self.task_times = []

        self.block_revision = tk.BooleanVar()


    def class_input(self):
        clearGUI()
        task_grid = tk.Frame(window)

        #Title
        self.heading = tk.Message(window, text=self.name)
        self.line_seperator = ttk.Separator(window, orient="horizontal")

        #Deadline input
        self.question_prompt1 = tk.Message(window, text="Days until test")
        self.deadline = tk.Entry(window, textvariable=self.string)

        #Tasks input
        self.task_heading = tk.Message(window, text="Tasks")

        self.task_name_heading = tk.Message(task_grid, text="Name")
        self.task_name_heading.grid(row=0, column=0)

        self.task_values_heading = tk.Message(task_grid, text="Count")
        self.task_values_heading.grid(row=0, column=1)

        self.task_times_heading = tk.Message(task_grid, text="Time(mins)")
        self.task_times_heading.grid(row=0, column=2)

        def tasks_add(): #Adds a row to the task grid

            print("task counter = ", self.task_counter)

            task_name_entry = tk.Entry(task_grid) #Creates entry
            task_name_entry.grid(row=(self.task_counter)+1, column=0) #Positions the entry on another row in the first column
            self.task_names.append(task_name_entry)

            task_value_entry = tk.Entry(task_grid)
            task_value_entry.grid(row=(self.task_counter)+1, column=1) #position in the second column
            self.task_values.append(task_value_entry)

            task_time_entry = tk.Entry(task_grid)
            task_time_entry.grid(row=(self.task_counter)+1, column=2) #poisitions in the third column
            self.task_times.append(task_time_entry)

            self.task_counter += 1 #increments task counter

            pack_widgets(task_grid)


        self.add_task = tk.Button(window, text="+", command=tasks_add) #Creates a button when pressed executes tasks_add function


        #Way of going through tasks
        block_revision_radio = tk.Radiobutton(window, text="Block revision (Complete all of one task before starting the next task)", variable=self.block_revision, value=True) #Creates choices which set the self.block_revision variable true or false
        mixed_revision_radio = tk.Radiobutton(window, text="Mixed revision (Go between different tasks. Start multiple tasks before finishing one)", variable=self.block_revision, value=False)


        #Submit button
        def submit():
            clearGUI()
            subject_class_handling()

        submit_button = tk.Button(window, text="Submit", command=submit) #Button that when clicked executes submit function

        def pack_widgets(task_grid):
            self.heading.pack()
            self.line_seperator.pack(fill="x")
            self.question_prompt1.pack()
            self.deadline.pack()
            self.line_seperator.pack(fill="x")
            self.task_heading.pack()


            task_grid.pack()
            self.add_task.pack()
            block_revision_radio.pack()
            mixed_revision_radio.pack()
            submit_button.pack()

        pack_widgets(task_grid)


















def subject_class_handling():
    subjects = [""] * number_of_subjects

    def create_class(subject_name, subject_number):
        subjects[subject_number] = subject(subject_name)
        print("Create class")
        subjects[subject_number].class_input()

    def new_class():
        global subject_number
        if subject_number < number_of_subjects:
            subject_number += 1
            print("Subject_number = ",subject_number)
            clearGUI()
            question_prompt = tk.Message(window, text=f"What is the name of subject {subject_number}?")
            subject_name = tk.Entry(window)
            submit = tk.Button(window, text="Submit", command=lambda: create_class(subject_name.get(),subject_number))

            question_prompt.pack()
            subject_name.pack()
            submit.pack()
        else:
            display_outputs()


    new_class()



def display_outputs():
    print("Display outputs")


def controlFunction(): #Main function which calls other functions
    getGeneralInputs()


controlFunction()
window.mainloop()