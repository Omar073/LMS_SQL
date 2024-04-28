import tkinter as tk
from tkinter import ttk
from add_user import AddUserPage
from remove_user import RemoveUserPage

class LibrarianHomePage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.config(bg="lightblue")  # Set background color

        # Title label
        title_label = tk.Label(self, text="Librarian Home Page", font=("Helvetica", 24), bg="lightblue")
        title_label.pack(pady=(20, 10))

        # Create a canvas and scrollable frame
        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add Book Card
        add_book_card = self.create_card(scrollable_frame, "Add Book", self.add_book)
        add_book_card.pack(padx=10, pady=10, fill='x')

        # Remove Book Card
        remove_book_card = self.create_card(scrollable_frame, "Remove Book", self.remove_book)
        remove_book_card.pack(padx=10, pady=10, fill='x')

        # Add User Card
        add_user_card = self.create_card(scrollable_frame, "Add User", self.add_user)
        add_user_card.pack(padx=10, pady=10, fill='x')

        #Add Genre Card
        add_genre_card = self.create_card(scrollable_frame, "Add Genre", self.add_genre)
        add_genre_card.pack(padx=10, pady=10, fill='x')

        # Remove User Card
        remove_user_card = self.create_card(scrollable_frame, "Remove User", self.remove_user)
        remove_user_card.pack(padx=10, pady=10, fill='x')

        # Add Event Card
        add_event_card = self.create_card(scrollable_frame, "Add Event", self.add_event)
        add_event_card.pack(padx=10, pady=10, fill='x')

        # Search Book Card
        search_book_card = self.create_card(scrollable_frame, "Search Book", self.search_book)
        search_book_card.pack(padx=10, pady=10, fill='x')

        # Logout Card
        logout_card = self.create_card(scrollable_frame, "Logout", self.logout)
        logout_card.pack(padx=10, pady=10, fill='x')

    def create_card(self, parent, title, command):
        card = tk.Button(parent, text=title, command=command, font=("Helvetica", 14), bg="#f0f0f0", relief="groove", width=30)
        return card

    def add_book(self):
        from add_book import AddBook
        self.controller.show_page(AddBook)

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
    
    def add_genre(self):
        from add_genre import AddGenre
        self.controller.show_page(AddGenre)
