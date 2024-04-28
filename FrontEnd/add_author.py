import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class AddAuthor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Labels and Entry fields for author details
        tk.Label(self, text="SSN:").grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.ssn_entry = tk.Entry(self)
        self.ssn_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Nationality:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.nationality_entry = tk.Entry(self)
        self.nationality_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Biography:").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.biography_entry = tk.Entry(self)
        self.biography_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Button to add author
        tk.Button(self, text="Add Author", command=self.add_author).grid(row=4, columnspan=2, padx=20, pady=20)
        
        tk.Button(self, text="Home", command=self.go_to_homepage).grid(row=5, columnspan=2, padx=20, pady=20)

    def add_author(self):
        ssn = self.ssn_entry.get()
        name = self.name_entry.get()
        nationality = self.nationality_entry.get()
        biography = self.biography_entry.get()

        if not ssn or not name:
            messagebox.showerror("Error", "SSN and Name are required fields")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO Author (SSN, Name, Nationality, Biography) VALUES (?, ?, ?, ?)",
                           (ssn, name, nationality, biography))
            self.db_connection.commit()
            messagebox.showinfo("Success", "Author added successfully")
            # Clear the entry fields after adding author
            self.ssn_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.nationality_entry.delete(0, tk.END)
            self.biography_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()

    def go_to_homepage(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)
