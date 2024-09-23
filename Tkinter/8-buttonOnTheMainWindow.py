import tkinter
import tkinter.messagebox


class BlankWindow:
    def __init__(self):
        # Initialize the Tkinter root window
        self.mainWindow = tkinter.Tk()

        # Set the title and size of the main window
        self.mainWindow.title("Main Window")
        self.mainWindow.geometry("300x200")

        # Add a button to the main window to trigger the message box
        self.show_message_button = tkinter.Button(self.mainWindow, text="Show Message")
        self.show_message_button.pack(pady=20)

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


# Create an instance of the BlankWindow class
if __name__ == "__main__":
    app = BlankWindow()
    app.run()
