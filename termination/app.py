import tkinter as tk
from termination.ui import create_main_ui
from termination.logic import confirm_exit, run_command
import threading
import itertools

class TerminationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Termination")
        self.geometry("600x400")
        self.configure(bg="black")
        self.output_box = create_main_ui(self, self.handle_exit, self.execute_command)

    def handle_exit(self):
        if confirm_exit():
            self.destroy()

    def execute_command(self, cmd):
        output = run_command(cmd)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, output)

def main():
    app = TerminationApp()
    app.mainloop()

if __name__ == "__main__":
    main()
