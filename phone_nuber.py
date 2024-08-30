from tkinter import *
import mysql.connector
from tkinter import ttk
import tkinter as tk


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "phone_number"
)

cursor = mydb.cursor()


def register_user(user, phone_number, i1, i2):
    q = f"INSERT INTO `nazli`(`name`, `phone_number`) VALUES ('{user}','{phone_number}')"
    cursor.execute(q)
    mydb.commit()

def delete_user(user, phone_number, i1, i2):
    q = f"DELETE FROM `nazli` WHERE `name` = '{user}' AND `phone_number` = '{phone_number}'"
    cursor.execute(q)
    mydb.commit()



q = "SELECT * FROM `nazli` WHERE 1"
cursor.execute(q)
result = cursor.fetchall()

window =  tk.Tk()
window.title("Phone Number")
window.geometry("800x500")
window.resizable(False, False)
name = StringVar()
phone_number = StringVar()
name_delete = StringVar()
phone_number_delete = StringVar()


lab_name = Label(window, text="Name").place(x=10, y=10)
lab_name_delete = Label(window, text="Name").place(x=350, y=10)
lab_phone_number_delete = Label(window, text="Phone Number").place(x=300, y=50)
entry_name_delete = Entry(window, textvariable=name_delete).place(x=400, y=10)
entry_phone_number_delete = Entry(window, textvariable=phone_number_delete).place(x=400, y=50)
lab_phone_number = Label(window, text="Phone Number").place(x=10, y=50)
entry_name = Entry(window, textvariable=name).place(x=100, y=10)
entry_phone_number = Entry(window, textvariable=phone_number).place(x=100, y=50)
btn_save = Button(window, text="Save", command=lambda: register_user(name.get(), phone_number.get(), name.set(""), phone_number.set(""))).place(x=10, y=100)
btn_delete = Button(window, text="Delete", command=lambda: delete_user(name_delete.get(), phone_number_delete.get(), name_delete.set(""), phone_number_delete.set(""))).place(x=400, y=100)



tree = ttk.Treeview(window, columns=("id","name", "phone_number"), show="headings")
tree.heading("id", text="ID")
tree.column("id", anchor=CENTER)
tree.heading("name", text="Name")
tree.column("name", anchor=CENTER)
tree.heading("phone_number", text="Phone Number")
tree.column("phone_number", anchor=CENTER)
tree.place(x=10, y=150)


for i in result:
    tree.insert("", "end", values=(i[0], i[1], i[2]))




window.mainloop()