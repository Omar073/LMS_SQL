import tkinter as tk
from login_page import LoginPage, show_signup_page

def main():
    root = tk.Tk()
    login_page = LoginPage(root, show_signup_page)
    root.mainloop()

if __name__ == "__main__":
    main()
