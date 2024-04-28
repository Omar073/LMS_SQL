import tkinter as tk
from tkinter import messagebox
# from user_homepage import UserHomePage  # Import the UserHomePage class if needed

class EventsPage(tk.Frame):
    def __init__(self, parent, controller, events):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Display Events
        event_labels = ['Event ID', 'Title', 'Date']
        for i, label_text in enumerate(event_labels):
            label = tk.Label(self, text=label_text, font=('Helvetica', 12, 'bold'))
            label.grid(row=0, column=i, padx=5, pady=5)

        for i, event in enumerate(events, start=1):
            for j, detail in enumerate(event):
                label = tk.Label(self, text=detail)
                label.grid(row=i, column=j, padx=5, pady=5)

        # Attend Button
        attend_button = tk.Button(self, text='Attend', command=self.attend_event)
        attend_button.grid(row=len(events) + 1, columnspan=len(event_labels), pady=10)

        # Back Button
        back_button = tk.Button(self, text='Back', command=lambda: controller.show_page(UserHomePage))
        back_button.grid(row=len(events) + 2, columnspan=len(event_labels), pady=10)

    def attend_event(self):
        # Logic to attend event
        # ...

        messagebox.showinfo('Success', 'You have attended the event')
