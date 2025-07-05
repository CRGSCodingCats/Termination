from tkinter import messagebox

def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")
