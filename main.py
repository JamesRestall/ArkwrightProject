# noinspection PyInterpreter
import tkinter as tk #imports GUI library
import tkinter.ttk as ttk



window = tk.Tk() #Creates window
window.title("Revision planner") #Sets title of the window
window.geometry("500x500") #Sets size of window


#creating empty arrays and variables for later
global subjects
global subject_number
Subject_entries = []
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
        setup_new_classes(True,0)

    Submit_Button = tk.Button(window, text="Submit", command=submit) #Creates a button, that when clicked runs the submit function
    Submit_Button.pack()


def setup_new_classes(list_setup,subject_number):

    #if list_setup:
        #print("Number of subjects = ", number_of_subjects)


    subject_number += 1

    def new_class(subject_number):

        print(subject_number)
        if subject_number <= number_of_subjects:

            print("Subject_number = ", subject_number)
            clearGUI()
            question_prompt = tk.Message(window, text=f"What is the name of subject {subject_number}?")
            subject_name = tk.Entry(window)
            submit = tk.Button(window, text="Submit", command=lambda: create_class(subject_name.get(), subject_number))

            question_prompt.pack()
            subject_name.pack()
            submit.pack()
        else:
            display_inputs()

    def create_class(subject_name, subject_number):

        print(subjects)
        print("subject_number: ",subject_number)
        subject_class = subject_instance(subject_name)
        subjects.append(subject_class) # Creates class subject with name subject_name in list subjects at index subject_number - 1
        print("Create class")
        subjects[subject_number-1].class_input(subject_number) #Executes class_input function in the function




    new_class(subject_number)

def display_inputs():
    print("Display outputs")
    for i in range(len(subjects)):
        print(subjects[i].block_revision)


    clearGUI()
    values_text = ["Deadline (days)", ""]
    max_task_rows = 3



    pre_display_message = tk.Message(window, text="Check subject values")
    pre_display_message.pack()

    title_seperator = ttk.Separator(window, orient="horizontal")
    title_seperator.pack(fill="x") #Formats the separator so that it fills the entire x axis (horizontal)

    grid = tk.Frame(window)


    for subject in range(number_of_subjects): #loops for each subject (column) creates grid with inputted values
        print(subjects[subject].task_names)

        grid_headings = tk.Message(grid, text=f"Subject {subject+1}")
        grid_headings.grid(row=0, column=subject+1)

        subject_name = tk.Message(grid, text=subjects[subject].name)
        subject_name.grid(row=1, column=subject+1)

        subject_deadline = tk.Message(grid, text=subjects[subject].deadline)
        subject_deadline.grid(row=2, column=subject+1)

        task_number = -3


        for task in range(len(subjects[subject].task_names)):
            task_number += 3
            print("Task names")
            try: #Tries to run this code
                task_name_input = subjects[subject].task_names[task].get()  # Retreives the text from the task_name of the index of the current subject
                task_value_input = subjects[subject].task_values[task].get()
                task_time_input = subjects[subject].task_times[task].get()

                print(subjects[subject].task_names)
                print(task_name_input)
                print(task_value_input)
                print(task_time_input)

                if (task*3) > max_task_rows:
                    print("Task rows")
                    max_task_rows += 3  # Increments task_rows by 3 so that the maximum number of rows is correct and doesn't ruin formatting

                task_name_entry = tk.Message(grid, text=task_name_input)
                task_name_entry.grid(row=task_number+3, column=subject+1)
                print(task_name_input)

                task_value_entry = tk.Message(grid, text=task_value_input)
                task_value_entry.grid(row=task_number+4, column=subject+1)

                task_time_entry = tk.Message(grid, text=task_time_input)
                task_time_entry.grid(row=task_number+5, column=subject+1)


            except: #Runs this code if the try code (line 127) fails

                    print("No more tasks")
                    task_name_entry = tk.Message(grid, text="") #Creates blank widgets so the format doesn't break
                    task_name_entry.grid(row=task_number+3, column=subject + 1)


        if subjects[i].block_revision == 0:
            subject_block = tk.Message(grid, text="Mixed")
        else:
            subject_block = tk.Message(grid, text="Blocks")

        subject_block.grid(row=max_task_rows+6, column=subject+1)

        def edit_subject(subject):
            print("Subject: ", subject)
            subjects[subject].class_input(subject)


        edit_button = tk.Button(grid, text="Edit", command=lambda: edit_subject(i))
        edit_button.grid(row=max_task_rows+7, column=subject+1)


    subject_title_name = tk.Message(grid, text="Name")
    subject_title_name.grid(row=1, column=0)

    subject_title_deadline = tk.Message(grid, text="Deadline (days)")
    subject_title_deadline.grid(row=2, column=0)

    for task_row_output in range(0, max_task_rows, 3):
        side_task_name_heading = tk.Message(grid, text=f"Task{int((task_row_output / 3)) + 1} name")
        side_task_name_heading.grid(row=task_row_output + 3, column=0)

        side_task_value_heading = tk.Message(grid, text=f"Task{int((task_row_output / 3)) + 1} count")
        side_task_value_heading.grid(row=task_row_output + 4, column=0)

        side_task_time_heading = tk.Message(grid, text=f"Task{int((task_row_output / 3)) + 1} time")
        side_task_time_heading.grid(row=task_row_output + 5, column=0)

    subject_block_name = tk.Message(grid, text="Order of revision")
    subject_block_name.grid(row=(max_task_rows) + 6, column=0)


    grid.pack()

    def submit_entries():
        clearGUI()
        calculate_plan_subjects()

    submit_entries = tk.Button(window, text="Submit entries", command=submit_entries)
    submit_entries.pack()

