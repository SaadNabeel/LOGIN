from tkinter import *

root = Tk()
root.title('Login Window')
root.geometry('300x300')
root.config(background="yellow")

l1 = Label(root, text="Login ID", bg="light blue", fg="red", font=('Arial', 15), padx=10, pady=10)
l1.pack()

e1 = Entry(root)
e1.pack(padx=10, pady=5)

l2 = Label(root, text="Password", bg="light green", fg="red", font=('Arial', 15), padx=10, pady=10)
l2.pack()

e2 = Entry(root, show="*")
e2.pack(padx=10, pady=5)

def msg():
    login_id = e1.get()
    password = e2.get()
    m1 = "Login ID:",login_id,"\nPassword:",password,
    l3 = Label(root, text=m1)
    l3.pack()

b1 = Button(root, text="Submit", bg="red", fg="white", command=msg)
b1.pack(padx=10, pady=10)

root.mainloop()
