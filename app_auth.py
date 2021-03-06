from tkinter import * 
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import os
import bcrypt

app = tk.ThemedTk() 
app.get_themes()
app.set_theme("yaru")
app.iconbitmap(r'libmanager.ico')  #restored to 1st commit code
app.title("login")

salt = b'$2b$12$itFgvfAw3zo0kHnzwfoRlO'
hashed_pw = bcrypt.hashpw('vps$lib'.encode('utf-8'),salt)

def Login():
    x = password_unsecured.get().encode('utf-8')
    if hashed_pw == bcrypt.hashpw(x,hashed_pw):

        try:
             print("correct password was entered.")
             messagebox.showinfo("Login Successful","You have successfully logged in.")
             app.destroy()
             os.system(r'main.py')
        except:
            messagebox.showerror("an error has error occured")
    else:
        messagebox.showwarning("Incorrect Password","The password you entered is incorrected")


txt_label = ttk.Label(app,text="Enter Password",font=('bold',12))
txt_label.grid(row=0,column=0,padx=15,pady=10)

password_unsecured = StringVar()
password_label = ttk.Entry(app,textvariable=password_unsecured,show="*")
password_label.grid(row=1,column=0,padx=15,pady=10)


Login_btn = ttk.Button(app,text="Login",command=Login)
Login_btn.grid(row=2,column=0,pady=10,padx=15)

app.mainloop()
