import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkLabel, CTkEntry, CTkButton
from db_connection import get_shared_connection

class SignUp(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent) 
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

        # Login Button
        login_button = tk.Button(self, text="Login", font=("Helvetica", 14))
        login_button.grid(row=2, columnspan=2, padx=20, pady=20)

        # Signup Button
        from login_page import LoginPage
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=lambda: controller.show_page(LoginPage))
        signup_button.grid(row=3, columnspan=2, padx=20, pady=10)




       