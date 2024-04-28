import tkinter as tk
from tkinter import messagebox
import logging  # Import the logging module
from db_connection import get_shared_connection

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

LARGE_FONT = ("Verdana", 12)

class LoginPage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.db_connection = get_shared_connection()
        # increase the width of the frame and set the height
        self.config(width=1000, height=1000)

        # Username Label and Entry
        username_label = tk.Label(self, text="Username:", font=("Helvetica", 14))
        username_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # Password Label and Entry
        password_label = tk.Label(self, text="Password:", font=("Helvetica", 14))
        password_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 14))
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Login Button
        login_button = tk.Button(self, text="Login", font=("Helvetica", 14), command=self.login)
        login_button.grid(row=2, columnspan=2, padx=20, pady=20)

        # Signup Button
        from sign_up_page import SignUp 
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=lambda: controller.show_page(SignUp))
        signup_button.grid(row=3, columnspan=2, padx=20, pady=10)

    def login(self):
        name = self.username_entry.get()  # Get the name instead of the username
        password = self.password_entry.get()

        if not name or not password:
            messagebox.showerror("Login Failed", "Name and password are required")
            return

        try:
            cursor = self.db_connection.cursor()

            # Execute the SQL function for sign-in
            cursor.execute("SELECT * FROM login1(?, ?)", (name, password))
            rows = cursor.fetchall()

            if rows:
                print("Login successful")
                from user_homepage import UserHomePage  # Import user homepage
                self.controller.show_page(UserHomePage)  # Redirect to user homepage
            else:
                print("Login failed. Invalid name or password")
                messagebox.showerror("Login Failed", "Invalid name or password")

        except Exception as e:
            print("Error:", e)
            logging.error("An error occurred during login: %s", e)  # Log the error
        finally:
            cursor.close()

    def show_signup_page(self):
        pass
