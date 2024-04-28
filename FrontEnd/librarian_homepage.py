import tkinter as tk
from tkinter import messagebox

class LibrarianHomePage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent, width=800, height=600) 
        self.controller = controller
        self.config(width=800, height=600)


        # Add Book Button
        add_book_button = tk.Button(self, text="Add Book", command=self.add_book)
        add_book_button.pack(pady=10)

        # Remove Book Button
        remove_book_button = tk.Button(self, text="Remove Book", command=self.remove_book)
        remove_book_button.pack(pady=10)

        # Add User Button
        add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        add_user_button.pack(pady=10)

        # Remove User Button
        remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        remove_user_button.pack(pady=10)

        # Add Event Button
        add_event_button = tk.Button(self, text="Add Event", command=self.add_event)
        add_event_button.pack(pady=10)

        # Search Book Button
        from search_book_libriran import SearchBookLibriran
        search_book_button = tk.Button(self, text="Search Book", command= lambda: self.controller.show_page(SearchBookLibriran))
        search_book_button.pack(pady=10)

        # Logout Button
        from login_page import LoginPage
        logout_button = tk.Button(self, text="Logout", command=lambda: self.controller.show_page(LoginPage))
        logout_button.pack(pady=10)


    def add_book(self):
        # Implement functionality to add a book
        print("Adding a book...")

    def remove_book(self):
        # Implement functionality to remove a book
        print("Removing a book...")

    def add_user(self):
        # Implement functionality to add a user
        print("Adding a user...")

    def remove_user(self):
        # Implement functionality to remove a user
        print("Removing a user...")

    def add_event(self):
        # Implement functionality to add an event
        print("Adding an event...")

    def search_book(self):
        # Implement functionality to search for a book
        print("Searching for a book...")

       