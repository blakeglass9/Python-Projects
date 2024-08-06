import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('700x400')
        self.master.title('Learning Tkinter!')
        self.master.config(bg='black')

        self.varFname = StringVar()
        self.varLname = StringVar()

        # Create and place the First Name label
        self.lblFName = Label(self, text='First Name:', font=("Helvetica", 16), fg='white', bg='black')
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        # Create and place the Last Name label
        self.lblLName = Label(self, text='Last Name:', font=("Helvetica", 16), fg='white', bg='black')
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        # Create and place the First Name entry
        self.txtFName = Entry(self, textvariable=self.varFname, font=("Helvetica", 16), fg='black', bg='white')
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        # Create and place the Last Name entry
        self.txtLName = Entry(self, textvariable=self.varLname, font=("Helvetica", 16), fg='black', bg='white')
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        # Create and place the Submit button
        self.btnSubmit = Button(self, text='Submit', font=("Helvetica", 16), command=self.submit_action, fg='black', bg='white')
        self.btnSubmit.grid(row=2, column=0, columnspan=2, pady=(30, 0))

        # Create and place the additional Submit button (as an example)
        self.btnAdditional = Button(self, text="Additional", width=10, height=2, command=self.submit, fg='black', bg='white')
        self.btnAdditional.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        # Create and place the display label
        self.lblDisplay = Label(self, text='', font=("Helvetica", 16), fg='white', bg='black')
        self.lblDisplay.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    def submit_action(self):
        # This function will be called when the Submit button is clicked
        first_name = self.varFname.get()
        last_name = self.varLname.get()
        greeting = f'Hello {first_name} {last_name}'
        self.lblDisplay.config(text=greeting)

    def submit(self):
        print("Additional Submit button clicked")

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
