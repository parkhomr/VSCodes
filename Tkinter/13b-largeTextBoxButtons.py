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

        self.Save_button = tkinter.Button(self.mainWindow, text="Save", command=self.save_data)
        self.Save_button.grid(row=4, column=0, pady=10)

        self.Get_button = tkinter.Button(self.mainWindow, text="Get", command=self.get_data)
        self.Get_button.grid(row=4, column=1, pady=10)

        self.data_text_box = tkinter.Text(self.mainWindow, height=10, width=50)
        self.data_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    def save_data(self):
        try:
            with open("afile.txt", 'w') as file:
                file.write(self.data_text_box.get(1.0, tkinter.END))
                tkinter.messagebox.showinfo(message="File saved")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to save file: {e}")

    def get_data(self):
        try:
            with open("afile.txt", 'r') as file:
                self.data_text_box.delete(1.0, tkinter.END)  # Clear the current text
                self.data_text_box.insert(tkinter.END, file.read())  # Insert the file content
        except Exception as e:
           tkinter.messagebox.showerror("Error", f"Failed to open file: {e}")


    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = TextBox()
app.run()