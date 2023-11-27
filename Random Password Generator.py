import tkinter as tk
import string as strg
from random import shuffle,randint

def create_label():
    global warning_size,state
    warning_size=tk.Label(interface,text='*Password size should be numeric and size should be greater than 8 and less than 25 ',bg='salmon',fg='red',font='Arial 14 bold')
    warning_size.pack(fill='both')
    state=True
    
def change(length):
    try:
        global state
        if (int(length)<8 or int(length)>25) :
            if state==False:
                create_label()
                password['text']=''
        else:
            if state==True:
                warning_size.destroy()
                state=False
                generating_password(int(length))
            pass_label.pack(pady=20)
            password.pack()
            refresh.pack(pady=18)
    except:
        if state==True:
            warning_size.destroy()
            state=False
        
        
def on_entry_change(event):
    new_value=length.get()
    change(new_value)
    if len(new_value)>2:
        length.delete(2,tk.END)
        
def generating_password(size):
    types=[strg.ascii_lowercase,strg.ascii_uppercase,strg.digits,strg.punctuation]
    characters=[]
    for type in types:
        for char in type:
            characters.append(char)
    shuffle(characters)
    generated_password=''
    for _ in range(size):
        generated_password+=str(characters[randint(0,len(characters)-1)])
    password['text']=generated_password

def onclick():
    new_value=length.get()
    generating_password(int(new_value))
    

state=False  
interface=tk.Tk()
interface.configure(bg='salmon')
interface.title('Random Password Generator')
interface.geometry('1100x400')
name=tk.Label(interface,text='Password Generator',width=50,fg='red',font=('Helvetica bold',20,'bold'),bg='light pink').pack(pady=20)
size_label=tk.Label(interface,text='Enter the size of the Required Password',width=40,font='arial 16 bold',bg='orange').pack(padx=20)
length=tk.Entry(interface,width=30,font='arial 14 normal',bg='sky blue')
length.bind('<KeyRelease>',on_entry_change)
length.pack(pady=15)
pass_label=tk.Label(interface,text='Generated Password',width=40,fg='white',bg='black',font=('Helvetica bold',22,'bold'))
password=tk.Label(interface,width=33,font='arial 16 bold',bg='white',fg='black')
refresh=tk.Button(interface,text='Refresh',width=10,font='arial 16 bold',bg='cyan',fg='black',command=onclick)
interface.mainloop()
