import tkinter as tk

def create_main_ui(root, exit_callback):
    label = tk.Label(root, text="Welcome to Termination", fg="lime", bg="black", font=("Courier", 16))
    label.pack(pady=20)

    quit_button = tk.Button(root, text="Exit", command=exit_callback, bg="darkred", fg="white")
    quit_button.pack(pady=10)
