import tkinter as tk
import pyodbc
from db_connection import connect

class LoginPage(tk.Frame):
    def __init__(self, master, show_signup_page_callback):
        super().__init__(master)
        self.master = master
        self.show_signup_page_callback = show_signup_page_callback
        self.db_connection = connect()  # Get the database connection

        self.create_widgets()

    def create_widgets(self):
        self.master.title("Login")
        self.master.geometry("300x200")

        # Username Label and Entry
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login Button
        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Signup Button
        self.signup_button = tk.Button(self.master, text="Signup", command=self.show_signup_page_callback)
        self.signup_button.grid(row=3, columnspan=2, padx=5, pady=5)

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

        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()

def show_signup_page():
    # Placeholder function to be implemented
    print("Show signup page")
