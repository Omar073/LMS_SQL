import tkinter as tk
from customtkinter import CTkLabel, CTkEntry, CTkButton
from sign_up_page import SignupPage
from db_connection import get_shared_connection  # Import the database connection function

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.db_connection = get_shared_connection()

        self.create_widgets()

    def create_widgets(self):
        self.master.title("Login")
        self.master.geometry("800x600")  # Larger screen size

        # Username Label and Entry
        self.username_label = CTkLabel(self.master, text="Username:", font=("Helvetica", 14))
        self.username_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = CTkEntry(self.master, font=("Helvetica", 14))
        self.username_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Password Label and Entry
        self.password_label = CTkLabel(self.master, text="Password:", font=("Helvetica", 14))
        self.password_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = CTkEntry(self.master, show="*", font=("Helvetica", 14))
        self.password_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Login Button
        self.login_button = CTkButton(self.master, text="Login", font=("Helvetica", 14), command=self.login)
        self.login_button.grid(row=3, columnspan=2, padx=20, pady=20)

        # Signup Button
        self.signup_button = CTkButton(self.master, text="Signup", font=("Helvetica", 14), command=self.show_signup_page)
        self.signup_button.grid(row=4, columnspan=2, padx=20, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Librarian WHERE Staff_ID = ? AND password = ?"
            cursor.execute(query, (username, password))
            row = cursor.fetchone()

            if row:
                print("Login successful")
                # Implement the logic to navigate to the next page or perform other actions upon successful login
            else:
                print("Login failed. Invalid username or password")
                # You can display a message to the user indicating login failure

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            self.db_connection.close()

    def show_signup_page(self):
        # Get the Tkinter root window
        root = self.winfo_toplevel()
        # Destroy the root window (which includes all its child widgets, including the login page)
        root.destroy()

        # Create a new Tkinter window for the SignupPage
        root = tk.Tk()
        signup_page = SignupPage(root, self.show_login_page)
        root.mainloop()



    def show_login_page(self):
        # Close the current signup page
        self.master.destroy()
        # Create a new Tkinter window for the LoginPage
        root = tk.Tk()
        login_page = LoginPage(root, self.show_signup_page_callback)
        root.mainloop()

def main():
    root = tk.Tk()
    login_page = LoginPage(root, None)  # Pass None as the show_signup_page_callback initially
    root.mainloop()

if __name__ == "__main__":
    main()
