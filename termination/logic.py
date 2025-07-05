from tkinter import messagebox
import subprocess

def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")

def run_command(command):
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        output = ""
        for line in process.stdout:
            output += line
        process.wait()
        return output
    except Exception as e:
        return f"Error: {e}"
