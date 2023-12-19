import tkinter as tk #GUI library

window = tk.Tk()
window.title("Revision planner")

def clearGUI():
    print("Clear gui")
    for widget in window.winfo_children():
        widget.destroy()


def getGeneralInputs():

    counter = 0

    input_var = tk.StringVar() #creates empty string variable
    Question_Messages = ["How many subjects do you take?", "Please enter the name for each subject"]


    Question_Entry = tk.Entry(window, textvariable=input_var)  # Gets input for number of subjects and stores it in variable input_var
    Question_Entry.pack()

    def askQuestion():
        print(counter)

        Question_Prompt = tk.Message(window, text=Question_Messages[counter])  # Displays message at the index of Question messages list
        Question_Prompt.pack()



        def row_Of_Subjects():
            NumberOfSubjects = int(input_var.get())
            print("Number of subjects: ",NumberOfSubjects)

            clearGUI()

            for i in range(NumberOfSubjects): #Creates a table of inputs for each subject
                Subject_Name_Entry = tk.Entry(window)
                Subject_Name_Entry.pack()

            ask_another()


        def submit():

            clearGUI()
            print(Question_Messages)
            print("Counter = ", counter)
            Question_Prompt = tk.Message(window, text=Question_Messages[counter])  # Displays message at the index of Question messages list
            Question_Prompt.pack()
            print(Question_Messages[counter])
            row_Of_Subjects()







        Submit_Button = tk.Button(window, text="Submit", command=submit)
        Submit_Button.pack()


    def ask_another():
        nonlocal counter #declares counter as global
        if counter < len(Question_Messages):
            askQuestion()
            counter += 1

    ask_another()




def controlFunction(): #Main function which calls other functions
    getGeneralInputs()

    window.mainloop()

controlFunction()