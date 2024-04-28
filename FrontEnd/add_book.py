import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class AddBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        self.configure(background="#f0f0f0")  # Set background color

        # Title "Add Book"
        title_label = tk.Label(self, text="Add Book", font=("Helvetica", 24), bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Labels and Entry fields for book details
        tk.Label(self, text="ISBN:", bg="#f0f0f0").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.isbn_entry = tk.Entry(self)
        self.isbn_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Title:", bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Date of Print:", bg="#f0f0f0").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Amount:", bg="#f0f0f0").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Create frames for genre, author, and publisher options
        genre_frame = self.create_dropdown_frame("Genre", row=1, column=4)
        author_frame = self.create_dropdown_frame("Authors", row=2, column=4)
        publisher_frame = self.create_dropdown_frame("Publisher", row=3, column=4)

        # Button to add book
        tk.Button(self, text="Add Book", command=self.add_book, bg="#4CAF50", fg="white", padx=10).grid(row=5, column=3, columnspan=2, padx=20, pady=(20, 10))
        
        tk.Button(self, text="Home", command=self.go_to_homepage, bg="#808080", fg="white", padx=10).grid(row=6, column=3, columnspan=2, padx=20, pady=10)

        # Fetch and populate dropdown menus
        self.fetch_options(genre_frame, "Genre")
        self.fetch_options(author_frame, "Author")
        self.fetch_options(publisher_frame, "Publisher")

    def create_dropdown_frame(self, label, row, column):
        frame = tk.Frame(self, bg="#f0f0f0")  # Set background color
        frame.grid(row=row, column=column, padx=20, pady=10 ,sticky="e")
        tk.Label(frame, text=f"{label}:", bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
        return frame

    def fetch_options(self, frame, option_type):
        try:
            cursor = self.db_connection.cursor()
            if option_type == "Genre":
                cursor.execute(f"SELECT Genre_ID, NAME FROM {option_type}")
            else:
                cursor.execute(f"SELECT SSN, NAME FROM {option_type}")
            options = cursor.fetchall()
            option_names = [option[1] for option in options]
            option_names.append("None")
            option_var = tk.StringVar(frame)
            option_var.set("None")  # Default option
            option_dropdown = tk.OptionMenu(frame, option_var, *option_names)
            option_dropdown.config(font=("Helvetica", 12), width=10)
            option_dropdown.pack(side=tk.LEFT, padx=10)
            setattr(self, f"{option_type.lower()}_var", option_var)  # Save option var for later use
            setattr(self, f"{option_type.lower()}_options", options)  # Save option names and IDs
        except Exception as e:
            print(f"Error fetching {option_type}:", e)
            messagebox.showerror("Error", f"An error occurred while fetching {option_type}")

    def add_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        date_of_print = self.date_entry.get()
        amount = self.amount_entry.get()
        genre_id = self.get_id_from_name(self.genre_var.get(), "genre")
        publisher_id = self.get_id_from_name(self.publisher_var.get(), "publisher")
        author_ids = [self.get_id_from_name(author, "author") for author in self.get_selected_authors()]

        if not isbn or not title or not date_of_print or not amount:
            messagebox.showerror("Error", "ISBN, title, date of print, and amount are required fields")
            return

        try:
            cursor = self.db_connection.cursor()
            # Insert into Book table
            cursor.execute("INSERT INTO Book (ISBN, Title, DateofPrint, amount, Genre_id, Publisher_id) VALUES (?, ?, ?, ?, ?, ?)",
                           (isbn, title, date_of_print, amount, genre_id, publisher_id))
            # Insert into Authors_Book table for each author
            for author_id in author_ids:
                cursor.execute("INSERT INTO Authors_Book (ISBN, author_id) VALUES (?, ?)", (isbn, author_id))
            self.db_connection.commit()
            messagebox.showinfo("Success", "Book added successfully")
            # Clear the entry fields after adding book
            self.isbn_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding the book: {e}")
        finally:
            cursor.close()

    def get_id_from_name(self, name, option_type):
        options = getattr(self, f"{option_type.lower()}_options")
        for option in options:
            if option[1] == name:
                return option[0]
        return None

    def get_selected_authors(self):
        return [self.author_var.get()]

    def go_to_homepage(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)

