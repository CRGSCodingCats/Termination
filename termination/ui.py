import tkinter as tk
from tkinter import scrolledtext

def create_main_ui(root, exit_callback, command_callback):
    label = tk.Label(root, text="Welcome to Termination", fg="lime", bg="black", font=("Courier", 16))
    label.pack(pady=10)

    quit_button = tk.Button(root, text="Exit", command=exit_callback, bg="darkred", fg="white")
    quit_button.pack(pady=5)

    cmd_label = tk.Label(root, text="Enter Command:", fg="white", bg="black")
    cmd_label.pack(pady=5)

    cmd_entry = tk.Entry(root, width=50, bg="black", fg="white", insertbackground="white")
    cmd_entry.pack()

    run_button = tk.Button(root, text="Run", command=lambda: command_callback(cmd_entry.get()), bg="green", fg="black")
    run_button.pack(pady=5)

    output_box = scrolledtext.ScrolledText(root, width=60, height=10, bg="black", fg="lime", font=("Courier", 10))
    output_box.pack(pady=10)

    spinner_label = tk.Label(root, text="", fg="white", bg="black", font=("Courier", 10))
    spinner_label.pack()

    return output_box, spinner_label
