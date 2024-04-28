import tkinter as tk
from tkinter import ttk
from user_homepage import UserHomePage
from db_connection import get_shared_connection

import pyodbc  # Assuming you're using pyodbc for database connection

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        self.db_connection = get_shared_connection()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Create a label to display the borrowed books
        self.books_label = tk.Label(self, text="Books:")
        self.books_label.pack(pady=10)

        # Add a button to load history
        load_button = tk.Button(self, text="Load History", command=self.load_history)
        load_button.pack(pady=10)
        
        # Add a button to go back to the user homepage
        back_button = tk.Button(self, text="Back to Homepage", command=self.back_to_homepage)
        back_button.pack(pady=10)
        
    def load_history(self):
        try:
            # Create a cursor object
            cursor = self.db_connection.cursor()
            
            # Call the stored procedure to retrieve borrowing history
            from login_page import LoogedInUserID  
            cursor.execute("EXEC GetUserBorrowHistory @UserId=?", (LoogedInUserID,))
            history_rows = cursor.fetchall()

            # Format the borrowed books as a string
            books_string = "Books: ["
            for i, row in enumerate(history_rows):
                if i != 0:
                    books_string += ", "
                books_string += str(row)
            books_string += "]"  

            # Display the borrowed books in the label
            self.books_label.config(text=books_string)

        except Exception as e:
            # Handle any errors
            print("Error:", e)

        finally:
            # Close the cursor
            cursor.close()
        
    def back_to_homepage(self):
        self.controller.show_frame(UserHomePage)
