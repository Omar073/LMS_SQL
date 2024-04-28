import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkLabel, CTkEntry, CTkButton
from db_connection import get_shared_connection

class SignUp(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent) 
        self.controller = controller
        self.db_connection = get_shared_connection()


        self.master.title("Signup")
        self.master.geometry("800x600")  # Larger screen size

        # Logo
        self.logo_label = CTkLabel(self.master, text="Your Logo", font=("Helvetica", 20))
        self.logo_label.grid(row=0, columnspan=2, pady=20)

        # Staff ID Label and Entry
        self.staff_id_label = CTkLabel(self.master, text="Staff ID:", font=("Helvetica", 14))
        self.staff_id_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.staff_id_entry = CTkEntry(self.master, font=("Helvetica", 14))
        self.staff_id_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Name Label and Entry
        self.name_label = CTkLabel(self.master, text="Name:", font=("Helvetica", 14))
        self.name_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.name_entry = CTkEntry(self.master, font=("Helvetica", 14))
        self.name_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Password Label and Entry
        self.password_label = CTkLabel(self.master, text="Password:", font=("Helvetica", 14))
        self.password_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = CTkEntry(self.master, show="*", font=("Helvetica", 14))
        self.password_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Email Label and Entry
        self.email_label = CTkLabel(self.master, text="Email:", font=("Helvetica", 14))
        self.email_label.grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.email_entry = CTkEntry(self.master, font=("Helvetica", 14))
        self.email_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Signup Button
        self.signup_button = CTkButton(self.master, text="Signup", font=("Helvetica", 14), command=self.signup)
        self.signup_button.grid(row=5, columnspan=2, padx=20, pady=20)

        # Login Button
        self.login_button = CTkButton(self.master, text="Login", font=("Helvetica", 14), command=self.show_login_page_callback)
        self.login_button.grid(row=6, columnspan=2, padx=20, pady=10)

    def signup(self):
        staff_id = self.staff_id_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        try:
            cursor = self.db_connection.cursor()

            # Execute the SQL function for sign-in
            cursor.execute("SELECT * FROM LibrarianSignInFunction(?, ?)", ("l", password))
            rows = cursor.fetchall()

            if rows:
                role = rows[0][0]  # Role is the first column of the result set
                if role == 'Librarian':
                    print("Login successful as Librarian")
                    # Implement navigation logic for librarian homepage
                elif role == 'Member':
                    print("Login successful as Member")
                    # Implement navigation logic for member homepage
                else:
                    print("Login failed. Invalid username or password")
                    # You can display a message to the user indicating login failure
            else:
                print("Login failed. Invalid username or password")
                # You can display a message to the user indicating login failur
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()

def show_login_page():
    # Placeholder function to be implemented
    print("Show login page")

