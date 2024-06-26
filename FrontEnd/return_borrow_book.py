import datetime
import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

LARGE_FONT = ("Verdana", 12)

class ReturnBorrowedBook(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()
        # Increase the width of the frame and set the height
        self.config(width=1000, height=1000)

        # refresh button
        refresh_button = tk.Button(self, text="Refresh", font=("Helvetica", 14), command=self.refresh)
        refresh_button.pack(pady=10)

        # Back Button
        from user_homepage import UserHomePage
        back_button = tk.Button(self, text="Back", font=("Helvetica", 14), command=lambda: controller.show_page(UserHomePage))
        back_button.pack(pady=10)
        
        # Initialize a list to store the ISBNs of previously displayed borrowed books
        self.displayed_books_isbn = []

        # Display initially borrowed books
        self.display_borrowed_books()

    def return_book(self, isbn):
        try:
            # Get the current date
            current_date = datetime.date.today()

            # Update the return date for the borrowed book
            cursor = self.db_connection.cursor()
            from login_page import LoogedInUserID

            cursor.execute("UPDATE Borrowing_Member SET return_date = ? WHERE ISBN = ? AND member_id = ? AND return_date IS NULL", ("2024-04-29", isbn, LoogedInUserID)) 
            self.db_connection.commit()

            # Display a success message
            messagebox.showinfo("Success", "Book returned successfully.")
            
            # Refresh the displayed borrowed books
            self.refresh()

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while returning the book")

        finally:
            cursor.close()

    def display_borrowed_books(self):
        try:
            cursor = self.db_connection.cursor()

            # Fetch the borrowed books for the current user with no return date
            from login_page import LoogedInUserID
            cursor.execute("SELECT BM.ISBN, M.Name, B.Title, BM.borrow_date FROM Borrowing_Member BM INNER JOIN Member M ON BM.member_id = M.Id INNER JOIN Book B ON BM.ISBN = B.ISBN  WHERE BM.return_date IS NULL AND BM.member_id = ? ;", (LoogedInUserID,))
            borrowed_books = cursor.fetchall()

            print("Borrowed books:", borrowed_books)

            # Display borrowed books that are not previously displayed
            for book in borrowed_books:
                if book[0] not in self.displayed_books_isbn:
                    self.displayed_books_isbn.append(book[0])
                    # Create a frame for each book card
                    book_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
                    book_frame.pack(pady=5, padx=10, fill=tk.BOTH)

                    # Display book details
                    book_label = tk.Label(book_frame, text=f"User ID: {LoogedInUserID}, Name: {book[1]}, Book Title: {book[2]}, Borrow Date: {book[3]}", font=("Helvetica", 12))
                    book_label.pack(side=tk.LEFT, padx=10, pady=5)

                    # Create a return button for the book
                    return_button = tk.Button(book_frame, text="Return", command=lambda isbn=book[0]: self.return_book(isbn))
                    return_button.pack(side=tk.RIGHT, padx=10, pady=5)

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while fetching borrowed books")

        finally:
            cursor.close()

    def refresh(self):
        # Clear the frame and reset the list of displayed ISBNs
        for widget in self.winfo_children():
            widget.destroy()
        self.displayed_books_isbn.clear()
        # Display newly borrowed books
        self.display_borrowed_books()

        from user_homepage import UserHomePage

        self.return_button = tk.Button(self, text="Home", font=("Helvetica", 14), command= lambda: self.controller.show_page(UserHomePage))
        self.return_button.pack(pady=10)

        self.refresh_button = tk.Button(self, text="Refresh", font=("Helvetica", 14), command=self.refresh)
        self.refresh_button.pack(pady=10)
