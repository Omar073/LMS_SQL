import tkinter as tk

def main():
    root = tk.Tk()
    from login_page import LoginPage

    login_page = LoginPage(root )
    root.mainloop()

if __name__ == "__main__":
    main()
