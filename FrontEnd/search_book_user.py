# Python code

import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkLabel, CTkEntry, CTkButton
from db_connection import get_shared_connection

class SearchBookLibriran(tk.Frame):
    def __init__(frame, parent, controller):
        tk.Frame.__init__(frame, parent)
        frame.controller = controller
        frame.db_connection = get_shared_connection()

        from librarian_homepage import LibrarianHomePage
        back_button = CTkButton(frame, text="Back", command=lambda: controller.show_page(LibrarianHomePage))
        back_button.grid(row=0, column=0, padx=20, pady=10, columnspan=4)

        # Search Label and Entry
        search_label = CTkLabel(frame, text="Search Book:", font=("Helvetica", 14))
        search_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        frame.search_entry = CTkEntry(frame, font=("Helvetica", 14))
        frame.search_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        search_button = CTkButton(frame, text="Search", font=("Helvetica", 14), command=frame.search_books)
        search_button.grid(row=1, column=2, padx=20, pady=10)

        # Sort Options
        sort_label = CTkLabel(frame, text="Sort By:", font=("Helvetica", 14))
        sort_label.grid(row=1, column=3, padx=20, pady=10, sticky="e")
        frame.sort_option = tk.StringVar(frame)
        frame.sort_option.set("None")  # Default option
        sort_options = ["None", "Ascending", "Descending"]
        sort_dropdown = tk.OptionMenu(frame, frame.sort_option, *sort_options)
        sort_dropdown.config(font=("Helvetica", 14), width=10)
        sort_dropdown.grid(row=1, column=4, padx=20, pady=10)

        # Fetch and populate Genre dropdown
        frame.genre_options = []
        try:
            cursor = frame.db_connection.cursor()
            cursor.execute("SELECT NAME FROM Genre")
            genres = cursor.fetchall()
            for genre in genres:
                frame.genre_options.append(genre[0])
            frame.genre_options.append("None")

        except Exception as e:
            print("Error fetching genres:", e)
            messagebox.showerror("Error", "An error occurred while fetching genres")
        frame.genre_option = tk.StringVar(frame)
        frame.genre_option.set("None")  # Default option
        genre_dropdown = tk.OptionMenu(frame, frame.genre_option, *frame.genre_options)
        genre_dropdown.config(font=("Helvetica", 14), width=15)
        genre_dropdown.grid(row=1, column=5, padx=20, pady=10)

        # Fetch and populate Publisher dropdown
        frame.publisher_options = []
        try:
            cursor = frame.db_connection.cursor()
            cursor.execute("SELECT NAME FROM Publisher")
            publishers = cursor.fetchall()
            for publisher in publishers:
                frame.publisher_options.append(publisher[0])
            
            frame.publisher_options.append("None")
        except Exception as e:
            print("Error fetching publishers:", e)
            messagebox.showerror("Error", "An error occurred while fetching publishers")
        frame.publisher_option = tk.StringVar(frame)
        frame.publisher_option.set("None")  # Default option
        publisher_dropdown = tk.OptionMenu(frame, frame.publisher_option, *frame.publisher_options)
        publisher_dropdown.config(font=("Helvetica", 14), width=15)
        publisher_dropdown.grid(row=1, column=6, padx=20, pady=10)

        # Create a scrollable frame for displaying books
        frame.scrollable_frame = tk.Frame(frame)
        frame.scrollable_frame.grid(row=2, column=0, columnspan=7, padx=20, pady=10)
        frame.canvas = tk.Canvas(frame.scrollable_frame, borderwidth=0, width=800, height=600)
        frame.scrollbar = tk.Scrollbar(frame.scrollable_frame, orient="vertical", command=frame.canvas.yview)
        frame.scrollable_frame_inner = tk.Frame(frame.canvas)
        frame.scrollable_frame_inner.bind("<Configure>", lambda e: frame.canvas.configure(scrollregion=frame.canvas.bbox("all")))
        frame.canvas.create_window((0, 0), window=frame.scrollable_frame_inner, anchor="nw")
        frame.canvas.configure(yscrollcommand=frame.scrollbar.set)
        frame.canvas.pack(side="left", fill="both", expand=True)  # Updated pack options
        frame.scrollbar.pack(side="right", fill="y")

        # Load all books initially
        frame.load_all_books()

    def load_all_books(frame):
        try:
            cursor = frame.db_connection.cursor()
            cursor.execute("EXEC SearchBooks @SearchTerm='', @Genre='', @Publisher='', @SortOption='None'")
            books = cursor.fetchall()

            frame.display_books(books)

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while loading books")

    def search_books(frame):
        # Clear previous search results
        for widget in frame.scrollable_frame_inner.winfo_children():
            widget.destroy()

        search_term = frame.search_entry.get()
        selected_genre = frame.genre_option.get()
        selected_publisher = frame.publisher_option.get()
        sort_option = frame.sort_option.get()

        try:
            cursor = frame.db_connection.cursor()
            cursor.execute("EXEC SearchBooks @SearchTerm=?, @Genre=?, @Publisher=?, @SortOption=?", 
                           (search_term, selected_genre, selected_publisher, sort_option))
            books = cursor.fetchall()

            frame.display_books(books)

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while searching for books")

    def display_books(frame, books):
        # Display books in a grid shape
        for i, book in enumerate(books):
            book_frame = tk.Frame(frame.scrollable_frame_inner, relief=tk.RIDGE, borderwidth=2)
            book_frame.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")

            # Book Name Label
            book_name_label = tk.Label(book_frame, text="Book Name: " + book[1], font=("Helvetica", 12))
            book_name_label.pack(anchor="w", padx=10, pady=5)

            # Quantity Label
            quantity_label = tk.Label(book_frame, text="Quantity: " + str(book[1]), font=("Helvetica", 12))
            quantity_label.pack(anchor="w", padx=10, pady=5)

            # Delete Button
            delete_button = tk.Button(book_frame, text="Delete", command=lambda book_name=book[1]: frame.delete_book(book_name))
            delete_button.pack(anchor="e", padx=10, pady=5)

        # Update the scroll region after adding books
        frame.canvas.configure(scrollregion=frame.canvas.bbox("all"))

    def delete_book(frame, book_name):
        # Implement functionality to delete the book
        print("Deleting book:", book_name)


# Test the SearchBookLibriran frame
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchBookLibriran(root, None)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
