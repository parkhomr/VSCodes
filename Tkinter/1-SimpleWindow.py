import tkinter
class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()

        # # Set the title of the window
        # self.mainWindow.title("A Beautiful Window")
        #
        # # Set the size of the window (width x height)
        # self.mainWindow.geometry("400x300")

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()

app = BlankWindow()
app.run()
