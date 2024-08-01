import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from product_controller import save_controller,find_all_controller


def save_click():
    status,data =  save_controller(category.get(), brand.get(), name.get(), price.get(), count.get())
    if status == True:
        msg.showinfo("saved", data)
        refresh_form()
    else:
        msg.showerror("save got error", data)

def refresh_form():
    code.set(0)
    category.set("")
    brand.set("")
    name.set("")
    price.set(0)
    count.set(0)

    status,find_all_products = find_all_controller()
    if status == True:
        # Clear table
        for row in table.get_children():
            table.delete(row)
        # Fill the table 
        for product in find_all_products:
            table.insert('',tk.END,values=product)
    else:
        msg.showerror("Find", "cant access to database")

def select_product(event):
    selected_product = table.item(table.focus())["values"]
    code.set(selected_product[0])
    category.set(selected_product[1])
    brand.set(selected_product[2])
    name.set(selected_product[3])
    price.set(selected_product[4])
    count.set(selected_product[5])
    # print(table.item(table.focus())["values"])



win = tk.Tk()
win.geometry("1000x500")
win.title("product_management")

header = tk.Label(win,text="Enter product info : ").place(x=10,y=10)

tk.Label(win,text="code").place(x=20,y=50)
tk.Label(win,text="category").place(x=20,y=90)
tk.Label(win,text="brand").place(x=20,y=130)
tk.Label(win,text="name").place(x=20,y=170)
tk.Label(win,text="price").place(x=20,y=210)
tk.Label(win,text="count").place(x=20,y=250)

code = tk.IntVar()
category = tk.StringVar()
brand = tk.StringVar()
name = tk.StringVar()
price = tk.IntVar()
count = tk.IntVar()




tk.Entry(win, textvariable=code ,state="disabled").place(x=90,y=50)
tk.Entry(win, textvariable=category).place(x=90,y=90)
tk.Entry(win, textvariable=brand).place(x=90,y=130)
tk.Entry(win, textvariable=name).place(x=90,y=170)
tk.Entry(win, textvariable=price).place(x=90,y=210)
tk.Entry(win, textvariable=count).place(x=90,y=250)

tk.Button(win , text="save", width=10, command=save_click).place(x=100,y=300)


table = ttk.Treeview(win, columns=(1,2,3,4,5,6), show="headings")
table.heading(1, text="code")
table.heading(2, text="category")
table.heading(3, text="brand")
table.heading(4, text="name")
table.heading(5, text="price")
table.heading(6, text="count")

table.column(1, width=60)
table.column(2, width=120)
table.column(3, width=120)
table.column(4, width=120)
table.column(5, width=80)
table.column(6, width=80)


table.bind("<ButtonRelease>", select_product)

table.place(x=300 , y=50)

refresh_form()

win.mainloop()