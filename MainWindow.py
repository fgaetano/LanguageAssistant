import tkinter as tk
import SecondWindow as secondWindow

class MainWindow:

  # Create the main window
  def __init__(self):

    self.window = tk.Tk()
    self.window.title("Language Selection")
    self.window.geometry("600x400")

    # Stores the user selected language
    self.language_var = tk.StringVar()

    # Create a label for the language selection
    label = tk.Label(self.window, text="Select a Language:")
    label.pack(pady=20)

    # Create radio buttons for language selection
    english_radio = tk.Radiobutton(self.window, text="English", variable=self.language_var, value="english")
    english_radio.pack()

    spanish_radio = tk.Radiobutton(self.window, text="Spanish", variable=self.language_var, value="spanish")
    spanish_radio.pack()

    french_radio = tk.Radiobutton(self.window, text="French", variable=self.language_var, value="french")
    french_radio.pack()

    # Create a button to start the exercises
    start_button = tk.Button(self.window, text="Start Exercises", command=self.start_exercises)
    start_button.pack(pady=20)
  
  # Run the main event loop
  def run(self):
    # Run the main event loop
    self.window.mainloop()

  def start_exercises(self):
    selected_language = self.language_var.get()
    self.window.destroy()  # Close the current window
    sw = secondWindow.SecondWindow()
    sw.run()
    # Perform actions based on the selected_language
    # For example, load the corresponding vocabulary dataset and start exercises