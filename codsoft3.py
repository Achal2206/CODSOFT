import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Select operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Enter valid numbers!")

# Create the GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation dropdown
operation_var = tk.StringVar()
operation_var.set("Select Operation")

tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide").pack(pady=10)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

# Result display
result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()