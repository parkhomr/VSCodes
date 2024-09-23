import tkinter
import tkinter.messagebox

class BlankWindow:
    def __init__(self):
        # Initialize the Tkinter root window
        self.mainWindow = tkinter.Tk()

        # Hide the root window
        self.mainWindow.withdraw()

    def run(self):
        # Show the message box
        tkinter.messagebox.showinfo("Warning", "Virus Detected", parent=self.mainWindow)

# Create an instance of the BlankWindow class
if __name__ == "__main__":
    app = BlankWindow()
    app.run()
