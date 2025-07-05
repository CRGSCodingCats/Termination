from tkinter import messagebox
import subprocess

def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")

def stream_command(command):
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in process.stdout:
            yield line
        process.wait()
    except Exception as e:
        yield f"Error: {e}\n"
