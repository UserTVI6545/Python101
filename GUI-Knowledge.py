from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

gui = Tk()
gui.title("โปรแกรมบันทึกข้อมูล") #ชื่อ title window
gui.geometry('500x400') #ขนาดของ window กว้าง x สูง

l1 = Label(gui,text="โปรแกรมบันทึกความรู้",font=("Angsana New",30),fg="green")
l1.place(x=30,y=20)
def botton2():
    text = "ตอนนี้มีเงินในบัญชี 300 บาท"  #message ใน popup
    messagebox.showinfo("เงินในบัญชี",text) #ชื่อ title ของ popup

def botton3():
    text = "Pythin 101, Math"
    messagebox.showinfo("วิชาเรียนวันที่ 10-20 ก.พ.",text)

#b1 = ttk.Button(gui,text="เงินมีอยู่กี่บาท") #ชื่อปุ่ม
#b1.pack(ipadx=20,ipady=20)

fb1 = LabelFrame(gui,text="Money") #คล้ายกระดาน
fb1.place(x=200,y=100)    
b2 = ttk.Button(fb1,text="เงินมีอยู่กี่บาท",command=botton2) #ชื่อปุ่ม
b2.pack(ipadx=20,ipady=20,padx=5,pady=5)

fb2 = LabelFrame(gui,text="Money") #คล้ายกระดาน
fb2.place(x=200,y=200)    
b3 = ttk.Button(fb2,text="สัปดาห์นี้เรียนวิชาอะไร",command=botton3) #ชื่อปุ่ม
b3.pack(ipadx=20,ipady=20,padx=5,pady=5)

gui.mainloop()