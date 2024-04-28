import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

LARGE_FONT= ("Verdana", 12)


LoogedInUserID = -1
class LoginPage(tk.Frame):  

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Username Label and Entry
        username_label = tk.Label(self, text="Username:", font=("Helvetica", 14))
        username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Password Label and Entry
        password_label = tk.Label(self, text="Password:", font=("Helvetica", 14))
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 14))
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")

        # Login Button
        login_button = tk.Button(self, text="Login", font=("Helvetica", 14), command=self.login)
        login_button.place(relx=0.5, rely=0.6, anchor="center")

        # Signup Button
        from sign_up_page import SignUp as Sig
        signup_button = tk.Button(self, text="Signup", font=("Helvetica", 14), command=lambda: controller.show_page(Sig))
        signup_button.place(relx=0.5, rely=0.65, anchor="center")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Login Failed", "Username and password are required")
            return
        

        try:
            cursor = self.db_connection.cursor()

            # Execute the SQL function for sign-in
            cursor.execute("SELECT * FROM LibrarianSignInFunction(?, ?)", (username, password))
            rows = cursor.fetchall()

            global LoogedInUserID

            if rows:
                role = rows[0][0]  # Role is the first column of the result set

                if role == 'Librarian':
                    print("Login successful as Librarian")

                    LoogedInUserID = rows[0][1]

                    from librarian_homepage import LibrarianHomePage
                    self.controller.show_page(LibrarianHomePage)
                elif role == 'Member':

                    print("Login successful as Member")
                    from user_homepage import UserHomePage
                    
                    LoogedInUserID = rows[0][1]

                    print("Logged in user ID login page:", LoogedInUserID)
                    self.controller.show_page(UserHomePage)
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
        pass  
