import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def openfile():
    f = filedialog.askopenfilename(initialdir="c:",
                                    title="Open File",
                                    filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    try:
        if f:
            thf = open(f)
            textArea.insert(tk.END, thf.read())
            thf.close()
        elif f == '':
            messagebox.showinfo("Cancel", "You Click Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")


# print(f)
window = tk.Tk()

window.title("My Database")
window.geometry("800x400")
