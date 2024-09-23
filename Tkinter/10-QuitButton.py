import tkinter as tk
import tkinter.messagebox
class BlankWindow:
    def __init__(self):
        # Initialize the Tkinter mainWindow window
        self.mainWindow = tkinter.Tk()

        # Set the title and size of the main window
        self.mainWindow.title("Main Window")
        self.mainWindow.geometry("300x200")

        # Add a button to the main window to quit the application
        self.quit_button = tk.Button(self.mainWindow, text="Save Me", command=self.quit_application)
        self.quit_button.pack(pady=20)

    def quit_application(self):
        # Comment out the next line to see what happens
        tkinter.messagebox.showinfo("Warning!", "Your Computer Has A Virus")
        # Close the application
        self.mainWindow.destroy()

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()

# Create an instance of the BlankWindow class and run the application
if __name__ == "__main__":
    app = BlankWindow()
    app.run()
