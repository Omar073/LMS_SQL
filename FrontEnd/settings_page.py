import tkinter as tk
from tkinter import messagebox
import pyodbc

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller, member_id):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.member_id = member_id

        # Call SQL function to retrieve member info
        member_info = self.get_member_info()

        # Display member info
        info_labels = ['ID', 'Name', 'Gender', 'Street Name', 'Building Number', 'City', 'Email']
        for i, label_text in enumerate(info_labels):
            label = tk.Label(self, text=label_text, font=('Helvetica', 12, 'bold'))
            label.grid(row=i, column=0, padx=5, pady=5)
            info = tk.Label(self, text=member_info[i])
            info.grid(row=i, column=1, padx=5, pady=5)

        # Back Button
        back_button = tk.Button(self, text='Back', command=lambda: controller.show_page(UserHomePage))
        back_button.grid(row=len(info_labels), columnspan=2, pady=10)

    def get_member_info(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=your_server;'
                                  'Database=your_database;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()

            # Execute SQL function to get member info
            cursor.execute("SELECT * FROM GetMemberInfo(?)", (self.member_id,))
            row = cursor.fetchone()

            if row:
                return row
            else:
                messagebox.showerror("Error", "Member not found")
                return None

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while retrieving member info")
            return None

        finally:
            cursor.close()
            conn.close()
