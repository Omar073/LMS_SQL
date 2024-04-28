import tkinter as tk 
from tkinter import ttk
from settings_page import SettingsPage
from login_page import LoginPage
from librarian_homepage import LibrarianHomePage
from user_homepage import UserHomePage
from sign_up_page import SignUp
from search_book_libriran import SearchBookLibriran
from add_user import AddUserPage
from remove_user import RemoveUserPage
from search_book_user import SearchBookUser
from return_borrow_book import ReturnBorrowedBook
from history import HistoryPage
from add_book import AddBook
from add_genre import AddGenre
  
LARGE_FONT= ("Verdana", 12)  
  
  
class SeaofBTCapp(tk.Tk):  

    def __init__(self, *args, **kwargs):  
          
        tk.Tk.__init__(self, *args, **kwargs)  
        container = tk.Frame(self, height= 50, width=50)  


        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1 , minsize= 800)  
        container.grid_columnconfigure(0, weight=1 , minsize= 800)  

        
        self.frames = {}  
  


        for F in (LoginPage, LibrarianHomePage, UserHomePage , SignUp ,SearchBookLibriran,AddUserPage,RemoveUserPage,ReturnBorrowedBook,HistoryPage, SearchBookUser,AddBook,AddGenre):
            frame = F(container, self)
            self.frames[F] = frame
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
# if __name__ == "__main__":
#     main()

# Path: FrontEnd/login_page.py
