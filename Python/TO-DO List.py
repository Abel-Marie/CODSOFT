import tkinter as tk
from tkinter import font

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        pass

def delete_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
    except:
        pass

def update_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
        task_list.insert(task_index, task_entry.get())
        task_entry.delete(0, tk.END)
    except:
        pass

# Creating the main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#15202B")
root.geometry("600x400")  

# Customizing fonts
custom_font = font.Font(family="Helvetica", size=12)

# Creating widgets
task_entry = tk.Entry(root, width=60, font=custom_font, bg="#253341", fg="white")
add_task_btn = tk.Button(root, text="Add Task", width=20, command=add_task, bg="#1DA1F2", fg="white", font=custom_font)
update_task_btn = tk.Button(root, text="Update Selected Task", width=20, command=update_task, bg="#1DA1F2", fg="white", font=custom_font)
task_list = tk.Listbox(root, width=50, height=15, font=custom_font, bg="#253341", fg="white")
delete_task_btn = tk.Button(root, text="Delete", width=20, command=delete_task, bg="#1DA1F2", fg="white", font=custom_font)

# Placing widgets 
task_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
add_task_btn.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
update_task_btn.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
delete_task_btn.pack(side=tk.TOP, fill=tk.X, padx=20, pady=15)

# Running the application
root.mainloop()
