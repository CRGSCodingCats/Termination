import tkinter as tk
from tkinter import messagebox

class TerminationApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Termination")
    self.geometry("400x300")
    self.configure(bg="black")

    self.label = tk.Label(self, text="Welcome to Termination", fg="lime", bg="black", font=("Courier", 16))
    self.label.pack(pady=20)

    self.quit_button = tk.Button(self, text="Exit", command=self.terminate, bg="darkred", fg="white")
    self.quit_button.pack(pady=10)

  def terminate(self):
    response = messagebox.askyesno("Exit", "Do you wish to terminate?")
    if response:
      self.destroy()

if __name__ == "__main__":
  app = TerminationApp()
  app.mainloop()
