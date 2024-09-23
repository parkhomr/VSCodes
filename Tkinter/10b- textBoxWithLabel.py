import tkinter as tk

class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tk.Tk()

        # Set the title of the window
        self.mainWindow.title("Text Input and Output")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("300x240")

        # Create and place the input label and textbox
        self.input_label = tk.Label(self.mainWindow, text="Enter text:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_textbox = tk.Entry(self.mainWindow)
        self.input_textbox.grid(row=0, column=1, padx=10, pady=10)

        # Create and place the button to process the input
        self.process_button = tk.Button(self.mainWindow, text="Get MyText", command=self.processInput)
        self.process_button.grid(row=1, column=1)

        # Create and place the output label
        self.output_label = tk.Label(self.mainWindow, text="Output will appear here", borderwidth=1, relief='ridge')
        self.output_label.grid(row=2, column=1, pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(self.mainWindow, text="Quit", command=self.quit_application)
        self.quit_button.grid(row=3, column=1, pady=10)

    def processInput(self):
        # Get the text from the input textbox and display it in the output label
        number1 = self.input_textbox.get()
        self.output_label.config(text=number1)

    def quit_application(self):
        # Close the application
        self.mainWindow.destroy()

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = BlankWindow()
app.run()
