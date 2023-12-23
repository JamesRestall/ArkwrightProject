import tkinter as tk #imports GUI library
import tkinter.ttk as ttk
from datetime import date


window = tk.Tk() #Creates window
window.title("Revision planner") #Sets title of the window
window.geometry("500x500") #Sets size of window


#creating empty arrays and variables for later
Subject_entries = []
date = date.today()
subject_number = 0
subjects = []



def clearGUI(): #Destroys all widgets in the gui
    print("Clear gui")
    for widget in window.winfo_children():
        widget.destroy()




def getGeneralInputs():
    clearGUI()
    print("Get General inputs")

    input_var = tk.StringVar() #creates empty string variable
    question_prompt = tk.Message(window, text="How many subjects do you take?") #Creates message widget with text"How many subhjects do you take?"
    number_of_subjects_entry = tk.Entry(window, textvariable=input_var) #Creates an input field in the window with the answer being assigned to the input_var variable

    question_prompt.pack() #Formats the widgets
    number_of_subjects_entry.pack()

    def submit():
        global number_of_subjects #makes the number_of_subjects global (any code in the program can access it)
        number_of_subjects = int(input_var.get()) #assigns the integer value of the input_var entry variable to number_of_subjects
        subject_class_handling(True)

    Submit_Button = tk.Button(window, text="Submit", command=submit) #Creates a button, that when clicked runs the submit function
    Submit_Button.pack()





class subject:
    def __init__(self,name): #Constructor, runs every time the class is created, I've used it to assign the empty arrays and pass in the parameter and set it to the class
        self.name = name
        self.string = tk.StringVar()  # Creates empty string variable so input is not type entry

        #For rest of values, creates empty lists, variables etc.
        self.task_names = []
        self.task_values = []
        self.task_times = []
        self.task_counter = 0



        self.block_revision = tk.BooleanVar()


    def class_input(self):
        clearGUI()

        deadline = tk.StringVar() #Creates empty string variable so the entry field doesn't produce a variable with type entry
        task_name = tk.StringVar()
        task_value = tk.StringVar()
        task_time = tk.StringVar()
        block_revision = tk.BooleanVar()

        task_grid = tk.Frame(window) #Creates a frame in the window (used for the grid later, line 95))

        #Title
        heading = tk.Message(window, text=f"{self.name} inputs")
        line_seperator1 = ttk.Separator(window, orient="horizontal") #Used to create a line which in this case goes horizontal

        #Deadline input
        question_prompt1 = tk.Message(window, text="Days until test")
        deadline_entry = tk.Entry(window, textvariable=deadline)
        line_seperator2 = ttk.Separator(window, orient="horizontal")

        #Tasks input
        task_heading = tk.Message(window, text="Tasks")

        task_name_heading = tk.Message(task_grid, text="Name")
        task_name_heading.grid(row=0, column=0)

        task_values_heading = tk.Message(task_grid, text="Count")
        task_values_heading.grid(row=0, column=1)

        task_times_heading = tk.Message(task_grid, text="Time(mins)")
        task_times_heading.grid(row=0, column=2)

        def tasks_add(): #Adds a row to the task grid

            print("task counter = ", self.task_counter)

            task_name_entry = tk.Entry(task_grid, textvariable=tk.StringVar()) #Creates entry
            task_name_entry.grid(row=(self.task_counter)+1, column=0) #Positions the entry on another row in the first column
            self.task_names.append(task_name_entry)

            task_value_entry = tk.Entry(task_grid, textvariable=tk.StringVar())
            task_value_entry.grid(row=(self.task_counter)+1, column=1) #position in the second column
            self.task_values.append(task_value_entry)

            task_time_entry = tk.Entry(task_grid, textvariable=tk.StringVar())
            task_time_entry.grid(row=(self.task_counter)+1, column=2) #positions in the third column
            self.task_times.append(task_time_entry)

            pack_widgets(task_grid)

            self.task_counter += 1





        add_task = tk.Button(window, text="+", command=tasks_add) #Creates a button when pressed executes tasks_add function
        line_seperator3 = ttk.Separator(window, orient="horizontal")


        #Way of going through tasks
        block_revision_radio = tk.Radiobutton(window, text="Block revision (Complete all of one task before starting the next task)", variable=block_revision, value=True) #Creates choices which set the self.block_revision variable true or false
        mixed_revision_radio = tk.Radiobutton(window, text="Mixed revision (Go between different tasks. Start multiple tasks before finishing one)", variable=block_revision, value=False)
        line_seperator4 = ttk.Separator(window, orient="horizontal")

        #Submit button
        def submit():
            clearGUI()
            print(deadline.get())

            #Assigns all the entry values into a class specific variable
            self.deadline = int(deadline.get())  # Converts deadline entry into integer
            self.task_name = task_name.get()
            self.task_value = task_value.get()
            self.task_time = task_time.get()
            self.block_revision = block_revision.get()




            subject_class_handling(False)



        submit_button = tk.Button(window, text="Submit", command=submit) #Button that when clicked executes submit function

        def pack_widgets(task_grid): #formats all the widgets
            heading.pack()
            line_seperator1.pack(fill="x")
            question_prompt1.pack()
            deadline_entry.pack()
            line_seperator2.pack(fill="x")
            task_heading.pack()


            task_grid.pack()
            add_task.pack()
            line_seperator3.pack(fill="x")

            block_revision_radio.pack()
            mixed_revision_radio.pack()

            line_seperator4.pack(fill="x")
            submit_button.pack()


        pack_widgets(task_grid)


















