import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class AddAuthor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Labels and Entry fields for user details
        tk.Label(self, text="ID:").grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Email:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Password:").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Gender:").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.gender_entry = tk.Entry(self)
        self.gender_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Street:").grid(row=5, column=0, padx=20, pady=10, sticky="e")
        self.street_entry = tk.Entry(self)
        self.street_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Building Number:").grid(row=6, column=0, padx=20, pady=10, sticky="e")
        self.building_entry = tk.Entry(self)
        self.building_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="City:").grid(row=7, column=0, padx=20, pady=10, sticky="e")
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # Button to add user
        tk.Button(self, text="Add User", command=self.add_user).grid(row=8, columnspan=2, padx=20, pady=20)
        
        tk.Button(self, text="Home", command=self.go_to_homepage).grid(row=9, columnspan=2, padx=20, pady=20)

    def add_user(self):
        member_id = self.id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        gender = self.gender_entry.get()
        street = self.street_entry.get()
        building = self.building_entry.get()
        city = self.city_entry.get()

        if not member_id or not name or not email or not password:
            messagebox.showerror("Error", "Name, email, and password are required fields")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO Member (ID, Name, email, password, Gender, Street_name, Building_number, City) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (member_id, name, email, password, gender, street, building, city))
            self.db_connection.commit()
            messagebox.showinfo("Success", "User added successfully")
            # Clear the entry fields after adding user
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.gender_entry.delete(0, tk.END)
            self.street_entry.delete(0, tk.END)
            self.building_entry.delete(0, tk.END)
            self.city_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()

    def go_to_homepage(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)
