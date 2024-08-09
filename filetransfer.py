import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Sets title of GUI window
        self.master.title("File Transfer")

        # Creates button to transfer files
        self.transfer_btn = Button(self.master, text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # Creates button to select files from source directory
        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Creates entry for source directory selection
        self.source_dir = Entry(self.master, width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select files for destination directory
        self.destDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter grid()
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 0))

        # Creates entry for destination directory selection
        self.dest_dir = Entry(self.master, width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.dest_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 0))

        # Creates button to exit the application
        self.exit_btn = Button(self.master, text="Exit", width=20, command=self.exitApp)
        # Positions exit button in GUI using tkinter grid()
        self.exit_btn.grid(row=3, column=1, padx=(200, 0), pady=(10, 15))

    # Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    # Creates function to select destination directory.
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.dest_dir.delete(0, END)
        self.dest_dir.insert(0, selectDestDir)

    # Creates function to transfer files.
    def transferFiles(self):
        # Get source and destination directories
        source = self.source_dir.get()
        destination = self.dest_dir.get()

        if not source or not destination:
            print("Please select both source and destination directories.")
            return
        
        # Check if source and destination directories exist
        if not os.path.isdir(source):
            print(f"Source directory does not exist: {source}")
            return
        
        if not os.path.isdir(destination):
            print(f"Destination directory does not exist: {destination}")
            return

        # Get a list of files in the source directory
        source_files = os.listdir(source)

        for file_name in source_files:
            source_file = os.path.join(source, file_name)
            destination_file = os.path.join(destination, file_name)

            if os.path.isfile(source_file):
                try:
                    shutil.move(source_file, destination_file)
                    print(f"{file_name} was successfully transferred.")
                except Exception as e:
                    print(f"Error transferring {file_name}: {e}")
            else:
                print(f"{file_name} is not a file and will be skipped.")

    # Creates function to exit the application.
    def exitApp(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
