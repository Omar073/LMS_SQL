import tkinter as tk

class UserHomePage(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent) 
        self.controller = controller
        self.config(width=800, height=600)
      

        # Search Book Button
        self.search_book_button = tk.Button(self, text="Search Book", command=self.search_book)
        self.search_book_button.pack(pady=10)

        # Borrow Book Button
        self.borrow_book_button = tk.Button(self, text="Borrow Book", command=self.borrow_book)
        self.borrow_book_button.pack(pady=10)

        # Attend Event Button
        self.attend_event_button = tk.Button(self, text="Attend Event", command=self.attend_event)
        self.attend_event_button.pack(pady=10)

        # Settings Button
        self.settings_button = tk.Button(self, text="Settings", command=self.settings)
        self.settings_button.pack(pady=10)

        

        # Logout Button
        from login_page import LoginPage
        self.logout_button = tk.Button(self, text="Logout", command= lambda: self.controller.show_frame(LoginPage))
        self.logout_button.pack(pady=10)

    def search_book(self):
        # Implement functionality to search for a book
        print("Searching for a book...")

    def borrow_book(self):
        # Implement functionality to borrow a book
        print("Borrowing a book...")

    def attend_event(self):
        # Implement functionality to attend an event
        print("Attending an event...")

    def settings(self):
        # Implement functionality to access user settings
        print("Accessing settings...")


    def logout(self):
        # Implement functionality to logout
        root = self.winfo_toplevel()
        root.destroy()
        from login_page import LoginPage
        login_page = LoginPage(root)
        root.mainloop()

# def main():
#     root = tk.Tk()
#     user_homepage = UserHomePage()
#     root.mainloop()

# if __name__ == "__main__":
#     main()
