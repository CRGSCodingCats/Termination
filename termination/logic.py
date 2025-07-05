from tkinter import messagebox

def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")
from tkinter import messagebox
import subprocess

def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
