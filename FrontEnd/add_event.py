import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  
from db_connection import get_shared_connection

class AddEventPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Event Id label and entry
        tk.Label(self, text="Event ID:").grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.event_id_entry = tk.Entry(self)
        self.event_id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # Title label and entry
        tk.Label(self, text="Title:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Event date label and entry
        tk.Label(self, text="Event Date:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.event_date_entry = DateEntry(self)  # Use DateEntry widget for event date
        self.event_date_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Button to add event
        tk.Button(self, text="Add Event", command=self.add_event).grid(row=3, columnspan=2, padx=20, pady=20)

        # Button to go back to the previous page
        tk.Button(self, text="Back", command=self.go_back).grid(row=4, columnspan=2, padx=20, pady=20)

    def add_event(self):
        event_id = self.event_id_entry.get()
        title = self.title_entry.get()
        event_date = self.event_date_entry.get_date().strftime('%Y-%m-%d')  # Get selected date in YYYY-MM-DD format

        if not event_id or not title or not event_date:
            messagebox.showerror("Error", "Event ID, Title, and Event Date are required fields")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO Event (Event_Id, Title, Event_date) VALUES (?, ?, ?)", (event_id, title, event_date))
            self.db_connection.commit()
            messagebox.showinfo("Success", "Event added successfully")
            self.event_id_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.event_date_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()

    def go_back(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)