def calculate_plan_subjects():
    for subject in range(len(subjects)):
        subjects[subject].calculate_plan()


class subject_instance:
    def __init__(self,name): #Constructor, runs every time the class is created, I've used it to assign the empty arrays and pass in the parameter and set it to the class
        self.name = name
        self.string = tk.StringVar()  # Creates empty string variable so input is not type entry

        #For rest of values, creates empty lists, variables etc.
        self.task_names = []
        self.task_values = []
        self.task_times = []
        self.task_counter = 0
        self.first_input = True
        self.total_relative_time = 0
        self.deadline = 0
        self.task_count_daily = []



        self.block_revision = tk.BooleanVar()


    def class_input(self, subject_number):
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
            task_name_value = tk.StringVar()
            task_value_value = tk.StringVar()
            task_time_value = tk.StringVar()


            print("task counter = ", self.task_counter)

            #parallel arrays
            self.task_names.append(task_name_value)
            self.task_values.append(task_value_value)
            self.task_times.append(task_time_value)

            task_name_entry = tk.Entry(task_grid, textvariable=task_name_value) #Creates entry
            task_name_entry.grid(row=(self.task_counter)+1, column=0) #Positions the entry on another row in the first column


            task_value_entry = tk.Entry(task_grid, textvariable=task_value_value)
            task_value_entry.grid(row=(self.task_counter)+1, column=1) #position in the second column


            task_time_entry = tk.Entry(task_grid, textvariable=task_time_value)
            task_time_entry.grid(row=(self.task_counter)+1, column=2) #positions in the third column


            pack_widgets(task_grid)
            print(task_value_value, " ", task_value_value, " ", task_time_value)
            print(self.task_names,self.task_values,self.task_times)

            self.task_counter += 1





        add_task = tk.Button(window, text="+", command=tasks_add) #Creates a button when pressed executes tasks_add function
        line_seperator3 = ttk.Separator(window, orient="horizontal")


        #Way of going through tasks
        block_revision_radio = tk.Radiobutton(window, text="Block revision (Complete all of one task before starting the next task)", variable=block_revision, value=True) #Creates choices which set the self.block_revision variable true or false
        mixed_revision_radio = tk.Radiobutton(window, text="Mixed revision (Go between different tasks. Start multiple tasks before finishing one)", variable=block_revision, value=False)
        line_seperator4 = ttk.Separator(window, orient="horizontal")

        #Submit button
        def submit(subject_number):
            clearGUI()
            print(deadline.get())


            #Assigns all the entry values into a class specific variable
            self.deadline = int(deadline.get())  # Converts deadline entry into integer
            self.task_name = task_name.get()
            self.task_value = task_value.get()
            self.task_time = task_time.get()
            self.block_revision = block_revision.get()



            if self.first_input:
                setup_new_classes(False,subject_number)
                self.first_input = False
            else:
                display_inputs()



        submit_button = tk.Button(window, text="Submit", command=lambda: submit(subject_number)) #Button that when clicked executes submit function with variable "subject_number" passed into it

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


    def calculate_plan(self):
        number_of_tasks = len(self.task_names)
        self.scaled_tasks = [0] * number_of_tasks
        self.time_per_day_task = [0] * number_of_tasks

        #Makes the length of time for each task and the count multiply so all the tasks scale
        for task in range(number_of_tasks):
            self.scaled_tasks[task] = int(self.task_values[task].get()) * int(self.task_times[task].get())
            self.total_relative_time += self.scaled_tasks[task] #Running total of total relative time
        print("scaled tasks: ",self.scaled_tasks)

        #Divides the relative timing of tasks with the deadline
        self.time_per_day = self.total_relative_time / self.deadline  # Works out the time needed for all tasks per day

        self.daily_task_counts = [0] * self.deadline
        self.daily_task_times = [0] * self.deadline





        def calculate_block_revision_plan():
            #Creates an array with arrays for each day until the deadline for each task
            self.task_timetable = [0] * number_of_tasks
            for task in range(number_of_tasks):
                self.task_timetable[task] = [0] * self.deadline #Each task array of days is stored in the task_timetable array



            task_doing = 0
            print("time per day: ",self.time_per_day)

            print("Task name: ", self.task_names[0].get())
            print("Task scaled: ", self.scaled_tasks)
            print("Task time: ", self.task_times[0].get())

            for day in range(self.deadline): # for each day of revision until deadline
                print(day)
                print(self.daily_task_times)
                print("Task timetable: ", self.task_timetable)
                print("Length of tasks: ", len(self.task_names))

                while self.daily_task_times[day] <= self.time_per_day: # while daily time spent on tasks is less than time meant to be spent per day on tasks


                    if self.scaled_tasks[task_doing] <= 0:  #If all the time for a task is complete
                        if task_doing < len(self.task_names)-1:
                            task_doing += 1 #Go onto the next task

                    print("task doing: ", task_doing)

                    self.scaled_tasks[task_doing] -= int(self.task_times[task_doing].get())
                    self.daily_task_times[day] += int(self.task_times[task_doing].get()) #Adds the time taken for the task
                    self.task_timetable[task_doing][day] += 1 #Increments the count of the current task for the current day



                    print("Daily task time: ", self.daily_task_times[day])




            print(self.time_per_day)
            print("Daily task counts: ", self.daily_task_counts)
            print("Daily task times: ", self.daily_task_times)

            display_subject_output_block(0)



        def calculate_mixed_revision_plan():
            self.task_count_daily = [0] * len(self.task_names) #Creates an array with the same number of indexes as the task number

            for task in range(len(self.task_names)):
                  task_count = int(self.task_values[task].get())
                  self.task_count_daily[task] = round(task_count / self.deadline, 0) #Divides the task count by the days until deadline and rounds the value to a whole number
                  print(self.task_names[task].get(), " count daily", self.task_count_daily[task])

            print("self task count daily: ", self.task_count_daily)

            display_subject_output_mixed(0)


        print("block revision: ", self.block_revision)

        if self.block_revision:
            calculate_block_revision_plan()
        else: #I.e. mixed revision
            calculate_mixed_revision_plan()










