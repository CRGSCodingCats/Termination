import tkinter as tk
from termination.ui import create_main_ui
from termination.logic import confirm_exit
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TerminationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Termination")
        self.geometry("400x300")
        self.configure(bg="black")
        create_main_ui(self, self.handle_exit)

    def handle_exit(self):
        if confirm_exit():
            self.destroy()

def main():
    app = TerminationApp()
    app.mainloop()

if __name__ == "__main__":
    main()
