import tkinter as tk
import customtkinter as ctk
import mysql.connector as mysql
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


conn = mysql.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'sliit'
)

cursor = conn.cursor()

count = 0
 
def db():  
    global count
    
    cfm = int(text3var.get())
    icnm = int(text4var.get())
    cm = int(text5var.get())
    appm = int(text6var.get()) 
    vivam = int(text7var.get())
    
    if count > 0:    
        if (cfm>100 or icnm>100 or cfm>100 or cm>100 or appm>100 or vivam>100) or (cfm<0 or icnm<0 or cfm<0 or cm<0 or appm<0 or vivam<0) :
            messagebox.showinfo(title = "Error", message = "Please Enter a Valid Mark")
            text3.delete("0",tk.END)
            text4.delete("0",tk.END)
            text5.delete("0",tk.END)
            text6.delete("0",tk.END)
            text7.delete("0",tk.END)
        else:   
            average = ((cfm+icnm+cm+appm+vivam)/5)
            
            textinfo = textvar.get()
            text1info = text1var.get()
            text2info = text2var.get()
            
            if average > 49:
                gradedb = "Pass"
            else:
                gradedb = "Fail"
                
            query_vals = (text1info,textinfo,text2info,gradedb)
                
            cursor.execute("INSERT INTO student (Registration_Number,Name,Batch,Grade) VALUES (%s,%s,%s,%s)",query_vals)
            
            conn.commit()
            
            text.delete("0",tk.END)
            text1.delete("0",tk.END)
            text2var.set(text2options[0])
            text3.delete("0",tk.END)
            text4.delete("0",tk.END)
            text5.delete("0",tk.END)
            text6.delete("0",tk.END)
            text7.delete("0",tk.END)
            
            count = 0
    else:
        messagebox.showinfo(title = "Error", message = "Calculate First !!!")

def claculate():
    global count
    cfm = int(text3var.get())
    icnm = int(text4var.get())
    cm = int(text5var.get())
    appm = int(text6var.get()) 
    vivam = int(text7var.get())
    
    if (cfm>100 or icnm>100 or cfm>100 or cm>100 or appm>100 or vivam>100) or (cfm<0 or icnm<0 or cfm<0 or cm<0 or appm<0 or vivam<0) :     
        messagebox.showinfo(title = "Error", message = "Please Enter a Valid Mark")
        text3.delete("0",tk.END)
        text4.delete("0",tk.END)
        text5.delete("0",tk.END)
        text6.delete("0",tk.END)
        text7.delete("0",tk.END)     
         
    else: 
        count += 1  
        average = ((cfm+icnm+cm+appm+vivam)/5)
        messagebox.showinfo(title = "Message", message = f"You Average Mark is :- { average}")

        if cfm > 49 :
            grade = "Pass"
        else:
            grade = "Fail"

        cfmlabel = ctk.CTkLabel(frame1, text = f"{grade}",font =("Arial",10))
        cfmlabel.grid(row = 1 ,column = 2, sticky = tk.W)

        if icnm > 49 :
            grade = "Pass"
        else:
            grade = "Fail"

        icnmlabel = ctk.CTkLabel(frame1, text = f"{grade}",font =("Arial",10))
        icnmlabel.grid(row = 2 ,column = 2, sticky = tk.W)

        if cm > 49 :
            grade = "Pass"
        else:
            grade = "Fail"

        cmlabel = ctk.CTkLabel(frame1, text = f"{grade}",font =("Arial",10))
        cmlabel.grid(row = 3 ,column = 2, sticky = tk.W)

        if appm > 49 :
            grade = "Pass"
        else:
            grade = "Fail"

        appmlabel = ctk.CTkLabel(frame1, text = f"{grade}",font =("Arial",10))
        appmlabel.grid(row = 4 ,column = 2, sticky = tk.W)

        if vivam > 49 :
            grade = "Pass"
        else:
            grade = "Fail"
        vivamlabel = ctk.CTkLabel(frame1, text = f"{grade}",font =("Arial",10))
        vivamlabel.grid(row = 5 ,column = 2, sticky = tk.W)
 
def close():
    if messagebox.askyesno(title="Quit?", message="Do you realy wnat to quit?"):
        root.destroy()
        
root = ctk.CTk()
root.geometry("500x400")
root.title("SLIIT")

SLIIT = ctk.CTkLabel(root,text = "SLIIT - Kandy", font = ("Arial",20))
SLIIT.pack(padx = 10, pady = 20)

frame = ctk.CTkFrame(root)
frame.columnconfigure(0,weight = 1)
frame.columnconfigure(1,weight = 0)
frame.columnconfigure(2,weight = 1)

frame1 = ctk.CTkFrame(root)
frame1.columnconfigure(0,weight = 1)
frame1.columnconfigure(1,weight = 1)
frame1.columnconfigure(2,weight = 1)

