from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Addition")
root.geometry("600x400")
input_box = Entry(root)
img=ImageTk.PhotoImage(Image.open("creditcard.jpg"))
label1=Label(root,image=img)
label1.pack()
input_box.pack()

def addition():
    
    
    try:
        get_input = int(input_box.get()) 
        messagebox.showinfo("Message","credit card accepted")
    except:
        messagebox.showinfo("Alert", "Credit car not accepted") 
    
button = Button(root , text= "check credit card", command = addition)
button.pack()
root.mainloop()
