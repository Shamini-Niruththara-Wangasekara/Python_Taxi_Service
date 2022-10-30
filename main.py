
from tkinter import *

from untitled3 import login

isLoged = False;
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def adminLogin():
    top =Toplevel()
    top.title("Admin Login")
    Label(top,text="Admin Login").grid(columnspan=2, row=0, column=0, pady=20)
    Label(top,text="User name").grid(column=0, row=1)
    Label(top, text="password").grid(column=0, row=2)
    paswrd = Entry(top, width=50)
    userName = Entry(top, width=50)
    def admin():
        Loged = login(userName.get(),paswrd.get(),  True)
        if Loged:
            Label(top, text="Success").grid(columnspan=2, column=0, row=4)
        else:
            Label(top, text="Failed").grid(columnspan=2, column=0, row=4)
    btn_login = Button(top, text="Login", command=admin)
    userName.grid(column=1, row=1)
    paswrd.grid(column=1, row=2)
    btn_login.grid(row=3, column=0, columnspan=2)

    Label(top, text="").grid(column=0, row=5, pady=20, columnspan=2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    message = Label(root, text="WELCOME TO SN CAB SERVICE")
    adminLogin = Button(root, text="Admin Login", command=adminLogin)
    message.pack()
    adminLogin.pack()
    mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
