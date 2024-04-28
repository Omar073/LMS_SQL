import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class SignUp(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.db_connection = get_shared_connection()
        self.config(width=800, height=600)

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

        # Role Label and OptionMenu
        role_label = tk.Label(self, text="Role:", font=("Helvetica", 14))
        role_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.role_var = tk.StringVar(self)
        self.role_var.set("User")  # Default role is User
        self.role_optionmenu = tk.OptionMenu(self, self.role_var, "User", "Librarian")
        self.role_optionmenu.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Signup Button
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=self.signup)
        signup_button.grid(row=3, columnspan=2, padx=20, pady=20)

        # Back to Login Button
        back_to_login_button = tk.Button(self, text="Back to Login", font=("Helvetica", 14), command=lambda: controller.show_page(LoginPage))
        back_to_login_button.grid(row=4, columnspan=2, padx=20, pady=10)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        # Perform signup process based on the entered data and selected role
        if username and password:
            if role == "User":
                # Sign up as a regular user
                # Implement user signup functionality here
                messagebox.showinfo("Success", "Sign up as User successful!")
            elif role == "Librarian":
                # Sign up as a librarian
                # Implement librarian signup functionality here
                messagebox.showinfo("Success", "Sign up as Librarian successful!")
            else:
                messagebox.showerror("Error", "Invalid role selected.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")
