import tkinter as tk
from tkinter import messagebox

class BorrowBookPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width=800, height=600)

        # Book ID Label and Entry
        self.book_id_label = tk.Label(self, text="Book ID:")
        self.book_id_label.pack(pady=10)

        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(pady=5)

        # Member ID Label and Entry
        self.member_id_label = tk.Label(self, text="Member ID:")
        self.member_id_label.pack(pady=10)

        self.member_id_entry = tk.Entry(self)
        self.member_id_entry.pack(pady=5)

        # Borrow Button
        self.borrow_button = tk.Button(self, text="Borrow", command=self.borrow_book)
        self.borrow_button.pack(pady=10)

        # Back Button
        from librarian_homepage import LibrarianHomePage
        back_button = tk.Button(self, text="Back",command=lambda: self.controller.show_page(LibrarianHomePage))
        back_button.pack(pady=10)

    def borrow_book(self):
        book_id = self.book_id_entry.get()
        member_id = self.member_id_entry.get()

        try:
            # Your borrowing functionality here
            pass
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", str(e))

    def back_to_homepage(self):
        self.controller.show_page(LibrarianHomePage)