def display_subject_output_mixed(subject_index):
    clearGUI()
    current_subject = subjects[subject_index]
    print("Subject name: ", current_subject.name)

    #Creates grid for title so they appear next to each other
    title_grid = tk.Frame(window)

    subject_title = tk.Message(title_grid, text=current_subject.name)
    subject_title.grid(row=0, column=1)

    title_seperator = ttk.Separator(window, orient="horizontal")
    title_seperator.pack(fill="x")  # Formats the separator so that it fills the entire x-axis (horizontal)
    def previous_subject():
        if subjects[subject_index - 1].block_revision: #If somethings exists at subjects[subject_index - 1].block_revision i.e. The previous subject is block revision
            display_subject_output_block(subject_index - 1)
        else: #If mixed revision
            display_subject_output_mixed(subject_index - 1)

    if subject_index > 0: #Makes sure there is a previous subject to go back to
        previous_subject_button = tk.Button(title_grid, text="<", command=previous_subject)
        previous_subject_button.grid(row=0, column=0)

    def next_subject():
        if subjects[subject_index + 1].block_revision:
            display_subject_output_block(subject_index + 1)
        else:  # If mixed revision
            display_subject_output_mixed(subject_index + 1)

    if subject_index+1 < len(subjects): #Makes sure there is another subject to go forward to
        next_subject_button = tk.Button(title_grid, text=">", command=next_subject)
        next_subject_button.grid(row=0, column=2)

    title_grid.pack()

    #No longer grid



    #Subject timetable grid
    timetable_grid = tk.Frame(window)

    timetable_name_heading = tk.Message(timetable_grid, text="Task Name")
    timetable_name_heading.grid(row=0, column=0)

    timetable_count_heading = tk.Message(timetable_grid, text="Count per day")
    timetable_count_heading.grid(row=0, column=1)

    print("Task count daily: ", current_subject.task_count_daily)

    for task in range(len(current_subject.task_names)): #For each task
        print("Task number: ", task)
        task_name_display = tk.Message(timetable_grid, text=current_subject.task_names[task].get())
        task_name_display.grid(row=task+1, column=0)

        task_count_display = tk.Message(timetable_grid, text=current_subject.task_count_daily[task])
        task_count_display.grid(row=task+1, column=1)

    timetable_grid.pack()





