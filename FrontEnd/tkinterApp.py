import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

	
		from librarian_homepage import LibrarianHomePage
		from user_homepage import UserHomePage
		from sign_up_page import SignupPage
		from login_page import LoginPage

		for F in (LibrarianHomePage, UserHomePage, SignupPage, LoginPage):

			frame = F(container, self)

			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(LoginPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
