import tkinter
import tkinter.messagebox

class TextBox:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()

        # Set the title of the window
        self.mainWindow.title("Text Input and Output")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("500x200")

        self.data_text_box = tkinter.Text(self.mainWindow, height=10, width=50)
        self.data_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = TextBox()
app.run()