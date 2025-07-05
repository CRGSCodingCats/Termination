import tkinter as tk
from termination.ui import create_main_ui
from termination.logic import confirm_exit, stream_command
import threading
import itertools

class TerminationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Termination")
        self.geometry("600x400")
        self.configure(bg="black")

        self.spinner_running = False
        self.spinner_chars = itertools.cycle('|/-\\-')

        self.output_box = create_main_ui(self, self.handle_exit, self.execute_command)

    def handle_exit(self):
        if confirm_exit():
            self.destroy()

    def execute_command(self, cmd):
        self.output_box.delete("1.0", tk.END)
        self.spinner_running = True
        self.update_spinner()
        thread = threading.Thread(target=self.stream_output_live, args=(cmd,))
        thread.start()

    def update_spinner(self):
        if self.spinner_running:
            next_char = next(self.spinner_chars)
            current_output = self.output_box.get("1.0", tk.END)
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, f"{current_output.strip()}\nRunning: {next_char}")
            self.output_box.see(tk.END)
            self.after(100, self.update_spinner)

    def stream_output_live(self, cmd):
        self.output_box.delete("1.0", tk.END)
        for line in stream_command(cmd):
            self.output_box.insert(tk.END, line)
            self.output_box.see(tk.END)
            self.update_idletasks()
        self.spinner_running = False

def main():
    app = TerminationApp()
    app.mainloop()

if __name__ == "__main__":
    main()
