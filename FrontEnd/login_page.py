import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

LARGE_FONT= ("Verdana", 12)

class LoginPage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.db_connection = get_shared_connection()

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
        from librarian_homepage import LibrarianHomePage
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=lambda: controller.show_page(LibrarianHomePage))
        signup_button.grid(row=3, columnspan=2, padx=20, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            cursor = self.db_connection.cursor()

            # Execute the SQL function for sign-in
            cursor.execute("SELECT * FROM LibrarianSignInFunction(?, ?)", (username, password))
            rows = cursor.fetchall()

            if rows:
                role = rows[0][0]  # Role is the first column of the result set
                if role == 'Librarian':
                    print("Login successful as Librarian")
                    # Handle successful login as Librarian
                elif role == 'Member':
                    print("Login successful as Member")
                    # Handle successful login as Member
                else:
                    print("Login failed. Invalid username or password")
                    messagebox.showerror("Login Failed", "Invalid username or password")
            else:
                print("Login failed. Invalid username or password")
                messagebox.showerror("Login Failed", "Invalid username or password")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()

    def show_signup_page(self):
        # Handle navigation to the signup page
        pass  # Implement this method as needed