def display_subject_output_block(subject_index):
    clearGUI()
    current_subject = subjects[subject_index]
    print("Subject name: ", current_subject.name)

    # Creates grid for title so they appear next to each other
    title_grid = tk.Frame(window)

    subject_title = tk.Message(title_grid, text=current_subject.name)
    subject_title.grid(row=0, column=1)

    def previous_subject():
        if subjects[subject_index-1].block_revision:
            display_subject_output_block(subject_index - 1)
        else:
            display_subject_output_mixed(subject_index - 1)


    if subject_index > 0:  # Makes sure there is a previous subject to go back to
        previous_subject_button = tk.Button(title_grid, text="<", command=previous_subject)
        previous_subject_button.grid(row=0, column=0)

    def next_subject():
        if subjects[subject_index + 1].block_revision:
            display_subject_output_block(subject_index + 1)
        else:  # If mixed revision
            display_subject_output_mixed(subject_index + 1)

    if subject_index + 1 < len(subjects):  # Makes sure there is another subject to go forward to
        next_subject_button = tk.Button(title_grid, text=">", command=next_subject)
        next_subject_button.grid(row=0, column=2)

    title_grid.pack()

    # No longer grid

    title_seperator = ttk.Separator(window, orient="horizontal")
    title_seperator.pack(fill="x")  # Formats the separator so that it fills the entire x-axis (horizontal)

    #Grid for the tasks timetable
    timetable_grid = tk.Frame(window)

    #Creates the days for the timetable
    for day in range(current_subject.deadline): #for each day
        day_header = tk.Message(timetable_grid, text=f"Day {day+1}")
        day_header.grid(row=0, column=day+1)

    #Creates the names for the subjects
    task_counter = 0

    for task in current_subject.task_names:
        task_counter += 1
        task_name = tk.Message(timetable_grid, text=task.get())
        task_name.grid(row=task_counter, column=0)


    #Fills in the timetable for each subject
    current_subject_counts = current_subject.task_timetable
    print("Current subject counts: ", current_subject_counts)

    for task in range(len(current_subject.task_names)):

        for day in range(current_subject.deadline):
            timetable_value = tk.Message(timetable_grid, text=current_subject_counts[task][day])
            timetable_value.grid(row=task+1, column=day+1)

    timetable_grid.pack()


getGeneralInputs()

window.mainloop()  # Loops updating the GUI
