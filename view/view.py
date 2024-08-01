import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg






win = tk.Tk()
win.geometry("400x550")
win.title("product_management")

header = tk.Label(win,text="Enter product info : ").place(x=10,y=10)

tk.Label(win,text="code").place(x=20,y=50)
tk.Label(win,text="name").place(x=20,y=90)
tk.Label(win,text="brand").place(x=20,y=130)
tk.Label(win,text="price").place(x=20,y=170)
tk.Label(win,text="count").place(x=20,y=210)

code = tk.IntVar()
name = tk.StringVar()
brand = tk.StringVar()
price = tk.IntVar()
count = tk.IntVar()




tk.Entry(win, textvariable=code).place(x=90,y=50)
tk.Entry(win, textvariable=name).place(x=90,y=90)
tk.Entry(win, textvariable=brand).place(x=90,y=130)
tk.Entry(win, textvariable=price).place(x=90,y=170)
tk.Entry(win, textvariable=count).place(x=90,y=210)

tk.Button(win , text="save", width=10, command=save_click).place(x=100,y=300)


win.mainloop()