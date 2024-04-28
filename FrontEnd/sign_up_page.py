import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection
from login_page import LoginPage

LARGE_FONT = ("Verdana", 12)

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()
        # Increase the width of the frame and set the height
        self.config(width=1000, height=1000)

      

        # Password Label and Entry
        password_label = tk.Label(self, text="Password:", font=("Helvetica", 14))
        password_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 14))
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Email Label and Entry
        email_label = tk.Label(self, text="Email:", font=("Helvetica", 14))
        email_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.email_entry = tk.Entry(self, font=("Helvetica", 14))
        self.email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Name Label and Entry
        name_label = tk.Label(self, text="Name:", font=("Helvetica", 14))
        name_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.name_entry = tk.Entry(self, font=("Helvetica", 14))
        self.name_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Gender Label and Entry
        gender_label = tk.Label(self, text="Gender:", font=("Helvetica", 14))
        gender_label.grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.gender_entry = tk.Entry(self, font=("Helvetica", 14))
        self.gender_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Street Name Label and Entry
        street_label = tk.Label(self, text="Street Name:", font=("Helvetica", 14))
        street_label.grid(row=5, column=0, padx=20, pady=10, sticky="e")
        self.street_entry = tk.Entry(self, font=("Helvetica", 14))
        self.street_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # Building Number Label and Entry
        building_label = tk.Label(self, text="Building Number:", font=("Helvetica", 14))
        building_label.grid(row=6, column=0, padx=20, pady=10, sticky="e")
        self.building_entry = tk.Entry(self, font=("Helvetica", 14))
        self.building_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        # City Label and Entry
        city_label = tk.Label(self, text="City:", font=("Helvetica", 14))
        city_label.grid(row=7, column=0, padx=20, pady=10, sticky="e")
        self.city_entry = tk.Entry(self, font=("Helvetica", 14))
        self.city_entry.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # Signup Button
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=self.signup)
        signup_button.grid(row=8, columnspan=2, padx=20, pady=20)

    def signup(self):
    # Retrieve data from entry fields
      password = self.password_entry.get()
      email = self.email_entry.get()
      name = self.name_entry.get()
      gender = self.gender_entry.get()
      street_name = self.street_entry.get()
      building_number = self.building_entry.get()
      city = self.city_entry.get()

      # Check if any of the required fields are empty
      if not password or not email or not name:
          messagebox.showerror("Signup Failed", "All fields are required")
          return

      try:
          cursor = self.db_connection.cursor()

          # Prepare the parameters
          params = [password, email, name, gender, street_name, building_number, city]

          # Execute the SQL procedure for signup
          cursor.execute("EXEC registeruser ?, ?, ?, ?, ?, ?, ?", params)  # Corrected procedure name
          self.db_connection.commit()

          # If execution reaches here, signup was successful
          messagebox.showinfo("Signup Successful", "User registered successfully")
          self.controller.show_page(LoginPage)  # Navigate back to login page after signup

      except Exception as e:
          print("Error:", e)
          messagebox.showerror("Signup Failed", "An error occurred during signup")

      finally:
          cursor.close()

