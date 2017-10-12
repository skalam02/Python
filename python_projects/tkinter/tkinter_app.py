from Tkinter import *

window=Tk()
window.wm_title("KG to gr,lb,oz converter")
def km_to_various():
    t1.delete(1.0,END)
    t2.delete(1.0,END)
    t3.delete(1.0,END)
    t1.insert(END,float(e1_value.get())*1000)
    t2.insert(END,float(e1_value.get())*2.20462)
    t3.insert(END,float(e1_value.get())*35.274)

kg = StringVar()
kg.set("KG")
l1 = Label(window, textvariable=kg)
l1.grid(row=0,column=0)


gram = StringVar()
gram.set("Grams")
l2 = Label(window, textvariable=gram)
l2.grid(row=1,column=0)

pound = StringVar()
pound.set("Pounds")
l3 = Label(window, textvariable=pound)
l3.grid(row=2,column=0)

ounces = StringVar()
ounces.set("Ounces")
l4 = Label(window, textvariable=ounces)
l4.grid(row=3,column=0)




b1 = Button(window,text="Execute",command=km_to_various)
b1.grid(row=0,column=2)

e1_value=StringVar()

e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=3,column=1)


window.mainloop()
