import tkinter as tk
import tkinter.messagebox

class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tk.Tk()

        # Set the title of the window
        self.mainWindow.title("Text Input and Output")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("200x200")

        # Create and place the input label and textbox
        self.input_label = tk.Label(self.mainWindow, text="Enter X:")
        self.input_label.grid(row=0, column=0, pady=10)

        self.input_textbox = tk.Entry(self.mainWindow)
        self.input_textbox.grid(row=0, column=1)

        self.input_label2 = tk.Label(self.mainWindow, text="Enter Y:")
        self.input_label2.grid(row=1, column=0)

        self.input_textbox2 = tk.Entry(self.mainWindow)
        self.input_textbox2.grid(row=1, column=1)

        # Create and place the button to process the input
        self.process_button = tk.Button(self.mainWindow, text="+", command=self.Add)
        self.process_button.grid(row=2, column=1, pady=10)

        # Create and place the output label
        self.output_label = tk.Label(self.mainWindow, text="Output will appear here", borderwidth=1, relief='ridge')
        self.output_label.grid(row=3, column=1, pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(self.mainWindow, text="Quit", command=self.quit_application)
        self.quit_button.grid(row=4, column=1, pady=10)

    def Add(self):
        try:
            # Get the text from the input textbox and display it in the output label
            number1 = float(self.input_textbox.get())
            number2 = float(self.input_textbox2.get())
            self.output_label.config(text=f"{number1 + number2}")
        except ValueError:
            # Handle invalid input (e.g., non-numeric values)
            tk.messagebox.showinfo("Error", "Unable to process. You likely entered an invalid input")


    def quit_application(self):
        # Close the application
        self.mainWindow.destroy()

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = BlankWindow()
app.run()
