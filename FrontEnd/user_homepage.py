import tkinter as tk

from events_page import EventsPage
from settings_page import SettingsPage

class UserHomePage(tk.Frame):  
    
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.config(bg="lightblue")  # Set background color

        # Title label
        title_label = tk.Label(self, text="User Home Page", font=("Helvetica", 24), bg="lightblue")
        title_label.pack(pady=(20, 10))

        # Search Book Button
        from search_book_user import SearchBookUser
        search_book_button = tk.Button(self, text="Search Book", command=lambda: self.controller.show_page(SearchBookUser), width=20)
        search_book_button.pack(pady=10)

        # Borrow History Button
        from history import HistoryPage
        borrow_history_button = tk.Button(self, text="Borrow History", command=lambda: self.controller.show_page(HistoryPage), width=20)
        borrow_history_button.pack(pady=10)




        # Return Book Button
        from return_borrow_book import ReturnBorrowedBook
        return_book_button = tk.Button(self, text="Return Book", command=lambda: self.controller.show_page(ReturnBorrowedBook), width=20)
        return_book_button.pack(pady=10)

        # Logout Button
        from login_page import LoginPage
        logout_button = tk.Button(self, text="Logout",  width=20, command=lambda: self.controller.show_page(LoginPage))
        logout_button.pack(pady=10)

    def attend_event(self):
        # Implement functionality to attend an event
        print("Attending an event...")
        self.controller.show_page(EventsPage)

    def settings(self):
        # Implement functionality to access  user settings
        print("Accessing settings...")
        self.controller.show_page(SettingsPage)

    def logout(self):
        # Implement functionality to logout

        self.controller.show_frame(LoginPage)
