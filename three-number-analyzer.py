from tkinter import*

a=Tk()

a.title("omar informa")

a.geometry("250x250")

a.configure(bg="dark green")

s=Entry(a,bg="yellow",fg="blue")

s.pack()

d=Entry(a,bg="yellow",fg="blue")

d.pack()

f=Entry(a,bg="yellow",fg="blue")

f.pack()

def h():
    
    a1=int(s.get())
    
    a2=int(d.get())
    
    a3=int(f.get())
    
    print("the big numbar :" , max(a1,a2,a3))

g=Button(a,text="the big",bg="black",fg="red",command=h)

g.place(x=0,y=120)

def j():
    
    a4=int(s.get())
    
    a5=int(d.get())
    
    a6=int(f.get())
    
    print("the small :" , min(a4,a5,a6))

k=Button(a,text="the small",bg="black",fg="green",command=j)

k.place(x=92,y=120)

def l():
    
    a7=int(s.get())
    
    a8=int(d.get())
    
    a9=int(f.get())
    
    print("total :" , a7+a8+a9 )

g=Button(a,text="total",bg="black",fg="blue",command=l)

g.place(x=200,y=120)

a.mainloop()