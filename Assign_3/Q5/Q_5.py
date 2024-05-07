import os
import shutil
from tkinter import *
from tkinter import filedialog

class FileManager:
    def __init__(self, master):
        self.master = master
        self.current_path = StringVar()
        self.current_path.set(os.getcwd())
        Label(master, text="Current Path:").grid(row=0)
        Entry(master, textvariable=self.current_path).grid(row=0, column=1)
        Button(master, text="Browse", command=self.browse).grid(row=0, column=2)
        Button(master, text="Copy", command=self.copy).grid(row=1, column=0)
        Button(master, text="Move", command=self.move).grid(row=1, column=1)
        Button(master, text="Delete", command=self.delete).grid(row=1, column=2)

    def browse(self):
        path = filedialog.askdirectory()
        self.current_path.set(path)

    def copy(self):
        src = filedialog.askopenfilename()
        dst = filedialog.askdirectory()
        shutil.copy(src, dst)

    def move(self):
        src = filedialog.askopenfilename()
        dst = filedialog.askdirectory()
        shutil.move(src, dst)

    def delete(self):
        file = filedialog.askopenfilename()
        os.remove(file)

root = Tk()
fm = FileManager(root)
root.mainloop()
