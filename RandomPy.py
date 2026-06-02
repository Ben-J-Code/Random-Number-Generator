import tkinter as Tkinter
from tkinter import messagebox as MessageBox
from random import randint as Random

List = []

Root = Tkinter.Tk()
Root.title("RandomPy")
Root.configure(bg="#101010")
Root.geometry("400x200+"+"410"+"+0")
Root.resizable(False, False)
Root.iconbitmap(__file__.replace("MainScript.py", "RandomPy.ico"))

Title = Tkinter.Label(Root, text="RandomPy", bg="#101010", fg="#FFFFFF", font=("Bahnschrift Light", 20, "bold"))
Title.pack(pady=5)

Entry1 = Tkinter.Entry(Root, bg="#101010", fg="#FFFFFF", font=("Bahnschrift Light", 20, "bold"), insertbackground="white")
Entry1.pack(pady=5)
Entry2 = Tkinter.Entry(Root, bg="#101010", fg="#FFFFFF", font=("Bahnschrift Light", 20, "bold"), insertbackground="white")
Entry2.pack(pady=5)

def ButtonCommand(Val1, Val2):
    if Val1 == "" or Val2 == "":
        MessageBox.showwarning(title="RandomPy", message="Looks like you forgot to input both entry boxes.\n\nTip: The top entry is the min value and the bottom entry is the max value.")
        return

    try:
        if Val1.isdigit():
            Val1 = int(Val1)
        else:
            Val1 = int(round(float(Val1), 0))

        if Val2.isdigit():
            Val2 = int(Val2)
        else:
            Val2 = int(round(float(Val2), 0))

        Return = Random(Val1, Val2)

        print(Return)
    except Exception as Error:
        MessageBox.showwarning(title="RandomPy", message=f"{Error}\n\nTip: RandomPy only accepts valid intigers and floats. (Floats are rounded to nearest whole intiger.)")
    else:
        MessageBox.showinfo(title="RandomPy", message=f"Result: {Return}")

Button = Tkinter.Button(Root, text="Spin!", bg="#101010", fg="#FFFFFF", activebackground="#101010", activeforeground="#FFFFFF", borderwidth=6, font=("Bahnschrift Light", 15, "bold"), command=lambda: ButtonCommand(Entry1.get(), Entry2.get()))
Button.pack(pady=5)

Root.mainloop()