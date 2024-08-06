import tkinter as tk
from tkinter import messagebox
import sqlite3

# Set up the database
def setup_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    phone_number TEXT,
                    email TEXT,
                    current_course TEXT)''')
    conn.commit()
    conn.close()

# Add student to database
def add_student():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()
    current_course = entry_current_course.get()

    if not (first_name and last_name and phone_number and email and current_course):
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return

    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (first_name, last_name, phone_number, email, current_course) VALUES (?, ?, ?, ?, ?)',
              (first_name, last_name, phone_number, email, current_course))
    conn.commit()
    conn.close()
    clear_entries()
    update_student_list()

# Delete selected student
def delete_student():
    selected_item = student_listbox.curselection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a student to delete")
        return

    student_id = student_listbox.get(selected_item[0]).split()[0]
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    update_student_list()

# Update the student listbox
def update_student_list():
    student_listbox.delete(0, tk.END)
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    for row in c.fetchall():
        student_listbox.insert(tk.END, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")
    conn.close()

# Clear form entries
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_current_course.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Tracking")

# Title label
title_label = tk.Label(root, text="Student Tracking", font=("Arial", 20))
title_label.pack(pady=10)

# Form frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# First name
tk.Label(form_frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(form_frame)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

# Last name
tk.Label(form_frame, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(form_frame)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

# Phone number
tk.Label(form_frame, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
entry_phone_number = tk.Entry(form_frame)
entry_phone_number.grid(row=2, column=1, padx=10, pady=5)

# Email
tk.Label(form_frame, text="Email:").grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Current course
tk.Label(form_frame, text="Current Course:").grid(row=4, column=0, padx=10, pady=5)
entry_current_course = tk.Entry(form_frame)
entry_current_course.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(form_frame, text="Submit", command=add_student)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Student listbox
student_listbox = tk.Listbox(root, width=80, height=15)
student_listbox.pack(pady=10)

# Delete button
delete_button = tk.Button(root, text="Delete Selected", command=delete_student)
delete_button.pack(pady=10)

# Initialize the database and the student list
setup_database()
update_student_list()

# Start the Tkinter event loop
root.mainloop()
