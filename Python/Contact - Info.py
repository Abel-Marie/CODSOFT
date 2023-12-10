import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x450")
        self.root.configure(bg="#15202B") 

        self.contacts = {}
        self.load_contacts()

        # Styling Variables
        label_color = "white"
        entry_bg = "#192734"
        entry_fg = "white"
        button_bg = "#1DA1F2"
        button_fg = "white"

        # Creating Widgets
        tk.Label(root, text="Name", bg="#15202B", fg=label_color).grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone", bg="#15202B", fg=label_color).grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email", bg="#15202B", fg=label_color).grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Address", bg="#15202B", fg=label_color).grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Contact", bg=button_bg, fg=button_fg, command=self.add_contact).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(root, text="View Contacts", bg=button_bg, fg=button_fg, command=self.view_contacts).grid(row=4, column=1, padx=10, pady=5)
        tk.Button(root, text="Search Contact", bg=button_bg, fg=button_fg, command=self.search_contact).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(root, text="Update Contact", bg=button_bg, fg=button_fg, command=self.update_contact_dialog).grid(row=5, column=1, padx=10, pady=5)
        tk.Button(root, text="Delete Contact", bg=button_bg, fg=button_fg, command=self.delete_contact_dialog).grid(row=6, column=0, padx=10, pady=5)

        # Contact List Box
        self.contact_list_box = tk.Listbox(root, height=15, width=50, bg=entry_bg, fg=entry_fg)
        self.contact_list_box.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            if name not in self.contacts:
                self.contacts[name] = {"phone": phone, "email": email, "address": address}
                self.save_contacts()
                messagebox.showinfo("Success", "Contact Added Successfully")
                self.clear_entries()
                self.view_contacts()
            else:
                messagebox.showerror("Error", "Contact with this name already exists")
        else:
            messagebox.showerror("Error", "Name and Phone are required")

    def view_contacts(self):
        self.contact_list_box.delete(0, tk.END)
        for name, info in self.contacts.items():
            self.contact_list_box.insert(tk.END, f"{name} - {info['phone']}")

    def search_contact(self):
        search_name = simpledialog.askstring("Search Contact", "Enter name of the contact")
        if search_name:
            search_name = search_name.strip()
            if search_name in self.contacts:
                info = self.contacts[search_name]
                messagebox.showinfo("Contact Found", f"Name: {search_name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            else:
                messagebox.showerror("Error", "Contact Not Found")

    def update_contact_dialog(self):
        update_name = simpledialog.askstring("Update Contact", "Enter name of the contact to update")
        if update_name:
            self.update_contact(update_name.strip())

    def update_contact(self, name):
        if name in self.contacts:
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            address = self.address_entry.get().strip()

            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.save_contacts()
            messagebox.showinfo("Success", "Contact Updated Successfully")
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Contact Not Found")

    def delete_contact_dialog(self):
        delete_name = simpledialog.askstring("Delete Contact", "Enter name of the contact to delete")
        if delete_name:
            self.delete_contact(delete_name.strip())

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact Deleted Successfully")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Contact Not Found")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
