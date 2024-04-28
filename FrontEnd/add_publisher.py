import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class AddPublisher(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Labels and Entry fields for publisher details
        tk.Label(self, text="ID:").grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Location:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.location_entry = tk.Entry(self)
        self.location_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Button to add publisher
        tk.Button(self, text="Add Publisher", command=self.add_publisher).grid(row=3, columnspan=2, padx=20, pady=20)
        
        tk.Button(self, text="Home", command=self.go_to_homepage).grid(row=4, columnspan=2, padx=20, pady=20)

    def add_publisher(self):
        publisher_id = self.id_entry.get()
        name = self.name_entry.get()
        location = self.location_entry.get()

        if not publisher_id or not name:
            messagebox.showerror("Error", "ID and Name are required fields")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO Publisher (SSN, NAME, Nationality) VALUES (?, ?, ?)",
                           (publisher_id, name, location))
            self.db_connection.commit()
            messagebox.showinfo("Success", "Publisher added successfully")
            # Clear the entry fields after adding publisher
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.location_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()

    def go_to_homepage(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)
