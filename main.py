import MainWindow as mainWindow

#Application entry point
class MainClass:
    def __init__(self):
        # Instantiate the UI window class
        self.my_window = mainWindow.MainWindow()

    def start(self):
        # Call the run method of the UI window instance
        self.my_window.run()

# Instantiate the main class
my_app = MainClass()

# Start the application
my_app.start()
