import tkinter as tk

window = tk.Tk()


window.iconbitmap('asset/icon.ico')
# label = tk.Label(text="Python rocks!")

window.title("My Database")
window.geometry("800x400") # W xH

button = tk.Button(
    text="READ CONFIG",
    width=25,
    height=5,
#    bg="blue",
#    fg="yellow",
)

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
'''
"red"
"orange"
"yellow"
"green"
"blue"
"purple"
'''

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"





label.pack()
button.pack()



window.mainloop()