import tkinter as tk
from tkinter import filedialog

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def check_files():
    # Add logic to check the files
    pass

def close_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Check files")

# Create and place the widgets
entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=1, padx=5, pady=5)

browse_button1 = tk.Button(root, text="Browse...", command=lambda: browse_file(entry1))
browse_button1.grid(row=0, column=0, padx=5, pady=5)

browse_button2 = tk.Button(root, text="Browse...", command=lambda: browse_file(entry2))
browse_button2.grid(row=1, column=0, padx=5, pady=5)

check_button = tk.Button(root, text="Check for files...", command=check_files)
check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='we')

close_button = tk.Button(root, text="Close Program", command=close_program)
close_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='we')

# Run the application
root.mainloop()
