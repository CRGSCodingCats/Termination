from tkinter import messagebox
import subprocess
import os
os.chdir(os.path.expanduser("~"))  # changes dir to user's home


def confirm_exit():
    return messagebox.askyesno("Exit", "Do you wish to terminate?")

def get_prompt():
    cwd = os.getcwd()
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        env_name = os.path.basename(venv_path)
        return f"({env_name}) TT {cwd}> "
    else:
        return f"TT {cwd}> "

def stream_command(command):
    yield get_prompt() + command + "\n"
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
