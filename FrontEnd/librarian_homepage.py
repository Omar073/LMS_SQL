import tkinter as tk

class LibrarianHomePage(tk.Tk):
    def __init__(self, master):
        super().__init__()
        self.title("Librarian Homepage")
        self.geometry("800x600")
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        # Add Book Button
        self.add_book_button = tk.Button(self, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=10)

        # Remove Book Button
        self.remove_book_button = tk.Button(self, text="Remove Book", command=self.remove_book)
        self.remove_book_button.pack(pady=10)

        # Add User Button
        self.add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=10)

        # Remove User Button
        self.remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        self.remove_user_button.pack(pady=10)

        # Add Event Button
        self.add_event_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_event_button.pack(pady=10)

        # Search Book Button
        self.search_book_button = tk.Button(self, text="Search Book", command=self.search_book)
        self.search_book_button.pack(pady=10)

        # Logout Button
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)


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
        
    def logout(self):
        # Check if the application window still exists
        if tk._default_root:
            # If the window exists, destroy it
            root = self.winfo_toplevel()
            root.destroy()
            # Create a new Tkinter window for the login page
            root = tk.Tk()
            from login_page import LoginPage as Log
            login_page = Log(root)
            root.mainloop()
