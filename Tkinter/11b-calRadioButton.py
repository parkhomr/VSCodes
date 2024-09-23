import tkinter
import tkinter.messagebox

class BlankWindow:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()

        # Set the title of the window
        self.mainWindow.title("Text Input and Output")

        # Set the size of the window (width x height)
        self.mainWindow.geometry("300x200")

        # Create and place the input label and textbox
        self.input_label = tkinter.Label(self.mainWindow, text="Enter X:")
        self.input_label.grid(row=0, column=0, pady=10)

        self.input_textbox = tkinter.Entry(self.mainWindow)
        self.input_textbox.grid(row=0, column=1)

        self.input_label2 = tkinter.Label(self.mainWindow, text="Enter Y:")
        self.input_label2.grid(row=1, column=0)

        self.input_textbox2 = tkinter.Entry(self.mainWindow)
        self.input_textbox2.grid(row=1, column=1)

        # Define a Tkinter variable to hold the selected operation
        self.selected_operation = tkinter.StringVar()
        self.selected_operation.set("Add")  # Set default value

        # Create RadioButtons for operation selection
        self.add_radio = tkinter.Radiobutton(self.mainWindow, text="Add", variable=self.selected_operation, value="Add")
        self.add_radio.grid(row=2, column=0, padx=10, pady=10)

        self.subtract_radio = tkinter.Radiobutton(self.mainWindow, text="Subtract", variable=self.selected_operation, value="Subtract")
        self.subtract_radio.grid(row=2, column=1, padx=10, pady=10)

        # Create and place the button to perform the operation
        self.calculate_button = tkinter.Button(self.mainWindow, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=1, pady=10)

        # Create and place the output label
        self.output_label = tkinter.Label(self.mainWindow, text="Output will appear here", borderwidth=1, relief='ridge')
        self.output_label.grid(row=4, column=1, padx=10, pady=10)

        # Create and place the quit button
        self.quit_button = tkinter.Button(self.mainWindow, text="Quit", command=self.quit_application)
        self.quit_button.grid(row=5, column=1, pady=10)

    def calculate(self):
        try:
            # Get the text from the input textboxes
            number1 = float(self.input_textbox.get())
            number2 = float(self.input_textbox2.get())

            # Determine the operation based on selected radio button
            operation = self.selected_operation.get()

            if operation == "Add":
                result = number1 + number2
            elif operation == "Subtract":
                result = number1 - number2
            else:
                raise ValueError("Unknown operation selected")

            # Update the output label with the result
            self.output_label.config(text=f"Result: {result}")

        except ValueError as e:
            # Handle invalid input (e.g., non-numeric values or unknown operation)
            tkinter.messagebox.showerror("Input Error", f"Error: {e}")


    def quit_application(self):
            # Close the application
            self.mainWindow.destroy()

    def run(self):
        # Start the Tkinter event loop
        self.mainWindow.mainloop()


app = BlankWindow()
app.run()
