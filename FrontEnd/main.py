import tkinter as tk 
from tkinter import ttk
from settings_page import SettingsPage
from login_page import LoginPage
from librarian_homepage import LibrarianHomePage
from user_homepage import UserHomePage
from sign_up_page import SignUp

  
  
LARGE_FONT= ("Verdana", 12)  
  
  
class SeaofBTCapp(tk.Tk):  

    def __init__(self, *args, **kwargs):  
          
        tk.Tk.__init__(self, *args, **kwargs)  
        container = tk.Frame(self)  
        container.pack_propagate(False)  

        

        container.config(width=1000, height=1000)

  
        container.pack(side="top", fill="both", expand=True)  
  
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)  

        
        self.frames = {}  
  
        for F in (LoginPage, LibrarianHomePage, UserHomePage , SignUp, SettingsPage):
            frame = F(container, self)  
            self.frames[F] = frame  
            frame.config(width=10000, height=10000)
            frame.grid(row=0, column=0, sticky="nsew")  
  
        self.show_frame(LoginPage)  
  
    def show_frame(self, cont):  
        frame = self.frames[cont]  
        frame.tkraise()  

    def show_page(self, page):
        for frame in self.frames.values():
            frame.pack_forget()
        self.show_frame(page)

app = SeaofBTCapp()  
app.mainloop() 
