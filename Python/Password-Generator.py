import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import pyperclip  

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        root.title("Password Generator")
        root.geometry("400x250")

        # Styling Variables
        label_color = "#333"
        button_bg = "#4CAF50"
        button_fg = "white"

        # Length Label and Entry
        tk.Label(root, text="Password Length:", fg=label_color).pack(pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        # Generate Button
        generate_btn = tk.Button(root, text="Generate Password", bg=button_bg, fg=button_fg, command=self.generate_password)
        generate_btn.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=5)

        # Copy Button
        copy_btn = tk.Button(root, text="Copy to Clipboard", bg="#FFC107", fg="black", command=self.copy_to_clipboard)
        copy_btn.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            password = self._generate_password_logic(length)
            self.result_label.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length.")

    def _generate_password_logic(self, length):
        if length < 4:
            raise ValueError("Password length should be at least 4 characters.")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = []

        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        for _ in range(length - 4):
            password.append(random.choice(characters))

        random.shuffle(password)
        return ''.join(password)

    def copy_to_clipboard(self):
        password = self.result_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Info", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
