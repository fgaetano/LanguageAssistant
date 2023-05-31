import tkinter as tk
import MainWindow as mainWindow

class SecondWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Second Window")
        self.window.geometry("600x400")

        # Create and configure the UI elements for the second window
        self.label = tk.Label(self.window, text="Welcome to the Second Window")
        self.label.pack(pady=20)

        self.back_button = tk.Button(self.window, text="Go Back", command=self.go_back)
        self.back_button.pack()

    def go_back(self):
        self.window.destroy()  # Close the current window
        mw = mainWindow.MainWindow()
        mw.run()

    def run(self):
        self.window.mainloop()