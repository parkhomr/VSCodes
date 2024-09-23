import tkinter as tk
class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tk.Tk()

        # Set the title of the window
        self.mainWindow.title("A Beautiful Window")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("400x300")

        self.label = tk.Label(self.mainWindow, text='Hello World!', borderwidth=1, relief='solid')

        self.label.pack()


    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()

app = BlankWindow()
app.run()