def subject_class_handling(list_setup):

    if list_setup:
        print("Number of subjects = ", number_of_subjects)


    def create_class(subject_name, subject_number):
        print(subjects)
        print(subject_number)
        subject_class = subject(subject_name)
        subjects.append(subject_class) #Creates class subject with name subject_name in list subjects at index subject_number - 1
        print("Create class")
        subjects[subject_number-1].class_input() #Executes class_input function in the function

    def new_class():
        global subject_number
        if subject_number < number_of_subjects:
            subject_number += 1
            print("Subject_number = ", subject_number)
            clearGUI()
            question_prompt = tk.Message(window, text=f"What is the name of subject {subject_number}?")
            subject_name = tk.Entry(window)
            submit = tk.Button(window, text="Submit", command=lambda: create_class(subject_name.get(), subject_number))

            question_prompt.pack()
            subject_name.pack()
            submit.pack()
        else:
            display_outputs(subjects)


    new_class()



def display_outputs(subjects):
    print("Display outputs")
    for i in range(len(subjects)):
        print(subjects[i].block_revision)

    def pre_display_gui():
        clearGUI()
        values_text = ["Deadline (days)", ""]
        task_rows = 0

        pre_display_message = tk.Message(window, text="Check subject values")
        pre_display_message.pack()

        title_seperator = ttk.Separator(window, orient="horizontal")
        title_seperator.pack(fill="x") #Formats the separator so that it fills the entire x axis (horizontal)

        grid = tk.Frame(window)


        subject_title_name = tk.Message(grid, text="Name")
        subject_title_name.grid(row=1, column=0)

        subject_title_deadline = tk.Message(grid, text="Deadline (days)")
        subject_title_deadline.grid(row=2, column=0)


        for i in range(number_of_subjects): #loops for each subject (column) creates grid with inputted values
            grid_headings = tk.Message(grid, text=f"Subject {i+1}")
            grid_headings.grid(row=0, column=i+1)

            subject_name = tk.Message(grid, text=subjects[i].name)
            subject_name.grid(row=1, column=i+1)

            subject_deadline = tk.Message(grid, text=subjects[i].deadline)
            subject_deadline.grid(row=2, column=i+1)

            for i in range(len(subjects[i].task_names)):
                print("Task names")
                try: #Trys to run this code
                    if subjects[i].task_names[i]:
                        print(subjects[i].task_names[i])

                    if i >= task_rows:
                        task_rows += 1  # Increments task_rows by 1 so that the maximum number of rows is correct and doesn't ruin formatting
                        task_name_entry = tk.Message(grid, text=subjects[i].task_names[i])
                        task_name_entry.grid(row=i+2, column=i+1)

                except: #Runs this code if the try code (256) fails

                        print("No more tasks")
                        task_name_entry = tk.Message(grid, text="")
                        task_name_entry.grid(row=i + 2, column=i + 1)



        grid.pack()

    pre_display_gui()

def controlFunction(): #Main function which calls other functions
    getGeneralInputs()


controlFunction()
window.mainloop()