import tkinter as tk
from tkinter import messagebox
from db_connection import get_shared_connection

class RemoveUserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db_connection = get_shared_connection()

        # Label and dropdown menu for user IDs
        tk.Label(self, text="Select User ID:").grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.selected_user_id = tk.StringVar(self)
        self.selected_user_id.set("Select User ID")  # Default prompt text
        self.user_id_dropdown = tk.OptionMenu(self, self.selected_user_id, "Select User ID")
        self.user_id_dropdown.config(width=20)  # Set dropdown width
        self.user_id_dropdown.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # Button to remove user
        tk.Button(self, text="Remove User", command=self.remove_user).grid(row=1, columnspan=2, padx=20, pady=20)

        # Button to go back to the librarian homepage
        tk.Button(self, text="Home", command=self.go_to_homepage).grid(row=2, columnspan=2, padx=20, pady=20)

        # Populate dropdown with user IDs
        self.populate_user_ids()

        # Bind a callback to the <Button-1> event to update the dropdown menu whenever it is clicked
        self.user_id_dropdown.bind("<Button-1>", lambda event: self.populate_user_ids())

    def populate_user_ids(self, *args):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT ID FROM Member")
            user_ids = cursor.fetchall()
            user_id_list = [str(user[0]) for user in user_ids]
            self.user_id_dropdown['menu'].delete(0, 'end')
            for id in user_id_list:
                self.user_id_dropdown['menu'].add_command(label=id, command=lambda id=id: self.selected_user_id.set(id))
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()


    def remove_user(self):
        user_id = self.selected_user_id.get()

        if user_id == "Select User ID":
            messagebox.showerror("Error", "Please select a user ID")
            return

        try:
            cursor = self.db_connection.cursor()
            # Check if the user ID exists in the Member table
            cursor.execute("SELECT ID FROM Member WHERE ID=?", (user_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", "User ID not found in the Member table")
               
                return
            
            # If the user ID exists, proceed to delete
            cursor.execute("DELETE FROM Member WHERE ID=?", (user_id,))
            self.db_connection.commit()
            messagebox.showinfo("Success", "User removed successfully")
            # Repopulate dropdown after removing user
            self.populate_user_ids()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            print(e)
        finally:
            cursor.close()


    def go_to_homepage(self):
        from librarian_homepage import LibrarianHomePage
        self.controller.show_page(LibrarianHomePage)
