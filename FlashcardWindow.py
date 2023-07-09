import tkinter as tk
import MainWindow as mainWindow
import random


class FlashcardWindow:

  def __init__(self, flashcards):
    self.flashcards = flashcards
    self.current_flashcard = None

    self.window = tk.Tk()
    self.window.title("Flashcard App")
    self.window.geometry("800x600")

    self.legend_label = tk.Label(self.window, text="Left-click on the flashcard to view the translation", font=("Arial", 12), wraplength=500)
    self.legend_label.pack(pady=20)

    self.label = tk.Label(self.window, text="")
    self.label.pack(pady=20)

    self.show_flashcard()

    self.next_button = tk.Button(self.window,
                                 text="Next",
                                 command=self.show_flashcard)
    self.next_button.pack()

    self.back_button = tk.Button(self.window,
                                 text="Go Back",
                                 command=self.go_back)

    self.label.bind("<Button-1>", self.show_translation)  # Bind left-click event to show translation

    self.back_button.pack()

  def show_flashcard(self):
    if self.flashcards:
      self.current_flashcard = random.choice(self.flashcards)
      self.label.config(text=self.current_flashcard.word)
      self.flashcards.remove(self.current_flashcard)
    else:
      self.label.config(text="No more flashcards")

  def run(self):
    self.window.mainloop()

  def go_back(self):
    self.window.destroy()  # Close the current window
    mw = mainWindow.MainWindow()
    mw.run()

  def show_translation(self, event):
    if self.current_flashcard:     
      self.label.config(text=self.current_flashcard.translation)
