import tkinter as tk
from tkinter import ttk
from add_user import AddUserPage
from remove_user import RemoveUserPage

class LibrarianHomePage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent, width=800, height=600) 
        self.controller = controller
        self.config(width=800, height=600)

        # Create a canvas and scrollable frame
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add Book Card
        add_book_card = self.create_card(scrollable_frame, "Add Book", self.add_book)
        add_book_card.grid(row=0, column=0, padx=10, pady=10)

        # Remove Book Card
        remove_book_card = self.create_card(scrollable_frame, "Remove Book", self.remove_book)
        remove_book_card.grid(row=0, column=1, padx=10, pady=10)

        # Add User Card
        add_user_card = self.create_card(scrollable_frame, "Add User", self.add_user)
        add_user_card.grid(row=1, column=0, padx=10, pady=10)

        # Remove User Card
        remove_user_card = self.create_card(scrollable_frame, "Remove User", self.remove_user)
        remove_user_card.grid(row=1, column=1, padx=10, pady=10)

        # Add Event Card
        add_event_card = self.create_card(scrollable_frame, "Add Event", self.add_event)
        add_event_card.grid(row=2, column=0, padx=10, pady=10)

        # Search Book Card
        search_book_card = self.create_card(scrollable_frame, "Search Book", self.search_book)
        search_book_card.grid(row=2, column=1, padx=10, pady=10)

        # Logout Card
        logout_card = self.create_card(scrollable_frame, "Logout", self.logout)
        logout_card.grid(row=3, columnspan=2, padx=10, pady=10)

    def create_card(self, parent, title, command):
        card = ttk.Button(parent, text=title, command=command, style="Card.TButton" , width=30)
        return card

    def add_book(self):
        print("Adding a book...")

    def remove_book(self):
        print("Removing a book...")

    def add_user(self):
        self.controller.show_page(AddUserPage)
        print("Adding a user...")

    def remove_user(self):
        self.controller.show_page(RemoveUserPage)
        print("Removing a user...")

    def add_event(self):
        print("Adding an event...")

    def search_book(self):
        from search_book_libriran import SearchBookLibriran
        self.controller.show_page(SearchBookLibriran)

    def logout(self):
        from login_page import LoginPage
        self.controller.show_page(LoginPage)



