import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to clear inputs
def clear_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Operator dropdown
operator_var = tk.StringVar(root)
operator_choices = ['+', '-', '*', '/']
operator_var.set('+')  # default value
operator_menu = tk.OptionMenu(root, operator_var, *operator_choices)
operator_menu.grid(row=0, column=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Buttons
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=0, padx=10, pady=10)

clear_btn = tk.Button(root, text="Clear", command=clear_inputs)
clear_btn.grid(row=2, column=1, padx=10, pady=10)

quit_btn = tk.Button(root, text="Quit", command=root.quit)
quit_btn.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()
