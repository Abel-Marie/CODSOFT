import tkinter as tk
from tkinter import messagebox

def on_click(number):
    current = entry.get()
    entry.insert(tk.END, str(number))

def on_clear():
    entry.delete(0, tk.END)

def on_operation(operator):
    current = entry.get()
    if current[-1] in '+-*/':
        return 
    entry.insert(tk.END, operator)

def on_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

# Set up the window
root = tk.Tk()
root.title("SImple Calculator")

# Entry field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=8, padx=15, pady=15)

# Defining buttons
# Numbers
for i in range(1, 10):
    button = tk.Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: on_click(i))
    button.grid(row=(3 - (i-1)//3), column=(i-1)%3)

button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: on_click(0))
button_0.grid(row=4, column=0)

# Operations
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: on_operation('+'))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: on_operation('-'))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: on_operation('*'))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: on_operation('/'))
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=on_clear)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=on_equal)

# buttons 
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
