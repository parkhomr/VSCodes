import tkinter
from tkinter import filedialog
from tkinter import messagebox


class TextBox:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()

        # Set the title of the window
        self.mainWindow.title("Text Input and Output")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("500x200")

        # Create a Text widget
        self.data_text_box = tkinter.Text(self.mainWindow, height=10, width=50)
        self.data_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create a menu bar
        self.menu_bar = tkinter.Menu(self.mainWindow)
        self.mainWindow.config(menu=self.menu_bar)

        # Create the File menu
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.mainWindow.quit)

    def open_file(self):
        # Open file dialog and get the file path
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.data_text_box.delete(1.0, tkinter.END)  # Clear the current text
                    self.data_text_box.insert(tkinter.END, file.read())  # Insert the file content
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        # Save file dialog and get the file path
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.data_text_box.get(1.0, tkinter.END))  # Save the text content
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


# Create an instance of the TextBox class and run the application
app = TextBox()
app.run()