frame2 = ctk.CTkFrame(root)
frame2.columnconfigure(0,weight = 1)
frame2.columnconfigure(1,weight = 1)

text2options = [
    "Py01",
    "Py02",
    "Py03",
    "Js01",
    "Jv01",
    "Jv02"
]

textvar =  ctk.StringVar()
text1var =  ctk.StringVar()
text2var =  ctk.StringVar()
text2var.set(text2options[0])

name = ctk.CTkLabel(frame, text ="Name ",font = ("Arial",15))
no = ctk.CTkLabel(frame, text ="Registration NO ", font = ("Arial",15))
batch = ctk.CTkLabel(frame, text ="Batch ", font = ("Arial",15))
equal = ctk.CTkLabel(frame, text =": ", font = ("Arial",15))
equal1 = ctk.CTkLabel(frame, text =": ", font = ("Arial",15))
equal2 = ctk.CTkLabel(frame, text =": ", font = ("Aria;",15))
text = ctk.CTkEntry(frame, width = 320 ,textvariable = textvar, )
text1 = ctk.CTkEntry(frame, width = 320, textvariable = text1var)
text2 = tk.OptionMenu(frame, text2var, *text2options)
text2.config(bg = "grey", activebackground = "grey", highlightbackground = "grey",font = ("Arial",10))
text2["menu"].config(bg = "grey", activebackground = "grey",font = ("Arial",10))

text3var = ctk.StringVar()
text4var = ctk.StringVar()
text5var = ctk.StringVar()
text6var = ctk.StringVar()
text7var = ctk.StringVar()

subject = ctk.CTkLabel(frame1, text =" Subject ",font = ("Arial",15))
marks = ctk.CTkLabel(frame1, text =" Marks ",font = ("Arial",15))
grade = ctk.CTkLabel(frame1, text =" Grade ",font = ("Arial",15))
cf = ctk.CTkLabel(frame1, text =" CF ",font = ("Arial",10))
icn = ctk.CTkLabel(frame1, text =" ICN ",font = ("Arial",10))
c = ctk.CTkLabel(frame1, text =" C# - SQL ",font = ("Arial",10))
app = ctk.CTkLabel(frame1, text =" App.Pkg ",font = ("Arial",10))
viva = ctk.CTkLabel(frame1, text =" Viva ",font = ("Arial",10))

text3 = ctk.CTkEntry(frame1, width = 80, textvariable = text3var)
text4 = ctk.CTkEntry(frame1, width = 80, textvariable = text4var)
text5 = ctk.CTkEntry(frame1, width = 80, textvariable = text5var)
text6 = ctk.CTkEntry(frame1, width = 80, textvariable = text6var)
text7 = ctk.CTkEntry(frame1, width = 80, textvariable = text7var)

name.grid(row = 0 ,column = 0, sticky = tk.W )
no.grid(row = 1 ,column = 0, sticky = tk.W )
batch.grid(row = 2 ,column = 0, sticky = tk.W )
equal.grid(row = 0 ,column = 1, sticky = tk.W)
equal1.grid(row = 1 ,column = 1, sticky = tk.W)
equal2.grid(row = 2 ,column = 1, sticky = tk.W)

text.grid(row = 0, column = 2, sticky = tk.W)
text1.grid(row = 1, column = 2, sticky = tk.W)
text2.grid(row = 2, column = 2, sticky = tk.W)

subject.grid(row = 0 ,column = 0, sticky = tk.W )
marks.grid(row = 0 ,column = 1, sticky = tk.W )
grade.grid(row = 0 ,column = 2, sticky = tk.W )
cf.grid(row = 1 ,column = 0, sticky = tk.W)
icn.grid(row = 2 ,column = 0, sticky = tk.W)
c.grid(row = 3 ,column = 0, sticky = tk.W)
app.grid(row = 4, column = 0, sticky = tk.W)
viva.grid(row = 5, column = 0, sticky = tk.W)

text3.grid(row = 1, column = 1, sticky = tk.W)
text4.grid(row = 2, column = 1, sticky = tk.W)
text5.grid(row = 3, column = 1, sticky = tk.W)
text6.grid(row = 4, column = 1, sticky = tk.W)
text7.grid(row = 5, column = 1, sticky = tk.W)

btn = ctk.CTkButton(frame2, text = "Calculate",font = ("Arial",15), command = claculate)
btn1 = ctk. CTkButton(frame2, text = "  Save  ",font = ("Arial",15), command = db)

btn.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)

frame.pack(fill = "x", padx = 10)
frame1.pack(fill = "x", pady = 10, padx = 10)
frame2.pack(fill = "x",padx = 10,pady =10)

root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()



