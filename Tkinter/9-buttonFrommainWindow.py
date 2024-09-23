import tkinter
import tkinter.messagebox


class BlankWindow:
    def __init__(self):
        # Initialize the Tkinter mainWindow window
        self.mainWindow = tkinter.Tk()

        # Set the title and size of the main window
        self.mainWindow.title("Main Window")
        self.mainWindow.geometry("300x200")

        # Add a button to the main window to trigger the message box
        self.show_message_button = tkinter.Button(self.mainWindow, text="Show Message", command=self.show_message)
        self.show_message_button.pack(pady=20)

    def show_message(self):
        # Show the message box
        tkinter.messagebox.showinfo("Warning!", "Your Computer Has A Virus")

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = BlankWindow()
app.run()
