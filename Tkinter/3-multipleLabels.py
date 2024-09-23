import tkinter as tk
class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tk.Tk()

        # Set the title of the window
        self.mainWindow.title("A Beautiful Window")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("400x300")

        self.label1 = tk.Label(self.mainWindow, text='Hello World!')
        self.label2 = tk.Label(self.mainWindow, text='This is my GUI program.')

        self.label1.pack()
        self.label2.pack()


    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()

app = BlankWindow()
app.run()
